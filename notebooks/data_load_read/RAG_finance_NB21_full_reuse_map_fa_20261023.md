<div dir="rtl" align="right">

# نقشهٔ جامع بازاستفاده از کارهای قبلی برای ۴۹ اقدام NB21

**پروژه:** RAG_finance — فاز دوم  
**تاریخ:** ۲۳ اکتبر ۲۰۲۶ / ۱ آبان ۱۴۰۵  
**شاخه:** `rag-phase2`  
**Commit بررسی‌شده:** `16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5`  
**ماهیت:** ممیزی فقط‌خواندنیِ دارایی‌ها و راهنمای مصرف مجدد؛ نه گزارش اجرای جدید، نه تغییر تیک‌ها و نه پذیرش رسمی کیفیت محصول.

## ۱. نتیجهٔ اجرایی

کار پروژه از صفر شروع نمی‌شود. دادهٔ سه‌منبعی، رجیستری ادعاهای منبع، Golden نسخه‌دار و داوری‌شده، نمایه‌ها، مقایسه‌های بازیابی، Context، پاسخ‌ها، Citation، ممیزی Test و تعدادی بازبینی محتوایی قبلاً ساخته شده‌اند. مهم‌ترین مشکل فعلی، **اتصال نتیجهٔ تاریخی به وظیفه و نسخهٔ فعلی** است؛ نه فقدان کلی کار قبلی.

این بررسی، علاوه بر ممیزی پیوست، رجیستری Claim و داوری‌های ردیفی آن، رجیستری بازبینی‌های قدیمی، آرشیو خانوادهٔ ۱۲، گزارش‌های پذیرش و شش خانوادهٔ Ablation را بررسی کرد. دو صرفه‌جویی مهم:

1. برای Completeness، پیش از استخراج دوبارهٔ الزامات از متن آزاد، زنجیرهٔ `candidate_id → claim_id → claim_text_fa → evidence → expected_answer → validation` موجود در Golden و رجیستری منبع مصرف شود. این زنجیره **مادهٔ مرجع و بازبینی** فراهم می‌کند؛ به‌تنهایی جامعیت الزامات هر سؤال یا صحت پاسخ فعلی را ثابت نمی‌کند.
2. برای Dense/Hybrid، حذف Reranker، تحلیل شکست، Bootstrap و بخشی از تنوع منبع، مقایسه و گزارش قبلی موجود است. اجرای مجدد موتور یا بازداوری کل جمعیت پیش‌فرض نیست.

سه گزاره نباید با هم اشتباه شوند:

- «کار قبلاً انجام و گزارش شده»؛
- «فایل مستقل آن اکنون در مخزن خوانده شده یا فقط مسیر و هش آن موجود است»؛
- «نتیجه برای همان معیار، همان Split و همان نسخهٔ پاسخ فعلی قابل پذیرش است».

## ۲. دامنهٔ بررسی و قدرت شواهد

### ۲.۱. آنچه واقعاً بررسی شد

- HEAD زندهٔ شاخه و درخت recursive مخزن: **۱۱۴۰ entry، بدون truncation**.
- دریافت و Parse فایل JSON تعداد **۲۶ نوت‌بوک**: فاز ۱، نوت‌بوک‌های اصلی مرتبط فاز ۲ و بخش گسترده‌ای از آرشیو خانوادهٔ ۱۲. این ۲۶ فایل در مجموع ۲۵۰۲ سل دارند؛ این عدد به معنی اجرای سل‌ها یا خواندن انسانی خط‌به‌خط تمام خروجی‌هایشان نیست. جست‌وجوی کد و خروجی‌ها، با خواندن تفصیلی بخش‌های مرتبط انجام شد.
- نوت‌بوک اصلی NB21 و NB20c از پیوست همین گفتگو خوانده شدند؛ Git Blob محاسبه‌شدهٔ هر دو با نسخهٔ مخزن یکسان است. بنابراین این دو، منابع تطبیق‌یافته با همان Snapshot محسوب می‌شوند.
- **۷۴ فایل مستقل JSON** شامل گزارش، قرارداد، Release، Manifest، Configuration و ارزیابی تاریخی خوانده و Parse شدند.
- رجیستری `human_review_registry.json` و رکوردهای بازبینی نمونهٔ آن خوانده شدند.
- فایل‌های ردیفی: ۴۰۳۹ نگاشت Raw Claim به Canonical Claim؛ ۴۰۰۶ متن Claim؛ ۶۲۳۷ داوری معنایی Claim منبع؛ ۳۸۱۷ رأی صلاحیت Seed خوانده و Parse شدند.
- `.gitignore`، فرم بازبینی مؤلف، فرم C120 و چارچوب سؤال‌ها نیز خوانده شدند.

### ۲.۲. محدودیت‌های واقعی

- دریافت مستقیم نوت‌بوک‌های حجیم ۱۵، ۲۰ و ۲۰بی در این نوبت با خطای انتقال مواجه شد. محتوا و شمارش‌های آن‌ها فقط در حد ممیزی پیوست، گزارش‌های مستقل خوانده‌شده و ارجاعات منابع دیگر استفاده شده‌اند؛ بازخوانی مستقیم کامل آن سه فایل در این ممیزی ادعا نمی‌شود.
- فایل فعال Golden v2 در درخت مخزن موجود است، ولی دریافت کامل JSONL ده‌مگابایتی آن در این نوبت موفق نشد. محتوای Schema و ساخت رکورد از NB12j، گزارش Freeze، Manifest و Readerهای NB21 بررسی شد. Hash تمام رکوردهای Golden در این نوبت دوباره محاسبه نشده است.
- بسیاری از Cacheها و فایل‌های `work/outputs` عمداً در Git ثبت نشده‌اند. این ممیزی به رایانهٔ کاربر دسترسی ندارد؛ وجود و هش همان فایل‌ها هنگام مصرف محلی کنترل می‌شود.
- هیچ نوت‌بوکی اجرا نشد، هیچ مدل یا API داوری فراخوانی نشد و هیچ فایل مخزن تغییر نکرد.
- تعداد دقیق درخواست‌های تکراری گذشته و مبلغ صرفه‌جویی ممکن، بدون Join ردیفی قابل اثبات نیست. این گزارش برای آن‌ها عدد حدسی نمی‌سازد.

### ۲.۳. کد وضعیت دارایی‌ها در این سند

| کد | معنی |
| --- | --- |
| `READ` | محتوای فایل مستقل در همین ممیزی خوانده و Parse شده است. |
| `NOTEBOOK_EVIDENCE` | کد/خروجی نوت‌بوک از ساخت یا کنترل Artifact خبر می‌دهد؛ خود فایل مستقل لزوماً در دسترس نیست. |
| `LOCAL_MATCHED` | پیوست همین گفتگو از نظر Git Blob با مخزن برابر است. |
| `ATTACHMENT_REPORTED` | وضعیت جدید در ممیزی پیوست گزارش شده، اما در Snapshot فعلی مخزن موجود نیست. |
| `NOT_FOUND_IN_TRACKED_TREE` | در فایل‌های tracked همین Snapshot پیدا نشده؛ فقدان روی سیستم کاربر نتیجه نمی‌شود. |
| `REUSE_CANDIDATE` | مادهٔ مرتبط موجود است؛ مصرف نهایی تابع تطبیق ورودی، نسخه، Split، وظیفه و دامنهٔ اعتبار است. |

## ۳. موجودی پایه و مرز جمعیت‌ها

| دارایی | موجودی | منشأ و حدود |
| --- | ---: | --- |
| Corpus پذیرفته‌شده | ۱۹۴۵۶ رکورد | NB08/NB09 و NB12h؛ ۵۲۹ Website، ۲۷۰۱ Book، ۱۶۲۲۶ Transcript. Hash مرجع: `9d72c709f81b1218c5aac064052c7ed1da34869f671e6e32762864e0ad70ea40`. |
| Raw Claimهای منبع | ۶۲۳۷ | گزارش و داوری ردیفی NB12i؛ Claim پاسخ فعلی نیستند. |
| Claimهای منبعِ Validated | ۴۰۳۹ | گزارش disposition؛ برخی ACCEPTهای مدل به‌علت ریسک بحرانی همچنان HOLD شده‌اند. |
| Canonical Claimهای منبع | ۴۰۰۶ | پس از Exact canonicalization؛ ادغام خودکار Semantic/Subsumption انجام نشده است. |
| شاهدهای رجیستری | ۴۱۲۵ occurrence | گزارش رجیستری؛ تکرار شاهد و منشأ حفظ شده است. |
| روابط Claim | ۲۵۱۶ | ۱۰۱ Exact provenance و ۲۴۱۵ رابطهٔ واجد Graph؛ رابطهٔ معنایی به معنی ادغام نیست. |
| Golden فعال | ۳۸۱۳ QA | Manifest و NB12j؛ Freeze مهندسی و داوری مدل ثبت شده است؛ تأیید مؤلف/استقلال انسانی کل جمعیت از آن نتیجه نمی‌شود. |
| Development | ۲۶۶۴ | قراردادهای مصرف NB16 تا NB21. |
| Test | ۱۱۴۹ | سابقهٔ مواجهه و اجرای تاریخی دارد؛ کاملاً دست‌نخورده معرفی نشود. |
| Chunk baseline جاری | ۳۴۸۸ | `baseline_phase1_char_safe`؛ مسیر واقعی NB13 تا NB18، نه اثبات برتری ساختارمحور. |
| پاسخ منتخب Development | ۲۶۱۸ موجود / ۴۶ مفقود | NB21-C303 و NB21B-C095؛ «مفقود در Snapshot منتخب» با «هیچ پاسخ تاریخی وجود ندارد» متفاوت است. |
| زنجیرهٔ Citation متصل | ۲۵۶۰ پاسخ | NB21B-C088/C095؛ لایهٔ ۵۸ پاسخ در این مسیر حل‌نشده است. |
| Context تولید متصل | ۲۵۵۱ پاسخ | NB21B-C093/C095؛ ۶۷ پاسخ نیازمند اتصال تاریخی‌اند. |

عددهای بالا را جمع نکنید. یک QA می‌تواند چند Claim، شاهد و نسخهٔ پاسخ داشته باشد. ثبت یک رکورد در چند Resume نیز چند اجرای تازه نیست.

## ۴. کشف مهم اول: رجیستری دانش منبع و Golden، مادهٔ مرجع آماده دارند

### ۴.۱. رجیستری Claim و داوری معنایی آن

منابع مستقل خوانده‌شده:

- [گزارش رجیستری Claim](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/knowledge_registry/claim_registry_report_v1.json)
- [گزارش داوری معنایی کامل](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/knowledge_registry/claim_validation_full_semantic_report_v1.json)
- [رکوردهای داوری معنایی](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/knowledge_registry/claim_validation_full_semantic_adjudication_v1.jsonl)
- [گزارش disposition](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/knowledge_registry/claim_validation_full_report_v1.json)

داور ثبت‌شده `Qwen3-30B-A3B` با Prompt `claim_semantic_fidelity_v3` است. برای ۶۲۳۷ Claim، ۴۶۹۸ ACCEPT، ۱۱۸۳ REJECT و ۳۵۶ REPAIR ثبت شده؛ disposition نهایی فقط ۴۰۳۹ را VALIDATED و ۶۵۹ مورد را HOLD_CRITICAL_RISK کرده است. بنابراین ACCEPT خام مدل با پذیرش نهایی یکسان نیست.

ابعاد ثبت‌شده شامل Entailment، Evidence completeness، Atomicity، Scope، Modality، Quantifier، Perspective و Standalone است. در سطح ردیف، متن Claim، `raw_claim_id`، Checkها، دلیل و تصمیم وجود دارد. فایل `claim_id_mapping_v1.jsonl` برای اتصال Raw به Canonical و `claim_embedding_text_index_v1.jsonl` برای متن Canonical نیز خوانده شد.

**مصرف مجاز:** تأیید منشأ و معنای Claim مرجع؛ بازاستفاده از شاهد و تشخیص خطرهایی مانند تغییر دامنه، شدت گزاره یا جهت رابطه. استخراج دوبارهٔ همان Claim از همان منبع لازم نیست.

**مرز:** این‌ها داوری Claim دانش منبع‌اند، نه داوری ۲۶۱۸ پاسخ تولیدشدهٔ فعلی. نه Groundedness پاسخ، نه Citation correctness و نه تمام الزامات ضروری سؤال را خودکار کامل نمی‌کنند. مدل Qwen این مسیر هم داوری مستقل انسانی محسوب نمی‌شود.

### ۴.۲. Golden قبلاً QA و رابطهٔ آن با Claim را اعتبارسنجی کرده است

در [NB12j آرشیوی](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12j_golden_dataset_v2_registry_driven_rebuild.ipynb)، Code Cell 25 ساخت هویت و Skeleton را ثبت می‌کند؛ Code Cell 57 اطلاعات نهایی QA و Validation را اضافه می‌کند؛ Cell 58 Freeze و Cell 61 سلامت Run-All-safe را گزارش می‌کنند.

فیلدهای قابل استفاده شامل این‌هاست:

```text
candidate_id, source_seed_slot_id, claim_id, claim_text_fa,
claim_type, claim_types, authority_class, raw_claim_ids,
evidence_ids, evidence_quotes, evidence_locators,
source_ids, document_ids, source_types,
evaluation_content.question,
evaluation_content.expected_answer,
evaluation_content.question_intent,
validation.answer_recovers_claim,
validation.question_targets_claim,
validation.answer_question_alignment,
validation.scope_fidelity,
validation.modality_quantifier_fidelity,
validation.no_neighbor_fact_drift,
validation.no_external_knowledge
```

قرارداد ساخت Skeleton، محتوا و lineage را حفظ می‌کند؛ Consumer باید Schema واقعی رکورد نهایی را بخواند و صرف نام‌های بالا Reader فرضی نسازد. به‌ویژه، محل محتوای نهایی QA در `evaluation_content` با فیلدهای قدیمی Skeleton اشتباه نشود.

**مصرف برای اقدام ۲۳:** سؤال فعلی را به Golden، Claim هدف، شاهد و QA مرجعِ همان نسخه وصل کنید. در سؤال‌های سادهٔ تک‌هدف، بررسی کفایت همان مادهٔ مرجع می‌تواند بسیار محدودتر از استخراج مجدد آزاد از تمام متن باشد. در سؤال مرکب، قیود، چند پاسخ معتبر و الزامات حذف‌شدنی باید جدا بررسی شوند. هیچ تبدیل خودکارِ «یک Claim = مرجع جامع همهٔ سؤال‌ها» تصویب نمی‌شود.

**مصرف برای اقدام ۲۲:** این داده مرجع پاسخ مطلوب را می‌دهد؛ وفاداری پاسخ تولیدشده همچنان باید نسبت به Context واقعی تولید بررسی شود. پاسخ می‌تواند به Context وفادار ولی نامربوط به سؤال باشد، یا بخشی از جواب مرجع را داشته باشد ولی ادعاهای اضافی بی‌پشتوانه بسازد.

### ۴.۳. اسناد تاریخی وضعیت مرحلهٔ خود را توصیف می‌کنند

قرارداد اولیهٔ Registry-driven و Manifest تجمیع خانوادهٔ ۱۲ هنوز عباراتی مثل `PENDING_AUTHOR_REVIEW` و `IN_PROGRESS` دارند؛ Manifest نهایی Golden، `FROZEN` و ۳۸۱۳ QA با PASS مدل را ثبت می‌کند. این تفاوت‌ها تناقض ساده یا مجوز انتخاب خوش‌بینانه‌ترین وضعیت نیستند: هر سند برای مرحله و نقش خود مصرف شود.

Golden v1 با ۵۷۳ مورد، Core-46 با ۴۶ مورد و Golden v2 با ۳۸۱۳ QA سه دارایی متفاوت‌اند. Core-46 مرجع Regression/کیفیت است و گزارش پذیرش آن صریحاً `ACCEPTED_EXPERIMENT_NOT_ACTIVE_DATASET` می‌گوید. جای Dataset فعال را بی‌مجوز نگیرد.

## ۵. کشف مهم دوم: رجیستری بازبینی، جواب مرجع و Citation قدیمی موجود است

[رجیستری بازبینی](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/data/phase2/human_review/human_review_registry.json) فقط یک عنوان نیست؛ متن سؤال، نسخهٔ Draft، Expected answer، Target evidence، Citation و تصمیم‌ها را نگه می‌دارد.

- `completed_human_review_cases`: تعداد ۲۲ مورد تاریخی.
- بخش `author_review`: ۲۸ مورد آماده؛ `final_review_status=NOT_STARTED`.
- در نمونه‌های خوانده‌شده، نام مرحلهٔ بازبینی، متن پاسخ مرجع، شاهد، دلیل، شناسهٔ Draft و تصمیم ACCEPT/REVISE موجود است.
- بعضی پرونده‌ها تبدیل حسابی مستقیم مانند «نیمی = ۵۰٪» را با منشأ مشخص ثبت کرده‌اند.
- `Human Reviewer` نام فیلد/نقش ثبت‌شده است؛ این ممیزی هویت و استقلال شخص واقعیِ بازبین را بیرون از Artifact احراز نکرده است. بازبینی مؤلف نیز صرفاً از نام فایل یا این برچسب نتیجه نمی‌شود.

**کاربرد:** مواد آماده برای کالیبره‌کردن Rubric، مثال‌های پاسخ معادل، مرجع موردیِ Completeness، Attribution و Regression. برای انتقال به Golden v2 باید سؤال، منبع، Claim، پاسخ و وظیفهٔ فعلی تطبیق داده شود. شباهت موضوع یا شناسهٔ Pilot قدیمی کافی نیست.

فرم `archive/C120.human_review.md` مربوط به بازبینی قصد درخواست است؛ مرجع Groundedness یا Completeness پاسخ مالی نیست. فرم ۲۸ مورد مؤلف نیز بدون رأی تکمیل‌شده، تأیید مؤلف محسوب نمی‌شود.

## ۶. کشف مهم سوم: Retrieval، تنوع منبع، latency و خطاها از قبل شواهد دارند

### ۶.۱. Dense / Sparse / Hybrid / Reranker

- NB13 و گزارش پذیرش آن، مدل منتخب `intfloat/multilingual-e5-small`، Revision و ۳۴۸۸ Chunk baseline را ثبت کرده‌اند. مقدارهای کل ۳۸۱۳ پرسش آن، Development-only فعلی محسوب نمی‌شوند.
- NB14، Release و lifecycle نمایهٔ Dense را ثبت کرده است؛ ساخت دوبارهٔ Embedding یا Index برای بازخوانی Metric لازم نیست.
- NB15 و Release مستقل Sparse، نمایه و نتایج Test را دارند؛ نسخهٔ تکراری بعضی Report/Handoffها زیر `notebooks/phase2/` نیز وجود دارد. فایل‌های هم‌Blob دوبار به‌عنوان شاهد مستقل یا دو اجرا شمرده نشوند.
- NB16 Code Cell 18 و `hybrid_retrieval_evidence_v1.json` مقایسهٔ پنج سیستم را دارند: Dense-only، Sparse-only، RRF، Weighted Hybrid و Weighted Hybrid با Source cap 3.
- NB17 Code Cell 15 تا 17، ارزیابی کامل Development، Bootstrap، Sliceها، خطاها و Freeze را دارند. Code Cell 16 تعداد ۸۹۳ بهبود، ۴۸۴ افت و ۱۲۸۷ بدون تغییر را گزارش می‌کند؛ این‌ها خانوادهٔ دیگری از شمارش‌اند و با انتقال Hit یکی نیستند.
- NB21-C192/C194/C195/C196/C304 و NB21B-C003 بازخوانی/تطبیق جدیدتر را انجام داده‌اند. بستهٔ ۱۹ تا ۲۱ با تصمیم اصلاحی همین چت در دامنهٔ ثبت‌شده بسته است؛ با این ممیزی دوباره باز نمی‌شود.

**احتیاط Metric:** Recall با Hit یکی نیست. MRR رتبهٔ کامل، Top-100 و MRR@10 متفاوت‌اند. NB21-C173 قبلاً اختلاف دامنهٔ تاریخی MRR را توضیح داده است؛ این مسئله را دوباره Debug نکنید. اختلاف tie-break Dense محلی با Qdrant تاریخی نیز حفظ شود.

### ۶.۲. Source diversity واقعاً در دو لایه آزمایش شده است

NB16 capهای ۱، ۲ و ۳ را در Retrieval آزمایش کرده، ولی Configuration نهایی آن `NO_HARD_CAP` است. NB18 سیاست واقعی Context را انتخاب کرده است:

```text
source_cap_per_source_id = 8
document_cap_per_member_document_id = 5
selection_order = reranker_order
evidence_only_token_budget = 7371
```

NB18-C62 تا C65، مقایسهٔ uncapped و capهای مختلف را دارند. سیاست منتخب ۲۴ آیتم Development را نسبت به تعداد کامل Top-10 حذف کرده است. بنابراین برای اقدام ۳۶ ابتدا همین مقایسهٔ Context مصرف شود؛ حذف cap غیرفعال NB16، Ablation سیاست فعال NB18 نیست.

**مرز:** اثر Context/پوشش Gold با اثر کیفیت پاسخ نهایی یکی نیست. اگر الزام اقدام ۳۶ کیفیت پاسخ را نیز می‌خواهد، فقط شکاف همان لایه باز بماند.

### ۶.۳. latency و هزینه از صفر شروع نمی‌شوند

Configuration بازرتبه‌بند latency اجرای محلی ONNX CPU با depth 50 را برای **۲۵۱۴ Query** ثبت کرده: p50 حدود **۶٫۰۲۱ ثانیه** و p95 حدود **۸٫۴۰۵ ثانیه**. این عدد latency سراسری محصول، کل ۲۶۶۴ Query یا زمان اجرای Cache نیست.

NB15 گزارش مستقل latency دارد؛ NB16/NB17 دادهٔ آزمایش و NB19/NB21B لاگ اجرای مدل دارند. برای اقدامات ۲۹ تا ۳۱ آن‌ها یک بار با واحد، سخت‌افزار، Run، warm/cold و Missing تجمیع شوند. نبود telemetry قدیمی به معنی صفر زمان یا صفر هزینه نیست؛ برآورد تعرفهٔ تاریخی هم صورتحساب واقعی نیست.

## ۷. وضعیت هر شش Ablation رسمی

| اقدام | شاهد قبلی | آنچه می‌توان بازاستفاده کرد | شکاف واقعی / نتیجهٔ ممنوع |
| ---: | --- | --- | --- |
| ۳۲ — بدون Persian normalization | NB08، sidecar Raw/Normalized، گزارش پذیرش | Policy، متن قبل/بعد، Offset/lineage و ۲۶۳ سند تغییرکرده از ۱۹۴۵۶ | وجود Normalizer، نتیجهٔ Ablation Retrieval نیست. حذف فقط Query یا کل Corpus/Index باید مشخص شود. بازاجرای تمام داده فقط در صورت نیاز اثبات‌شده. |
| ۳۳ — Character در برابر Structure-aware | NB11، Candidate registry، قرارداد Freeze و NB12h-C39 | baseline=۳۴۸۸، small=۲۵۲۶، medium=۱۷۹۹، child=۲۷۲۱، parent=۱۴۴۷؛ تحلیل ساختاری و مرزها | انتخاب نهایی Production در قرارداد NB11 باز است. شواهد ساختاری بهبود Retrieval را اثبات نمی‌کند. Mapping Gold هر Chunking باید از همان Source locator بازسازی/مصرف شود. |
| ۳۴ — Dense-only در برابر Hybrid | NB16-C18 و Evidence JSON؛ NB21-C192/C304 | نتایج، تنظیمات، Split، داوری انتخاب و بخش بزرگی از جدول مقایسه | همسانی عمق و تعریف MRR، اجرای Dense/Qdrant در برابر Dense محلی و محدودیت استنتاج خالص حفظ شود. |
| ۳۵ — بدون Reranker | NB17-C15/C16/C17؛ NB21-C192/C195/C196/C304 | همان Pool پنجاه‌تایی، اختلاف زوجی، Bootstrap و شکست‌ها | مقایسهٔ Pool متفاوت اثر خالص Reranker نیست؛ نیازی به اجرای مجدد مدل برای نتایج معتبر موجود نیست. |
| ۳۶ — بدون Source diversity | NB16 آزمایش cap؛ NB18-C62..C65 و Configuration نهایی | مقایسهٔ uncapped با سیاست واقعی source=8/document=5 در Context | cap اختیاری NB16 جای سیاست فعال NB18 نیست؛ اثر Retrieval/Context به پاسخ نهایی تعمیم داده نشود. |
| ۳۷ — بدون Citation verifier | NB19-C195، مسیرهای Claim gate/Source citation و NB21B-C023..C077 | تعریف کنترل‌های واقعی، اتصال‌ها، Failure و دادهٔ قبل/بعدِ موجود در صورت اتصال معتبر | Verifier مستقل معنایی از structural validator و رأی پشتیبانی مدل جداست. نبود verifier مستقل را با یک Proxy پنهان نکنید؛ وجود Ablation کامل از شواهد خوانده‌شده اثبات نشد. |

در این ممیزی هیچ‌یک از شش اقدام خودکار تیک نمی‌خورد. «دارای مواد قابل استفاده» با «بستهٔ کامل پذیرفته‌شده» متفاوت است.

## ۸. پاسخ و بازبینی‌های قبلی: کدام به کدام معیار می‌خورند؟

### ۸.۱. NB19 — Development و Test را جدا نگه دارید

NB19-C195 برای ۲۶۶۴ Development این موجودی را گزارش کرده است:

- ۲۲۲۴ واجد Internal support و ۴۴۰ Blocked؛
- ۵۶۴۰ Claim با پشتیبانی ثبت‌شدهٔ مدل؛
- ۱۰۵۳۲ Citation با محدودهٔ دقیق Source؛
- کنترل اتصال Claim/Evidence/Citation و برابری متن Chunk، PASS؛
- Entailment مستقل، دقت جایگاه Claim داخل پاسخ و مقایسه با Gold، ارزیابی‌نشده.

این رکوردها برای اقدام ۲۲ و ۲۴ **Reuse candidate** هستند. نسخهٔ پاسخ را با Snapshot فعلی تطبیق دهید؛ ۵۶۴۰ را با ۶۶۰۵ Claim Checkpoint در موجودی جدیدتر جمع نزنید.

NB19-C235 تا C239 برای ۱۱۴۹ Test، مسیر `chatgpt_recovery` با `NON_INDEPENDENT_AGENT_REVIEW` را تحویل داده‌اند. این‌ها اجرای زندهٔ Qwen یا مرجع مستقل نیستند. برای اقدام ۳۹ سابقهٔ Test و برای ۲۷/۲۸ محدودیت منشأ را تأمین می‌کنند؛ برای تکمیل ۲۶۶۴ Development جایگزین نمی‌شوند.

### ۸.۲. NB20 / NB20b / NB20c — محتوا را بخوانید، برچسب را تبدیل نکنید

ممیزی پیوست برای NB20/NB20b وجود ۱۱۴۹ بازبینی محدوده‌دار، رجیستری C371 و کنترل C372 را گزارش می‌کند. در این ممیزی NB20c تطبیق‌یافته مستقیماً بررسی شد:

- C393: تعداد ۵۶۲ پروندهٔ کاملاً متصل؛ برای ۵۰۹ مورد، `evidence_reviews` و `response_assessment_fa` وجود دارد. نبود فیلد صریح Metric، نبود محتوای مفید را ثابت نمی‌کند.
- همان خروجی، پذیرش رسمی را BLOCKED و اعتبار مستقل معنایی را برقرارنشده گزارش می‌کند. از متن نظر، برچسب رسمی حدسی نسازید.
- C454/C455: بازپخش و تحویل ۱۱۴۹ ممیزی پسینی؛ `NONCRITICAL=1149`، اما ایمنی زنده، صحت همهٔ پاسخ‌ها و تکمیل کل فاز دوم تأیید نشده است.
- Calibration قبلی هدف «حضور کامل شاهد مرجع در Context» داشته؛ احتمال صحت پاسخ یا Confidence نهایی محصول نیست. Brier/Log loss و ECE را با هم و با حدود اصلی مصرف کنید.

**مصرف مجاز:** شاهد و دلیل قبلی برای همان پاسخ و همان وظیفه، Failure case، تاریخچهٔ Safety، مرجع کالیبراسیون در دامنهٔ اصلی. برچسب NONCRITICAL جای Groundedness/Completeness/No-answer نمی‌نشیند.

### ۸.۳. NB21 / NB21b — Reader و تطبیق‌های موفق را تکرار نکنید

NB21-C020 تعریف Metric، C026 قرارداد Slice، C034 Blueprint، C040 Rubric، C041 موجودی مرجع، C165 Gold mapping، C173 تبیین MRR، C192..C196 Benchmark و C303 Runner مستقل را دارند. C302 صریحاً تفکیک کرده: ثبت تصمیم اقدام ۱۵ کامل است، ولی `official_numeric_semantic_scoring_authorized=false` و روش جمعیت پذیرفته نشده است.

NB21b در Snapshot مخزن **تا C101** است؛ C095 دامنهٔ معیارها را جدا کرده و C096..C101 بستهٔ ۶۴تایی و ترمیم‌های آن را ثبت کرده‌اند. C101، ۱۳۰ الزام حفظ‌شده و ۹ الزام بازیابی‌شدهٔ دیگر را گزارش می‌کند؛ این اعداد شمار الزام‌اند، نه شمار پاسخ‌های نهایی پذیرفته‌شده، و هنوز semantic acceptance ندارند.

ممیزی پیوست از پیشرفت محلی **C118/C119** خبر می‌دهد: دفتر ۸۱ پرونده، ۷۵ قابل‌سنجش و ۶ مرجع مبهم؛ ۱۰۶ الزام بررسی‌شده. C119 از ۱۱۱ مورد، ۵۳ ارسال، ۴۷ پروندهٔ محلی معتبر با ۶۴ پیشنهاد الزام و ۶ Held داشته است. این اطلاعات `ATTACHMENT_REPORTED` است؛ این ممیزی خروجی مستقل آن‌ها را در مخزن ندیده است.

**ممنوع:** عددسازی «۸۱ + ۴۷ = ۱۲۸ پروندهٔ پذیرفته‌شده». هم‌پوشانی، نسخه، پذیرش و واحد شمارش ابتدا روشن شود. ۸۱ نیز کل کارهای قدیمی پروژه نیست.

## ۹. نگاشت تک‌تک ۴۹ اقدام به دارایی و حداقل کار باقی‌مانده

این جدول **تصمیم تیک جدید نیست**. وضعیت اداری از چک‌لیست و تصمیم‌های همین گفتگو می‌آید؛ ستون آخر، کار لازم برای مصرف شاهد یا رفع شکاف را توضیح می‌دهد. شمارهٔ اقدام همیشه متعلق به چک‌لیست NB21 است، نه NB20.

| اقدام | موضوع | دارایی قابل استفادهٔ مجدد | حداقل کار لازم / مرز پذیرش |
| ---: | --- | --- | --- |
| ۱ | مأموریت و مرزها | نقشهٔ تفصیلی، NB21-C057 و چک‌لیست | مأموریت دوباره طراحی نشود؛ تغییر دامنه فقط مستند. |
| ۲ | Git و نسخه | HEAD همین ممیزی و Preflightهای قبلی | وضعیت محلی هنگام اجرا فقط یک بار بررسی شود؛ HEAD امروز، وضعیت دیروز را اثبات نمی‌کند. |
| ۳ | فایل مرجع | NB21 اصلی و 21b ادامه | نسخهٔ سوم ساخته نشود؛ 21b ادامهٔ NB21 است. |
| ۴ | تحویل C455 | NB20c-C454/C455 و هش تحویل | فایل محلی و ارجاعات لازم مصرف شوند؛ بازاجرای عمومی NB20c ممنوع. |
| ۵ | موجودی Canonical | Manifestهای داده، Golden، Chunk، Releaseهای NB13..18 و C303 | فهرست موجود را به‌روز/متصل کنید؛ Inventory از صفر نسازید. |
| ۶ | Cache و آزمایش‌ها | NB12i/j، NB16..20c، NB21 و این ممیزی | نتیجهٔ تاریخی را به وظیفهٔ فعلی Join کنید؛ مفقود در Reader را «انجام‌نشده» نگویید. |
| ۷ | منشأ خروجی | NB19-C195 و Test recovery، NB20c و C060/C069 | Split، مدل، Agent review، Cache و Replay جدا بمانند. |
| ۸ | Gap matrix | C017/C034/C041، C095 و ممیزی پیوست | مسئول واقعی هر شکاف و وضعیت اتصال مشخص شود؛ شکاف تکراری نسازید. |
| ۹ | تعریف Metric | NB21-C020 و C040 | تعریف و مخرج قبلی مصرف؛ نام مشابه Metric مجوز همسان‌فرض‌کردن نیست. |
| ۱۰ | Slice معتبر | تاکسونومی، Corpus authority، C026/C194 و پیشنهادهای C329 | نگاشت پیشنهادشده پذیرفته‌شده نیست؛ شکاف Topic/Question type و جزئیات Authority حفظ شود. |
| ۱۱ | Test و طرح مقایسه | NB21-C027..C032، ارزیابی تاریخی NB15..17 | سابقهٔ Test پاک یا از نو دست‌نخورده اعلام نشود. |
| ۱۲ | آستانه/بودجه/Freeze | C034، Freezeهای جزئی NB16..18 و C095 | معیارهای مصوب نسخهٔ نهایی و اختلاف پوشش ۹۰٪/۹۵٪ تعیین تکلیف شود؛ Target اولیه Gate نهایی نیست. |
| ۱۳ | Rubric و مرجع | C035..C041، رجیستری بازبینی و Golden lineage | مواد قدیمی مصرف؛ استقلال و کفایت جدا ثبت شوند. |
| ۱۴ | آزمون روش | C298..C301 و NB21B-C047..C069 | آزمایش‌های تشخیصی موجود تکرار نشوند؛ فقط خطای جدیدِ مشخص. |
| ۱۵ | تصمیم روش | C302 و تصمیم‌های ناظر ثبت‌شده در C078/C095 | ثبت تصمیم کامل است؛ امتیاز مستقل جمعیت هنوز از آن نتیجه نمی‌شود. |
| ۱۶ | Reader/Join | C303 و C014/C083/C086/C088 | آداپتور در محل معتبر اصلاح شود؛ Readerهای موازی نسازید. |
| ۱۷ | Smoke/Pilot | C303 Pilot/Resume/Replay و آزمون‌های موجود | همان Pipeline با همان ورودی دوباره آزمایش نشود؛ تغییر مؤثر دلیل تست محدود است. |
| ۱۸ | Runner قابل ادامه | C303 و Cacheهای دارای request fingerprint | خروجی معتبر دوباره Dispatch نشود؛ attempts نامعلوم با resend خودکار جبران نشوند. |
| ۱۹ | تطبیق Retrieval | NB16/NB17 و C192/C304 | در دامنهٔ ثبت‌شده بسته؛ همان مقایسه تکرار نشود. |
| ۲۰ | Metric روی Dev/Slice معتبر | C003 و تصمیم اصلاحی ناظر | در دامنهٔ مصوب بسته؛ Missing نگاشت‌ها و الزام باز اقدام ۱۰ در گزارش بماند. |
| ۲۱ | اختلاف/پوشش/شکست Retrieval | C173/C195/C196/C304 | در دامنهٔ ثبت‌شده بسته؛ شکست‌های شناخته‌شده به Error catalogue منتقل شوند. |
| ۲۲ | Groundedness | NB19 support، C060/C069 و Context متصل C093 | Claimهای پاسخ فعلی، شاهد Context و رأی مرتبط تطبیق؛ Source Claim داوری‌شده جای پاسخ فعلی نیست. |
| ۲۳ | Completeness | Golden Claim/QA/Validation، رجیستری ۲۲ بازبینی و C018/C019/C063 و C118 گزارش‌شده | مرجع ضرورت/کفایت و پوشش پاسخ؛ فقط Missing واقعی استخراج شود؛ B10 محفوظ. |
| ۲۴ | Citation | NB19-C195، C023..C077 و ۱۲۱۷۸ Citation گزارش‌شدهٔ C088 | تعلق به نسخهٔ پاسخ، معنای رابطه و پوشش Claim جدا از Locator؛ ۳۱ نگاشت باز تعیین وضعیت واقعی شود. |
| ۲۵ | Attribution | Corpus کانونی، Schema، Acceptanceهای منبع و C090 | نقش نمایش‌داده‌شده و الزام نمایش جدا؛ منشأ هویت و انتساب داخل پاسخ کنترل شود. |
| ۲۶ | No-answer | پاسخ/routeهای NB19، سیاست NB20 و محدودیت مرجع Golden | Intent یا NONCRITICAL برچسب truth پاسخ‌پذیری نیست؛ مرجع معتبر مثبت/منفی و Clarification لازم است. |
| ۲۷ | Safety | رجیستری ۱۱۴۹ Test و C436/C439/C455 | ممیزی پسینی و رفتار مولد زنده جدا؛ شمار بحرانی صفر به معنای ایمنی همهٔ جمعیت نیست. |
| ۲۸ | Confidence | Calibration و Handoff NB20c | هدف احتمال حضور شاهد و محدودیت استقلال منتقل شود؛ بازکالیبراسیون عمومی پیش‌فرض نیست. |
| ۲۹ | latency | NB15 test report، NB16، NB17 latency، لاگ NB19 | یک جدول بر حسب Run/مرحله/تعداد واقعی؛ Cache latency به‌جای تولید زنده ننشیند. |
| ۳۰ | Token/Cost/Failure | Cacheهای API و خروجی‌های NB19/NB20/NB21 | Usage یکتا با request fingerprint؛ Resume و unknown billing جدا. |
| ۳۱ | Trade-off | ADRهای Hybrid/Reranker/Context و گزارش هزینه | تجمیع کیفیت/هزینه در دامنهٔ همسان؛ Fresh API لازم نیست مگر شکاف اندازه‌گیری مصوب. |
| ۳۲ | Normalization ablation | NB08 sidecar و Policy | وجود before/after مصرف؛ اثر Retrieval/پاسخ هنوز جدا تعیین شود. |
| ۳۳ | Chunking ablation | NB11 Candidateها و NB12h استقلال Gold | Candidateها بازسازی نشوند؛ فقط شکاف Index/Metric و Mapping سازگار. |
| ۳۴ | Dense/Hybrid | NB16-C18 و C192/C304 | بازاستفادهٔ مقایسهٔ هم‌قرارداد؛ محدودیت depth/tie-break حفظ شود. |
| ۳۵ | Reranker ablation | NB17-C15 و NB21 Same-pool | نتایج همان Pool و عدم قطعیت موجود مصرف شود. |
| ۳۶ | Diversity ablation | NB18-C62..C65 و capهای واقعی | اثر Context موجود؛ اثر پاسخ نهایی فقط در صورت مطالبه و نبود Cache باز بماند. |
| ۳۷ | Verifier ablation | NB19 کنترل‌های واقعی و C195 | verifier مستقلِ ناموجود جعل نشود؛ قبل/بعد معتبر یا شکاف صریح. |
| ۳۸ | Freeze نهایی | Releaseهای مؤلفه و Manifestهای موجود | Freeze کل آزمایش NB21، روش و Gate هنوز یکپارچه نشده؛ سابقهٔ Test حفظ شود. |
| ۳۹ | ارزیابی نهایی Test | نتایج Retrieval Test، Test recovery و ممیزی NB20c | بخش تاریخی قابل مصرف؛ Missing معتبر طبق طرح ثابت؛ اجرای کل Test از صفر نه. |
| ۴۰ | مقایسه زوجی/عدم قطعیت | Bootstrapهای NB16/NB17 و C195 | دامنه/واحد resampling و هم‌بستگی منابع تطبیق؛ CI یک معیار به معیار دیگر منتقل نشود. |
| ۴۱ | Error taxonomy | NB17-C16، C196، شکست داور B05 و Holdها | خطاهای موجود را یکپارچه کنید؛ تولید خطای مصنوعی تازه لازم نیست. |
| ۴۲ | Failure cases | لاگ اختلاف‌ها و شاهدهای متصل | شناسه، نسخه، شدت، مسئول و Regression متناظر؛ موارد سخت حذف نشوند. |
| ۴۳ | مقایسه فاز ۱ | phase1/10_evaluation و فایل ده‌سؤالی ۲۰۲۶/۰۷/۰۹ | هشت in_scope و دو out_of_scope تاریخی؛ مقایسهٔ هم‌شرط هنوز نیازمند تطبیق، نه ادعای برتری از دو Dataset. |
| ۴۴ | گزارش‌های نهایی | تمام گزارش‌های مؤلفه و این نقشه | تجمیع شواهد در خروجی رسمی NB21؛ گزارش ممیزی جای Benchmark کامل نیست. |
| ۴۵ | Regression Gate | Core-46، ده سؤال فاز۱، خطاهای واقعی و Gateهای مؤلفه | آستانه/وابستگی مصوب و پوشش معتبر؛ FAIL یا نامعین با تیک پوشانده نشود. |
| ۴۶ | Manifest/Handoff NB22 | الگوی Releaseهای NB16..18 و C455 | فقط بستهٔ NB21 با وضعیت واقعی Gate ساخته شود؛ Release کل فاز۲ نیست. |
| ۴۷ | Reload | کدها و الگوی C303/C454 و Manifestها | Reload زنجیرهٔ خروجی نهایی NB21، نه تکرار همهٔ تولیدات تاریخی. |
| ۴۸ | اجرای پاک | سابقهٔ Run-All-safe NB12j، Final Healthهای NB10/NB17/NB18 | 21b فعلی دارای FIX، history dependency و Error ذخیره‌شده است؛ اجرای امن نهایی هنوز اثبات نشده. |
| ۴۹ | Summary/چک‌لیست | شاهدهای پایان هر اقدام و تصمیم ناظر | سربرگ قدیمی، ۱۹ تیک واقعی جدول و ۳۰ مورد باز هماهنگ شوند؛ تعداد تیک درصد کیفیت نیست. |

## ۱۰. قرارداد لازم برای بازاستفادهٔ ردیفی

### ۱۰.۱. کلید تطبیق براساس وظیفه

| وظیفه | کلید لازم | چیزی که لازم نیست |
| --- | --- | --- |
| استخراج/بازبینی مرجع سؤال | هش سؤال، Claim هدف، مجموعهٔ منابع و محدودهٔ بررسی، نسخهٔ قرارداد مرجع | هش پاسخ تولیدشده، اتصال Context یا Citation آن، مگر خود منبع لازم فقط از آن مسیر در دسترس باشد. |
| Groundedness | هش پاسخ، Claim/Span پاسخ، Context واقعی تولید و نسخهٔ Rubric | یکسان‌بودن Candidate ID به‌تنهایی کافی نیست. |
| پوشش Completeness | کلید مرجع پذیرفته‌شده + هش پاسخ فعلی + قرارداد تطابق معنایی | متن Golden به‌تنهایی یا الزام‌های ساخته‌شده پس از دیدن پاسخ برای بهترشدن امتیاز. |
| Citation | هش نسخهٔ پاسخ/بسته، Claim، Citation، شاهد و Locator | پشتیبانی همان Claim از شاهد دیگری در Context، صحت همین Citation را ثابت نمی‌کند. |
| Attribution | انتساب بیان‌شده یا مورد مشمول نمایش + شناسهٔ منبع/نقش/Metadata version | حضور نام صاحب مجموعه یا خالی‌بودن انتساب. |
| Safety/No-answer | سؤال، پاسخ/Policy، مرجع همان وظیفه، Split و دامنهٔ ریسک | NONCRITICAL جای مرجع پاسخ‌پذیری یا درستی پاسخ نیست. |

### ۱۰.۲. یک دفتر Reuse بر دارایی موجود، نه Pipeline موازی تازه

دفتر/Runner فعلی را توسعه دهید؛ صرفاً برای این گزارش Notebook یا رجیستری موازی ساخته نشود. برای هر رکوردِ بالقوهٔ مصرف:

```text
checklist_action, split, candidate_id,
question_sha256, selected_answer_sha256_if_required,
task_type, source_scope_fingerprint, rubric_or_policy_version,
historical_artifact_path, historical_file_hash,
record_pointer, request_fingerprint_if_present,
review_origin, source_witness, original_decision,
reuse_disposition, reuse_reason, remaining_gap
```

وضعیت‌های پیشنهادی دفتر، بدون تغییر رکورد تاریخی:

- `REUSE_EXACT`: ورودی و وظیفه منطبق؛ نتیجه در همان دامنه مصرف شود.
- `REUSE_WITH_SCHEMA_ADAPTER`: ساختار متفاوت ولی معنای قابل انتقال؛ آداپتور مشتق با منشأ صریح.
- `REVIEW_EXISTING_CONTENT`: دلیل و شاهد موجود، ولی نتیجهٔ معیار صریح/معتبر نیست؛ محتوا بررسی شود، نه ارسال خودکار دوباره.
- `VERSION_CONFLICT`: پاسخ، سؤال یا منبع تغییر کرده؛ نتیجهٔ تاریخی حفظ و اثر اختلاف تعیین شود.
- `SOURCE_OR_BINDING_UNRESOLVED`: فایل/اتصال در محدودهٔ بررسی پیدا نشده؛ فقدان کلی اعلام نشود.
- `GENUINE_NEW_WORK`: پس از تطبیق، وظیفهٔ لازم واقعاً بدون نتیجهٔ قابل مصرف مانده است؛ فقط این بخش نامزد کار تازه است.

نبود استقلال یک رأی، آن را بی‌ارزش نمی‌کند؛ می‌تواند در گزارش برآورد مدل، راهنمای بازبینی یا نمونهٔ خطا مصرف شود. ولی کیفیت استقلال بدون دلیل ارتقا نیابد. رأی ردشده/منسوخ با رأی مؤثر فعلی یکی نشود.

### ۱۰.۳. راه اتصال مرجع برای اقدام ۲۳

1. از رکورد فعال Golden، سؤال و Claim هدف و evidenceهای همان رکورد خوانده شود.
2. از `claim_id_mapping_v1.jsonl` به Raw Claim و از داوری ردیفی به Fidelity و Failureهای مرجع وصل شوید.
3. disposition نهایی رجیستری را لحاظ کنید؛ ACCEPT خام مدل یا شباهت embedding کافی نیست.
4. الزامات و پاسخ‌های جایگزینِ موجود در رجیستری بازبینی و دفاتر NB21b برای همان سؤال/منبع تطبیق داده شوند.
5. اگر تمام مادهٔ لازم موجود است، فقط ضرورت، قیود و کفایت سؤال در همان ماده بازبینی شود؛ استخراج آزاد تازه پیش‌فرض نیست.
6. اگر بخشی از سؤال هنوز پوشش ندارد، فقط الزام/شاهد مفقود بررسی شود. متن سؤال/منبع خراب با حدس اصلاح نشود.
7. پاسخ فعلی پس از تثبیت مرجع سنجیده شود. جدول «پوشش الزام» با جدول «وفاداری ادعاهای اضافی پاسخ» جدا بماند.

این مسیر اجازه نمی‌دهد تمام Claimهای مربوط به یک موضوع را الزامات پاسخ یک سؤال فرض کنید. روابط Subsumption/Overlap هم فقط راهنمای کشف‌اند و حقیقت مرجع یا الزام جامع را به‌تنهایی تعیین نمی‌کنند.

## ۱۱. چه چیزهایی هنوز نداریم یا در این بررسی اثبات نشده‌اند؟

| موضوع | وضعیت دقیق |
| --- | --- |
| نقشهٔ کامل Reuse در سطح پاسخ/وظیفه | مواد لازم گسترده است، ولی شمار نهایی رکوردهای دقیقاً قابل مصرف و تکرارهای قابل حذف هنوز Join ردیفی می‌خواهد. |
| مرجع جامع Completeness برای همهٔ Dev | Golden و رجیستری منبع وجود دارند؛ کفایت حداقل الزامات برای همهٔ سؤال‌ها هنوز ثابت نشده است. |
| ارزیابی رسمی مستقل همهٔ پاسخ‌ها | از PASS داور مدل یا سلامت JSON نتیجه نمی‌شود؛ نتایج مدل در سطح برآورد حفظ شوند. |
| Topic و Question type پذیرفته‌شدهٔ جمعیت | پیشنهادهای ۲۶۶۴ سؤال موجودند، اما پذیرش نگاشت مستقل اثبات نشده؛ اقدام ۱۰ باز است. |
| اتصال پاسخ/Context/Citation تمام Dev | برخی شمارش‌ها هنوز ۴۶ پاسخ، ۶۷ Context و ۵۸ لایهٔ Citation حل‌نشده نشان می‌دهند؛ این‌ها دامنه‌های متفاوت‌اند. |
| شش Ablation کامل پاسخ نهایی | شواهد Retrieval و Context فراوان است؛ Normalization/Chunking/Verifier و اثر پاسخ در حد لازم هنوز باید تفکیک شوند. |
| Gate نهایی NB21 | آستانه‌های مصوب، اختلاف ۹۰٪/۹۵٪ و وابستگی‌ها باید تعیین تکلیف شوند؛ Gateهای مؤلفه جای آن نیستند. |
| Release کل فاز۲ و Handoff پذیرفته‌شدهٔ فاز۳ | NB22 و NB23 در درخت فعلی یافت نشدند؛ Releaseهای مؤلفه و C455 جای این تحویل نیستند. |
| Package/CLI و tests فاز۲ طبق نقشه | مسیرهای `src/phase2/` و `tests/phase2/` در این Snapshot یافت نشدند؛ کار Notebook معادل وجود این زیرساخت نیست. |
| صحت هر منبع و هویت بازبین بیرون از Artifact | این ممیزی read-only چنین تأیید بیرونی انجام نداده؛ provenance موجود باید با دامنهٔ واقعی بیان شود. |

در نبود فایل tracked از عبارت `NOT_FOUND_IN_TRACKED_TREE` استفاده شود، نه «ساخته نشده». به‌خصوص `claims_raw`، `claims_validated` و `claims_deduplicated` و همهٔ `artifacts/**/work/` تحت الگوهای ignore هستند. `claim_evidence_links`، Knowledge graph و Corpus پذیرفته‌شده نیز در درخت فعلی دیده نشدند؛ علت همهٔ آن‌ها از نام مسیر قابل استنتاج نیست. بازسازی آن‌ها با مدل راه جبران پیش‌فرض نیست.

## ۱۲. ترتیب ادامه برای چت اجرایی

**بستهٔ فعال همان ۲۲ تا ۲۵ است؛ این ممیزی مجوز پرش به ۲۹/۳۰ یا بازکردن دوبارهٔ ۱۹ تا ۲۱ نیست.**

### بستهٔ اول — مصرف موجودی قبل از هر ارسال تازه

از Reader و Cacheهای فعلی، زنجیرهٔ Golden/Registry و بررسی‌های NB19/NB20 را برای وظیفهٔ مورد نظر Join کنید. خروجی باید در سطح رکورد مصرف واقعی ایجاد کند، نه صرفاً Discovery/فهرست دیگری:

- چه تعداد مرجع/رأی دقیقاً مصرف شد؛
- چه تعداد محتوای موجود با بازبینی محدود قابل استفاده شد؛
- چه تعداد تعارض نسخه یا اتصال حل‌نشده باقی است؛
- چه تعداد کار تازه با دلیل مشخص واقعاً لازم است.

برای C119ِ گزارش‌شده، ۵۳ خروجی اجراشده و نتایج سالم محفوظ بمانند. ۵۸ ارسال‌نشده و ۶ Held قبل از تصمیم Reuse به ارسال تازه تبدیل نشوند. «Reuse هنوز اثبات نشده» نیز به‌تنهایی به معنی «API لازم است» نیست.

### بستهٔ دوم — ارزیابی واقعیِ مواد پذیرفتنی

الزامات مرجع معتبر موجود را به پاسخ فعلی اعمال کنید؛ هم‌زمان Groundedness/Citation/Attribution آماده را مصرف کنید. تأخیر مرجع Completeness نباید بقیهٔ معیارها را بدون وابستگی واقعی متوقف کند. برای هر معیار denominator و answer-level coverage جدا ثبت شود. خروجی مدل، اصلاح ناظر و مرجع انسانی با منشأ خودشان تفکیک شوند.

### بستهٔ سوم — فقط شکافِ باقی‌مانده

اگر پس از دو بستهٔ بالا وظیفهٔ ضروریِ فاقد نتیجه باقی ماند، طرح محدود همان شکاف، contract سازگار، Cache key، تعداد درخواست، خروجی و هزینه ارائه شود. سیاست مجوز جاری کاربر در همان چت اجرا ملاک است؛ این سند مجوز خرج تازه یا درخواست تأیید تکراری نیست. مقدار بودجه و سابقهٔ مجوز از حافظه یا برآورد تاریخی حدس زده نشود.

### حد توقف و پایان

- شاهد متعارض، نسخهٔ نامعلوم یا معنای مفقود باعث HOLD همان رکورد/معیار شود؛ ورودی معتبر بقیه خودکار حذف نشود.
- سلامت قالب یا تعداد سطر شرط کافی پایان اقدام معنایی نیست.
- اقدام‌های ۲۲ تا ۲۵ فقط براساس شرط پایان خودشان و پوشش واقعی تعیین وضعیت شوند؛ دفتر محدود به جای کل Development معرفی نشود.
- پس از تعیین تکلیف این بسته، ادامهٔ عادی ۲۶ تا ۲۸ است. بسته‌های بعدی در زمان خود از همین نقشه مواد آماده را مصرف کنند.

## ۱۳. دستور آمادهٔ انتقال به چت اجرایی

```text
این فایل نقشهٔ بازاستفاده است، نه دستور ساخت Pipeline تازه یا مجوز API.
بستهٔ فعال NB21 همچنان اقدامات ۲۲ تا ۲۵ است.

پیش از هر استخراج یا داوری تازه، کار قبلی را براساس وظیفه و نسخه تطبیق بده:
۱) Golden v2 و claim_id/claim_text/evidence/validation آن؛
۲) رجیستری Claim، raw-to-canonical mapping و داوری‌های معنایی منبع؛
۳) expected-answer/citation reviewهای رجیستری قدیمی و Core-46؛
۴) support و citationهای NB19 برای Development؛
۵) بازبینی‌های NB20 فقط در Split و وظیفهٔ اصلی‌شان؛
۶) دفاتر و اصلاحات معتبر NB21/NB21b، از جمله خروجی‌های سالم C118/C119.

نبود فیلد یا اتصال در Reader جدید را فقدان کار قبلی اعلام نکن.
نبود فایل در Git، فقدان محلی را ثابت نمی‌کند؛ Artifact قبلی را با مدل نساز.
برای مرجع Completeness، پاسخ تولیدشده و اتصال Citation شرط مستقل نیستند.
داوری Claim منبع را داوری پاسخ فعلی، و NONCRITICAL را کیفیت پاسخ معرفی نکن.
Golden/Corpus/پاسخ/سیاست فریز‌شده تغییر نکنند.

همین Runner/دفتر فعلی را برای تصمیم Reuse ردیفی مصرف/تکمیل کن؛
رجیستری موازی و زنجیرهٔ Discovery تازه لازم نیست.
خروجی بعدی باید رکوردهای مصرف‌شده و شکاف واقعیِ باقی‌مانده را مشخص کند
و سپس سنجش پاسخ را با مواد موجود جلو ببرد؛ فقط گزارش وضعیت نساز.

مدل اصلی DeepSeek، اصلاح B05، اصلاح B08، وضعیت B10 و محدودیت‌های استقلال محفوظ‌اند.
retry خودکار و بازاجرای عمومی نوت‌بوک‌های قدیمی انجام نشود.
اگر API ضروری شد، فقط کار باقی‌مانده طبق مجوز و بودجهٔ همان چت.
هیچ تیک تازه‌ای از این ممیزی نتیجه نمی‌شود.
```

## ۱۴. رسید منابع منتخب و نشانی‌های دقیق

همهٔ لینک‌ها به Commit بررسی‌شده پین شده‌اند. مسیر `work/outputs` وقتی فایل tracked نیست، در کد/خروجی نوت‌بوک تولیدکننده پیدا می‌شود و باید محلی خوانده شود.

| شناسه | منبع | جایگاه شاهد |
| --- | --- | --- |
| E01 | [چک‌لیست NB21](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/NB21_remaining_work_checklist_fa.md) | ۴۹ اقدام؛ جدول ۱۹ تیک دارد ولی سربرگ و بخش قدم بعد هنوز قدیمی‌اند. |
| E02 | [NB21 اصلی](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/21_evaluation_and_ablation.ipynb) | C020، C026، C034، C041، C165، C173، C192..C196، C302..C304، C329. پیوست محلی هم‌Blob. |
| E03 | [NB21b](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/21b_evaluation_and_ablation_continued.ipynb) | ۲۱۸ سل / ۱۰۹ کد؛ آخرین گام C101، نه C119. |
| E04 | [NB12i آرشیوی](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12i_claim_registry_and_knowledge_graph.ipynb) | Code Cell 27..31: canonicalization، Graph، گزارش رجیستری و Final Health. |
| E05 | [NB12j آرشیوی](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12j_golden_dataset_v2_registry_driven_rebuild.ipynb) | Cells 25، 57، 58، 61: هویت، QA/validation، Freeze و سلامت. |
| E06 | [رجیستری بازبینی](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/data/phase2/human_review/human_review_registry.json) | completed_human_review_cases، expected_answer_review، citation_review و author_review. |
| E07 | [Claim ID mapping](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/knowledge_registry/claim_id_mapping_v1.jsonl) | ۴۰۳۹ اتصال Raw → Canonical. |
| E08 | [متن Canonical Claim](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/knowledge_registry/claim_embedding_text_index_v1.jsonl) | ۴۰۰۶ متن با claim_text_sha256 و raw_claim_ids. |
| E09 | [داوری Claim منبع](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/knowledge_registry/claim_validation_full_semantic_adjudication_v1.jsonl) | ۶۲۳۷ رکورد متن/دلیل/Check/decision؛ مربوط به دانش منبع. |
| E10 | [داوری صلاحیت Seed](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/golden_dataset_v2/golden_v2_seed_suitability_judgments_v1.jsonl) | ۳۸۱۷ رکورد صلاحیت Seed؛ Dataset نهایی ۳۸۱۳ رکورد دارد. |
| E11 | [Hybrid evidence](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/data/phase2/retrieval/hybrid_retrieval_v1/hybrid_retrieval_evidence_v1.json) | development، ablation، source_diversity، ADR و independent_test. |
| E12 | [Reranker config](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/reranking/reranker_configuration_v1.json) | development_selection، Bootstrap، latency، depth و Revision. |
| E13 | [Context config](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/context_builder/context_builder_configuration_v1.json) | cap فعال و budget، محدودیت topic/parent/conflict. |
| E14 | [NB18](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/18_context_builder.ipynb) | C62..C65 آزمایش uncapped/capped؛ C90..C93 نوشتن، Reload و Final Health. |
| E15 | [NB19](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/19_generation_and_citation.ipynb) | C195 Development support؛ C235..C239 Test recovery و زنجیرهٔ تحویل. |
| E16 | [NB20c](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/20c_answerability_safety_confidence_audit_and_acceptance.ipynb) | C393، C454، C455؛ پیوست محلی هم‌Blob. |
| E17 | [Phase1 evaluation](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/data/evaluation/rag_evaluation_20260709_153736.json) | ده پاسخ ذخیره‌شده، sources/retrieved_chunks و from_cache. |
| E18 | [Normalization acceptance](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/reports/phase2/persian_normalization_acceptance_v1.json) | Raw/Normalized sidecar و Policy واقعی. |
| E19 | [Chunk candidate registry](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/artifacts/phase2/chunking/candidate_registry_evaluation_v1.json) | Candidateهای موجود؛ Production selection باز. |
| E20 | [Sparse test report](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/reports/phase2/sparse_test_evaluation_v1.json) | متریک، Slice، Failure و latency قبلی. |

### هش‌های مرجعِ مهم — نوع هش را مخلوط نکنید

| مورد | نوع | مقدار |
| --- | --- | --- |
| Snapshot مخزن | Git Commit SHA-1 | `16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5` |
| NB21 اصلی | Git Blob SHA-1 | `4405d634de02e8e95df717a4f727bade2ea730e7` |
| NB20c | Git Blob SHA-1 | `d459195412e4740d48ba5f84b9b54a4b66b15606` |
| NB21b | Git Blob SHA-1 | `61874cb471666df55b6569ee70d04fdcd515099b` |
| Golden فعال | SHA-256 بایت فایلِ ثبت‌شده در Manifest | `b9ca18e710686ddca48a25c637840b716adb306717cafd8ec7c96ce9e182e6f2` |
| Golden payload | SHA-256 payloadِ ثبت‌شده | `539635b4c89e8f4eda41dde8106e04307c063f3fe0f5db402ef0440802233a03` |
| Corpus پذیرفته‌شده | SHA-256 بایت فایلِ ثبت‌شده | `9d72c709f81b1218c5aac064052c7ed1da34869f671e6e32762864e0ad70ea40` |
| Claim registry report | SHA-256 ثبت‌شده در تولیدکننده | `f7951467ca49d1bac1e1c1efee9e93e756f24fbf6db02e500e35a6672b21d645` |
| Canonical claims | SHA-256 ثبت‌شده؛ فایل مستقل در tree پیدا نشد | `8d1080d6519faa8ca5d4614256dbabf04426170b8f914f606eb3088d1f2c08bb` |
| Full semantic adjudication | SHA-256 ثبت‌شده در Report؛ JSONL این نوبت خوانده شد | `2e508f6f02d98a878e97ef3e161d7dcbe2f2b6778fcd5b6df7660937e6996c27` |
| C455 handoff | SHA-256 بایت فایلِ گزارش‌شده | `9b08c7991964ea8cc99ba2cc9e47e9bed7104d8c3231b75fe77277ef86475ae1` |

برای مصرف نهایی، Hash همان فایل محلی و تعریف هش از تولیدکننده کنترل شود. این جدول Hash ثبت‌شده را با محاسبهٔ مجدد این ممیزی یکسان معرفی نمی‌کند.

## ۱۵. حدود نتیجهٔ ناظر

**داریم:** زیرساخت و مادهٔ مرجع فراوان، بازبینی‌های ثبت‌شده در چند مسیر، مقایسه‌های Retrieval، شواهد فنی استناد و دفاتر جاری ارزیابی. ۸۱ یا ۲۴ پروندهٔ یک دفتر، شمار تمام کار پروژه نیست.

**هنوز اثبات نکرده‌ایم:** چه تعداد از وظایف فعلی دقیقاً از آن مواد پوشش می‌گیرند؛ کیفیت رسمی همهٔ پاسخ‌های جاری؛ کفایت مرجع برای همهٔ سؤال‌ها؛ تمام Ablationهای لازم؛ Gate و Release نهایی.

**تصمیم:** قبل از کار تازه، نتیجهٔ قدیمی را در همان وظیفه و نسخه مصرف کنید؛ برای چیزی که موجود ولی نامتصل است Reader را اصلاح کنید؛ فقط شکاف ضروری باقی‌مانده را اجرا کنید. این ممیزی هیچ تیک، PASS معنایی، مجوز API یا تغییر در تاکسونومی صادر نمی‌کند.


## پیوست الف — فهرست نوت‌بوک‌های دریافت‌شده

این فهرست رسید دسترسی است؛ هیچ‌یک در این ممیزی اجرا نشدند. شمارهٔ Cell در متن گزارش براساس عنوان سل است و با index صفرمبنای JSON اشتباه نشود.

| مسیر | سل / کد | Git Blob SHA-1 |
| --- | ---: | --- |
| [notebooks/phase1/10_evaluation.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase1/10_evaluation.ipynb) | 25 / 13 | `57e4d4512622baaa66353dc6b05e4c5d33a9b3a6` |
| [notebooks/phase2/00_environment_and_baseline.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/00_environment_and_baseline.ipynb) | 30 / 11 | `eb96bbd17a725bd7ee17f17c4d5e2a4a410a83e8` |
| [notebooks/phase2/07_unified_schema_and_lineage.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/07_unified_schema_and_lineage.ipynb) | 61 / 30 | `8953c8930a4cf238e3136a461965c6b30d0691ea` |
| [notebooks/phase2/08_persian_normalization.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/08_persian_normalization.ipynb) | 47 / 23 | `ef69dc79438f38ccc9e01ca1b9a050206f14259c` |
| [notebooks/phase2/09_deduplication_and_quality.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/09_deduplication_and_quality.ipynb) | 89 / 43 | `0a5e07401f8752761f7f980afb04d18316f19650` |
| [notebooks/phase2/10_taxonomy_and_knowledge_engineering.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/10_taxonomy_and_knowledge_engineering.ipynb) | 90 / 44 | `e94d839b5b22592995f4693d3bc4d8ae7504dd40` |
| [notebooks/phase2/11_chunking_benchmark.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/11_chunking_benchmark.ipynb) | 55 / 28 | `118bd09c2566f54ff8f556fef92fde5c5ff65f77` |
| [notebooks/phase2/12_golden_dataset.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/12_golden_dataset.ipynb) | 20 / 12 | `1629ebcd71a0b2fd4e290638d36abd4ca8007fc2` |
| [notebooks/phase2/13_embedding_benchmark.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/13_embedding_benchmark.ipynb) | 140 / 69 | `7c13a1fb9b802644eca3eefee8ba791fcf9857f3` |
| [notebooks/phase2/13_embedding_benchmark_closure_candidate.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/13_embedding_benchmark_closure_candidate.ipynb) | 147 / 73 | `bafdf4ebddbb022785980f23db05041f84a1b972` |
| [notebooks/phase2/14_dense_index.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/14_dense_index.ipynb) | 34 / 17 | `1f8a8a82f2f1fbadc8e05977d8b129572381f2bf` |
| [notebooks/phase2/16_hybrid_retrieval.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/16_hybrid_retrieval.ipynb) | 45 / 22 | `11c4e4de24657175518673f0daeb619ed05f5944` |
| [notebooks/phase2/17_reranking.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/17_reranking.ipynb) | 45 / 22 | `8efa6fa4b15a07de8a1ad71d13939d53e95e8a0b` |
| [notebooks/phase2/18_context_builder.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/18_context_builder.ipynb) | 188 / 93 | `3f8cee1ad69ffc613f7752227b56433d545b9e3c` |
| [notebooks/phase2/19_generation_and_citation.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/19_generation_and_citation.ipynb) | 480 / 239 | `99ae4625a3153eb8e32e378e02bfbf322df121df` |
| [notebooks/phase2/21b_evaluation_and_ablation_continued.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/21b_evaluation_and_ablation_continued.ipynb) | 218 / 109 | `61874cb471666df55b6569ee70d04fdcd515099b` |
| [notebooks/phase2/archive/series12_notebooks/12b_golden_dataset_continuation_compact.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12b_golden_dataset_continuation_compact.ipynb) | 209 / 104 | `5ccebf301cc0bcd4407f2130e3582d89ba345f6c` |
| [notebooks/phase2/archive/series12_notebooks/12c_human_review_for_author.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12c_human_review_for_author.ipynb) | 13 / 6 | `4d5b7e54e0fe24ec0b1cb74c6f86f51e26b5dbf4` |
| [notebooks/phase2/archive/series12_notebooks/12d_second_human_review.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12d_second_human_review.ipynb) | 28 / 14 | `951ab12d6dbade9676553ca37ff6de06c83dc2ce` |
| [notebooks/phase2/archive/series12_notebooks/12e_golden_dataset_full_generation.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12e_golden_dataset_full_generation.ipynb) | 154 / 82 | `fe2b2be3c06784152258c5900f45d8d5b97ed847` |
| [notebooks/phase2/archive/series12_notebooks/12f_author_feedback_integration.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12f_author_feedback_integration.ipynb) | 29 / 14 | `d98c00eaf68a0957533595675b26f68708c0636b` |
| [notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_quality_rebuild_lab.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_quality_rebuild_lab.ipynb) | 32 / 18 | `03d942a8d271446debc3c25b326c78a5036400fa` |
| [notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_rebuild_clean.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_rebuild_clean.ipynb) | 50 / 40 | `bd178cc20df6f4f8be6c03c7ab7206a2f70c2f6c` |
| [notebooks/phase2/archive/series12_notebooks/12h_pilot_and_expansion_audit.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12h_pilot_and_expansion_audit.ipynb) | 84 / 41 | `2d78c6560e94d256f3cf918f62c9657a81630cfa` |
| [notebooks/phase2/archive/series12_notebooks/12i_claim_registry_and_knowledge_graph.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12i_claim_registry_and_knowledge_graph.ipynb) | 63 / 31 | `51ee952bc2cd25fafc195b4a70cb38faa259d945` |
| [notebooks/phase2/archive/series12_notebooks/12j_golden_dataset_v2_registry_driven_rebuild.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5/notebooks/phase2/archive/series12_notebooks/12j_golden_dataset_v2_registry_driven_rebuild.ipynb) | 126 / 61 | `2ff507e1eaf373b5d9061ad7658386bc43867851` |

### پیوست‌های هم‌Blob با مخزن

| مسیر مخزن | سل | Git Blob SHA-1 |
| --- | ---: | --- |
| `notebooks/phase2/21_evaluation_and_ablation.ipynb` | 694 | `4405d634de02e8e95df717a4f727bade2ea730e7` |
| `notebooks/phase2/20c_answerability_safety_confidence_audit_and_acceptance.ipynb` | 906 | `d459195412e4740d48ba5f84b9b54a4b66b15606` |

## پیوست ب — فهرست ۷۴ فایل JSON مستقل خوانده‌شده

وجود این فایل‌ها با خواندن تمام Cacheهای ارجاعی آن‌ها یکسان نیست. وضعیت نهایی هر موضوع از نسخه و نقش همان Artifact تفسیر شود، نه صرف نام فایل.

| مسیر | Git Blob SHA-1 |
| --- | --- |
| `artifacts/phase2/chunking/candidate_registry_evaluation_v1.json` | `2cbce48084e9978dad09d3dcce9f0f855fa2a133` |
| `artifacts/phase2/chunking/chunk_contract_evaluation_freeze_v1.json` | `856ef42bdb3490cd584a8e21056f36de5066e7ee` |
| `artifacts/phase2/context_builder/context_builder_configuration_v1.json` | `0041928536e479a8dee0ce46a70a88e9b569a234` |
| `artifacts/phase2/context_builder/context_builder_release_v1.json` | `68a9fa006e076b5010a36de103ce3388b6b7920c` |
| `artifacts/phase2/context_builder/nb19_context_builder_handoff_v1.json` | `b825a1040ec212b00712a8c645ded70983a4d99d` |
| `artifacts/phase2/dense_index/dense_index_release_v1.json` | `0a18f4a55354b7519372ee033ad241698689270b` |
| `artifacts/phase2/dense_index/nb16_dense_index_handoff_v1.json` | `3b8f29fcd29cbed00ea8433ea8d132b57f0bb65b` |
| `artifacts/phase2/embedding/embedding_release_v1.json` | `0d1c4440f9f5c1d8d3234025e7ef7b04ad8f4ca2` |
| `artifacts/phase2/embedding/nb14_dense_index_handoff_v1.json` | `c3fb3fdfa00ceddab49b0664de1ecbde909afd5b` |
| `artifacts/phase2/golden_dataset_v2/golden_dataset_v2_final_report.json` | `7833c59b24c32e13ac9bfc26121ef07ca86bb3fc` |
| `artifacts/phase2/golden_dataset_v2/golden_dataset_v2_manifest.json` | `e48cda976795b51a951e7adc398d34cc0837d45d` |
| `artifacts/phase2/golden_dataset_v2/golden_dataset_v2_registry_driven_contract_v1.json` | `a446733dc22760b1625adc849553b650a087277c` |
| `artifacts/phase2/golden_dataset_v2/golden_v2_seed_suitability_report_v1.json` | `d50537e65239b8541eabf4882c8a84ee980069d1` |
| `artifacts/phase2/golden_dataset_v2/golden_v2_semantic_seed_suitability_contract_v1.json` | `9b39545ba4095eba064472b8af25f23485de8ee1` |
| `artifacts/phase2/golden_dataset_v2/twelve_series_consolidated_manifest_v1.json` | `25192f26ac1158e8e3e91d8cb1bc729450cbd3ce` |
| `artifacts/phase2/hybrid_retrieval/hybrid_configuration_v1.json` | `4166351d2fb223daf2083bd065251c5dc45fa7a5` |
| `artifacts/phase2/hybrid_retrieval/hybrid_retrieval_release_v1.json` | `e9478923b436366a541f0c9017bebf6a3ebe1247` |
| `artifacts/phase2/hybrid_retrieval/nb17_hybrid_retrieval_handoff_v1.json` | `430a79f1f9057168c15ea744fa8de402e5e73f21` |
| `artifacts/phase2/knowledge_registry/claim_dedup_relation_consolidation_report_v1.json` | `fc4fc76438d25d917fa49eb6a1fa9fa14eaeb8ad` |
| `artifacts/phase2/knowledge_registry/claim_dedup_stage1_report_v1.json` | `972e0936aa7dcc8f06eff061492429fe0b244878` |
| `artifacts/phase2/knowledge_registry/claim_exact_canonicalization_report_v1.json` | `662c91e2c6333d58027a63449c79bfb3986c67ad` |
| `artifacts/phase2/knowledge_registry/claim_extraction_full_report_v1.json` | `7a4b3ec9ed753c1010382e213c826b20924475d5` |
| `artifacts/phase2/knowledge_registry/claim_extraction_pilot_final_report_v1.json` | `04e3bc4c42260a26376c316ea40870dc2ac391b2` |
| `artifacts/phase2/knowledge_registry/claim_extraction_pilot_report_v1.json` | `16fa46fd59ac9023dde26a1bd88d579941428e94` |
| `artifacts/phase2/knowledge_registry/claim_extraction_pilot_report_v2.json` | `2535f9c3f10dd6e2035985ebecaf952e01de4e89` |
| `artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v1.json` | `c80d0786a847359d015a5b339511e499cc46900b` |
| `artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v2.json` | `07b7b514e440d2ad54b7d3c4c1152fb1dc3d76c5` |
| `artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v3.json` | `a8a4e1afeae31ec9ebf3ce6a985183a4c05cf418` |
| `artifacts/phase2/knowledge_registry/claim_extraction_prompt_window_contract_v1.json` | `2c8860a8c6b823b954ec4751e62f1eb1969786e9` |
| `artifacts/phase2/knowledge_registry/claim_extraction_unit_contract_v1.json` | `46530041153c51b4f1f9c2b0938255ac4c35d7b4` |
| `artifacts/phase2/knowledge_registry/claim_extraction_validation_contract_v1.json` | `c844a3171536211567451d429cebae6809630ecd` |
| `artifacts/phase2/knowledge_registry/claim_registry_contract_v1.json` | `9fc73c93471917a45de54127d870f97a9e560a14` |
| `artifacts/phase2/knowledge_registry/claim_registry_report_v1.json` | `ecbf7db111a5f89e0e272a2e4bfcb4551fbfb5aa` |
| `artifacts/phase2/knowledge_registry/claim_relation_projection_report_v1.json` | `44887d8e35aec67a94e8eae828edc9b0920cead8` |
| `artifacts/phase2/knowledge_registry/claim_semantic_candidate_generation_report_v1.json` | `9caf691c31a1ac83f6d750ed7732f9a0d13e2baa` |
| `artifacts/phase2/knowledge_registry/claim_semantic_candidate_selection_report_v1.json` | `0a32240f6d20486c5197b9001b66edb3c5a1158d` |
| `artifacts/phase2/knowledge_registry/claim_semantic_relation_full_report_v1.json` | `1b81d3b733dfbe3faa1ac99c07ec68036222ba5d` |
| `artifacts/phase2/knowledge_registry/claim_semantic_relation_pilot_report_v1.json` | `8ba2f682640aa830ee93c9bca870a519832feb87` |
| `artifacts/phase2/knowledge_registry/claim_validation_full_report_v1.json` | `e598c141f83879b777903fc298139677a37ad9fe` |
| `artifacts/phase2/knowledge_registry/claim_validation_full_semantic_report_v1.json` | `dc80996d8c81674296102b7b306fe1d3f75afe0c` |
| `artifacts/phase2/knowledge_registry/knowledge_graph_build_report_v1.json` | `031dbf999e60fe397f037337b9ab6a9862b3b08d` |
| `artifacts/phase2/reranking/nb18_reranker_handoff_v1.json` | `5f61133553fb6d07f717686cbdd451a5defc4541` |
| `artifacts/phase2/reranking/reranker_configuration_v1.json` | `0cb1959eef52863ce959532cf4000763e2650bd9` |
| `artifacts/phase2/reranking/reranker_release_v1.json` | `df11a6df082389366c32e37cab557b124329e9de` |
| `artifacts/phase2/sparse_index/nb16_sparse_index_handoff_v1.json` | `e7db4a9c9eda698a9906cd68f7dee8b6c533446a` |
| `artifacts/phase2/sparse_index/sparse_index_release_v1.json` | `b42f28ea4c777b26988634932524b6790603d5b0` |
| `data/evaluation/rag_evaluation_20260709_153736.json` | `988045ea26fbbfaef7698ba9101473cf10a7e2bd` |
| `data/phase2/context/context_builder_v1/context_builder_manifest.json` | `464b6fab88c0b0410e815202104747568cda2043` |
| `data/phase2/context/context_builder_v1/context_builder_reload_validation_v1.json` | `7b6477b437fe1c2d1ef71a73211b04bfc7a94b63` |
| `data/phase2/retrieval/hybrid_retrieval_v1/hybrid_reload_validation_v1.json` | `888b7f47677039604f84414f21510efd5c9ead40` |
| `data/phase2/retrieval/hybrid_retrieval_v1/hybrid_retrieval_evidence_v1.json` | `942bef991e2ec7aa9b24ff428eb419efe9871dd4` |
| `data/phase2/retrieval/hybrid_retrieval_v1/hybrid_retrieval_manifest.json` | `5f275c7a82329d29909006b69a70ddd17101df84` |
| `data/phase2/retrieval/reranker_v1/reranker_evidence_v1.json` | `45eebb2dd617a8f3662ee56342b38fbaf693e9f4` |
| `data/phase2/retrieval/reranker_v1/reranker_manifest.json` | `a8e66616913b6119f4083819b3035903ef83f0bb` |
| `data/phase2/retrieval/reranker_v1/reranker_reload_validation_v1.json` | `4bcb52071b41039863f0aa1742dc46effb6847ab` |
| `notebooks/phase2/reports/phase2/sparse_test_evaluation_v1.json` | `5b2a5abf3919b560453109959a83c9181f10e367` |
| `reports/phase2/book_ingestion_acceptance_v1.json` | `5fa6bedbec8d93afaf7febca5e847e8c44d17f1a` |
| `reports/phase2/book_inventory_acceptance_v1.json` | `b12adecf068d237576d5e0e8355bdbe425a0b638` |
| `reports/phase2/competency_freeze_v1.json` | `5c600b11c719de04ad774dd4a6f433eada59ef0d` |
| `reports/phase2/context_builder_acceptance_v1.json` | `6ec63f7a90d207b1841999985d1a8e5663343286` |
| `reports/phase2/deduplication_quality_acceptance_v1.json` | `f4343f6e7f2505e61bc399a1ae79dfd4f793dc18` |
| `reports/phase2/dense_index_acceptance_v1.json` | `e3f5b7ed5a9a02de516797e7755b6d056eac311e` |
| `reports/phase2/embedding_benchmark_acceptance_v1.json` | `d8b7180930b43e40dbded9532d5f19b1cae0a05d` |
| `reports/phase2/environment_baseline_v1.json` | `ede415ad9c396c18253ae46c653a3c15941155aa` |
| `reports/phase2/golden_dataset_final_adjudicated_acceptance_v1.json` | `4b0d42123372d8aa4e39d65635e06ab243ae3c85` |
| `reports/phase2/hybrid_retrieval_acceptance_v1.json` | `5f9234f559491a9688b13040de5bc9ded72e982f` |
| `reports/phase2/persian_normalization_acceptance_v1.json` | `dbcd154389550a2f54db679a4dffcbf27a5aa8bb` |
| `reports/phase2/reranker_acceptance_v1.json` | `10d6d1ff9bd8a0c344913651ea47f22308a53a28` |
| `reports/phase2/sparse_index_acceptance_v1.json` | `15cce973ae782e8ba6b3aa293e393481b0eab8db` |
| `reports/phase2/taxonomy_freeze_v1.json` | `bed535892cce4ce3e778b9aab22104bc3cb6cf26` |
| `reports/phase2/transcript_ingestion_acceptance_v1.json` | `896906c90fa47aa6d8dcea265d4d7d95cc91dfd5` |
| `reports/phase2/transcript_inventory_acceptance_v1.json` | `581e3c768b9d19ccb0c4077f576821f8f25fed0a` |
| `reports/phase2/unified_schema_lineage_acceptance_v1.json` | `ca6804bfce0fcf707a770d9d09b49817872abbb2` |
| `reports/phase2/website_acceptance_v1.json` | `b261ece9d4dab83f275e1233c0356a86c3fa2a82` |

## پیوست پ — ورودی مکالمه و وضعیت جدیدتر

ممیزی پیوست با نام `RAG_finance_NB21_prior_work_reuse_audit_fa(1).md` در همین گفتگو خوانده شد. وضعیت C118/C119 و سیاست هزینه‌ای گزارش‌شده در آن، شاهد فایل پیوست است؛ این ممیزی آن‌ها را به‌عنوان نسخهٔ تازهٔ مخزن معرفی نمی‌کند. این گزارش یک سند تکمیلی جدید است و فایل پیوست یا فایل مخزن را جایگزین نمی‌کند.


</div>
