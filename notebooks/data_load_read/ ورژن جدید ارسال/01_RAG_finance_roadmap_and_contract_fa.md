# ۱. نقشه، دامنه و قرارداد پروژهٔ RAG_finance

**نسخهٔ مجموعه:** ۱٫۰ — ۲۳ اکتبر ۲۰۲۶. این سند قرارداد و مسیر را توضیح می‌دهد؛ وضعیت اجرای هر الزام در فایل ۲ است.

## راه استفاده از چهار فایل

| فایل | چه زمانی خوانده شود؟ | مسئولیت |
| --- | --- | --- |
| ۱ — نقشه و قرارداد | شروع پروژه، تغییر دامنه یا اختلاف نقشه‌ها | هدف، ترتیب مراحل، منابع، معیارها و تحویل |
| ۲ — شواهد و وضعیت | ادامهٔ هر چت و انتخاب گام بعد | انجام‌شده‌ها، خروجی‌ها، موانع و جلوگیری از دوباره‌کاری |
| ۳ — API | طراحی یا اجرای هر بستهٔ مدل | اتصال، قرارداد درخواست، هزینه، Cache، خطا و Resume |
| ۴ — همکاری و کدنویسی | شروع هر چت اجرایی | قالب پاسخ، سل‌ها، رفع خطا، استقلال و پایان Notebook |

دو فایل ۳ و ۴ هستهٔ قابل استفاده در پروژه‌های دیگر دارند؛ بخش‌های مشخصات RAG_finance به‌طور جدا علامت خورده‌اند. مدل، هزینه، مسیر و مجوز همین پروژه به پروژهٔ دیگر منتقل نمی‌شود. برای ادامهٔ عادی RAG چهار فایل کافی‌اند؛ اصل ۱۶ پیوست این نوبت دوباره لازم نیست. نوت‌بوک یا Artifact محلیِ جدید و تعیین‌کننده همچنان باید در دسترس باشد.

## مرجعیت و حل تعارض

۱. دستور صریح و جدید کاربر برای همان موضوع مقدم است. ۲. نقشهٔ معتبر دامنه و مسئولیت را تعیین می‌کند. ۳. قرارداد نسخه‌دار همان آزمایش، تعریف سنجش را تعیین می‌کند. ۴. خروجی واقعی و Artifact معتبر وضعیت اجرا را نشان می‌دهد. ۵. ممیزی و متن انتقال راهنمای یافتن شواهدند. این ترتیب مجوز تغییر خودسرانهٔ Golden، آستانه یا سیاست فریز‌شده نیست.

اگر تعارض قابل حل از اسناد نیست، دو گزاره، منشأ، اثر اجرایی و تصمیم لازم مشخص شود. اعداد و قواعد قدیمی از تاریخچه حذف نمی‌شوند، ولی دستور جاری تلقی نمی‌شوند. گفتن «مطمئن نیستم» از پرکردن شکاف با حدس بهتر است. توضیح و رأی همین دستیار، بدون شاهد صلاحیت و استقلال، Human Gold یا مرجع مستقل نیست.

### تعارض‌های شناخته‌شدهٔ این مجموعه

| موضوع | تفسیر لازم |
| --- | --- |
| نام NB21 تا NB23 | نام معتبر: Evaluation/Ablation، Release/Reproducibility، Phase3 Handoff. ترتیب قدیمی بخش ۲۶ Execution Protocol برای نام‌گذاری اجرا نشود. |
| اقدام فعال | متن Skill قدیمی تا C008/اقدام۲۰ است؛ تصمیم بعدی اقدامات۱۹–۲۱ را دامنه‌دار بسته و مسیر۲۲–۲۵ را فعال کرده است. وضعیت امروز از فایل۲ و خروجی جدید خوانده شود. |
| Mini و DeepSeek | راهنمای اتصال Mini تاریخی است؛ مدل اصلی ادامهٔ ثبت‌شده DeepSeek-V4-Flash است. |
| اجازهٔ API | تأییدخواهی هر درخواست کوچک، با سیاست هزینهٔ ثبت‌شدهٔ جدید جایگزین شده؛ اختلاف مرز دقیق۵۰۰هزار در فایل۳ صریح باقی است. |
| Rights | Gate محدودکنندهٔ مصنوعی و INTERNAL_EVALUATION_ONLY طبق Guardrails لغو شده‌اند؛ Metadata حقوقی حفظ می‌شود. این حکم، پذیرش کیفیت یا مجوز Git نیست. |
| پوشش Citation | Targetهای۰٫۹۰ و۹۵٪ در دو نقشه متفاوت‌اند؛ خودکار معیار آسان‌تر انتخاب نشود. مصوبهٔ مؤثر در اقدام۱۲ لازم است. |
| Health و Run All | استقلال Runtime و بازخوانی Artifact لازم است؛ خواندن execution_count نسخهٔ قدیمی دیسک در حین Run All معیار سلامت Runtime نیست. بررسی ساختاری نسخهٔ ذخیره‌شده جداست. |
| Imports و ماژول‌ها | Imports مرکزی و استفاده از کد پایدار موجود حفظ شود؛ استقلال از Kernel قبلی لازم است، تکثیر همهٔ توابع در هر سل لازم نیست. |

## مخزن و منابع دقیق

- مخزن: https://github.com/Shahbazi-Amir/RAG_finance
- شاخه: https://github.com/Shahbazi-Amir/RAG_finance/tree/rag-phase2
- نقشه‌ها: https://github.com/Shahbazi-Amir/RAG_finance/tree/rag-phase2/data/Road_Maps
- نوت‌بوک‌ها: https://github.com/Shahbazi-Amir/RAG_finance/tree/rag-phase2/notebooks/phase2
- برنامهٔ تفصیلی: https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_phase2_modular_notebooks_execution_plan.md
- نقشهٔ عملیاتی: https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_phase2_operational_roadmap.md
- نقشهٔ مادر: https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_master_roadmap.md
- چارچوب سؤال و اعتبارسنجی: https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_questions_assessments_and_validation_framework_fa.md
- چک‌لیست NB21: https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/NB21_remaining_work_checklist_fa.md
- چک‌لیست NB20: https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/NB20_remaining_work_checklist_fa.md

آخرین HEAD خوانده‌شده در ممیزی قبلی همین گفتگو `16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5` بود. این نوبت بازسازمان‌دهی پیوست‌هاست و بررسی تازهٔ HEAD یا اجرای Notebook نیست. HEAD محلی و remote و محتوای ذخیره‌نشده یکی نیستند. هیچ مسیر پیشنهادی نقشه صرفاً با نوشته‌شدن در نقشه، موجود یا ساخته‌شده محسوب نمی‌شود.

## محصول و مرز فازها

هدف، پاسخ تخصصی مستند از دانش اختصاصی، با حفظ صاحب گزاره، شاهد، محدودیت و قابلیت ارزیابی است. وجود یک Vector DB یا حجم زیاد داده شرط کافی پایان نیست. توصیهٔ شخصی خریدوفروش و پیش‌بینی پرریسک از آموزش عمومی سواد مالی تفکیک می‌شود.

| فاز | مسئولیت | تحویل |
| --- | --- | --- |
| ۱ | Demo و Baseline تاریخی | داده، تنظیمات، پاسخ‌ها، ارزیابی کوچک و محدودیت‌های فریز‌شده |
| ۲ | Knowledge/RAG Core سه‌منبعی | Dataset/Index نسخه‌دار، Retrieval، Context، پاسخ و Citation، Safety و Benchmark |
| ۳ | پلتفرم و عرضهٔ چندکاربره | API، احراز هویت، جداسازی کاربر، پایگاه‌داده، عملیات، استقرار و Restore |
| ۴ | ارزیابی آموزشی و مربیگری | آزمون، قواعد و محاسبه، مسیر یادگیری، اقدام، پیگیری و پنل مدیریت |

آماده‌سازی مستقل فاز بعد، اگر صریحاً مجاز باشد، پذیرش فاز۲ را ایجاد نمی‌کند. NB21 نباید مسئولیت استقرار، Restore کل محصول یا طراحی کامل فاز۳ را جذب کند.

## ترتیب نوت‌بوک‌ها و مسئولیت

| بازه | کار |
| --- | --- |
| ۰۰ | محیط، Baseline و نسخه‌ها |
| ۰۱–۰۲ | دریافت و پذیرش سایت |
| ۰۳–۰۴ | موجودی و استخراج کتاب |
| ۰۵–۰۶ | موجودی و استخراج Transcript |
| ۰۷ | Schema و Lineage مشترک |
| ۰۸ | نرمال‌سازی فارسی و نگهداری متن خام/نرمال |
| ۰۹ | Dedup و کیفیت |
| ۱۰ | Taxonomy، Authority و مهندسی دانش |
| ۱۱ | Candidateهای Chunking و Benchmark |
| ۱۲ و آرشیو خانوادهٔ۱۲ | Claim Registry، Golden، بازبینی، Repair و Freeze |
| ۱۳ | Embedding benchmark |
| ۱۴–۱۵ | Dense و Sparse Index |
| ۱۶–۱۷ | Hybrid و Reranking |
| ۱۸ | Context Builder |
| ۱۹ | Generation و Claim-level Citation |
| ۲۰،20b،20c | Answerability، Safety، Confidence و ممیزی‌های دامنه‌دار |
| ۲۱ و21b | Evaluation، شش Ablation، تحلیل خطا و Regression |
| ۲۲ | `22_release_and_reproducibility.ipynb` |
| ۲۳ | `23_phase3_handoff.ipynb` |

نام دقیق فایل‌های موجود و دارایی‌های خروجی در فایل۲ است. شمارهٔ سل، شمارهٔ Notebook و شمارهٔ اقدام چک‌لیست سه شناسهٔ متفاوت‌اند. ادامهٔ فیزیکی21b، Notebook۲۲ نیست.

## داده، Authority و انتساب

Corpus پذیرفته‌شدهٔ تاریخی۱۹۴۵۶ رکورد دارد: Website۵۲۹، Book۲۷۰۱، Transcript۱۶۲۲۶. مرجع پس از NB10 چهار لایه را ثبت کرده: Core primary۱۴۷۰۵، Supervised secondary۴۵۳، Contextual nonprimary۱۹۴۴ و Unresolved context۲۳۵۴. این‌ها شمارش تاریخی همان سندند؛ به‌روزرسانی از فایل واقعی انجام می‌شود.

سه مفهوم مستقل بمانند: Knowledge Authority برای جایگاه دانش، Source Attribution برای صاحب واقعی متن و Conversation Context برای فهم گفت‌وگو. مجاورت سؤال مجری با پاسخ دکتر، آن سؤال را به دکتر منتسب نمی‌کند. مقالهٔ تحت سردبیری، نوشتهٔ مستقیم سردبیر نیست.

کتاب: Work، Edition، File، Chapter/Section/Paragraph حفظ شوند. صفحه فقط با نسخهٔ صفحه‌بندی‌شدهٔ معتبر؛ وگرنه Anchor پایدار. Transcript: برنامه، قسمت، نقش گوینده، نوبت گفت‌وگو و زمانِ موجود نگهداری شوند؛ timestamp ناموجود ساخته نشود. Website: byline و شاهد نویسندگی/سردبیری مرجع باشند. Near-duplicate و ویرایش‌های متفاوت بدون قرارداد ادغام نشوند. Lineage همهٔ منابع حفظ شود.

## Taxonomy، Curriculum و شکاف دانش

هفت موضوع فریز‌شده: `financial_literacy_foundations`، `spending_saving_money_management`، `credit_debt_banking`، `work_income`، `investment`، `risk_insurance` و `financial_decision_making`.

Taxation ماژول آموزشی بدون والد موضوعی است؛ موضوع اصلی هشتم نیست. Curriculum/Subtopic با Topic و Module یکی نیست. واژه‌های عام مانند قیمت، سود و انتخاب Global alias یک موضوع نیستند. «مبانی سواد مالی» برچسب پیش‌فرض هر مفهوم مالی نیست. چندبرچسبی به مطالبهٔ مستقل نیاز دارد. پیشنهاد Topic یا Question type با نگاشت پذیرفته‌شده فرق دارد؛ Missing با حدس تکمیل نشود.

پوشش کم Transcript، شکست Retrieval یا نبود واژه در evidence_terms به‌تنهایی Knowledge Gap یا OUT_OF_SCOPE را ثابت نمی‌کند. مرز کاتالوگ حل‌نشده با ابهام سؤال فرق دارد. Chunking نمی‌تواند Taxonomy را بازطراحی کند. جزئیات Program-specific context، Competency، prerequisite، learning stages و قرارداد Chunk در بخش‌های کامل مرجع داده در انتهای همین فایل حفظ شده‌اند.

## قرارداد سنجش و شش Ablation

Golden فعال تاریخی۳۸۱۳ QA است: Development۲۶۶۴ و Test۱۱۴۹. Development برای انتخاب و مقایسه است. سابقهٔ مشاهدهٔ Test در پروژه موجود است؛ Test دست‌نخورده معرفی نشود و برای retuning مصرف نشود. ارزیابی قدیمی با جمعیت متفاوت، مقایسهٔ کنترل‌شدهٔ جدید نیست.

Recall با Hit، MRR@k با Full ranking، سلامت Citation با پشتیبانی معنایی و نمرهٔ Reranker با احتمال صحت پاسخ یکسان نیستند. هر جدول باید جمعیت، Eligible، Missing، مخرج، k، rank depth، Gold mapping، واحد تجمیع و محدودیت را نشان دهد. Slice بدون نگاشت معتبر با وضعیت روشن و تعداد گزارش شود.

شش مقایسهٔ لازم: حذف Normalization؛ Character در برابر Structure-aware؛ Dense در برابر Hybrid؛ حذف Reranker؛ حذف Source diversity؛ حذف Citation verifier. برای هرکدام، جزء واقعاً فعال، متغیر تغییرکرده، ورودی ثابت، نسخهٔ Index/Gold و لایهٔ اثر مشخص شوند. کنترل ساختاری، Proxy یا حذف یک گزینهٔ غیرفعال جای Ablation اصلی نیست. نتیجهٔ Context/Retrieval به کیفیت پاسخ تعمیم داده نشود.

Threshold و بودجه باید در قرارداد مؤثر تثبیت شوند؛ Target اولیهٔ نقشه، Gate مصوب فعلی نیست. اختلاف معیارها و سابقهٔ Test افشا شود. پوشش نامعین با حذف موارد سخت بهتر نشان داده نشود. حداقل تعداد بازبین یا آستانهٔ۵٪ از این مجموعه تصویب نمی‌شود.

## خروجی و شرط پایان

هر Notebook دارای ورودی نسخه‌دار، خروجی قابل بازخوانی، شرایط PASS/FAIL و Handoff مستقل است. هر خروجی مهم باید در حد نیاز مسیر و تعریف هش، Schema/version، تنظیمات، تعداد، منشأ، محدودیت و وضعیت داشته باشد. شرح الگوی نوشتن و Reload در فایل۴ است.

NB21 باید Benchmark، Ablation report، Error taxonomy، Failure cases، مقایسهٔ فاز۱ و Regression Gate و اتصال لازم برای NB22 را تحویل دهد. سلامت فنی، تکمیل ارزیابی، PASS کیفیت و پذیرش Release جدا هستند. ارزیابی سالم می‌تواند کیفیت نامطلوب و Gate=FAIL نشان دهد. گزارش معتبر با پایین‌آوردن پسینی Gate به PASS تبدیل نمی‌شود.

پایان فاز۲ علاوه بر NB21 به Release/Reproducibility و Handoff نیاز دارد. تا آن زمان، پذیرش ایمنی زنده، استقرار یا کل محصول از تیک‌های محدود نتیجه نمی‌شود. هیچ Gate حقوقی لغوشده دوباره ساخته نشود.

## پرامپت استفاده از این فایل

```text
این فایل قرارداد دامنهٔ پروژه است. وضعیت انجام کار را از فایل شواهد و آخرین خروجی بخوان. نقشه را با وضعیت تاریخی یا پیشنهاد اجرای آینده یکی نگیر. تعارض‌ها را مستند حل کن؛ مسئولیت Notebookها را جابه‌جا نکن و برای ادامهٔ معمول دوباره نقشه‌سازی نکن.
```


## راهنمای همراهان

- [1 — 01_RAG_finance_roadmap_and_contract_fa.md](01_RAG_finance_roadmap_and_contract_fa.md)
- [2 — 02_RAG_finance_evidence_and_notebook_status_fa.md](02_RAG_finance_evidence_and_notebook_status_fa.md)
- [3 — 03_API_execution_and_RAG_profile_fa.md](03_API_execution_and_RAG_profile_fa.md)
- [4 — 04_step_by_step_chat_and_notebook_protocol_fa.md](04_step_by_step_chat_and_notebook_protocol_fa.md)

## فهرست منابع ورودی و محل مصرف

| شناسه | فایل ورودی | جایگاه قطعات | SHA-256 بایت اصل |
| --- | --- | --- | --- |
| S01 | RAG_finance_chat_execution_protocol_fa(3).md | [2](02_RAG_finance_evidence_and_notebook_status_fa.md#s01-u002)، [3](03_API_execution_and_RAG_profile_fa.md#s01-u003)، [4](04_step_by_step_chat_and_notebook_protocol_fa.md#s01-u001) | `15a808cd9e415532c81897b6e924730145e27f81ead6971b64bd0af71a5268d0` |
| S02 | RAG_finance_data_dr_roudi_COMPLETE(5).md | [1](01_RAG_finance_roadmap_and_contract_fa.md#s02-u001) | `df63d3f0886abd294a7ee7bab38437fb7d3ec3fc85b21d83be317abc45485d9c` |
| S03 | RAG_finance_independent_audit_2026-08-20 (5).md | [1](01_RAG_finance_roadmap_and_contract_fa.md#s03-u001) | `8558445102d3f124df14a0564c3a2e1bfd3fa1124ee38b294f03462c977144eb` |
| S04 | RAG_finance_master_roadmap(5).md | [1](01_RAG_finance_roadmap_and_contract_fa.md#s04-u001) | `d5532545004506820f0577dec40f69b13a037c3d5d34f8ce609b76c573a12953` |
| S05 | RAG_finance_NB21_full_reuse_map_fa_20261023(5).md | [2](02_RAG_finance_evidence_and_notebook_status_fa.md#s05-u001) | `7f7fa66b053c9d5643e41f24b35fe26f1b98571057618567710aaa4819d4eaae` |
| S06 | RAG_finance_NB21_prior_work_reuse_audit_fa(5).md | [2](02_RAG_finance_evidence_and_notebook_status_fa.md#s06-u001) | `3317ce455fa676232303db95eed144374a458537d02444dbcf41cb91334b292a` |
| S07 | RAG_finance_NB21_Project_Skill_Reference_FA(4).md | [1](01_RAG_finance_roadmap_and_contract_fa.md#s07-u014)، [2](02_RAG_finance_evidence_and_notebook_status_fa.md#s07-u018)، [3](03_API_execution_and_RAG_profile_fa.md#s07-u007)، [4](04_step_by_step_chat_and_notebook_protocol_fa.md#s07-u001) | `2a6f7b5c7e19c704e5a8a3c7d8c2a2d3848d4262c030442f9d58b3d83d0c36f7` |
| S08 | RAG_finance_Phase2_before_NB21_transfer_fa_20261023(3).md | [2](02_RAG_finance_evidence_and_notebook_status_fa.md#s08-u001) | `172810c121e712aba9b0e7456b561b7bdc963798fa3e064ae55bd1b2a7090100` |
| S09 | RAG_finance_Phase2_Execution_Protocol_FA(5).md | [1](01_RAG_finance_roadmap_and_contract_fa.md#s09-u003)، [3](03_API_execution_and_RAG_profile_fa.md#s09-u008)، [4](04_step_by_step_chat_and_notebook_protocol_fa.md#s09-u001) | `139676ec06826b55bb40b51e6a9af4f97a2dbd13609c7488a828f3b6262f5a68` |
| S10 | RAG_finance_phase2_notebook_execution_guardrails_fa(5).md | [1](01_RAG_finance_roadmap_and_contract_fa.md#s10-u007)، [3](03_API_execution_and_RAG_profile_fa.md#s10-u014)، [4](04_step_by_step_chat_and_notebook_protocol_fa.md#s10-u001) | `69fc3d738f5f67193f5a3256a32be68d39733605766bfacf584a373cd695913a` |
| S11 | RAG_finance_phase2_operational_roadmap(5).md | [1](01_RAG_finance_roadmap_and_contract_fa.md#s11-u001) | `6f8d4502665e148cd099e0f8b811c4541d19bfaf862a2653493d0a1989b2b38c` |
| S12 | Universal Step-by-Step Coding Project Master Prompt — Revised v6(5).md | [4](04_step_by_step_chat_and_notebook_protocol_fa.md#s12-u001) | `1287af019b4736f1b74ef6cc1dddc3afa2658460db7e8de2c2106879a4825d08` |
| S13 | روش همکاری و پردازش API در RAG_finance : NB21(5).md | [2](02_RAG_finance_evidence_and_notebook_status_fa.md#s13-u011)، [3](03_API_execution_and_RAG_profile_fa.md#s13-u001)، [4](04_step_by_step_chat_and_notebook_protocol_fa.md#s13-u002) | `28f40d05cf4886e6477f3347a42dc37a77a6315112fd719e444d139eb2de2acb` |
| S14 | RAG_finance_model_connection_guide_FA(4).md | [3](03_API_execution_and_RAG_profile_fa.md#s14-u001) | `21334286106b69d800e7e509142c6bd0d07ad0ee7ff53ec322f2dcdeef4be1f2` |
| S15 | RAG_finance_phase2_API_audit_20261008(4).md | [2](02_RAG_finance_evidence_and_notebook_status_fa.md#s15-u001)، [3](03_API_execution_and_RAG_profile_fa.md#s15-u012) | `232afd80e846486f48b89c60fc5ee1218fe3b2a56f0212eeef64d78fde88a3b4` |
| S16 | NB21_remaining_work_checklist_fa(5).md | [2](02_RAG_finance_evidence_and_notebook_status_fa.md#s16-u001) | `271ba3edaff9530a9057bdfcc38c667d6c09f733eb89895b70b3cf95e1e965a6` |

## بخش منابع کامل و قابل ردیابی

این بخش، جزئیات اصلی منابع را نگه می‌دارد؛ خلاصهٔ آن‌ها نیست. بخش اجرایی ابتدای فایل، روش استفاده و تعارض‌ها را تعیین می‌کند. متن تاریخی داخل منبع، فرمان Resume امروز نیست. قطعات کاملاً یکسان فقط یک‌بار آمده‌اند و در محل تکرار، ارجاع صریح دارند. عنوان‌ها و پوشش HTML صرفاً برای خوانایی تنظیم شده‌اند؛ کد، عدد، مسیر، حکم و محدودیتِ یکتای منابع حذف نشده است.

هر قطعه شناسهٔ ثابت Sxx.xxx دارد؛ این شناسه برای ارجاع سند است و شمارهٔ سل یا اقدام پروژه نیست. با جست‌وجوی نام منبع، شناسه، Cell، مسیر یا هش می‌توان مستقیم به بخش لازم رفت. منابع کامل را لازم نیست در هر نوبت دوباره از ابتدا بخوانید.

## فهرست بخش‌های کامل این فایل

- [S02.001 — معرفی، نسخه و منشأ سند](#s02-u001)
- [S02.002 — مرجع جامع داده‌ها، Knowledge Authority و قیود طراحی RAG Finance — Dr. Komeil Roudi](#s02-u002)
- [S02.003 — 1. هدف این سند](#s02-u003)
- [S02.004 — 2. سه مفهوم که هرگز نباید با هم یکی شوند](#s02-u004)
- [S02.005 — 2.1. Knowledge Authority](#s02-u005)
- [S02.006 — 2.2. Source Attribution](#s02-u006)
- [S02.007 — 2.3. Conversation Context](#s02-u007)
- [S02.008 — 3. Corpus پذیرفته‌شده Phase 2](#s02-u008)
- [S02.009 — 4. مدل رسمی Knowledge Authority پس از NB10](#s02-u009)
- [S02.010 — Tier 1 — CORE_PRIMARY_KNOWLEDGE](#s02-u010)
- [S02.011 — Tier 2 — SUPERVISED_SECONDARY_KNOWLEDGE](#s02-u011)
- [S02.012 — Tier 3 — CONTEXTUAL_NONPRIMARY](#s02-u012)
- [S02.013 — Tier 4 — UNRESOLVED_CONTEXT](#s02-u013)
- [S02.014 — 5. Website Data](#s02-u014)
- [S02.015 — 6. Book Data](#s02-u015)
- [S02.016 — 7. Transcript Data](#s02-u016)
- [S02.017 — 7.1. Authority profile رسمی Transcript](#s02-u017)
- [S02.018 — 8. سیاست Speaker در Transcript](#s02-u018)
- [S02.019 — 9. Program-specific Context](#s02-u019)
- [S02.020 — `program:khane-to`](#s02-u020)
- [S02.021 — `program:asre-shirin`](#s02-u021)
- [S02.022 — `program:chehelston`](#s02-u022)
- [S02.023 — `program:uni-tehran`](#s02-u023)
- [S02.024 — 10. Deduplication Policy](#s02-u024)
- [S02.025 — 11. Rights / Release Gate](#s02-u025)
- [S02.026 — 12. Frozen Taxonomy v1](#s02-u026)
- [S02.027 — 12.1. هفت Top-level Topic](#s02-u027)
- [S02.028 — 13. Curriculum Nodes فریز‌شده](#s02-u028)
- [S02.029 — 14. Taxation](#s02-u029)
- [S02.030 — 15. Context-dependent Terms](#s02-u030)
- [S02.031 — 16. Behavioral Economics](#s02-u031)
- [S02.032 — 17. Frozen Competency / Prerequisite v1](#s02-u032)
- [S02.033 — 18. Learning Stages](#s02-u033)
- [S02.034 — 19. Knowledge Gap Policy](#s02-u034)
- [S02.035 — 20. چرا Transcript Mapping پایین به معنی Gap نیست](#s02-u035)
- [S02.036 — 21. Local Conversation Context Discovery](#s02-u036)
- [S02.037 — 22. الزامات Chunking برای Book](#s02-u037)
- [S02.038 — 23. الزامات Chunking برای Website](#s02-u038)
- [S02.039 — 24. الزامات Chunking برای Transcript](#s02-u039)
- [S02.040 — 25. Chunking نباید Taxonomy را بازنویسی کند](#s02-u040)
- [S02.041 — 26. Chunk Lineage Contract پیشنهادی](#s02-u041)
- [S02.042 — 27. Chunk ID](#s02-u042)
- [S02.043 — 28. Chunk Size نباید از قبل فرض شود](#s02-u043)
- [S02.044 — 29. معیارهای ارزیابی Chunking](#s02-u044)
- [S02.045 — Structural](#s02-u045)
- [S02.046 — Authority / Attribution](#s02-u046)
- [S02.047 — Retrieval](#s02-u047)
- [S02.048 — Context quality](#s02-u048)
- [S02.049 — Citation](#s02-u049)
- [S02.050 — 30. Golden / Evaluation Dataset برای Chunking](#s02-u050)
- [S02.051 — Book](#s02-u051)
- [S02.052 — Website](#s02-u052)
- [S02.053 — Transcript](#s02-u053)
- [S02.054 — 31. Final retrieval behavior مطلوب](#s02-u054)
- [S02.055 — 32. Open Gates که NB11 نباید فراموش کند](#s02-u055)
- [S02.056 — 33. Source of Truth برای شروع NB11](#s02-u056)
- [S02.057 — Accepted corpus](#s02-u057)
- [S02.058 — NB09 acceptance](#s02-u058)
- [S02.059 — Frozen taxonomy](#s02-u059)
- [S02.060 — Taxonomy freeze report](#s02-u060)
- [S02.061 — Frozen competency](#s02-u061)
- [S02.062 — Competency freeze report](#s02-u062)
- [S02.063 — 34. قواعد انتقال به چت بعدی](#s02-u063)
- [S02.064 — 35. خلاصۀ یک‌خطی](#s02-u064)
- [S03.001 — معرفی، نسخه و منشأ سند](#s03-u001)
- [S03.002 — گزارش مستقل ممیزی فنی RAG_finance](#s03-u002)
- [S03.003 — ۱. Executive Summary](#s03-u003)
- [S03.004 — حکم نهایی کوتاه](#s03-u004)
- [S03.005 — امتیاز پیشرفت واقعی](#s03-u005)
- [S03.006 — تصمیم Go / No-Go](#s03-u006)
- [S03.007 — پنج فاصله بحرانی](#s03-u007)
- [S03.008 — ۲. روش ممیزی و سطح اطمینان شواهد](#s03-u008)
- [S03.009 — شواهد مستقیم بررسی‌شده](#s03-u009)
- [S03.010 — شواهد غیرقابل بازاجرای مستقل در این ممیزی](#s03-u010)
- [S03.011 — ۳. وضعیت فعلی Repository](#s03-u011)
- [S03.012 — ۳.۱ ساختار کلیدی](#s03-u012)
- [S03.013 — ۳.۲ شاخه و تاریخچه](#s03-u013)
- [S03.014 — ۳.۳ داده‌های موجود](#s03-u014)
- [S03.015 — ۳.۴ Website Ingestion V2](#s03-u015)
- [S03.016 — ۳.۵ <bdi dir="ltr">Video/Transcript</bdi>](#s03-u016)
- [S03.017 — ۳.۶ Book](#s03-u017)
- [S03.018 — ۳.۷ RAG و Application قدیمی](#s03-u018)
- [S03.019 — ۴. ماتریس تطبیق با Roadmap فاز ۲](#s03-u019)
- [S03.020 — <bdi dir="ltr">Phase 2 Foundation</bdi>](#s03-u020)
- [S03.021 — <bdi dir="ltr">Website Pipeline</bdi>](#s03-u021)
- [S03.022 — <bdi dir="ltr">Video Pipeline</bdi>](#s03-u022)
- [S03.023 — <bdi dir="ltr">Book Pipeline</bdi>](#s03-u023)
- [S03.024 — <bdi dir="ltr">Unified Dataset</bdi>](#s03-u024)
- [S03.025 — <bdi dir="ltr">RAG Layer</bdi>](#s03-u025)
- [S03.026 — <bdi dir="ltr">Evaluation</bdi>](#s03-u026)
- [S03.027 — ۵. بررسی معماری «Professional Financial Literacy Advisory RAG»](#s03-u027)
- [S03.028 — <bdi dir="ltr">Multi-source Architecture</bdi>](#s03-u028)
- [S03.029 — <bdi dir="ltr">Data Lineage</bdi>](#s03-u029)
- [S03.030 — Citation و دفاع‌پذیری](#s03-u030)
- [S03.031 — کنترل Hallucination](#s03-u031)
- [S03.032 — معماری هدف پیشنهادی](#s03-u032)
- [S03.033 — ۶. ارزیابی آمادگی دانش‌بنیان](#s03-u033)
- [S03.034 — معیار رسمی و دامنه اطمینان](#s03-u034)
- [S03.035 — آیا پروژه فعلی فقط «مدل آماده + Vector DB» است؟](#s03-u035)
- [S03.036 — وضعیت مؤلفه‌های دفاع‌پذیری](#s03-u036)
- [S03.037 — ریسک‌های خاص پرونده](#s03-u037)
- [S03.038 — نتیجه دانش‌بنیان](#s03-u038)
- [S03.039 — ۷. تفاوت «دستیار هوشمند سواد مالی» با «جستجوی متن»](#s03-u039)
- [S03.040 — قابلیت‌های ضروری محصول](#s03-u040)
- [S03.041 — روش صحیح Confidence](#s03-u041)
- [S03.042 — ۸. Roadmap اصلاحی اولویت‌بندی‌شده](#s03-u042)
- [S03.043 — P0 — ضروری؛ پیش از توسعه قابلیت‌های نمایشی بیشتر](#s03-u043)
- [S03.044 — P1 — مهم؛ برای محصول قابل ارائه و پرونده قوی](#s03-u044)
- [S03.045 — P2 — بهبود و تمایز بیشتر](#s03-u045)
- [S03.046 — ۹. Benchmark و آزمایش‌های الزامی](#s03-u046)
- [S03.047 — Baselineهایی که باید مقایسه شوند](#s03-u047)
- [S03.048 — <bdi dir="ltr">Metrics</bdi>](#s03-u048)
- [S03.049 — روش علمی گزارش](#s03-u049)
- [S03.050 — ۱۰. نمودارها و گزارش‌های لازم](#s03-u050)
- [S03.051 — نمودارها](#s03-u051)
- [S03.052 — گزارش‌ها](#s03-u052)
- [S03.053 — ۱۱. ساختار پیشنهادی Repository نهایی](#s03-u053)
- [S03.054 — ۱۲. فهرست مدارک لازم برای ارائه دانش‌بنیان](#s03-u054)
- [S03.055 — مدارک محصول و فناوری](#s03-u055)
- [S03.056 — مدارک دانش فنی و R&D](#s03-u056)
- [S03.057 — مدارک داده و حقوق](#s03-u057)
- [S03.058 — مدارک تجاری و عملیاتی](#s03-u058)
- [S03.059 — مدارک Safety و دامنه محصول](#s03-u059)
- [S03.060 — ۱۳. Acceptance Criteria برای پایان هر فاز](#s03-u060)
- [S03.061 — پایان Data Foundation](#s03-u061)
- [S03.062 — پایان Retrieval](#s03-u062)
- [S03.063 — پایان Safety](#s03-u063)
- [S03.064 — پایان Productization](#s03-u064)
- [S03.065 — ۱۴. مشکلاتی که باید فوراً اصلاح یا شفاف شوند](#s03-u065)
- [S03.066 — ۱۵. نظر نهایی Auditor](#s03-u066)
- [S03.067 — ضمیمه A — مسیر اجرایی پیشنهادی ۱۲ مرحله‌ای](#s03-u067)
- [S03.068 — ضمیمه B — وضعیت Production Readiness](#s03-u068)
- [S03.069 — ضمیمه C — اسناد Repository مشاهده‌شده](#s03-u069)
- [S04.001 — معرفی، نسخه و منشأ سند](#s04-u001)
- [S04.002 — نقشه کلان چهار فاز RAG_finance](#s04-u002)
- [S04.003 — ۱. تعریف محصول نهایی](#s04-u003)
- [S04.004 — ۲. چرا کاربر باید این محصول را به AI عمومی ترجیح دهد؟](#s04-u004)
- [S04.005 — ۳. معماری کلان قابلیت‌ها](#s04-u005)
- [S04.006 — ۴. نقشه چهار فاز](#s04-u006)
- [S04.007 — ۵. فاز ۱ - Baseline و میراث قابل استفاده](#s04-u007)
- [S04.008 — ۶. فاز ۲ - Knowledge & RAG Core](#s04-u008)
- [S04.009 — هدف](#s04-u009)
- [S04.010 — سه خانواده منبع](#s04-u010)
- [S04.011 — خروجی](#s04-u011)
- [S04.012 — Gate](#s04-u012)
- [S04.013 — ۷. فاز ۳ - Platform & Launch](#s04-u013)
- [S04.014 — هدف](#s04-u014)
- [S04.015 — خروجی](#s04-u015)
- [S04.016 — Gate](#s04-u016)
- [S04.017 — ۸. فاز ۴ - مربی سواد مالی و پنل مدیریت](#s04-u017)
- [S04.018 — هدف](#s04-u018)
- [S04.019 — خروجی کاربر](#s04-u019)
- [S04.020 — خروجی پنل مدیریت](#s04-u020)
- [S04.021 — Gate](#s04-u021)
- [S04.022 — ۹. قرارداد تحویل بین فازها](#s04-u022)
- [S04.023 — ۱۰. مسیر دانش فنی و دانش‌بنیان](#s04-u023)
- [S04.024 — ۱۱. قواعد مشترک اجرای پروژه](#s04-u024)
- [S04.025 — ۱۲. شاخص نهایی موفقیت](#s04-u025)
- [S04.026 — ۱۳. تصمیم نهایی](#s04-u026)
- [S07.014 — ۸. مخزن، شاخه، مسیرها و اختیار](#s07-u014)
- [S07.015 — ۹. دامنهٔ رسمی و تقدم نقشه‌ها](#s07-u015)
- [S07.016 — ۱۰. قیود دانش و سه منبع](#s07-u016)
- [S07.017 — ۱۱. تاکسونومی و وضعیت نگاشت](#s07-u017)
- [S09.003 — 1. اصل حاکم: وفاداری کامل به نقشه‌ی اصلی](#s09-u003)
- [S09.012 — 10. Scope Creep ممنوع](#s09-u012)
- [S09.013 — 11. Research Path و Production Path جدا بمانند](#s09-u013)
- [S09.020 — 18. داده و Artifact فریز‌شده دست‌نخورده بماند](#s09-u020)
- [S09.021 — 19. Historical Notebookها و مسیر Canonical مخلوط نشوند](#s09-u021)
- [S09.022 — 20. Benchmark باید روی داده‌ی واقعی پروژه باشد](#s09-u022)
- [S09.023 — 21. Metric بدون تفسیر کافی نیست](#s09-u023)
- [S09.031 — 26. ترتیب رسمی ادامه Phase 2 حفظ شود](#s09-u031)
- [S10.007 — ۶. سیاست Development و Test](#s10-u007)
- [S10.015 — ۱۴. Metadata و عدم استنتاج](#s10-u015)
- [S10.016 — ۱۵. مجوز پروژه](#s10-u016)
- [S11.001 — معرفی، نسخه و منشأ سند](#s11-u001)
- [S11.002 — نقشه عملیاتی فاز ۲ RAG_finance](#s11-u002)
- [S11.003 — ۱. تعریف Done فاز ۲](#s11-u003)
- [S11.004 — ۲. مدل منشأ و مالکیت منابع](#s11-u004)
- [S11.005 — ۳. جریان کل فاز ۲](#s11-u005)
- [S11.006 — ۴. بسته P2-01 - Freeze و Baseline فاز ۱](#s11-u006)
- [S11.007 — کارها](#s11-u007)
- [S11.008 — خروجی](#s11-u008)
- [S11.009 — Gate](#s11-u009)
- [S11.010 — ۵. بسته P2-02 - Data Contract، Stable IDs و Versioning](#s11-u010)
- [S11.011 — کارها](#s11-u011)
- [S11.012 — خروجی](#s11-u012)
- [S11.013 — Gate](#s11-u013)
- [S11.014 — ۶. بسته P2-03 - Website Pipeline V2](#s11-u014)
- [S11.015 — کارها](#s11-u015)
- [S11.016 — Gate](#s11-u016)
- [S11.017 — ۷. بسته P2-04 - Book Pipeline](#s11-u017)
- [S11.018 — کارها](#s11-u018)
- [S11.019 — Gate](#s11-u019)
- [S11.020 — ۸. بسته P2-05 - Video/Audio Transcript Pipeline](#s11-u020)
- [S11.021 — کارها](#s11-u021)
- [S11.022 — Gate](#s11-u022)
- [S11.023 — ۹. بسته P2-06 - Canonical Dataset و Quality](#s11-u023)
- [S11.024 — کارها](#s11-u024)
- [S11.025 — معیار](#s11-u025)
- [S11.026 — ۱۰. بسته P2-07 - فارسی‌سازی و Source-aware Chunking](#s11-u026)
- [S11.027 — کارها](#s11-u027)
- [S11.028 — Gate](#s11-u028)
- [S11.029 — ۱۱. بسته P2-08 - Golden Dataset](#s11-u029)
- [S11.030 — طراحی پیشنهادی](#s11-u030)
- [S11.031 — هر رکورد](#s11-u031)
- [S11.032 — Gate](#s11-u032)
- [S11.033 — ۱۲. بسته P2-09 - Embedding و Index V2](#s11-u033)
- [S11.034 — کارها](#s11-u034)
- [S11.035 — Gate](#s11-u035)
- [S11.036 — ۱۳. بسته P2-10 - Retrieval Engineering](#s11-u036)
- [S11.037 — آزمایش‌ها](#s11-u037)
- [S11.038 — Metrics](#s11-u038)
- [S11.039 — Gate](#s11-u039)
- [S11.040 — ۱۴. بسته P2-11 - Context، Generation و Citation](#s11-u040)
- [S11.041 — کارها](#s11-u041)
- [S11.042 — Citation](#s11-u042)
- [S11.043 — Gate](#s11-u043)
- [S11.044 — ۱۵. بسته P2-12 - Answerability، Safety و Confidence](#s11-u044)
- [S11.045 — Taxonomy درخواست](#s11-u045)
- [S11.046 — Confidence](#s11-u046)
- [S11.047 — Gate](#s11-u047)
- [S11.048 — ۱۶. بسته P2-13 - Tests، CI و Reproducibility](#s11-u048)
- [S11.049 — Gate](#s11-u049)
- [S11.050 — ۱۷. بسته P2-14 - مستندات دانش فنی](#s11-u050)
- [S11.051 — ۱۸. ترتیب اجرای واقعی](#s11-u051)
- [S11.052 — ۱۹. Gate نهایی و تحویل به فاز ۳](#s11-u052)
- [S11.053 — ۲۰. معیارهای پیشنهادی اولیه](#s11-u053)
- [S11.054 — ۲۱. تصمیم اجرایی](#s11-u054)


## جزئیات منبع S02

> فایل اصلی: RAG_finance_data_dr_roudi_COMPLETE(5).md
>
> مرجع داده و Authority پس از NB10؛ شمارش‌ها و Gateهای قدیمی وضعیت امروز نیستند. بخش اجرایی ابتدای این فایل، قاعدهٔ استفاده از متن زیر است.



<a id="s02-u001"></a>

### S02.001 — معرفی، نسخه و منشأ سند




<a id="s02-u002"></a>

### S02.002 — مرجع جامع داده‌ها، Knowledge Authority و قیود طراحی RAG Finance — Dr. Komeil Roudi

#### مرجع جامع داده‌ها، Knowledge Authority و قیود طراحی RAG Finance — Dr. Komeil Roudi

**نسخه:** پس از تکمیل Notebook 10 — Taxonomy & Knowledge Engineering  
**وضعیت:** مرجع انتقالی برای ادامه Phase 2 و طراحی Chunking / Retrieval  
**Primary Knowledge Authority:** Dr. Komeil Roudi

---


<a id="s02-u003"></a>

### S02.003 — 1. هدف این سند

#### 1. هدف این سند

این سند مرجع ثابت برای درک ماهیت داده‌های پروژه `RAG_finance` و نحوۀ استفاده از آن‌ها در مراحل بعدی RAG است.

هدف پروژه ساخت یک Knowledge Base عمومی مالی نیست. هدف، ساخت یک RAG تخصصی است که:

- دانش مستقیم دکتر کمیل رودی را در بالاترین سطح Authority نگه دارد؛
- محتوای تحت نظارت ایشان را به‌عنوان Secondary Evidence حفظ کند؛
- سؤال‌ها، مجری‌ها، مهمان‌ها و شرکت‌کنندگان را برای Context نگه دارد؛
- هیچ محتوایی را فقط به دلیل حضور در Corpus به دکتر نسبت ندهد؛
- Lineage، Source Identity، Attribution، Rights و Locator را در تمام مراحل حفظ کند؛
- در Retrieval و Generation بتواند میان «دانش مستقیم دکتر»، «دانش تحت نظارت»، «Context مکالمه» و «Context حل‌نشده» تفاوت واقعی ایجاد کند.

اصل مرکزی پروژه:

> **Primary Knowledge Structure باید از Core Primary Corpus استخراج شود و پراکندگی Secondary / Guest / Contextual content نباید ساختار دانش اصلی را بازطراحی کند.**

---


<a id="s02-u004"></a>

### S02.004 — 2. سه مفهوم که هرگز نباید با هم یکی شوند

#### 2. سه مفهوم که هرگز نباید با هم یکی شوند

در تمام Pipeline باید این سه مفهوم جدا بمانند:


<a id="s02-u005"></a>

### S02.005 — 2.1. Knowledge Authority

##### 2.1. Knowledge Authority

این Evidence تا چه حد مجاز است ساختار دانش اصلی پروژه را تعریف کند.


<a id="s02-u006"></a>

### S02.006 — 2.2. Source Attribution

##### 2.2. Source Attribution

متن واقعاً توسط چه فرد یا Source تولید شده است.


<a id="s02-u007"></a>

### S02.007 — 2.3. Conversation Context

##### 2.3. Conversation Context

متنی که لزوماً Primary Knowledge نیست، اما برای فهم سؤال، پاسخ، استدلال یا ادامۀ گفتگو لازم است.

مثال:

1. سؤال مجری
2. پاسخ دکتر
3. سؤال تکمیلی شرکت‌کننده
4. توضیح تکمیلی دکتر

در چنین حالتی Context باید حفظ شود، اما سؤال مجری یا شرکت‌کننده نباید به دکتر Attribution شود.

---


<a id="s02-u008"></a>

### S02.008 — 3. Corpus پذیرفته‌شده Phase 2

#### 3. Corpus پذیرفته‌شده Phase 2

Artifact اصلی پذیرفته‌شده:

`data/phase2/processed/documents_dedup_quality_accepted_v1.jsonl`

تعداد کل:

**19,456 Document**

SHA256:

`9d72c709f81b1218c5aac064052c7ed1da34869f671e6e32762864e0ad70ea40`

توزیع Source Type:

| Source Type | تعداد |
|---|---:|
| Website | 529 |
| Book | 2,701 |
| Transcript | 16,226 |
| **Total** | **19,456** |

این Dataset برای Internal Phase 2 Processing پذیرفته شده است.

نکتۀ مهم:

> Processing Acceptance با Formal Release Eligibility یکی نیست.

---


<a id="s02-u009"></a>

### S02.009 — 4. مدل رسمی Knowledge Authority پس از NB10

#### 4. مدل رسمی Knowledge Authority پس از NB10

پس از Reconciliation نهایی، کل Corpus در چهار لایۀ رسمی قرار می‌گیرد.


<a id="s02-u010"></a>

### S02.010 — Tier 1 — CORE_PRIMARY_KNOWLEDGE

##### Tier 1 — CORE_PRIMARY_KNOWLEDGE

**14,705 Document**

اجزاء:

- Book: **2,701**
- Website Direct Author: **76**
- Transcript Primary: **11,928**

این لایه تنها لایه‌ای است که می‌تواند ساختار اصلی Topic / Subtopic / Curriculum / Competency را تعریف یا تغییر دهد.


<a id="s02-u011"></a>

### S02.011 — Tier 2 — SUPERVISED_SECONDARY_KNOWLEDGE

##### Tier 2 — SUPERVISED_SECONDARY_KNOWLEDGE

**453 Document**

این لایه شامل Websiteهایی است که نویسندۀ مستقیم آن‌ها دکتر نیست، اما تحت نظارت / سردبیری / تأیید علمی ایشان منتشر شده‌اند.

کاربرد:

- Supporting Evidence
- Coverage Extension
- Retrieval Support
- Terminology Support
- Cross-check

اما:

> Tier 2 نباید Primary Taxonomy را override یا reshape کند.


<a id="s02-u012"></a>

### S02.012 — Tier 3 — CONTEXTUAL_NONPRIMARY

##### Tier 3 — CONTEXTUAL_NONPRIMARY

**1,944 Document**

عمدتاً شامل:

- Host
- Guest
- Participant
- Other explicit non-primary speaker
- Human-confirmed secondary guest

کاربرد:

- سؤال
- Context
- مقایسه
- Dialogue reconstruction
- فهم پاسخ دکتر

اما:

> نباید به‌عنوان دیدگاه مستقیم دکتر ارائه شود.


<a id="s02-u013"></a>

### S02.013 — Tier 4 — UNRESOLVED_CONTEXT

##### Tier 4 — UNRESOLVED_CONTEXT

**2,354 Document**

Speaker یا Attribution این Segmentها با Evidence فعلی به‌طور قابل اتکا حل نشده است.

سیاست:

- حذف نشوند.
- به دکتر نسبت داده نشوند.
- برای Context و Review حفظ شوند.
- تا وجود Evidence جدید در ساختار Primary Knowledge اثر تعیین‌کننده نداشته باشند.

---


<a id="s02-u014"></a>

### S02.014 — 5. Website Data

#### 5. Website Data

کل Website:

**529**

تقسیم رسمی:

- Direct Author / Primary: **76**
- Editorial Supervision / Secondary: **453**

اصل:

> Direct Author و Editorial Supervision دو سطح Evidence متفاوت هستند.

برای Retrieval پاسخ‌هایی مانند «نظر دکتر چیست؟» یا «دکتر چه می‌گوید؟»، Direct Author باید بر Secondary اولویت داشته باشد.

453 مقالۀ تحت نظارت همچنان ارزشمند هستند، اما نباید به شکل «نوشتۀ مستقیم دکتر» Citation یا Generation شوند.

---


<a id="s02-u015"></a>

### S02.015 — 6. Book Data

#### 6. Book Data

کل Book Documentها:

**2,701**

کتاب‌ها از قوی‌ترین منابع Primary Corpus هستند.

در طراحی RAG باید بین مفاهیم زیر تفاوت حفظ شود:

`Work != Edition != File`

موارد مهمی که باید در Chunking و Retrieval حفظ شوند:

- Work ID
- Edition ID در صورت وجود
- Heading Path
- Section / Chapter relation
- Page / stable locator فقط اگر واقعاً معتبر باشد
- Source lineage
- Parent / child structural relation
- document_id
- raw/source relation

کتاب‌ها فقط مجموعه‌ای از Paragraphهای مستقل نیستند؛ ساختار آموزشی و ترتیب Headingها در NB10 برای کشف Curriculum استفاده شده است.

بنابراین:

> Chunking کتاب نباید Heading hierarchy را نابود کند.

---


<a id="s02-u016"></a>

### S02.016 — 7. Transcript Data

#### 7. Transcript Data

کل Transcript:

**16,226 Segment**


<a id="s02-u017"></a>

### S02.017 — 7.1. Authority profile رسمی Transcript

##### 7.1. Authority profile رسمی Transcript

- `PRIMARY_CANONICAL_ATTRIBUTION`: **11,209**
- `PRIMARY_EXPLICIT_SOURCE_MARKER`: **718**
- `PRIMARY_HUMAN_CONFIRMED_OVERLAY`: **1**
- `SECONDARY_HUMAN_CONFIRMED_OVERLAY`: **1**
- `NONPRIMARY_EXPLICIT_CONTEXT`: **1,943**
- `UNRESOLVED_SPEAKER_CONTEXT`: **2,354**

Transcript Primary Total:

**11,928**

Transcript Contextual Non-primary Total:

**1,944**

Unresolved:

**2,354**

---


<a id="s02-u018"></a>

### S02.018 — 8. سیاست Speaker در Transcript

#### 8. سیاست Speaker در Transcript

Canonical Speaker اصلی پروژه:

`Dr. Komeil Roudi`

ولی Canonical Attribution فقط با Evidence ثبت می‌شود.

قواعد:

1. Unknown Speaker inference ممنوع است.
2. Speaker label با Canonical Identity یکی نیست.
3. Alias فقط در Scope واقعی Program معتبر است.
4. Guest / Host / Participant باید هویت مستقل داشته باشند.
5. سؤال و Context نباید صرفاً به دلیل نزدیک بودن به پاسخ دکتر، به دکتر نسبت داده شود.
6. Human-confirmed overlays باید از Parser attribution قابل تفکیک بمانند.
7. Chunking نباید مرز Speaker را به شکل مخرب Merge کند.

اصل:

> **Preserve Context, do not collapse Attribution.**

---


<a id="s02-u019"></a>

### S02.019 — 9. Program-specific Context

#### 9. Program-specific Context

بعضی Programها Solo نیستند و Chunking آن‌ها باید Conversation-aware باشد.


<a id="s02-u020"></a>

### S02.020 — `program:khane-to`

##### `program:khane-to`

Human-confirmed structure:

- Dr. Komeil Roudi
- one host

7 Segment دارای labelهای غیرمنتظره در Review Queue باقی مانده‌اند.

این 7 مورد:

- حذف نشده‌اند،
- Hard Quarantine نشده‌اند،
- برای Review حفظ شده‌اند.


<a id="s02-u021"></a>

### S02.021 — `program:asre-shirin`

##### `program:asre-shirin`

Human-confirmed structure:

- دو Season
- Dr. Komeil Roudi
- یک مجری زن
- حدود 8 شرکت‌کنندۀ زن

Open metadata gap:

- `season_number` برای **902 Segment** موجود نیست.

این یک Metadata Gap است، نه Structural Failure.


<a id="s02-u022"></a>

### S02.022 — `program:chehelston`

##### `program:chehelston`

شامل Contextهایی با Guestهای دیگر است.

بنابراین:

- تمام Content آن Primary Dr. Roudi نیست.
- Speaker-aware / context-aware chunking ضروری است.
- Unlabeled / unresolved paragraphs نباید به‌صورت حدسی Primary شوند.


<a id="s02-u023"></a>

### S02.023 — `program:uni-tehran`

##### `program:uni-tehran`

دارای گفتگوها و Contextهای چندنفره است.

در NB10 دیده شد بعضی Conceptها مانند Taxation در Conversation alternation ظاهر می‌شوند:

- Segment مستقیم دکتر
- Segment سؤال / توضیح دیگران
- Segment unresolved

بنابراین chunking صرفاً بر اساس window ثابت بدون Speaker/Conversation boundary می‌تواند Attribution را خراب کند.

---


<a id="s02-u024"></a>

### S02.024 — 10. Deduplication Policy

#### 10. Deduplication Policy

NB09 نشان داد شباهت متنی به تنهایی اثبات Duplicate نیست.

نتایج:

- Exact Duplicate Groups: **192**
- Members: **931**
- Near-duplicate candidate pairs: **15,929**
- Cross-source candidate pairs: **37,796**
- Automatic deletion: **0**
- Automatic merge: **0**
- Automatic canonicalization: **0**

اصل:

> `Exact Duplicate ≠ Automatic Source Deletion`

و:

> `High Similarity ≠ Same Evidence`

در Chunking نیز این اصل ادامه دارد:

> دو Chunk مشابه از دو Source مختلف نباید صرفاً به دلیل similarity به یک Source واحد collapse شوند.

Source independence و lineage باید حفظ شود.

---


<a id="s02-u025"></a>

### S02.025 — 11. Rights / Release Gate

#### 11. Rights / Release Gate

در وضعیت فعلی:

- Internal Processing Allowed: **19,456**
- Formal Release Eligible: **0**
- Rights state: `EVIDENCE_REQUIRED`
- Release status: `BLOCKED_PENDING_RIGHTS`

اصل:

> `EVIDENCE_REQUIRED` یک Release Gate است، نه Data Quality Failure.

بنابراین Chunking داخلی Phase 2 مجاز است، ولی Export / Publication / Formal Release باید Rights-aware باقی بماند.

---


<a id="s02-u026"></a>

### S02.026 — 12. Frozen Taxonomy v1

#### 12. Frozen Taxonomy v1

Artifact:

`artifacts/phase2/taxonomy/taxonomy_v1.json`

SHA256:

`335690044b2e4eff684f7f347809f2c5cb8c39624a939dc01408d9ca898fe977`

Status:

`FROZEN`


<a id="s02-u027"></a>

### S02.027 — 12.1. هفت Top-level Topic

##### 12.1. هفت Top-level Topic

1. `financial_literacy_foundations`
2. `spending_saving_money_management`
3. `credit_debt_banking`
4. `work_income`
5. `investment`
6. `risk_insurance`
7. `financial_decision_making`

---


<a id="s02-u028"></a>

### S02.028 — 13. Curriculum Nodes فریز‌شده

#### 13. Curriculum Nodes فریز‌شده

Taxonomy v1 دارای **7 Curriculum Node** است.

مهم‌ترین ساختار استخراج‌شده از Primary Curriculum:

`work_income`  
→ `children_business`

و زیر آن:

- `goods_and_services_basics`
- `entrepreneurship_production_resources`
- `children_business_pricing`
- `children_business_profit`
- `product_presentation_and_promotion`

همچنین:

- `giving_and_gifting`

به‌عنوان Curriculum Node واقعی ثبت شده و Bridge آن به:

`spending_saving_money_management`

است.

---


<a id="s02-u029"></a>

### S02.029 — 14. Taxation

#### 14. Taxation

`taxation_and_financial_obligations`

به‌عنوان:

`CROSS_TOPIC_EDUCATIONAL_MODULE`

در Level 2 ثبت شده است.

قواعد:

- Top-level Topic جدید نیست.
- به زور زیر یک Topic خاص قرار نگرفته است.
- Global alias نیست.
- در Chunking باید بتوان Evidence آن را از چند Context نگه داشت.
- Retrieval بعداً می‌تواند Module-specific باشد بدون دستکاری Top-level Taxonomy.

---


<a id="s02-u030"></a>

### S02.030 — 15. Context-dependent Terms

#### 15. Context-dependent Terms

مفاهیمی مانند:

- انتخاب
- قیمت
- سود

در سطح Global به یک Topic واحد Alias نشده‌اند.

قیمت و سود فقط در Context مشخص `children_business` نقش Structural Local Subtopic دارند.

نتیجه برای Chunking:

> وجود term به تنهایی برای تعیین Topic Chunk کافی نیست؛ local structural context و source hierarchy مهم است.

---


<a id="s02-u031"></a>

### S02.031 — 16. Behavioral Economics

#### 16. Behavioral Economics

Evidence اصلی برای `behavioral_economics` در Core Primary Corpus برای Promotion به Core Taxonomy v1 کافی نبود.

وضعیت:

`NOT_PROMOTED_TO_CORE_TAXONOMY_V1`

بنابراین Secondary / Guest dispersion نباید در Chunking یا retrieval labeling باعث شود این مفهوم به شکل implicit به یک Core Topic تبدیل شود.

---


<a id="s02-u032"></a>

### S02.032 — 17. Frozen Competency / Prerequisite v1

#### 17. Frozen Competency / Prerequisite v1

Artifact:

`artifacts/phase2/competency/competency_prerequisite_v1.json`

SHA256:

`f12f6c1631d77f29042b2009ca9dc8dee406d23ccdccdbb103c0e8cade781e87`

Status:

`FROZEN`

ساختار:

- Competencies: **24**
- Top-level Topics: **7**
- Learning Stages: **6**
- Recommended Learning Progressions: **17**
- Hard Prerequisites: **0**
- Cross-topic prerequisite: **0**
- Cycles: **0**

اصل:

> Taxonomy Node الزاماً Competency مستقل ایجاد نمی‌کند.

---


<a id="s02-u033"></a>

### S02.033 — 18. Learning Stages

#### 18. Learning Stages

Stageها:

1. `understand`
2. `self_assess`
3. `analyze`
4. `plan`
5. `act`
6. `review_and_improve`

توزیع فعلی Competency:

- understand: 5
- self_assess: 7
- analyze: 2
- plan: 8
- act: 2
- review_and_improve: 0

خالی بودن `review_and_improve` در v1 Knowledge Gap اعلام نشده است.

---


<a id="s02-u034"></a>

### S02.034 — 19. Knowledge Gap Policy

#### 19. Knowledge Gap Policy

در این پروژه:

`Unmapped Document != Knowledge Gap`

و:

`Retrieval Failure != Knowledge Gap`

و:

`Secondary-only Evidence != Proof of Knowledge Gap`

Knowledge Gap واقعی فقط پس از حداقل این مراحل قابل اثبات است:

1. تعریف Target Competency / Learning Objective
2. بررسی Core Primary Evidence
3. بررسی Coverage
4. بررسی Chunkability
5. بررسی Indexability
6. بررسی Retrieval
7. رد Retrieval failure
8. بررسی Answerability
9. بررسی Citation support
10. سپس اعلام Knowledge Gap

---


<a id="s02-u035"></a>

### S02.035 — 20. چرا Transcript Mapping پایین به معنی Gap نیست

#### 20. چرا Transcript Mapping پایین به معنی Gap نیست

در NB10 Top-level observability در Core Primary Corpus حدود 36.7% بود، اما این عدد به تنهایی Quality Failure نیست.

به‌ویژه در Transcript:

- Segmentها ممکن است کوتاه باشند.
- معنی آن‌ها به turnهای قبل و بعد وابسته باشد.
- pronoun / ellipsis داشته باشند.
- Topic term در همان Segment ظاهر نشود.
- Speaker context در Segment مجاور باشد.

بنابراین Chunking حرفه‌ای می‌تواند بخش مهمی از مسئلۀ Retrievability را حل کند بدون اینکه Taxonomy تغییر کند.

---


<a id="s02-u036"></a>

### S02.036 — 21. Local Conversation Context Discovery

#### 21. Local Conversation Context Discovery

NB10 نشان داد Local Conversation Context برای Transcript ارزشمند است.

سیاست Audit اولیه:

- فقط همان Conversation Unit
- حداکثر 3 Neighbor قبل
- حداکثر 3 Neighbor بعد
- Program و Speaker name به‌تنهایی Topic vote ایجاد نمی‌کنند
- حداقل 2 Neighbor supporting
- حداقل support ratio برابر 2/3
- خروجی فقط `LOCAL_CONTEXT_CANDIDATE`
- بدون Rechunk
- بدون تغییر Document Topic

این نتیجه برای NB11 مهم است:

> Chunking Transcript باید Context را بازیابی‌پذیر کند، اما نباید Contextual speaker content را به Primary speaker collapse کند.

---


<a id="s02-u037"></a>

### S02.037 — 22. الزامات Chunking برای Book

#### 22. الزامات Chunking برای Book

NB11 نباید یک chunk size واحد را کورکورانه روی Book اعمال کند.

حداقل باید Benchmark شود:

- Heading-aware segmentation
- Paragraph grouping
- Section boundary
- maximum / target token size
- overlap policy
- short-section handling
- heading inheritance
- parent context
- stable locator preservation
- cross-page continuity
- activity / exercise boundaries
- table/list handling در صورت وجود

Chunk باید بتواند Heading path را حفظ کند.

---


<a id="s02-u038"></a>

### S02.038 — 23. الزامات Chunking برای Website

#### 23. الزامات Chunking برای Website

Website دو Authority class دارد:

- Direct Author
- Editorial Supervision

Chunk باید metadata لازم برای این تفاوت را نگه دارد.

Benchmark باید بررسی کند:

- heading-aware chunk
- paragraph chunk
- semantic grouping
- boilerplate separation
- citation URL / locator retention
- article title / tag context
- Authority metadata propagation

---


<a id="s02-u039"></a>

### S02.039 — 24. الزامات Chunking برای Transcript

#### 24. الزامات Chunking برای Transcript

Transcript احتمالاً حساس‌ترین Source Type پروژه است.

باید Benchmark شود:

- Turn-level chunking
- multi-turn conversational windows
- speaker-aware windows
- question-answer pairing
- answer + minimal preceding question
- topic-shift boundary
- conversation-unit boundary
- episode boundary
- overlap between adjacent conversational chunks
- unresolved speaker handling
- long monologue segmentation
- short utterance aggregation
- attribution contamination rate

قواعد سخت:

1. Episode/Conversation boundary نباید شکسته شود.
2. Speaker باید در metadata حفظ شود.
3. Chunk چندSpeakerه باید explicit participant/speaker composition داشته باشد.
4. Chunk نباید متن Guest را به Dr. Roudi attribution کند.
5. سؤال Context می‌تواند همراه پاسخ باشد، ولی Attribution داخلی باید قابل بازیابی بماند.
6. Context window باید benchmark شود، نه حدس زده شود.
7. Fixed-size-only strategy نباید بدون مقایسه پذیرفته شود.

---


<a id="s02-u040"></a>

### S02.040 — 25. Chunking نباید Taxonomy را بازنویسی کند

#### 25. Chunking نباید Taxonomy را بازنویسی کند

Taxonomy و Competency v1 Frozen هستند.

NB11 می‌تواند:

- Chunk metadata بسازد.
- Chunk → Topic candidate بسازد.
- Parent Document relation بسازد.
- Hierarchy context منتقل کند.
- Retrieval labels آزمایشی بسازد.

اما نباید بدون Version جدید و Evidence جدید:

- Top-level Topic اضافه کند.
- Curriculum Node حذف/اضافه کند.
- Competency تغییر دهد.
- Authority layer تغییر دهد.
- Attribution را بازنویسی کند.

---


<a id="s02-u041"></a>

### S02.041 — 26. Chunk Lineage Contract پیشنهادی

#### 26. Chunk Lineage Contract پیشنهادی

هر Chunk حداقل باید بتواند به این زنجیره برگردد:

`chunk_id`  
→ `document_id`  
→ `source_id`  
→ `source_type`  
→ `source lineage`  
→ raw/interim source  
→ stable locator

Metadata مهم:

- chunk_id
- parent_document_id
- source_type
- source_id
- language
- authority_layer
- author / speaker
- content_origin
- title
- heading_path در صورت وجود
- conversation / episode ID در Transcript
- chunk ordinal
- character/token offsets در صورت قابل اتکا بودن
- rights
- attribution
- lineage
- taxonomy references فقط به شکل versioned metadata

---


<a id="s02-u042"></a>

### S02.042 — 27. Chunk ID

#### 27. Chunk ID

Chunk ID باید:

- deterministic باشد؛
- stable parent relation داشته باشد؛
- با تغییر chunking version قابل تشخیص باشد؛
- collision نداشته باشد؛
- از index position موقت وابسته نباشد.

Naming نهایی باید بعد از Discovery conventions Repository تعیین شود و نباید از قبل تحمیل شود.

---


<a id="s02-u043"></a>

### S02.043 — 28. Chunk Size نباید از قبل فرض شود

#### 28. Chunk Size نباید از قبل فرض شود

قبل از انتخاب Production Strategy باید چند Candidate Strategy ساخته و مقایسه شود.

برای مثال:

- کوچک
- متوسط
- بزرگ
- structural
- semantic
- hybrid structural-semantic
- source-specific

معیار انتخاب نباید «رایج بودن» باشد.

معیار:

> measured retrieval + context quality + attribution integrity + citation precision

---


<a id="s02-u044"></a>

### S02.044 — 29. معیارهای ارزیابی Chunking

#### 29. معیارهای ارزیابی Chunking

حداقل دسته‌های Metric پیشنهادی:


<a id="s02-u045"></a>

### S02.045 — Structural

##### Structural

- chunk count
- token distribution
- very-short chunk rate
- overlong chunk rate
- boundary break rate
- empty chunk rate
- duplicate chunk rate
- parent lineage validity


<a id="s02-u046"></a>

### S02.046 — Authority / Attribution

##### Authority / Attribution

- speaker contamination rate
- multi-speaker ambiguity rate
- primary/nonprimary mixing profile
- unresolved-speaker handling


<a id="s02-u047"></a>

### S02.047 — Retrieval

##### Retrieval

در صورت ساخت Evaluation Set:

- Recall@k
- MRR
- nDCG
- hit rate


<a id="s02-u048"></a>

### S02.048 — Context quality

##### Context quality

- answer evidence completeness
- unnecessary context rate
- question-answer continuity
- topic coherence


<a id="s02-u049"></a>

### S02.049 — Citation

##### Citation

- citation correctness
- locator validity
- citation coverage

فقط Metricهای واقعاً محاسبه‌شده باید گزارش شوند.

---


<a id="s02-u050"></a>

### S02.050 — 30. Golden / Evaluation Dataset برای Chunking

#### 30. Golden / Evaluation Dataset برای Chunking

برای انتخاب Strategy باید Sampleهای نماینده از هر Source Type وجود داشته باشد.

ضروری است نمونه‌ها شامل موارد سخت باشند:


<a id="s02-u051"></a>

### S02.051 — Book

###### Book
- short heading
- long section
- exercise
- multi-topic page
- deep hierarchy
- children_business branch
- giving/gifting


<a id="s02-u052"></a>

### S02.052 — Website

###### Website
- direct author
- supervised
- short article
- long article
- multi-topic strong evidence
- boilerplate-heavy case


<a id="s02-u053"></a>

### S02.053 — Transcript

###### Transcript
- solo monologue
- question → answer
- host → doctor → participant
- unresolved speaker
- Chehelston guest
- Uni Tehran multi-speaker
- short utterance
- long utterance
- topic shift
- Taxation discussion
- giving/budget conversation

---


<a id="s02-u054"></a>

### S02.054 — 31. Final retrieval behavior مطلوب

#### 31. Final retrieval behavior مطلوب

در Generation نهایی، سیستم باید بتواند:

1. Evidence مستقیم دکتر را ترجیح دهد.
2. Secondary evidence را با هویت Secondary حفظ کند.
3. Context مجری / مهمان را فقط در صورت نیاز وارد کند.
4. Source و Speaker را اشتباه Attribution نکند.
5. Citation را به Parent Source قابل ردیابی نگه دارد.
6. از تکرار مصنوعی ناشی از cross-source reuse جلوگیری کند.
7. در تعارض، Authority را در ranking قابل استفاده نگه دارد.
8. در نبود Evidence کافی abstain کند.
9. Topic / Competency را با Retrieval Quality اشتباه نگیرد.

---


<a id="s02-u055"></a>

### S02.055 — 32. Open Gates که NB11 نباید فراموش کند

#### 32. Open Gates که NB11 نباید فراموش کند

- Rights: 19,456 records هنوز `EVIDENCE_REQUIRED`
- 2,354 unresolved transcript speaker context
- 7 Khane-To review items
- 902 Asre-Shirin segments بدون season metadata
- near-duplicate universal threshold وجود ندارد
- cross-source similarity duplicate proof نیست
- automatic canonicalization انجام نشده
- `review_and_improve` هنوز Competency مستقل ندارد
- Knowledge Gap هنوز formally established نشده است

---


<a id="s02-u056"></a>

### S02.056 — 33. Source of Truth برای شروع NB11

#### 33. Source of Truth برای شروع NB11


<a id="s02-u057"></a>

### S02.057 — Accepted corpus

##### Accepted corpus

`data/phase2/processed/documents_dedup_quality_accepted_v1.jsonl`

SHA256:

`9d72c709f81b1218c5aac064052c7ed1da34869f671e6e32762864e0ad70ea40`


<a id="s02-u058"></a>

### S02.058 — NB09 acceptance

##### NB09 acceptance

`reports/phase2/deduplication_quality_acceptance_v1.json`

SHA256:

`14dfa748988db17a19c6d9d5e1eac2eb7d23c0a1699dcc7add18a2bf461fe4f3`


<a id="s02-u059"></a>

### S02.059 — Frozen taxonomy

##### Frozen taxonomy

`artifacts/phase2/taxonomy/taxonomy_v1.json`

SHA256:

`335690044b2e4eff684f7f347809f2c5cb8c39624a939dc01408d9ca898fe977`


<a id="s02-u060"></a>

### S02.060 — Taxonomy freeze report

##### Taxonomy freeze report

`reports/phase2/taxonomy_freeze_v1.json`

SHA256:

`fe182b0c7c6d5ad7d5dfc2aa794fa096e85001b517040a8396d5fb4c0b17e530`


<a id="s02-u061"></a>

### S02.061 — Frozen competency

##### Frozen competency

`artifacts/phase2/competency/competency_prerequisite_v1.json`

SHA256:

`f12f6c1631d77f29042b2009ca9dc8dee406d23ccdccdbb103c0e8cade781e87`


<a id="s02-u062"></a>

### S02.062 — Competency freeze report

##### Competency freeze report

`reports/phase2/competency_freeze_v1.json`

SHA256:

`19bb27288f49e057859da3bc668f54fac440a89a2636ff5d2e49033665f0dd11`

---


<a id="s02-u063"></a>

### S02.063 — 34. قواعد انتقال به چت بعدی

#### 34. قواعد انتقال به چت بعدی

چت بعدی نباید NB09 یا NB10 را از صفر بازسازی کند.

Workflow:

`DISCOVER → INSPECT → VALIDATE → DESIGN CHUNKING BENCHMARK → BUILD CANDIDATES → EVALUATE → DECIDE → FREEZE`

نه:

`guess chunk size → chunk everything → embed`

---


<a id="s02-u064"></a>

### S02.064 — 35. خلاصۀ یک‌خطی

#### 35. خلاصۀ یک‌خطی

**RAG Finance یک RAG تخصصی با محوریت دانش دکتر کمیل رودی است؛ Core Primary Knowledge ساختار اصلی دانش را تعیین می‌کند، Secondary Knowledge فقط Supporting است، Conversation Context باید بدون Attribution collapse حفظ شود، Taxonomy و Competency v1 اکنون Frozen هستند، و NB11 باید با Benchmark واقعی و Source-specific strategy بهترین Chunking را برای Book، Website و Transcript انتخاب کند.**


## جزئیات منبع S03

> فایل اصلی: RAG_finance_independent_audit_2026-08-20 (5).md
>
> ممیزی تاریخی۲۰اوت؛ ضعف‌ها، درصدها، Go/No-Go و توصیه‌ها به Snapshot همان زمان تعلق دارند. بخش اجرایی ابتدای این فایل، قاعدهٔ استفاده از متن زیر است.



<a id="s03-u001"></a>

### S03.001 — معرفی، نسخه و منشأ سند




<a id="s03-u002"></a>

### S03.002 — گزارش مستقل ممیزی فنی RAG_finance

#### گزارش مستقل ممیزی فنی RAG_finance

وضعیت Phase 2، معماری RAG، آمادگی محصول و مسیر دانش‌بنیان

| **Repository** | <bdi dir="ltr">Shahbazi-Amir/RAG_finance</bdi>                |
|----------------|------------------------------------------|
| **Branch**     | rag-phase2                               |
| **Commit**     | <bdi dir="ltr">96c0f0c7d09f4bff107ed71664a0c57ed09f3214</bdi> |
| **تاریخ**      | ۲۰ اوت ۲۰۲۶                              |
| **دامنه**      | ممیزی فقط‌خواندنی؛ بدون تغییر در مخزن     |


<a id="s03-u003"></a>

### S03.003 — ۱. Executive Summary

##### ۱. Executive Summary


<a id="s03-u004"></a>

### S03.004 — حکم نهایی کوتاه

###### حکم نهایی کوتاه

مسیر کلان پروژه—ساخت RAG تخصصی سواد مالی بر پایه مقاله، کتاب و Transcript—**درست و قابل دفاع است**؛ اما وضعیت فعلی مخزن هنوز یک **نمونه مهندسی/تحقیقاتی با دو نسل متفاوت** است، نه محصول Production Ready و نه پرونده آماده ارزیابی دانش‌بنیان.

مخزن دو لایه دارد:

1.  **نسل قدیمی Demo:** زنجیره کامل Embedding → Qdrant → Retrieval → Generation → Streamlit که روی ۷۶ مقاله و ۱۶۸ Chunk ساخته شده است. این لایه برای اثبات امکان‌پذیری خوب است، اما Dense-only، بدون Reranker، بدون Hybrid Search، بدون Citation در سطح ادعا و با ارزیابی بسیار کوچک است.

2.  **نسل جدید Phase 2:** Website Ingestion V2 برای ۵۲۹ مقاله با Discovery، Raw Snapshot، Hash، Validation، Stable ID، Manifest، Extraction و Quality Summary. این بخش نسبت به Demo قدیمی بسیار حرفه‌ای‌تر است، ولی هنوز Notebookمحور است و خروجی‌های اصلی آن به‌علت .gitignore داخل مخزن نیستند.

کتاب‌ها و Transcriptها به‌عنوان **ورودی داده** در Repository وجود دارند: ۷ فایل DOCX کتاب و ۲۱۳ فایل Markdown در مجموعه نهایی Transcript. بااین‌حال Pipeline استاندارد و قابل بازتولید Phase 2 برای این دو منبع، Schema رسمی، Manifest مستقل، Chunking منبع‌محور و Lineage یکپارچه هنوز وجود ندارد.


<a id="s03-u005"></a>

### S03.005 — امتیاز پیشرفت واقعی

###### امتیاز پیشرفت واقعی

بر اساس ۳۸ بند Roadmap ارائه‌شده و روش امتیازدهی DONE=1، PARTIAL=0.5، MISSING=0 و حذف NOT NEEDED از مخرج:

- **پیشرفت Phase 2: حدود ۳۹٪** (14.5 / 37)

- **آمادگی Production: حدود ۲۰٪**

- **آمادگی پرونده فنی دانش‌بنیان: حدود ۲۵٪**

این درصدها اندازه‌گیری مدیریتی‌اند، نه گواهی رسمی. دلیل اختلاف آن‌ها این است که داشتن داده و Notebook با داشتن محصول پایدار، قابل آزمون، قابل استقرار و قابل دفاع نزد ارزیاب یکسان نیست.


<a id="s03-u006"></a>

### S03.006 — تصمیم Go / No-Go

###### تصمیم Go / No-Go

- ادامه پروژه: **GO**

- ارائه فوری برای ارزیابی دانش‌بنیان: **NO-GO**

- ادامه با همان معماری Demo قدیمی: **NO-GO**

- ادامه با معماری سه‌منبعی، Provenance، Hybrid Retrieval، Reranking، Citation، Safety و Evaluation: **GO**


<a id="s03-u007"></a>

### S03.007 — پنج فاصله بحرانی

###### پنج فاصله بحرانی

1.  نبود Dataset یکپارچه و Versioned برای هر سه منبع.

2.  نبود استناد دقیق به صفحه/فصل/زمان و نبود Claim-level Citation.

3.  نبود Benchmark و Golden Dataset معتبر؛ ارزیابی فعلی فقط ۱۰ سؤال است.

4.  نبود تست، CI، Docker، Lockfile و مسیر اجرای قابل بازتولید.

5.  نبود پرونده R&D و شواهد تمایز فنی؛ در وضع فعلی ارزیاب می‌تواند پروژه را «مدل آماده + Vector DB» تلقی کند.


<a id="s03-u008"></a>

### S03.008 — ۲. روش ممیزی و سطح اطمینان شواهد

##### ۲. روش ممیزی و سطح اطمینان شواهد


<a id="s03-u009"></a>

### S03.009 — شواهد مستقیم بررسی‌شده

###### شواهد مستقیم بررسی‌شده

- Tree کامل شاخه rag-phase2: ۹۰۴ Entry و ۷۱۳ فایل.

- Metadata مخزن، Branch و Commit head.

- README، .gitignore، <bdi dir="ltr">requirements.txt</bdi> و <bdi dir="ltr">config/settings.py.</bdi>

- کدهای <bdi dir="ltr">app.py</bdi> و ماژول‌های <bdi dir="ltr">src/embeddings</bdi>، <bdi dir="ltr">src/retrieval</bdi>، <bdi dir="ltr">src/generation</bdi>، <bdi dir="ltr">src/cache</bdi> و <bdi dir="ltr">src/pipeline.</bdi>

- Notebook جدید <bdi dir="ltr">notebooks/phase2/01_website_ingestion.ipynb</bdi> شامل ۱۷۵ Cell؛ هر ۸۲ Code Cell اجرا شده و Error ذخیره‌شده ندارد.

- Notebookهای قدیمی Preprocessing، Chunking، Embedding، Vector Store، Retrieval، Generation، Pipeline و Evaluation.

- <bdi dir="ltr">website_manifest_v1.json</bdi> با ۵۲۹ رکورد.

- فایل ارزیابی ۱۰ سؤالی و چند نمونه Transcript و اسناد بازبینی آن‌ها.

- تاریخچه Commitهای اصلی شاخه، شامل اضافه‌شدن Transcriptها و کتاب‌ها در ۲۰ اوت ۲۰۲۶.


<a id="s03-u010"></a>

### S03.010 — شواهد غیرقابل بازاجرای مستقل در این ممیزی

###### شواهد غیرقابل بازاجرای مستقل در این ممیزی

خروجی‌های زیر در .gitignore هستند و در Tree Commit بررسی‌شده وجود ندارند:

- <bdi dir="ltr">data/phase2/raw/</bdi>

- <bdi dir="ltr">data/phase2/interim/website_extracted_v2.json</bdi>

- <bdi dir="ltr">reports/phase2/data_quality/website_extraction_v2.json</bdi>

- <bdi dir="ltr">reports/phase2/ingestion/website_ingestion_v2.json</bdi>

- Vector Store و Embeddingهای تولیدشده

بنابراین صحت اعداد ۵۲۹/۵۲۹ از دو مدرک پشتیبانی می‌شود: خروجی‌های ذخیره‌شده داخل Notebook و فایل Manifest؛ اما Snapshotهای ignored در این ممیزی مجدداً اجرا یا Hash-verify نشدند. برای ممیزی رسمی باید Artifact Registry یا Dataset Release قابل دریافت وجود داشته باشد.


<a id="s03-u011"></a>

### S03.011 — ۳. وضعیت فعلی Repository

##### ۳. وضعیت فعلی Repository


<a id="s03-u012"></a>

### S03.012 — ۳.۱ ساختار کلیدی

###### ۳.۱ ساختار کلیدی

| **مسیر**                                       | **وضعیت واقعی**                                                                       | **ارزیابی**                                   |
|------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------|
| <bdi dir="ltr">README.md</bdi>                                      | معرفی مفهومی RAG؛ هنوز از مقاله و کتاب نام می‌برد و وضعیت سه‌منبعی جدید را منعکس نمی‌کند | ناقص/قدیمی                                    |
| <bdi dir="ltr">notebooks/phase2/01_website_ingestion.ipynb</bdi>    | Pipeline کامل Website V2، ۵۲۹ مقاله، Hash و Validation                                | قوی‌ترین دارایی فنی فعلی                       |
| <bdi dir="ltr">data/phase2/manifests/website_manifest_v1.json</bdi> | ۵۲۹ رکورد با Stable ID و Version                                                      | مفید ولی محدود به وب‌سایت                      |
| <bdi dir="ltr">data/books/</bdi>                                    | ۷ فایل DOCX، شامل نسخه‌های ظاهراً مشابه/بازطراحی‌شده                                     | داده موجود؛ Pipeline وجود ندارد               |
| <bdi dir="ltr">data/transcripts/final/</bdi>                        | ۲۱۳ فایل MD در ۷ مجموعه                                                               | داده ارزشمند؛ Schema و Timestamp یکنواخت نیست |
| <bdi dir="ltr">notebooks/02...10</bdi>                              | زنجیره RAG قدیمی روی ۷۶ مقاله و ۱۶۸ Chunk                                             | <bdi dir="ltr">Demo/Prototype</bdi>                                |
| <bdi dir="ltr">src/</bdi>                                           | چهار جزء اصلی RAG و Cache                                                             | کد ساده و قابل فهم؛ نه Production Grade       |
| <bdi dir="ltr">app.py</bdi>                                         | Streamlit chat، تاریخچه JSON و نمایش Source                                           | Demo UI                                       |
| <bdi dir="ltr">data/evaluation/...json</bdi>                        | ۱۰ سؤال؛ ۸ in-scope و ۲ out-of-scope                                                  | Smoke test، نه Benchmark                      |
| <bdi dir="ltr">tests/</bdi>                                         | وجود ندارد                                                                            | بحرانی                                        |
| <bdi dir="ltr">.github/workflows/</bdi>                             | وجود ندارد                                                                            | <bdi dir="ltr">CI/CD</bdi> وجود ندارد                              |
| <bdi dir="ltr">docs/</bdi>                                          | وجود ندارد                                                                            | مستندسازی معماری/عملیات وجود ندارد            |
| <bdi dir="ltr">Docker/Compose</bdi>                                 | وجود ندارد                                                                            | استقرار بازتولیدپذیر وجود ندارد               |


<a id="s03-u013"></a>

### S03.013 — ۳.۲ شاخه و تاریخچه

###### ۳.۲ شاخه و تاریخچه

- Default branch مخزن main است، اما ممیزی روی rag-phase2 انجام شد.

- Head شاخه: 96c0f0c7 با پیام ogtanos aram added در ۲۰ اوت ۲۰۲۶.

- Commit قبلی f46501cc هفت فایل کتاب را اضافه کرده است.

- Commit 9e2e1ebf مجموعه‌های چهلستون/بانک ملت و فایل‌های مرتبط را اضافه کرده است.

- تاریخچه قدیمی‌تر از June–July 2026 نشان‌دهنده ساخت مرحله‌ای Demo: ingestion، chunking، embedding، Qdrant، retrieval، generation، cache، app و evaluation است.

- Branch محافظت‌شده نیست و Required Status Check ندارد.

- Commit head امضاشده/Verified نیست.

- نام و کیفیت پیام Commitها یکنواخت نیست (just، ogtanos aram added و غلط‌های نگارشی). این موضوع مانع فنی محصول نیست، اما برای پرونده قابل ممیزی و مدیریت R&D ضعیف است.


<a id="s03-u014"></a>

### S03.014 — ۳.۳ داده‌های موجود

###### ۳.۳ داده‌های موجود

- ۵۲۹ مقاله در Website Manifest.

- ۷ فایل DOCX کتاب؛ چند فایل ممکن است نسخه‌های متفاوت یک اثر باشند. چون Deduplication و Canonical Book Registry وجود ندارد، تعداد «اثر مستقل» از روی نام فایل قطعی نیست.

- ۲۱۳ فایل Markdown زیر <bdi dir="ltr">data/transcripts/final/</bdi>:

- asre_shirin: ۲۶

- chehelstion_finup_ketabbaz_bankmellat: ۵۵

- dar-jostojo-final-C: ۵۹، که بخشی از آن‌ها فایل‌های <bdi dir="ltr">Audit/Extracted</bdi> هستند و همگی Episode مستقل نیستند

- khane-to: ۱۳

- mq: ۸

- tarbiat-morabi: ۱۴

- uni-tehran: ۳۸

> **عدد ۲۱۳ تعداد فایل Markdown است، نه تعداد قطعی Episode مستقل. برای عدد رسمی باید Transcript Manifest ساخته شود و فایل‌های محتوایی، Audit، Candidate و Supplemental از هم تفکیک شوند.**


<a id="s03-u015"></a>

### S03.015 — ۳.۴ Website Ingestion V2

###### ۳.۴ Website Ingestion V2

موارد مثبت:

- کشف Pagination بدون Hard-code شدن تعداد صفحات.

- ۵۲۹ مقاله یکتا و Canonical URL بر اساس article_id.

- Stable ID به شکل website:\<article_id\>.

- ذخیره Raw HTML و <bdi dir="ltr">source.json</bdi>.

- SHA-256 روی Bytes خام.

- Validation ساختاری HTML.

- Retry، Resume و رفع Root Cause خطای <bdi dir="ltr">Cookie/HTTP</bdi> 400.

- استخراج Title، Body، Author، Tags و Metadata.

- نرمال‌سازی Soft Hyphen و متن.

- گزارش خروجی Notebook: ۵۲۹ <bdi dir="ltr">Title/Body/Author/Hash</bdi> غیرخالی.

موارد منفی:

- کل Pipeline در Notebook است؛ <bdi dir="ltr">Package/CLI/Job</bdi> مستقل ندارد.

- Manifest Commit‌شده هنوز status=discovered و author=null دارد، حتی با وجود تکمیل استخراج در خروجی Notebook؛ یعنی State نهایی و Manifest همگام نیستند.

- version=1 صرفاً یک فیلد است؛ Dataset Versioning واقعی، Changelog، Parent Version و Snapshot Hash وجود ندارد.

- Incremental Update فقط Resume دانلودهای موجود را پوشش می‌دهد؛ تشخیص <bdi dir="ltr">Add/Change/Delete</bdi> و سیاست Reprocessing مستند نیست.

- گزارش‌های تولیدشده ignored و در دسترس ممیز نیستند.

- Notebook به مسیر مطلق macOS وابسته است و Reproducibility محیطی ندارد.

- Assertions و تست خودکار وجود ندارد؛ Validationها عمدتاً print هستند.


<a id="s03-u016"></a>

### S03.016 — ۳.۵ <bdi dir="ltr">Video/Transcript</bdi>

###### ۳.۵ <bdi dir="ltr">Video/Transcript</bdi>

موارد مثبت:

- حجم قابل توجه متن بازبینی‌شده و Curated.

- Metadata انسانی در ابتدای بسیاری از فایل‌ها: برنامه، قسمت، موضوع، مدت، منبع و وضعیت بازبینی.

- در dar-jostojo شواهدی از <bdi dir="ltr">Raw/Machine/Reviewed/Final</bdi> و Audit اختلاف‌ها وجود دارد؛ این یک دارایی R&D ارزشمند است.

موارد منفی:

- Schema رسمی و Machine-readable واحد وجود ندارد؛ Metadata در Markdown آزاد نوشته شده است.

- Timestamp در سطح <bdi dir="ltr">Segment/Sentence</bdi> حفظ نشده و Citation زمانی قابل اتکا نیست.

- Speaker ID در بعضی مجموعه‌ها وجود دارد و در بعضی‌ها نه؛ یکنواخت نیست.

- ASR Confidence، Segment Hash، Audio Asset ID، <bdi dir="ltr">Start/End</bdi> Time و Revision Lineage عمومی وجود ندارد.

- فایل‌های Episode، Supplemental، Candidate Difference و Review در یک Tree داده‌ای کنار هم‌اند و هنوز نقش هرکدام در Knowledge Base با Manifest تعیین نشده است.

- Validator، Chunker و Quality Report اختصاصی Transcript وجود ندارد.


<a id="s03-u017"></a>

### S03.017 — ۳.۶ Book

###### ۳.۶ Book

موارد مثبت:

- فایل‌های Word در Repository حاضرند.

- نسخه‌های بازطراحی RTL می‌تواند استخراج فارسی را ساده‌تر کند.

موارد منفی:

- هیچ Book Manifest یا Canonical Work ID وجود ندارد.

- نسخه‌های مشابه یک کتاب از هم تفکیک نشده‌اند؛ Risk ورود محتوای تکراری بالاست.

- <bdi dir="ltr">Chapter/Heading</bdi> Extraction، Paragraph Anchor، <bdi dir="ltr">Page/Location</bdi> Mapping، <bdi dir="ltr">Footnote/Table</bdi> handling و Cleaning وجود ندارد.

- صفحه در DOCX پایدار نیست؛ برای Citation باید یا PDF مرجع نهایی ثبت شود، یا Anchor پایدار فصل/بخش/پاراگراف ساخته شود.

- حقوق نشر، مجوز استفاده و دامنه مجاز نمایش متن در Repository مستند نشده است.


<a id="s03-u018"></a>

### S03.018 — ۳.۷ RAG و Application قدیمی

###### ۳.۷ RAG و Application قدیمی

موارد مثبت:

- اجزای Embedder، Retriever، Generator و Cache از هم جدا شده‌اند.

- Qdrant Payload شامل chunk_id، article_id، title، url و text است.

- Prompt از مدل می‌خواهد خارج از Context پاسخ ندهد.

- UI منابع بازیابی‌شده را نمایش می‌دهد.

- برای دو سؤال out-of-scope پاسخ «در منابع موجود پاسخ کافی پیدا نشد» ثبت شده است.

موارد منفی:

- RAG فعلی روی Dataset قدیمی ۷۶ مقاله/۱۶۸ Chunk است، نه Dataset سه‌منبعی جدید.

- Retrieval فقط Dense Vector Search است؛ Hybrid، <bdi dir="ltr">Sparse/BM25</bdi> و Reranking ندارد.

- Threshold بازیابی و Answerability Model وجود ندارد؛ Abstention وابسته به رفتار LLM است.

- Citation صرفاً فهرست Sourceهای Retrieval است، نه اثبات اینکه هر ادعای پاسخ توسط کدام Span پشتیبانی شده است.

- Context Builder فقط Concatenation ساده Top-k است؛ کنترل Token Budget، Diversity، Source Balance، Dedup و Conflict ندارد.

- Cache Key فقط متن Normalizeشده سؤال است؛ Dataset Version، Model Version، Prompt Version و top_k در کلید نیستند. بنابراین پاسخ قدیمی می‌تواند بعد از تغییر Knowledge Base باقی بماند.

- در مسیر Cache، داده retrieved_chunks می‌تواند با سیاست خالی‌کردن منابع در حالت Abstention ناسازگار شود.

- تاریخچه Chat در JSON مشترک ذخیره می‌شود؛ Multi-user isolation، Privacy، Retention و Concurrent write ندارد.

- هیچ Rate Limit، Auth، Audit Log، Observability یا API Contract وجود ندارد.

- ادعای پشتیبانی از ۱۵۰۰ کاربر در README هیچ Load Test یا معماری Deployment پشتیبان ندارد.


<a id="s03-u019"></a>

### S03.019 — ۴. ماتریس تطبیق با Roadmap فاز ۲

##### ۴. ماتریس تطبیق با Roadmap فاز ۲


<a id="s03-u020"></a>

### S03.020 — <bdi dir="ltr">Phase 2 Foundation</bdi>

###### <bdi dir="ltr">Phase 2 Foundation</bdi>

| **مورد**           | **وضعیت** | **مدرک/فاصله**                                                                     |
|--------------------|-----------|------------------------------------------------------------------------------------|
| Freeze Phase 1     | PARTIAL   | Demo قدیمی قابل مشاهده است؛ <bdi dir="ltr">Tag/Release</bdi> رسمی، Baseline Report و Freeze policy نیست |
| Baseline           | DONE      | ۷۶ مقاله/۱۶۸ Chunk برای Demo و ۵۲۹ مقاله برای Website V2 ثبت شده                   |
| Document Schema    | PARTIAL   | Schema ضمنی Website وجود دارد؛ JSON Schema مشترک سه‌منبعی نیست                      |
| Stable IDs         | PARTIAL   | Website ID مناسب است؛ <bdi dir="ltr">Book/Video</bdi> ID استاندارد نیست                                 |
| Manifest           | PARTIAL   | فقط Website Manifest وجود دارد                                                     |
| Dataset Versioning | PARTIAL   | فیلد Version هست؛ <bdi dir="ltr">Release/Hash/Parent/Changelog</bdi> نیست                               |


<a id="s03-u021"></a>

### S03.021 — <bdi dir="ltr">Website Pipeline</bdi>

###### <bdi dir="ltr">Website Pipeline</bdi>

| **مورد**           | **وضعیت** | **مدرک/فاصله**                                                 |
|--------------------|-----------|----------------------------------------------------------------|
| Discovery          | DONE      | ۵۲۹ مقاله و Pagination خودکار                                  |
| Raw Storage        | DONE      | HTML + <bdi dir="ltr">source.json</bdi>؛ خروجی ignored ولی اجرای Notebook ثبت شده   |
| Extraction         | DONE      | ۵۲۹ رکورد و Metadata                                           |
| Validation         | DONE      | Hash و Structure Validation؛ ۵۲۹ معتبر در خروجی Notebook       |
| Incremental Update | PARTIAL   | Resume هست؛ <bdi dir="ltr">Diff/Delete/Reprocess</bdi> policy نیست                  |
| Crawl Report       | PARTIAL   | تولید می‌شود ولی Artifact قابل ممیزی در <bdi dir="ltr">Repository/Release</bdi> نیست |
| Processing         | DONE      | Extraction و نرمال‌سازی فارسی اولیه کامل است                    |
| Chunking           | MISSING   | Chunking V2 برای ۵۲۹ مقاله وجود ندارد                          |


<a id="s03-u022"></a>

### S03.022 — <bdi dir="ltr">Video Pipeline</bdi>

###### <bdi dir="ltr">Video Pipeline</bdi>

| **مورد**               | **وضعیت** | **مدرک/فاصله**                                                    |
|------------------------|-----------|-------------------------------------------------------------------|
| Transcript Schema      | PARTIAL   | Metadata انسانی موجود، Contract یکنواخت و JSON Schema نیست        |
| Validation             | PARTIAL   | بازبینی انسانی وجود دارد؛ Validator خودکار و Coverage Report نیست |
| Normalization          | PARTIAL   | متن‌های نهایی پاک‌سازی شده‌اند؛ قواعد واحد و تست‌شده نیست             |
| Timestamp Preservation | MISSING   | <bdi dir="ltr">Start/End</bdi> زمان Segmentها در خروجی نهایی نیست                      |
| Chunking               | MISSING   | Pipeline اختصاصی Video وجود ندارد                                 |


<a id="s03-u023"></a>

### S03.023 — <bdi dir="ltr">Book Pipeline</bdi>

###### <bdi dir="ltr">Book Pipeline</bdi>

| **مورد**            | **وضعیت**  | **مدرک/فاصله**                                                             |
|---------------------|------------|----------------------------------------------------------------------------|
| <bdi dir="ltr">PDF/EPUB</bdi> Processing | NOT NEEDED | ورودی فعلی DOCX است؛ به‌جای آن <bdi dir="ltr">DOCX/PDF-reference</bdi> processing باید اضافه شود |
| Chapter Extraction  | MISSING    | Pipeline یا خروجی فصل‌بندی دیده نشد                                         |
| Page Metadata       | MISSING    | <bdi dir="ltr">Page/Location</bdi> یا Paragraph Anchor وجود ندارد                               |
| Cleaning            | MISSING    | قواعد پاک‌سازی و QA کتاب وجود ندارد                                         |
| Chunking            | MISSING    | Chunking اختصاصی کتاب وجود ندارد                                           |


<a id="s03-u024"></a>

### S03.024 — <bdi dir="ltr">Unified Dataset</bdi>

###### <bdi dir="ltr">Unified Dataset</bdi>

| **مورد**       | **وضعیت** | **مدرک/فاصله**                             |
|----------------|-----------|--------------------------------------------|
| Common Schema  | MISSING   | سه منبع هنوز Contract واحد ندارند          |
| Deduplication  | MISSING   | Dedup بین نسخه کتاب/مقاله/ویدیو وجود ندارد |
| Quality Report | PARTIAL   | فقط Website Quality Summary وجود دارد      |


<a id="s03-u025"></a>

### S03.025 — <bdi dir="ltr">RAG Layer</bdi>

###### <bdi dir="ltr">RAG Layer</bdi>

| **مورد**        | **وضعیت** | **مدرک/فاصله**                                         |
|-----------------|-----------|--------------------------------------------------------|
| Embedding       | PARTIAL   | Demo قدیمی؛ Dataset جدید Embedding نشده                |
| Vector Database | PARTIAL   | Qdrant Demo؛ Collection versioning و migration نیست    |
| Retrieval       | PARTIAL   | Dense-only و بدون ارزیابی Retrieval                    |
| Hybrid Search   | MISSING   | <bdi dir="ltr">BM25/Sparse</bdi> وجود ندارد                                 |
| Reranking       | MISSING   | <bdi dir="ltr">Cross-encoder/LLM</bdi> reranker وجود ندارد                  |
| Context Builder | PARTIAL   | Concatenation ساده؛ <bdi dir="ltr">Budget/Diversity/Conflict</bdi> ندارد    |
| Citation        | PARTIAL   | Source list هست؛ Claim-level و <bdi dir="ltr">Page/Time</bdi> citation نیست |


<a id="s03-u026"></a>

### S03.026 — <bdi dir="ltr">Evaluation</bdi>

###### <bdi dir="ltr">Evaluation</bdi>

| **مورد**        | **وضعیت** | **مدرک/فاصله**                                                         |
|-----------------|-----------|------------------------------------------------------------------------|
| Golden Dataset  | MISSING   | ۱۰ سؤال بدون Gold <bdi dir="ltr">Evidence/Answer</bdi>                                      |
| Benchmark       | PARTIAL   | یک Smoke Test ده‌سؤالی وجود دارد                                        |
| Regression Test | MISSING   | Gate خودکار و مقایسه نسخه‌ها نیست                                       |
| Metrics         | MISSING   | فقط شمارش Reject دو سؤال؛ <bdi dir="ltr">Retrieval/Faithfulness/Citation</bdi> metrics نیست |


<a id="s03-u027"></a>

### S03.027 — ۵. بررسی معماری «Professional Financial Literacy Advisory RAG»

##### ۵. بررسی معماری «Professional Financial Literacy Advisory RAG»


<a id="s03-u028"></a>

### S03.028 — <bdi dir="ltr">Multi-source Architecture</bdi>

###### <bdi dir="ltr">Multi-source Architecture</bdi>

در سطح Intent درست است، اما در پیاده‌سازی **هنوز Multi-source نیست**. سه منبع در Storage دیده می‌شوند، ولی فقط Website V2 Pipeline دارد و RAG قدیمی فقط مقالات را مصرف می‌کند. Multi-source زمانی محقق است که هر منبع Adapter مستقل داشته باشد و همه در Common Document Contract ادغام شوند.


<a id="s03-u029"></a>

### S03.029 — <bdi dir="ltr">Data Lineage</bdi>

###### <bdi dir="ltr">Data Lineage</bdi>

برای وب‌سایت بخشی از Lineage وجود دارد: URL → Raw HTML → Hash → Extracted Record. برای کتاب و Transcript، Lineage یکنواخت وجود ندارد. Lineage کامل باید این زنجیره را ثبت کند:

<div dir="ltr" align="left">source asset → source version/hash → extraction run → normalization version → document ID → chunk ID → embedding model/version → index version → retrieval event → answer → cited evidence</div>


<a id="s03-u030"></a>

### S03.030 — Citation و دفاع‌پذیری

###### Citation و دفاع‌پذیری

Citation فعلی واقعی و کافی نیست. نمایش عنوان/URL منابع Retrieval ثابت نمی‌کند جمله پاسخ از همان منابع آمده است. Citation حرفه‌ای باید:

- برای Website به URL + Article ID + <bdi dir="ltr">Span/Paragraph</bdi> Anchor متصل باشد.

- برای Book به <bdi dir="ltr">Work/Edition</bdi> + Chapter + Page یا Paragraph Anchor متصل باشد.

- برای Video به <bdi dir="ltr">Program/Episode</bdi> + <bdi dir="ltr">Start/End</bdi> Timestamp متصل باشد.

- هر Claim مهم پاسخ را به یک یا چند Evidence Span نگاشت کند.

- Citation Entailment را بررسی کند: آیا Evidence واقعاً Claim را پشتیبانی می‌کند؟


<a id="s03-u031"></a>

### S03.031 — کنترل Hallucination

###### کنترل Hallucination

Prompt به‌تنهایی کنترل Hallucination محسوب نمی‌شود. کنترل قابل دفاع حداقل به این اجزا نیاز دارد:

1.  Retrieval Quality Gate و حداقل Evidence Coverage.

2.  <bdi dir="ltr">Answerability/Abstention</bdi> classifier کالیبره‌شده.

3.  تولید پاسخ در قالب Claimهای قابل Cite.

4.  Citation verification یا entailment check.

5.  سیاست Conflict، Freshness و Unknown.

6.  Regression suite برای سؤال‌های خارج از دامنه، گمراه‌کننده و تزریق Prompt.


<a id="s03-u032"></a>

### S03.032 — معماری هدف پیشنهادی

###### معماری هدف پیشنهادی

1.  **Source adapters:** Website، Book و Video؛ مستقل ولی با Contract مشترک.

2.  **Immutable raw zone:** محتوا، حقوق منبع، Hash و زمان دریافت.

3.  **Canonical document layer:** Schema واحد، Stable ID، Version و Lineage.

4.  **Source-aware chunking:** فصل/پاراگراف، Topic Shift و Timestamp.

5.  **Dual index:** Dense + <bdi dir="ltr">Sparse/BM25</bdi> با فیلتر Metadata.

6.  **Reranker:** مدل مناسب فارسی یا Multilingual و آزمایش مقایسه‌ای.

7.  **Context compiler:** Dedup، <bdi dir="ltr">MMR/Diversity</bdi>، Source balance، Token budget و conflict grouping.

8.  **Grounded generation:** پاسخ آموزشی، Claim IDs و Citation اجباری.

9.  **<bdi dir="ltr">Safety/policy</bdi> layer:** مرزبندی آموزش با توصیه سرمایه‌گذاری شخصی.

10. **<bdi dir="ltr">Evaluation/observability</bdi>:** نسخه‌محور، قابل بازتولید و دارای Release Gate.


<a id="s03-u033"></a>

### S03.033 — ۶. ارزیابی آمادگی دانش‌بنیان

##### ۶. ارزیابی آمادگی دانش‌بنیان


<a id="s03-u034"></a>

### S03.034 — معیار رسمی و دامنه اطمینان

###### معیار رسمی و دامنه اطمینان

منابع رسمی عمومی تأکید می‌کنند ارزیابی بر محصول شرکت و تشخیص کارگروه متکی است؛ آیین‌نامه اجرایی نیز مسئولیت تدوین حوزه‌ها و معیارها را به ساختار ارزیابی می‌دهد. منابع رسمی صندوق نوآوری، «سطح فناوری/پیچیدگی»، «دانش فنی» و «نمونه اولیه» را از معیارهای اصلی معرفی کرده‌اند. همچنین آخرین نسخه معیارها و فهرست کالا/خدمت باید در سامانه رسمی زمان اقدام کنترل شود.

منابع مرجع:

- آیین‌نامه اجرایی قانون حمایت از شرکت‌های دانش‌بنیان — صندوق نوآوری و شکوفایی — <bdi dir="ltr">https://www.inif.ir/-regulations-executive-law</bdi>

- اصلاح آیین‌نامه اجرایی و وظایف کارگروه — پایگاه قوانین و مقررات — <bdi dir="ltr">https://qavanin.ir/Law/TreeText/?IDS=7646595681372737421</bdi>

- توضیح رسمی صندوق درباره معیارهای سطح فناوری، دانش فنی و نمونه اولیه — <bdi dir="ltr">https://www.inif.ir/fullcontent/-/asset_publisher/YASjeuXFqbaQ/content/id/646562</bdi>


<a id="s03-u035"></a>

### S03.035 — آیا پروژه فعلی فقط «مدل آماده + Vector DB» است؟

###### آیا پروژه فعلی فقط «مدل آماده + Vector DB» است؟

**در Demo فعلی: تا حد زیادی بله.** اجزای اصلی، API سازگار OpenAI، Qdrant و Streamlit هستند و Retrieval نیز Dense-only است. Website Ingestion V2 و بازبینی Transcriptها نشانه‌های مهندسی اختصاصی ارزشمندند، اما هنوز به محصول نهایی متصل و با Benchmark اثبات نشده‌اند.


<a id="s03-u036"></a>

### S03.036 — وضعیت مؤلفه‌های دفاع‌پذیری

###### وضعیت مؤلفه‌های دفاع‌پذیری

| **مؤلفه**              | **وضعیت فعلی** | **برای دفاع چه لازم است؟**                        |
|------------------------|----------------|---------------------------------------------------|
| معماری اختصاصی         | PARTIAL        | Architecture Decision Record و پیاده‌سازی سه‌منبعی  |
| Pipeline اختصاصی داده  | PARTIAL        | Website قوی؛ <bdi dir="ltr">Book/Video</bdi> باید هم‌سطح شوند           |
| Normalization فارسی    | PARTIAL        | قواعد، Corpus خطا، تست و Ablation                 |
| Data Engineering       | PARTIAL        | Orchestration، lineage، artifacts و quality gates |
| Versioning             | PARTIAL        | <bdi dir="ltr">Dataset/Index/Prompt/Model</bdi> releases               |
| Evaluation Framework   | MISSING        | Golden set، metrics، dashboards، gates            |
| Benchmark              | MISSING        | Baseline comparisons و گزارش آماری                |
| Retrieval Optimization | MISSING        | Hybrid، reranking، tuning و ablation              |
| Citation System        | PARTIAL        | Claim-level <bdi dir="ltr">page/time/span</bdi> citations              |
| Knowledge Engineering  | PARTIAL        | Taxonomy، source policy، <bdi dir="ltr">conflict/freshness</bdi>       |
| Automated Testing      | MISSING        | <bdi dir="ltr">unit/integration/data/eval/security/load</bdi>          |
| Reproducibility        | MISSING        | Docker، pinned deps، CLI، immutable artifacts     |


<a id="s03-u037"></a>

### S03.037 — ریسک‌های خاص پرونده

###### ریسک‌های خاص پرونده

1.  **مالکیت و مجوز داده:** عبارت knowledge_owner=Dr. Komeil Roudi برای تمام ۵۲۹ مقاله، به‌تنهایی سند حقوقی مالکیت یا مجوز نیست. قرارداد/مجوز استفاده از مقاله، کتاب، صوت و Transcript باید جداگانه موجود باشد.

2.  **تکرار محتوا:** چند نسخه کتاب و همپوشانی مقاله/ویدیو می‌تواند Benchmark و Retrieval را مصنوعی بهبود دهد.

3.  **وابستگی به سرویس آماده:** اگر تمایز در <bdi dir="ltr">Data/Knowledge/Retrieval/Safety</bdi> اثبات نشود، پرونده ممکن است Integrator ساده تلقی شود.

4.  **نبود شواهد R&D:** Commitها تاریخچه کار را نشان می‌دهند، ولی فرضیه، آزمایش، نتیجه منفی، انتخاب معماری و مقایسه علمی ثبت نشده است.

5.  **محصول نبودن:** Notebook و Streamlit Demo به‌تنهایی نمونه محصول قابل ارزیابی سازمانی نیست.


<a id="s03-u038"></a>

### S03.038 — نتیجه دانش‌بنیان

###### نتیجه دانش‌بنیان

- **قابلیت بالقوه:** دارد.

- **آمادگی فعلی برای تأیید:** کافی نیست.

- **شرط تبدیل شدن به پرونده قوی:** باید ارزش فنی حول «سامانه دانش‌محور فارسیِ قابل استناد و ایمن برای آموزش مالی» اثبات شود، نه حول استفاده از LLM و Vector DB.


<a id="s03-u039"></a>

### S03.039 — ۷. تفاوت «دستیار هوشمند سواد مالی» با «جستجوی متن»

##### ۷. تفاوت «دستیار هوشمند سواد مالی» با «جستجوی متن»

| **جستجوی متن**                 | **دستیار هوشمند آموزشی مالی**                |
|--------------------------------|----------------------------------------------|
| چند سند مشابه برمی‌گرداند       | سؤال را تحلیل و هدف آموزشی را تشخیص می‌دهد    |
| مسئولیت صحت پاسخ ندارد         | پاسخ Grounded با Claim-level Citation می‌سازد |
| معمولاً Unknown را تشخیص نمی‌دهد | در نبود Evidence مناسب صریحاً Abstain می‌کند   |
| تفاوت آموزش/مشاوره را نمی‌فهمد  | Intent و Risk را طبقه‌بندی می‌کند              |
| Context ثابت Top-k             | Context متنوع، dedupشده و متناسب با نوع سؤال |
| بدون مسیر یادگیری              | توضیح مرحله‌ای، مثال، تمرین و پیگیری یادگیری  |
| Source list ساده               | صفحه/فصل/زمان و توضیح نقش هر منبع            |
| Score شباهت                    | Confidence کالیبره‌شده از چند سیگنال          |


<a id="s03-u040"></a>

### S03.040 — قابلیت‌های ضروری محصول

###### قابلیت‌های ضروری محصول

- پاسخ مستند با Citation در سطح Claim.

- تشخیص «پاسخ کافی وجود ندارد» با Threshold کالیبره‌شده.

- تفکیک Intent: آموزش عمومی، برنامه‌ریزی مالی عمومی، درخواست توصیه شخصی، پیش‌بینی بازار و معامله.

- امتناع/هشدار برای توصیه سرمایه‌گذاری شخصی بدون داده و مجوز مناسب.

- توضیح اینکه پاسخ از چه نوع منابعی ساخته شده و اختلاف منابع چیست.

- Confidence به‌صورت بالا/متوسط/پایین یا عدد کالیبره، نه Score خام Qdrant.

- ثبت Feedback، Trace و Evidence برای Audit.

- Privacy و عدم ذخیره اطلاعات حساس مالی بدون رضایت و سیاست Retention.


<a id="s03-u041"></a>

### S03.041 — روش صحیح Confidence

###### روش صحیح Confidence

Confidence نباید از «اعتماد مدل» یا فقط شباهت برداری ساخته شود. پیشنهاد:

<div dir="ltr" align="left">Confidence = calibrated(retrieval coverage, evidence agreement, citation entailment, source quality, answerability margin, freshness)</div>

عدد نهایی باید روی Validation Set کالیبره شود و Reliability <bdi dir="ltr">Diagram/Brier</bdi> Score داشته باشد.


<a id="s03-u042"></a>

### S03.042 — ۸. Roadmap اصلاحی اولویت‌بندی‌شده

##### ۸. Roadmap اصلاحی اولویت‌بندی‌شده


<a id="s03-u043"></a>

### S03.043 — P0 — ضروری؛ پیش از توسعه قابلیت‌های نمایشی بیشتر

###### P0 — ضروری؛ پیش از توسعه قابلیت‌های نمایشی بیشتر

###### P0.1 تثبیت Baseline و ساخت سند معماری

خروجی‌ها:

- <bdi dir="ltr">docs/architecture/system-context.md</bdi>

- <bdi dir="ltr">docs/architecture/data-flow.md</bdi>

- <bdi dir="ltr">docs/adr/ADR-001-multisource-contract.md</bdi>

- <bdi dir="ltr">docs/phase1-baseline.md</bdi>

- <bdi dir="ltr">Tag/Release</bdi> رسمی برای Demo قدیمی

معیار پایان: هر عضو تیم بداند Dataset قدیمی و Phase 2 جدید چه تفاوتی دارند و کدام مسیر Canonical است.

###### P0.2 ساخت Data Contract واحد

خروجی‌ها:

- <bdi dir="ltr">schemas/source_manifest.schema.json</bdi>

- <bdi dir="ltr">schemas/document.schema.json</bdi>

- <bdi dir="ltr">schemas/chunk.schema.json</bdi>

- <bdi dir="ltr">schemas/retrieval_event.schema.json</bdi>

فیلدهای حداقلی Document:

<div dir="ltr" align="left">document_id, source_type, source_id, source_version, title, language, authors, rights, canonical_uri, content_hash, extracted_at, extractor_version, quality_status, parent_document_id, location, text</div>

فیلدهای حداقلی Chunk:

<div dir="ltr" align="left">chunk_id, document_id, chunker_version, text, text_hash, start_char, end_char, heading_path, page, timestamp_start, timestamp_end, speaker, source_uri</div>

###### P0.3 تکمیل Pipeline کتاب و ویدیو

خروجی‌ها:

- <bdi dir="ltr">src/ingestion/books/</bdi>

- <bdi dir="ltr">src/ingestion/videos/</bdi>

- Manifest مستقل هر منبع

- Validation Report و Reject Queue

- Stable IDs و Lineage

معیار پایان: Run دوباره همان ورودی، خروجی Deterministic با ID و Hash یکسان بسازد.

###### P0.4 Dataset Versioning و Artifact Registry

خروجی‌ها:

- Dataset release مانند kb-2026.08.1

- <bdi dir="ltr">dataset_manifest.json</bdi> با Hash تمام اجزا

- Changelog و Parent Version

- محل Artifact خارج Git برای <bdi dir="ltr">Raw/Interim/Index</bdi>

معیار پایان: یک ممیز با یک دستور بتواند Dataset مشخص را بازیابی و Verify کند.

###### P0.5 Golden Dataset و Safety Policy

حداقل ۳۰۰ سؤال در نسخه اول:

- ۱۲۰ سؤال <bdi dir="ltr">factoid/conceptual</bdi>

- ۶۰ سؤال multi-hop

- ۴۰ سؤال <bdi dir="ltr">cross-source/conflict</bdi>

- ۳۰ سؤال out-of-scope

- ۳۰ سؤال <bdi dir="ltr">personal-advice/unsafe</bdi>

- ۲۰ سؤال <bdi dir="ltr">noisy/typo/Persian</bdi> variants

برای هر سؤال: Gold Answer، Gold Evidence Span، Source ID، Difficulty، Intent، Safety Label و Acceptable Abstention.

###### P0.6 Retrieval قابل دفاع

- <bdi dir="ltr">BM25/Sparse + Dense Hybrid.</bdi>

- Metadata filters و Source routing.

- <bdi dir="ltr">Reranker.</bdi>

- <bdi dir="ltr">Source-aware chunking.</bdi>

- Claim-level citation و Citation verifier.

- <bdi dir="ltr">Answerability gate.</bdi>

###### P0.7 تست و Reproducibility

- <bdi dir="ltr">pyproject.toml</bdi> و dependency lock.

- CLIهای idempotent؛ Notebook فقط برای توضیح/آزمایش.

- Dockerfile و Compose برای <bdi dir="ltr">App/API/Vector</bdi> DB.

- Unit، Integration، Data Contract و End-to-end tests.

- CI با <bdi dir="ltr">lint/type/test/data-smoke/eval-smoke.</bdi>


<a id="s03-u044"></a>

### S03.044 — P1 — مهم؛ برای محصول قابل ارائه و پرونده قوی

###### P1 — مهم؛ برای محصول قابل ارائه و پرونده قوی

1.  API مستقل از UI با OpenAPI و Versioning.

2.  Auth، rate limit، tenant isolation و secure secret management.

3.  PostgreSQL برای <bdi dir="ltr">conversation/feedback</bdi> با consent و retention.

4.  Observability: trace هر پاسخ، نسخه <bdi dir="ltr">Dataset/Index/Prompt/Model</bdi> و cited spans.

5.  Evaluation Dashboard و Release Gate.

6.  Load Test با <bdi dir="ltr">p50/p95</bdi> latency، throughput، error rate و <bdi dir="ltr">cost/query.</bdi>

7.  Security tests: prompt injection، data exfiltration، malicious documents و PII leakage.

8.  R&D dossier شامل فرضیه‌ها، Ablationها، نتایج منفی و انتخاب مدل.

9.  Data rights register و قراردادهای محتوا.

10. Pilot واقعی با کاربران و تحلیل خطا/رضایت/یادگیری.


<a id="s03-u045"></a>

### S03.045 — P2 — بهبود و تمایز بیشتر

###### P2 — بهبود و تمایز بیشتر

1.  <bdi dir="ltr">Taxonomy/Ontology</bdi> سواد مالی و Query routing موضوعی.

2.  Learning path، quiz و سنجش پیش/پس از آموزش.

3.  Personalization آموزشی بدون ورود به توصیه سرمایه‌گذاری شخصی.

4.  Conflict-aware answers و نمایش دیدگاه‌های متفاوت.

5.  Freshness-aware web recrawl و change impact analysis.

6.  مدل Embedding یا Reranker بهینه‌شده برای فارسی مالی، در صورت اثبات سود با Benchmark.

7.  Human review console برای اصلاح Evidence، Dataset و Safety cases.


<a id="s03-u046"></a>

### S03.046 — ۹. Benchmark و آزمایش‌های الزامی

##### ۹. Benchmark و آزمایش‌های الزامی


<a id="s03-u047"></a>

### S03.047 — Baselineهایی که باید مقایسه شوند

###### Baselineهایی که باید مقایسه شوند

1.  <bdi dir="ltr">BM25 only.</bdi>

2.  Dense only فعلی.

3.  Hybrid بدون Reranker.

4.  <bdi dir="ltr">Hybrid + Reranker.</bdi>

5.  Generic chunking در برابر source-aware chunking.

6.  بدون Normalization فارسی در برابر Normalization نسخه‌دار.

7.  بدون Citation verifier در برابر با Citation verifier.


<a id="s03-u048"></a>

### S03.048 — <bdi dir="ltr">Metrics</bdi>

###### <bdi dir="ltr">Metrics</bdi>

**Retrieval:** Recall@<bdi dir="ltr">1/3/5/10</bdi>، MRR، nDCG@k، Hit Rate و source-diversity. **Generation:** Faithfulness، Answer Correctness، Completeness و Conciseness. **Citation:** Citation Precision، Citation <bdi dir="ltr">Recall/Coverage</bdi>، Entailment و Location Accuracy. **Abstention:** <bdi dir="ltr">Precision/Recall/F1</bdi> برای Answerable و Unanswerable، False-safe-answer rate. **Safety:** نرخ تولید توصیه شخصی نامجاز، نرخ عبور Prompt Injection و PII leakage. **Operations:** <bdi dir="ltr">p50/p95/p99</bdi> latency، throughput، error rate، availability و <bdi dir="ltr">cost/query.</bdi> **Calibration:** Brier Score، Expected Calibration Error و Reliability Diagram.


<a id="s03-u049"></a>

### S03.049 — روش علمی گزارش

###### روش علمی گزارش

- Dataset ثابت و Versioned.

- <bdi dir="ltr">Train/Dev/Test</bdi> یا <bdi dir="ltr">Development/Test</bdi> جدا.

- Bootstrap confidence interval برای اختلاف مدل‌ها.

- تحلیل خطا به تفکیک Source، Intent، Difficulty و Safety.

- ثبت Config، Seed، <bdi dir="ltr">Model/Prompt/Index</bdi> versions.

- Release فقط وقتی Regression Gate پاس شود.


<a id="s03-u050"></a>

### S03.050 — ۱۰. نمودارها و گزارش‌های لازم

##### ۱۰. نمودارها و گزارش‌های لازم


<a id="s03-u051"></a>

### S03.051 — نمودارها

###### نمودارها

1.  <bdi dir="ltr">System Context Diagram.</bdi>

2.  <bdi dir="ltr">End-to-end Data Lineage Diagram.</bdi>

3.  سه Pipeline مستقل <bdi dir="ltr">Website/Book/Video</bdi> و نقطه ادغام.

4.  Dataset composition به تفکیک Source، Topic، Length و Quality.

5.  <bdi dir="ltr">Deduplication/overlap</bdi> matrix میان منابع.

6.  Retrieval benchmark chart برای Baselineها.

7.  <bdi dir="ltr">Accuracy/Faithfulness/Citation dashboard.</bdi>

8.  <bdi dir="ltr">Confidence reliability diagram.</bdi>

9.  <bdi dir="ltr">Latency/cost/throughput chart.</bdi>

10. Error taxonomy و Pareto chart.


<a id="s03-u052"></a>

### S03.052 — گزارش‌ها

###### گزارش‌ها

- Dataset Card و Data Datasheet.

- <bdi dir="ltr">Model/System Card.</bdi>

- <bdi dir="ltr">R&D Technical Report.</bdi>

- <bdi dir="ltr">Benchmark Report.</bdi>

- <bdi dir="ltr">Safety & Responsible AI Report.</bdi>

- <bdi dir="ltr">Data Rights & Licensing Register.</bdi>

- <bdi dir="ltr">Security/Privacy Threat Model.</bdi>

- <bdi dir="ltr">Deployment/Operations Manual.</bdi>

- <bdi dir="ltr">Validation & Acceptance Report.</bdi>

- Pilot Report و User Feedback Analysis.

- Change Log و Release Notes.


<a id="s03-u053"></a>

### S03.053 — ۱۱. ساختار پیشنهادی Repository نهایی

##### ۱۱. ساختار پیشنهادی Repository نهایی


```text
RAG_finance/
├── README.md
├── pyproject.toml
├── uv.lock | poetry.lock
├── Makefile
├── Dockerfile
├── docker-compose.yml
├── configs/
│ ├── ingestion/
│ ├── retrieval/
│ └── evaluation/
├── schemas/
│ ├── source_manifest.schema.json
│ ├── document.schema.json
│ └── chunk.schema.json
├── src/rag_finance/
│ ├── ingestion/{website,books,videos}/
│ ├── normalization/
│ ├── chunking/
│ ├── lineage/
│ ├── indexing/
│ ├── retrieval/
│ ├── reranking/
│ ├── context/
│ ├── generation/
│ ├── citations/
│ ├── safety/
│ ├── evaluation/
│ └── api/
├── data/
│ ├── manifests/
│ ├── samples/
│ └── README.md
├── evals/
│ ├── golden/
│ ├── adversarial/
│ └── baselines/
├── tests/
│ ├── unit/
│ ├── integration/
│ ├── data_contract/
│ └── end_to_end/
├── docs/
│ ├── architecture/
│ ├── adr/
│ ├── data/
│ ├── safety/
│ ├── operations/
│ └── knowledge_based_dossier/
├── reports/
│ ├── benchmarks/
│ ├── data_quality/
│ └── releases/
└── .github/workflows/
```


<a id="s03-u054"></a>

### S03.054 — ۱۲. فهرست مدارک لازم برای ارائه دانش‌بنیان

##### ۱۲. فهرست مدارک لازم برای ارائه دانش‌بنیان


<a id="s03-u055"></a>

### S03.055 — مدارک محصول و فناوری

###### مدارک محصول و فناوری

- معرفی محصول، مسئله، مشتری و ارزش پیشنهادی.

- Architecture Document و Data Flow.

- توضیح اجزای اختصاصی و اجزای Third-party.

- Technology <bdi dir="ltr">Readiness/TRL</bdi> evidence و Demo قابل بررسی.

- Datasheet محصول، API و Deployment topology.

- <bdi dir="ltr">Repo/Release/Commit</bdi> history و فهرست اعضای فنی.


<a id="s03-u056"></a>

### S03.056 — مدارک دانش فنی و R&D

###### مدارک دانش فنی و R&D

- دفترچه R&D با سؤال فنی، فرضیه، آزمایش، نتیجه و تصمیم.

- گزارش ساخت Pipeline فارسی و خطاهای ویژه فارسی/<bdi dir="ltr">ASR/RTL.</bdi>

- Benchmark و Ablation Study.

- گزارش Retrieval Optimization و Citation Verification.

- مستند Reproducibility و Test reports.

- شرح دانش فنی داخلی و وابستگی‌های خارجی.


<a id="s03-u057"></a>

### S03.057 — مدارک داده و حقوق

###### مدارک داده و حقوق

- فهرست منابع، مالک، مجوز، تاریخ و محدودیت استفاده.

- قرارداد/اجازه استفاده از کتاب‌ها، مقالات، صوت‌ها و Transcriptها.

- Dataset Card، Manifest و Hash release.

- سیاست Privacy، Retention و حذف داده کاربر.

- سیاست امنیت و مدیریت دسترسی.


<a id="s03-u058"></a>

### S03.058 — مدارک تجاری و عملیاتی

###### مدارک تجاری و عملیاتی

- شرکت حقوقی، تیم، نقش‌ها و سوابق.

- نمونه قرارداد/فاکتور/Pilot در صورت نیاز نوع ارزیابی.

- بازار هدف، رقبا و تمایز کمی.

- <bdi dir="ltr">SLA/SLO</bdi>، Load Test و هزینه سرویس.

- برنامه نگهداری، پشتیبانی و به‌روزرسانی Knowledge Base.


<a id="s03-u059"></a>

### S03.059 — مدارک Safety و دامنه محصول

###### مدارک Safety و دامنه محصول

- تعریف دقیق «آموزش مالی» و موارد خارج از دامنه.

- سیاست عدم ارائه توصیه سرمایه‌گذاری شخصی بدون داده/مجوز.

- Risk Register و Incident Response.

- نتایج Red Team و سؤال‌های پرخطر.

- متن Disclaimer، Consent و مسیر ارجاع به متخصص انسانی.


<a id="s03-u060"></a>

### S03.060 — ۱۳. Acceptance Criteria برای پایان هر فاز

##### ۱۳. Acceptance Criteria برای پایان هر فاز


<a id="s03-u061"></a>

### S03.061 — پایان Data Foundation

###### پایان Data Foundation

- سه Manifest معتبر و Common Schema پاس‌شده.

- ۱۰۰٪ Documentها Stable ID، Hash، Rights و Lineage داشته باشند.

- Duplicateهای Exact و Near-duplicate گزارش و تعیین تکلیف شوند.


<a id="s03-u062"></a>

### S03.062 — پایان Retrieval

###### پایان Retrieval

- Recall@5 هدف روی Test Set از قبل تعریف و پاس شود.

- Hybrid+Reranker به‌طور آماری از Dense-only بهتر باشد.

- Citation location accuracy برای هر سه منبع گزارش شود.


<a id="s03-u063"></a>

### S03.063 — پایان Safety

###### پایان Safety

- نرخ پاسخ نامجاز به درخواست توصیه شخصی زیر حد مصوب تیم باشد.

- Abstention <bdi dir="ltr">precision/recall</bdi> و False-safe-answer rate پاس شوند.

- Prompt injection suite بدون نشت داده پاس شود.


<a id="s03-u064"></a>

### S03.064 — پایان Productization

###### پایان Productization

- Build و Test در CI سبز.

- Deployment از محیط خالی با دستور مستند موفق.

- Trace کامل یک Answer از سؤال تا <bdi dir="ltr">Dataset/Chunk/Citation</bdi> قابل بازیابی باشد.

- Load Test ادعای ظرفیت را اثبات کند.


<a id="s03-u065"></a>

### S03.065 — ۱۴. مشکلاتی که باید فوراً اصلاح یا شفاف شوند

##### ۱۴. مشکلاتی که باید فوراً اصلاح یا شفاف شوند

1.  README باید وضعیت واقعی سه منبع، Phase <bdi dir="ltr">1/2</bdi> و محدودیت Demo را توضیح دهد.

2.  دو محل Raw قدیمی <bdi dir="ltr">data/raw/...</bdi> و <bdi dir="ltr">src/ingestion/data/raw/...</bdi> باید از <bdi dir="ltr">Code/Data</bdi> separation برخوردار شوند؛ داده زیر src مناسب نیست.

3.  <bdi dir="ltr">requirements.txt</bdi> باید Version pin و Lockfile داشته باشد.

4.  مسیرهای مطلق /<bdi dir="ltr">Users/macbookpro/...</bdi> باید از Notebookها حذف و Configمحور شوند.

5.  Manifest Website باید State نهایی و Versioning واقعی را بازتاب دهد.

6.  Chat history و Cache تولیدی نباید به‌عنوان Artifact عادی Commit شوند؛ Privacy و Staleness risk دارند.

7.  Assertions و تست‌های خودکار باید جای Print-based validation را بگیرند.

8.  فایل‌های Audit Transcript نباید بدون Manifest به‌عنوان Knowledge Document وارد Index شوند.

9.  نسخه‌های کتاب باید Canonicalize و حقوق استفاده‌شان ثبت شود.

10. ادعای ظرفیت ۱۵۰۰ کاربر تا زمان Load Test از README حذف یا با برچسب Target مشخص شود.


<a id="s03-u066"></a>

### S03.066 — ۱۵. نظر نهایی Auditor

##### ۱۵. نظر نهایی Auditor

این پروژه **قابلیت تبدیل شدن به محصول دانش‌بنیان را دارد**، چون داده تخصصی فارسی، Pipeline جدید وب‌سایت، فرایند بازبینی Transcript و مسئله واقعی <bdi dir="ltr">Citation/Safety</bdi> در حوزه مالی می‌توانند پایه دانش فنی قابل دفاع باشند.

اما در وضعیت Commit بررسی‌شده:

- محصول سه‌منبعی هنوز ساخته نشده است.

- RAG موجود بیشتر یک Demo Dense RAG است.

- معیارهای علمی کیفیت و Safety اثبات نشده‌اند.

- پرونده R&D، Reproducibility و حقوق داده ناقص است.

پس جمع‌بندی حرفه‌ای این است:

> **مسیر درست است، ولی ادامه مسیر باید از «جمع‌آوری داده و تکمیل Notebook» به «مهندسی محصول قابل اندازه‌گیری، قابل استناد، قابل بازتولید و ایمن» تغییر کند.**

اولویت صحیح بعدی، Embedding کردن سریع همه داده‌ها نیست. ابتدا باید Common Schema، Stable IDs، Manifest کتاب/ویدیو، Lineage، Deduplication و Golden Dataset تکمیل شود. سپس Retrieval و Generation روی Dataset نسخه‌دار ساخته و با Benchmark مقایسه شوند.


<a id="s03-u067"></a>

### S03.067 — ضمیمه A — مسیر اجرایی پیشنهادی ۱۲ مرحله‌ای

##### ضمیمه A — مسیر اجرایی پیشنهادی ۱۲ مرحله‌ای

1.  Freeze و Tag رسمی Demo قدیمی.

2.  تعریف Contract و ID policy.

3.  Book Manifest و canonicalization نسخه‌ها.

4.  Video Manifest و timestamp <bdi dir="ltr">recovery/segmentation.</bdi>

5.  انتقال Website Notebook به <bdi dir="ltr">Package/CLI.</bdi>

6.  Unified normalized documents و Quality Gate.

7.  Source-aware chunking و Dataset Release v1.

8.  <bdi dir="ltr">Dense/BM25</bdi> baselines و Golden Retrieval set.

9.  <bdi dir="ltr">Hybrid + Reranker + Context compiler.</bdi>

10. <bdi dir="ltr">Grounded generation + claim citations + safety.</bdi>

11. <bdi dir="ltr">Regression/Load/Security</bdi> tests و Observability.

12. Pilot، R&D dossier و آماده‌سازی پرونده ارزیابی.


<a id="s03-u068"></a>

### S03.068 — ضمیمه B — وضعیت Production Readiness

##### ضمیمه B — وضعیت Production Readiness

| **جزء**             | **Demo**      | **Production Ready**                       |
|---------------------|---------------|--------------------------------------------|
| Website ingestion   | بله           | خیر؛ Notebookمحور و Artifact غیرقابل دسترس |
| Book ingestion      | خیر           | خیر                                        |
| Video ingestion     | داده حاضر است | خیر                                        |
| Unified dataset     | خیر           | خیر                                        |
| Dense retrieval     | بله           | خیر                                        |
| <bdi dir="ltr">Hybrid/rerank</bdi>       | خیر           | خیر                                        |
| Citation            | نمایش Source  | خیر؛ Claim-level نیست                      |
| Evaluation          | Smoke test    | خیر                                        |
| Streamlit UI        | بله           | خیر                                        |
| <bdi dir="ltr">Tests/CI/Deployment</bdi> | خیر           | خیر                                        |


<a id="s03-u069"></a>

### S03.069 — ضمیمه C — اسناد Repository مشاهده‌شده

##### ضمیمه C — اسناد Repository مشاهده‌شده

- README شاخه rag-phase2 — <bdi dir="ltr">https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/README.md</bdi>

- <bdi dir="ltr">Website Ingestion V2 Notebook — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/01_website_ingestion.ipynb</bdi>

- <bdi dir="ltr">Website Manifest v1 — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/phase2/manifests/website_manifest_v1.json</bdi>

- <bdi dir="ltr">RAG Pipeline — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/src/pipeline/rag_pipeline.py</bdi>

- <bdi dir="ltr">Qdrant Retriever — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/src/retrieval/qdrant_retriever.py</bdi>

- <bdi dir="ltr">Evaluation Notebook — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/10_evaluation.ipynb</bdi>


## جزئیات منبع S04

> فایل اصلی: RAG_finance_master_roadmap(5).md
>
> نقشهٔ مادر؛ شرح هدف است، نه فهرست کار انجام‌نشدهٔ امروز. بخش اجرایی ابتدای این فایل، قاعدهٔ استفاده از متن زیر است.



<a id="s04-u001"></a>

### S04.001 — معرفی، نسخه و منشأ سند




<a id="s04-u002"></a>

### S04.002 — نقشه کلان چهار فاز RAG_finance

#### نقشه کلان چهار فاز RAG_finance

**از Demo تا RAG حرفه‌ای، لانچ چندکاربره و مربی شخصی سواد مالی**

| <span dir="ltr">Repository</span> | <span dir="ltr">Shahbazi-Amir/RAG_finance</span> |
| ---: | ---: |
| Branch مبنا | <span dir="ltr">rag-phase2</span> |
| Commit ممیزی | <span dir="ltr">96c0f0c7d09f4bff107ed71664a0c57ed09f3214</span> |
| تاریخ نسخه | ۲۱ اوت ۲۰۲۶ |
| دامنه | فازهای ۱ تا ۴ و قرارداد تحویل بین آن‌ها |


<a id="s04-u003"></a>

### S04.003 — ۱. تعریف محصول نهایی

##### ۱. تعریف محصول نهایی

محصول نهایی سه کار متفاوت را با مرز روشن انجام می‌دهد:

- دانش معتبر: پاسخ به پرسش‌های سواد مالی فقط با شواهد Corpus اختصاصی.
- آموزش هدفمند: تشخیص سطح، شکاف دانشی و پیشنهاد محتوای مناسب.
- مربیگری عملی: تبدیل آموزش به هدف، اقدام کوچک، پیگیری و ارزیابی مجدد.
محصول در نسخه پایه «مشاور خریدوفروش دارایی» نیست. توصیه سرمایه‌گذاری شخصی، پیش‌بینی بازار و تصمیم مالی پرریسک باید خارج از Policy باشد یا به انسان/مرجع مجاز ارجاع شود.


<a id="s04-u004"></a>

### S04.004 — ۲. چرا کاربر باید این محصول را به AI عمومی ترجیح دهد؟

##### ۲. چرا کاربر باید این محصول را به AI عمومی ترجیح دهد؟

| مزیت | رفتار قابل مشاهده در محصول |
| ---: | ---: |
| اعتبار صاحب دانش | هر پاسخ به مقاله، کتاب یا دقیقه مشخص از محتوای مؤلف متصل است |
| پاسخ قابل دفاع | هر ادعای واقعی Claim-level Citation و Evidence دارد |
| تشخیص نبود پاسخ | سیستم در نبود شاهد، سؤال روشن‌کننده می‌پرسد یا Abstain می‌کند |
| روش آموزشی منسجم | Taxonomy و مسیر یادگیری از روش و محتوای مؤلف ساخته می‌شود |
| کاربرد شخصی ایمن | قواعد و ماشین‌حساب‌های نسخه‌دار از داده ساخت‌یافته استفاده می‌کنند |
| رشد قابل اندازه‌گیری | آزمون قبل/بعد، اقدام‌ها، Check-in و تغییر امتیاز ثبت می‌شود |
| شفافیت | کاربر می‌بیند پاسخ از کجا آمده، چه داده‌ای استفاده شده و محدودیت چیست |


<a id="s04-u005"></a>

### S04.005 — ۳. معماری کلان قابلیت‌ها

##### ۳. معماری کلان قابلیت‌ها

مالکیت و منابع دانش             ↓     فاز ۲: Knowledge & RAG Core             ↓     فاز ۳: Web Platform & Production Launch             ↓     فاز ۴: Assessment + Learning + Planning + Admin             ↓     نتیجه: رشد قابل سنجش سواد و سلامت مالی

در سطح محصول، چهار موتور مستقل اما هماهنگ وجود دارد:

1. RAG Engine: پاسخ مستند از منابع اختصاصی.
2. Assessment Engine: آزمون و امتیازدهی قطعی و نسخه‌دار.
3. Planning Engine: قواعد، ماشین‌حساب‌ها و برنامه اقدام.
4. Conversation Engine: گفت‌وگو، توضیح و هدایت کاربر بدون تغییر خودسرانه محاسبات.


<a id="s04-u006"></a>

### S04.006 — ۴. نقشه چهار فاز

##### ۴. نقشه چهار فاز

| فاز | هدف | خروجی نهایی | وضعیت بر اساس فایل‌های پروژه |
| ---: | ---: | ---: | ---: |
| فاز ۱ | اثبات امکان RAG | Demo کامل Website → Qdrant → Answer → Streamlit | انجام‌شده؛ Baseline |
| فاز ۲ | مهندسی دانش و RAG حرفه‌ای | RAG Core سه‌منبعی، نسخه‌دار، قابل استناد و Benchmark | فاز اجرایی جاری |
| فاز ۳ | دیپلوی و لانچ روی سایت | Web/PWA چندکاربره با DB، امنیت، عملیات و چت عمومی | پس از Gate فاز ۲ |
| فاز ۴ | مشاور/مربی مالی و پنل گسترده | Assessment، پروفایل، مسیر، اقدام، پیشرفت و Admin | پس از پایداری فاز ۳ |


<a id="s04-u007"></a>

### S04.007 — ۵. فاز ۱ - Baseline و میراث قابل استفاده

##### ۵. فاز ۱ - Baseline و میراث قابل استفاده

دارایی‌های اثبات‌شده فاز ۱:

- ۷۶ مقاله نویسنده، ۱۶۸ Chunk و Embeddingهای ۳۰۷۲بعدی.
- Qdrant Local، Dense Retrieval و Qwen3-30B-A3B.
- Cache، Streamlit، تاریخچه JSON/SQLite و Evaluation ده‌سؤالی.
- ساختار ماژولار اولیه در src.
فاز ۱ نباید توسعه پیدا کند؛ باید Tag، Baseline و به‌عنوان مرجع مقایسه فریز شود. محدودیت‌های Dense-only، Character Chunking، Evaluation کوچک و Citation سطح Source باید در گزارش Baseline ثبت شوند.


<a id="s04-u008"></a>

### S04.008 — ۶. فاز ۲ - Knowledge & RAG Core

##### ۶. فاز ۲ - Knowledge & RAG Core


<a id="s04-u009"></a>

### S04.009 — هدف

###### هدف

تبدیل سه خانواده منبع به Dataset قابل ردیابی و ساخت موتور پاسخ مستند، ایمن و قابل ارزیابی.


<a id="s04-u010"></a>

### S04.010 — سه خانواده منبع

###### سه خانواده منبع

- Website: مقاله‌های مستقیم مؤلف و مقاله‌های تولیدشده زیر نظر سردبیری او.
- Books: کتاب، مقاله بلند و نوشته‌های تألیفی مؤلف؛ با تفکیک Work/Edition.
- Video/Audio: تدریس، آموزش، مصاحبه و برنامه تلویزیونی تبدیل‌شده به Transcript.


<a id="s04-u011"></a>

### S04.011 — خروجی

###### خروجی

- Registry حقوق و منشأ محتوا.
- Pipeline مستقل و تکرارپذیر برای هر منبع.
- Common Schema، Stable IDs، Lineage، Dataset/Index releases.
- Source-aware Chunking، Hybrid Retrieval و Reranker فقط در صورت اثبات.
- Context Builder، Claim-level Citation، Answerability و Safety.
- Golden Dataset، Benchmark، Regression و System/Dataset/Model cards.


<a id="s04-u012"></a>

### S04.012 — Gate

###### Gate

پاسخ هر سؤال از Dataset و Index نسخه‌دار تا Claim، Chunk، Document و Raw source قابل ردیابی باشد و نتیجه Benchmark از محیط تمیز تکرار شود.


<a id="s04-u013"></a>

### S04.013 — ۷. فاز ۳ - Platform & Launch

##### ۷. فاز ۳ - Platform & Launch


<a id="s04-u014"></a>

### S04.014 — هدف

###### هدف

عرضه واقعی RAG فاز ۲ روی سایت برای کاربران ثبت‌شده، با ذخیره امن گفت‌وگو و امکان عملیات پایدار.


<a id="s04-u015"></a>

### S04.015 — خروجی

###### خروجی

- Web/PWA واکنش‌گرا، FastAPI و PostgreSQL.
- Auth/session، consent، tenant/user isolation و RLS.
- Conversation، message، citation، retrieval/model run و feedback.
- Qdrant پایدار برای دانش عمومی؛ Redis و Object Storage.
- Dockerized deployment، reverse proxy، TLS، backup/restore و CI/CD.
- Staging، Production، observability، rate limit، cost guard و incident runbook.


<a id="s04-u016"></a>

### S04.016 — Gate

###### Gate

کاربر واقعی بتواند وارد شود، چت کند، Citation را باز کند، تاریخچه خود را ببیند و هیچ داده‌ای بین کاربران نشت نکند؛ Release و rollback و restore آزمایش شده باشد.


<a id="s04-u017"></a>

### S04.017 — ۸. فاز ۴ - مربی سواد مالی و پنل مدیریت

##### ۸. فاز ۴ - مربی سواد مالی و پنل مدیریت


<a id="s04-u018"></a>

### S04.018 — هدف

###### هدف

عبور از «پرسش‌وپاسخ» به چرخه رشد:

Assess → Explain → Plan → Act → Check-in → Reassess


<a id="s04-u019"></a>

### S04.019 — خروجی کاربر

###### خروجی کاربر

- Onboarding و رضایت داده.
- آزمون سواد و سلامت مالی، سطح‌بندی و نمایش شکاف‌ها.
- پروفایل اختیاری درآمد، هزینه، بدهی، پس‌انداز و هدف.
- مسیر یادگیری و محتوای منتخب از سه منبع.
- برنامه اقدام دوره‌ای با قواعد شفاف.
- Check-in، یادآوری، بازآزمون و نمودار پیشرفت.
- توضیح منبع، Confidence components و ارجاع موارد حساس.


<a id="s04-u020"></a>

### S04.020 — خروجی پنل مدیریت

###### خروجی پنل مدیریت

- مدیریت Taxonomy، محتوا، Release و Rights.
- مدیریت سؤال/آزمون/Scoring version.
- مدیریت قواعد، Policy، Prompt و Feature flag.
- مشاهده کیفیت Retrieval/Citation/Safety و صف بازبینی.
- پشتیبانی کاربر با دسترسی محدود و Audit‌شده.
- گزارش رشد آموزشی و سلامت سرویس.


<a id="s04-u021"></a>

### S04.021 — Gate

###### Gate

در پایلوت کنترل‌شده، مسیر کامل از Assessment تا Reassessment کار کند و اثر با KPIهای رفتاری و آموزشی سنجیده شود؛ خروجی عددی حساس فقط از Rules/Calculators نسخه‌دار تولید شود.


<a id="s04-u022"></a>

### S04.022 — ۹. قرارداد تحویل بین فازها

##### ۹. قرارداد تحویل بین فازها

| تحویل | اجزای الزامی |
| ---: | ---: |
| فاز ۱ → ۲ | Tag، Baseline، Dataset/Model/Prompt config و Known limitations |
| فاز ۲ → ۳ | RAG API contract، Dataset/Index IDs، Citation schema، Policy و Eval report |
| فاز ۳ → ۴ | Auth/consent، user isolation، event model، conversation API و operational SLOs |
| فاز ۴ → بهره‌برداری | Assessment/Rules versions، pilot report، safety review و product KPI dashboard |


<a id="s04-u023"></a>

### S04.023 — ۱۰. مسیر دانش فنی و دانش‌بنیان

##### ۱۰. مسیر دانش فنی و دانش‌بنیان

پرونده فنی باید در طول کار ساخته شود، نه در پایان:

| محور دفاع | شواهد لازم |
| ---: | ---: |
| مهندسی داده اختصاصی | سه Pipeline، Schema، Lineage، Rights و Quality reports |
| مهندسی بازیابی | Baseline، Hybrid/Reranker experiments و Ablation |
| اعتماد و استناد | Claim citation، verifier، answerability و conflict handling |
| فارسی و حوزه مالی | Normalizer، Taxonomy، آزمون و Policy تخصصی |
| محصول هوشمند | Assessment/Planning engines و جداسازی منطق قطعی از LLM |
| اثر | Golden tests، pilot، pre/post assessment و action completion |
| بازتولیدپذیری | ADR، experiment registry، CI، releases و runbooks |

طبق آیین‌نامه، تعیین حوزه‌ها و معیارهای تشخیص مصادیق در اختیار کارگروه مربوط است و معیارها می‌توانند تغییر کنند؛ بنابراین این نقشه تضمین تأیید رسمی نیست. مرجع حقوقی: <span dir="ltr">https://qavanin.ir/Law/TreeText/?IDS=7646595681372737421</span>


<a id="s04-u024"></a>

### S04.024 — ۱۱. قواعد مشترک اجرای پروژه

##### ۱۱. قواعد مشترک اجرای پروژه

- هر Task باید Code، Test، Acceptance، Documentation و Commit مشخص داشته باشد.
- Notebook برای Exploration است؛ مسیر اصلی باید Package/CLI/API باشد.
- Raw data تغییرناپذیر و هر Release دارای Hash باشد.
- هیچ تصمیم معماری بدون ADR و هیچ انتخاب مدل بدون Benchmark نباشد.
- هیچ Secret، PII یا Test set محرمانه وارد Git نشود.
- هر Claim پاسخ باید Citation معتبر یا دلیل Abstention داشته باشد.
- اطلاعات شخصی کاربر در PostgreSQL باقی بماند و بدون نیاز روشن وارد Vector DB نشود.
- تغییرات Dataset، Index، Prompt، Policy و Rules باید Versioned و قابل Rollback باشند.


<a id="s04-u025"></a>

### S04.025 — ۱۲. شاخص نهایی موفقیت

##### ۱۲. شاخص نهایی موفقیت

معیار موفقیت، تعداد پیام نیست:

- کیفیت Citation و Grounded answer.
- تشخیص صحیح سؤال بی‌پاسخ و پرریسک.
- تکمیل آزمون و مسیر یادگیری.
- انجام اقدام پیشنهادشده.
- بهبود آزمون مجدد و شاخص‌های تعریف‌شده.
- حفظ حریم خصوصی و نبود نشت بین کاربران.
- هزینه و پایداری قابل کنترل.


<a id="s04-u026"></a>

### S04.026 — ۱۳. تصمیم نهایی

##### ۱۳. تصمیم نهایی

مسیر چهارمرحله‌ای درست است، به شرط آنکه:

1. فاز ۲ با RAG Core واقعی و Benchmark بسته شود.
2. فاز ۳ فقط Demo آنلاین نباشد و الزامات محصول چندکاربره را پاس کند.
3. فاز ۴ چت را به Assessment، Rules، Action و Outcome متصل کند.
4. مستندات دانش فنی در هر Gate هم‌زمان تولید شوند.

با این مرزبندی، پروژه دلیل روشنی برای انتخاب شدن به‌جای AI عمومی دارد و از نظر فنی قابلیت تبدیل شدن به محصول قابل دفاع را خواهد داشت.


## جزئیات منبع S07

> فایل اصلی: RAG_finance_NB21_Project_Skill_Reference_FA(4).md
>
> مرجع ترکیبی قدیمی تا C008/اقدام۲۰؛ نصب Skill انجام نشده؛ Snapshot آن دستور Resume فعلی نیست. بخش اجرایی ابتدای این فایل، قاعدهٔ استفاده از متن زیر است.



<a id="s07-u014"></a>

### S07.014 — ۸. مخزن، شاخه، مسیرها و اختیار

##### ۸. مخزن، شاخه، مسیرها و اختیار

| مورد | مقدار |
| --- | --- |
| مخزن | https://github.com/Shahbazi-Amir/RAG_finance |
| شاخه | `rag-phase2` |
| فاز دوم | `notebooks/phase2/` |
| نقشه‌ها | `data/Road_Maps/` |
| چک‌لیست | `notebooks/phase2/NB21_remaining_work_checklist_fa.md` |
| NB21 اصلی | `notebooks/phase2/21_evaluation_and_ablation.ipynb` |
| فایل ادامه | `notebooks/phase2/21b_evaluation_and_ablation_continued.ipynb` |
| خروجی‌ها | `artifacts/phase2/evaluation_and_ablation/work/outputs/` |
| مسیر گزارش‌شدهٔ Mac | `/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance` |
| شاخهٔ پشتیبان تاریخی | `backup/nb21-before-sync-c110245` |

- مسیر شخصی فقط اطلاعات محیط است؛ داخل منطق نوت‌بوک Hard-code نشود. Project root از ساختار واقعی کشف شود.
- مخزن از سوی این چت فقط خوانده شود. بدون درخواست صریح، Commit، Push، تغییر Branch، ویرایش چک‌لیست یا تغییر مستقیم فایل مخزن انجام نشود.
- اجرا روی سیستم کاربر در VS Code/Jupyter است. کد کامل برای کاربر ارائه می‌شود.
- فقط در صورت نیاز واقعی خواندن مخزن، دسترسی همان موقع بررسی شود. در این چت، دریافت زندهٔ GitHub ناموفق و `git ls-remote` نیازمند احراز هویت شد؛ تأیید زندهٔ Remote ادعا نشود.
- آخرین Preflight کاربر: HEAD محلی `db24206cb953324a960bbe90c0cf8aaed964295f`، شاخه `rag-phase2`، Working tree پاک و بدون تعارض؛ مرجع محلی `origin/rag-phase2` برابر HEAD بود. **`remote_checked_live=false`**.
- این وضعیت لحظه‌ای است؛ ذخیرهٔ سل‌های بعدی ممکن است فایل محلی را تغییر دهد.
- `pull --autostash`، `git add .`، Force push یا `git add -f` برای شواهد ignored خودکار پیشنهاد نشوند.


<a id="s07-u015"></a>

### S07.015 — ۹. دامنهٔ رسمی و تقدم نقشه‌ها

##### ۹. دامنهٔ رسمی و تقدم نقشه‌ها

فاز ۲: Knowledge/RAG Core سه‌منبعی، داده و Index نسخه‌دار، Retrieval، پاسخ مستند، Citation، Answerability، Safety و Benchmark. فاز ۳: پلتفرم و لانچ چندکاربره. فاز ۴: Assessment، مسیر یادگیری، برنامه اقدام و پایش رشد.

ترتیب درست انتهای فاز دوم، طبق اصلاح صریح تحویل و چک‌لیست:

| نوت‌بوک | مأموریت |
| --- | --- |
| NB21 | `21_evaluation_and_ablation.ipynb`؛ ارزیابی، شش Ablation و Regression Gate |
| NB21b | ادامهٔ فیزیکی همان NB21، نه NB22 |
| NB22 | `22_release_and_reproducibility.ipynb`؛ Release و بازتولیدپذیری |
| NB23 | `23_phase3_handoff.ipynb`؛ قرارداد تحویل فاز سوم |

بخش ۲۶ Execution Protocol ترتیب قدیمی Regression/Performance/Release را دارد؛ برای نام و دامنهٔ ادامه استفاده نشود. قواعد معتبر همان پروتکل مانند Cache-first، عدم تضعیف Validation و حفظ Evidence برقرارند.

خروجی‌های رسمی NB21: Benchmark report، Ablation report، Error taxonomy، Failure cases، Phase-1 comparison و Regression Gate؛ به‌علاوهٔ اتصال‌ها و Manifest لازم برای مصرف مستقل NB22.

شش Ablation الزامی: بدون Persian normalization؛ Character در برابر Structure-aware؛ Dense-only در برابر Hybrid؛ بدون Reranker؛ بدون Source diversity؛ بدون Citation verifier. مقایسهٔ Proxy یا گزینهٔ ازقبل‌غیرفعال، Ablation کامل نیست.

عددهای Target در نقشه‌ها بدون مصوبه، Gate قطعی نیستند. اختلاف مستند Coverage استناد ۰٫۹۰ در برنامهٔ تفصیلی و ۹۵٪ در نقشهٔ عملیاتی باید با تصمیم معتبر حل شود؛ معیار آسان‌تر خودسرانه انتخاب نشود.

برنامهٔ تفصیلی نوت‌بوک‌ها، چارچوب سؤالات و README در پیوست‌های موجودِ این چت به‌عنوان فایل مستقل نبودند؛ گزارش نقل‌شده از تحویل/چک‌لیست را مطالعهٔ مستقیم زندهٔ آن‌ها معرفی نکن. فایل‌های مربوط در صورت نیاز از همان پروژه دریافت/خوانده شوند، نه با درخواست ارسال دوبارهٔ تمام پیوست‌ها.


<a id="s07-u016"></a>

### S07.016 — ۱۰. قیود دانش و سه منبع

##### ۱۰. قیود دانش و سه منبع

- Website: نویسنده مستقیم با نظارت سردبیری یکسان نیست؛ نویسنده واقعی حفظ شود.
- Book: Work، Edition و File جدا؛ صفحه فقط با مرجع صفحه‌بندی معتبر، وگرنه Anchor پایدار.
- Transcript: گوینده، مجری، مهمان و Context حفظ شوند؛ مجاورت با پاسخ دکتر، انتساب به او ایجاد نمی‌کند.
- Knowledge Authority، Source Attribution و Conversation Context جدا بمانند.
- موضوع حل‌نشده، شکست Retrieval و پوشش کم به‌تنهایی Knowledge Gap واقعی نیستند.
- مشابهت متن به‌تنهایی مجوز حذف/ادغام منبع نیست؛ Lineage و استقلال منابع حفظ شوند.
- مرجع دادهٔ پس از NB10 جمعیت ۱۹٬۴۵۶ Document را گزارش کرده: Website=529، Book=2701، Transcript=16226. این‌ها snapshot تاریخی سندند، نه شمارش تازهٔ سیستم.
- چهار لایهٔ همان مرجع: Core primary=14705، Supervised secondary=453، Contextual nonprimary=1944، Unresolved context=2354. Unresolved به دکتر نسبت داده نشود.
- حقوق محتوا: طبق Guardrails و دستور پروژه مجوز پردازش تأیید شده؛ Gate مصنوعی حقوقی یا محدودسازی خودکار به INTERNAL_EVALUATION_ONLY دوباره ساخته نشود. Metadata تاریخی Rights حفظ شود. این مجوز جای شاهد کیفیت و ایمنی نیست.


<a id="s07-u017"></a>

### S07.017 — ۱۱. تاکسونومی و وضعیت نگاشت

##### ۱۱. تاکسونومی و وضعیت نگاشت

فایل تاکسونومی:

```text
artifacts/phase2/taxonomy/taxonomy_v1.json
SHA256: 335690044b2e4eff684f7f347809f2c5cb8c39624a939dc01408d9ca898fe977
```

هفت موضوع اصلی: `financial_literacy_foundations`، `spending_saving_money_management`، `credit_debt_banking`، `work_income`، `investment`، `risk_insurance`، `financial_decision_making`.

- `taxation_and_financial_obligations` ماژول آموزشی بدون والد موضوعی است؛ موضوع اصلی هشتم نیست.
- `product_presentation_and_promotion` گرهٔ Curriculum/Subtopic با ارتباط `work_income` است؛ ماژول مجاز تازه از آن ساخته نشود.
- واژه‌های قیمت، سود و انتخاب Global alias یک موضوع نیستند؛ زمینهٔ محلی و ساختار منبع مهم است.
- `financial_literacy_foundations` برچسب پیش‌فرض تمام مفاهیم مالی نیست؛ مفاهیم سواد مالی، اهمیت، آموزش، استانداردها و توانمندی مالی باید واقعاً مطرح باشند.
- Topic از subject درخواست، Question type از task درخواست تعیین شود. نبود پاسخ کافی، نوع درخواست را خودکار نامعلوم نمی‌کند.
- Topic/Authority/Question type با حدس پر نشوند. نگاشت نامعتبر با `NOT_ASSESSED_NO_CANONICAL_MAPPING` و تعداد گزارش شود.
- نبود واژه در فهرست لنگرها، به‌تنهایی اثبات OUT_OF_SCOPE نیست. نقص قرارداد با ابهام خود سؤال یکی نیست.
- چندبرچسبی نیازمند موضوع/مطالبهٔ مستقل است؛ صرف واژه در پاسخ یا شمول منطقی یک برچسب، برچسب اضافی ایجاد نکند.

ده نوع سؤال پیشنهادی: `CAUSE_EXPLANATION`، `COMPARISON`، `CONDITION_CONSTRAINT`، `DEFINITION`، `ENUMERATION_CLASSIFICATION`، `EXAMPLE_APPLICATION`، `FACT_IDENTIFICATION`، `PROCEDURE_ACTION`، `QUANTITATIVE`، `RECOMMENDATION_DECISION`.

وضعیت‌ها: ASSIGNED؛ MODULE_ONLY فقط برای موضوع؛ AMBIGUOUS؛ OUT_OF_SCOPE؛ INSUFFICIENT_CONTEXT. MODULE_ONLY نیازمند labels خالی و module_ids غیرخالی است؛ برای وضعیت‌های نامعین دیگر labels/modules خالی بمانند.


## جزئیات منبع S09

> فایل اصلی: RAG_finance_Phase2_Execution_Protocol_FA(5).md
>
> Execution Protocol؛ نام‌گذاری قدیمی بخش۲۶ با ترتیب معتبر NB21/NB22/NB23 جایگزین شده است. بخش اجرایی ابتدای این فایل، قاعدهٔ استفاده از متن زیر است.



<a id="s09-u003"></a>

### S09.003 — 1. اصل حاکم: وفاداری کامل به نقشه‌ی اصلی

#### 1. اصل حاکم: وفاداری کامل به نقشه‌ی اصلی

نقشه‌های رسمی Phase 2، مرجع تعیین Scope، ترتیب Notebookها، مسئولیت هر
Notebook و Definition of Done هستند.

هیچ Notebook نباید به‌دلیل آزمایش‌های جانبی، ایده‌های جدید یا توسعه‌ی
تدریجی، مسئولیت Notebookهای بعدی را به خود جذب کند.

اگر بین وضعیت فعلی Notebook و Roadmap تعارضی وجود داشت:

1.  ابتدا تعارض مشخص شود.
2.  Scope رسمی Roadmap ملاک قرار گیرد.
3.  کار تاریخی مفید حفظ شود، اما نباید Scope رسمی را تغییر دهد.
4.  کار خارج از Scope یا به Notebook رسمی خودش منتقل شود یا فقط به‌عنوان
    Experiment تاریخی ثبت شود.

**قاعده:**\
هر Notebook باید فقط مأموریت خودش را کامل کند؛ نه کمتر و نه بیشتر.

------------------------------------------------------------------------


<a id="s09-u012"></a>

### S09.012 — 10. Scope Creep ممنوع

#### 10. Scope Creep ممنوع

در حین کار ممکن است ایده‌ی مفیدی برای مرحله‌ی دیگری پیدا شود.

این ایده نباید فوراً Notebook فعلی را بزرگ کند.

مثلاً:

-   NB13 مأمور Embedding Benchmark است.
-   NB14 مأمور Dense Index است.
-   NB15 مأمور Sparse Index است.
-   NB16 مأمور Hybrid Retrieval است.
-   NB17 مأمور Reranking است.

اگر هنگام NB14 ایده‌ی Reranking ایجاد شد، آن را ثبت می‌کنیم اما NB14 را به
آزمایشگاه Reranking تبدیل نمی‌کنیم.

**هر Notebook یک مسئولیت اصلی دارد.**

------------------------------------------------------------------------


<a id="s09-u013"></a>

### S09.013 — 11. Research Path و Production Path جدا بمانند

#### 11. Research Path و Production Path جدا بمانند

آزمایش exploratory می‌تواند مفید باشد، اما نباید با مسیر Canonical مخلوط
شود.

هر نتیجه باید مشخص کند که یکی از این‌هاست:

-   Experimental
-   Candidate
-   Accepted
-   Canonical
-   Frozen
-   Historical / Archived

یک Experiment موفق تا زمانی که Gateهای رسمی را پاس نکرده، نباید به‌عنوان
تصمیم Production معرفی شود.

------------------------------------------------------------------------


<a id="s09-u020"></a>

### S09.020 — 18. داده و Artifact فریز‌شده دست‌نخورده بماند

#### 18. داده و Artifact فریز‌شده دست‌نخورده بماند

Golden Dataset، Registry، Index Snapshot یا هر Artifact فریز‌شده نباید
صرفاً برای راحتی اجرای Notebook بعدی تغییر داده شود.

اگر Notebook جدید با Artifact Canonical سازگار نیست، Notebook جدید باید
اصلاح شود؛ نه اینکه حقیقت مرجع پروژه برای سازگار شدن با کد جدید دستکاری
شود.

------------------------------------------------------------------------


<a id="s09-u021"></a>

### S09.021 — 19. Historical Notebookها و مسیر Canonical مخلوط نشوند

#### 19. Historical Notebookها و مسیر Canonical مخلوط نشوند

Notebookهای قدیمی برای Provenance و تاریخچه مفیدند، اما نباید باعث ابهام
شوند که مسیر اصلی پروژه کدام است.

در هر خانواده:

-   یک مسیر Canonical مشخص باشد.
-   نسخه‌های Superseded/Experimental در Archive بمانند.
-   Artifact نهایی مستقل از سردرگمی تاریخی قابل شناسایی باشد.

Archive به معنی حذف تاریخچه نیست؛ به معنی جداکردن تاریخچه از مسیر اجرایی
اصلی است.

------------------------------------------------------------------------


<a id="s09-u022"></a>

### S09.022 — 20. Benchmark باید روی داده‌ی واقعی پروژه باشد

#### 20. Benchmark باید روی داده‌ی واقعی پروژه باشد

تصمیم‌های اصلی مانند انتخاب Embedding، Retrieval Strategy، Reranker و
Query Rewrite نباید صرفاً بر Benchmark عمومی یا شهرت مدل تکیه کنند.

Benchmark عمومی می‌تواند اطلاعات کمکی بدهد، اما تصمیم Production باید تا
حد ممکن با:

-   Golden Dataset پروژه
-   داده فارسی پروژه
-   سه منبع اصلی پروژه
-   Queryهای واقعی یا نماینده
-   Metricهای رسمی

پشتیبانی شود.

------------------------------------------------------------------------


<a id="s09-u023"></a>

### S09.023 — 21. Metric بدون تفسیر کافی نیست

#### 21. Metric بدون تفسیر کافی نیست

فقط تولید یک عدد کافی نیست.

برای Benchmarkهای اصلی باید مشخص شود:

-   Metric چه چیزی را اندازه می‌گیرد؟
-   Baseline چیست؟
-   Candidate چیست؟
-   بهبود یا افت کجاست؟
-   Failureها در چه نوع Query یا Source رخ می‌دهند؟
-   هزینه و Latency چه تغییری کرده؟
-   آیا نتیجه برای Promotion کافی است؟

هدف، تصمیم مهندسی مبتنی بر Evidence است؛ نه تولید جدول‌های زیاد بدون
نتیجه.

------------------------------------------------------------------------


<a id="s09-u031"></a>

### S09.031 — 26. ترتیب رسمی ادامه Phase 2 حفظ شود

#### 26. ترتیب رسمی ادامه Phase 2 حفظ شود

مسیر اصلی پروژه باید طبق Roadmap رسمی ادامه پیدا کند:

`00 Environment/Baseline`\
`→ 01 Website Ingestion`\
`→ 02 Website Acceptance`\
`→ 03 Book Inventory`\
`→ 04 Book Ingestion`\
`→ 05 Transcript Inventory`\
`→ 06 Transcript Ingestion`\
`→ 07 Unified Schema & Lineage`\
`→ 08 Persian Normalization`\
`→ 09 Deduplication & Quality`\
`→ 10 Taxonomy & Knowledge Engineering`\
`→ 11 Chunking Benchmark`\
`→ 12 Golden Dataset`\
`→ 13 Embedding Benchmark`\
`→ 14 Dense Index`\
`→ 15 Sparse Index`\
`→ 16 Hybrid Retrieval`\
`→ 17 Reranking`\
`→ 18 Query Rewrite`\
`→ 19 Citation & Grounding`\
`→ 20 Evaluation Harness`\
`→ 21 Regression Suite`\
`→ 22 Performance & Cost Benchmark`\
`→ 23 Release Candidate`

تغییر این ترتیب یا ادغام مسئولیت‌ها فقط در صورت وجود دلیل مهندسی مستند و
سازگار با Roadmap مجاز است.

------------------------------------------------------------------------


## جزئیات منبع S10

> فایل اصلی: RAG_finance_phase2_notebook_execution_guardrails_fa(5).md
>
> Guardrails؛ قاعدهٔ لغو Gate مصنوعی حقوقی و استقلال از Kernel قبلی حفظ شود. بخش اجرایی ابتدای این فایل، قاعدهٔ استفاده از متن زیر است.



<a id="s10-u007"></a>

### S10.007 — ۶. سیاست Development و Test

##### ۶. سیاست Development و Test

Development برای انتخاب Policy، Threshold، Budget، مدل، روش و Ablation استفاده می‌شود. Test فقط پس از Freeze قابل استفاده است.

بعد از مشاهده Test، Configuration، Threshold، Prompt و Budget نباید تغییر کنند. هر Artifact نهایی باید ثبت کند:

```text
configuration_changed_after_test = false
test_queries_accessed_for_retuning = false
```

اگر نقشه به Independent Test evaluation نیاز ندارد، Test metric مصنوعی ایجاد نکن و فقط Policy فریز‌شده را در محدوده لازم اعمال کن.


<a id="s10-u015"></a>

### S10.015 — ۱۴. Metadata و عدم استنتاج

##### ۱۴. Metadata و عدم استنتاج

Metadata ناقص را با حدس پر نکن. Author، Speaker، Content authority، Topic، Parent، Rights، Locator و Conflict label فقط از فیلد Canonical مربوط به خودشان گرفته شوند.

در نبود داده معتبر، یکی از وضعیت‌های مستند زیر را ثبت کن:

```text
NOT_PRESENT
NOT_APPLICABLE
NOT_ASSESSED_NO_CANONICAL_MAPPING
UPSTREAM_METADATA_LIMITATION
```


<a id="s10-u016"></a>

### S10.016 — ۱۵. مجوز پروژه

##### ۱۵. مجوز پروژه

کارفرما مجوز کامل انجام پردازش‌های این پروژه را تأیید کرده است. Gate محدودکننده قبلی مجوز از جریان پروژه حذف شده است.

- Gate مصنوعی `INTERNAL_EVALUATION_ONLY` دوباره ایجاد نکن.
- Status تحویل را بدون دلیل به `READY_FOR_INTERNAL_EVALUATION_ONLY` محدود نکن.
- Rights موجود را فقط به‌عنوان Metadata منبع حفظ کن.
- نبود بعضی فیلدهای Rights را Blocker فنی Notebook نکن.
- مجوز تأییدشده کارفرما را بدون دستور صریح دوباره زیر سؤال نبر.

این موضوع شامل مجوز API پولی یا تغییر Repository نیست؛ آن‌ها همچنان اجازه جداگانه می‌خواهند.


## جزئیات منبع S11

> فایل اصلی: RAG_finance_phase2_operational_roadmap(5).md
>
> نقشهٔ عملیاتی؛ آستانه‌ها Target اولیه‌اند؛ محدودیت حقوقی لغوشده دوباره Gate نشود. بخش اجرایی ابتدای این فایل، قاعدهٔ استفاده از متن زیر است.



<a id="s11-u001"></a>

### S11.001 — معرفی، نسخه و منشأ سند




<a id="s11-u002"></a>

### S11.002 — نقشه عملیاتی فاز ۲ RAG_finance

#### نقشه عملیاتی فاز ۲ RAG_finance

**Knowledge Engineering، RAG Core، Citation، Safety و Evaluation**

| <span dir="ltr">Repository</span> | <span dir="ltr">Shahbazi-Amir/RAG_finance</span> |
| ---: | ---: |
| Branch مبنا | <span dir="ltr">rag-phase2</span> |
| Commit ممیزی | <span dir="ltr">96c0f0c7d09f4bff107ed71664a0c57ed09f3214</span> |
| تاریخ نسخه | ۲۱ اوت ۲۰۲۶ |
| دامنه | RAG Core؛ خارج از Deployment و پنل شخصی |


<a id="s11-u003"></a>

### S11.003 — ۱. تعریف Done فاز ۲

##### ۱. تعریف Done فاز ۲

فاز ۲ زمانی تمام است که:

- مقاله، کتاب و Transcript هرکدام Pipeline مستقل و قابل تکرار داشته باشند.
- هر Document و Chunk به Raw source و مالکیت/منشأ آن برگردد.
- Dataset، Chunk set، Embedding و Index نسخه‌دار و قابل بازسازی باشند.
- Retrieval با Baselineهای Dense و Sparse مقایسه شده باشد.
- انتخاب Hybrid/Reranker فقط با Benchmark انجام شده باشد.
- پاسخ ساخت‌یافته، Claim-level Citation و Citation verification داشته باشد.
- سؤال بی‌پاسخ، مبهم و پرریسک تشخیص داده شود.
- Golden Dev/Test، Regression gate و گزارش فنی وجود داشته باشد.


<a id="s11-u004"></a>

### S11.004 — ۲. مدل منشأ و مالکیت منابع

##### ۲. مدل منشأ و مالکیت منابع

نباید Author، Knowledge Owner، Curator و Rights Holder با یکدیگر مخلوط شوند.

| گروه | content_origin پیشنهادی | نکته ثبت |
| ---: | ---: | ---: |
| مقاله مستقیم مؤلف | <span dir="ltr">primary_author</span> | author و knowledge_owner هر دو مؤلف |
| مقاله زیر نظر سردبیری | <span dir="ltr">editorial_supervised</span> | author واقعی جدا؛ curation_owner مؤلف |
| کتاب و نوشتار تألیفی | <span dir="ltr">authored_work</span> | work، edition و rights evidence |
| تدریس و آموزش مؤلف | <span dir="ltr">self_instruction</span> | speaker، program و timestamp |
| مصاحبه | <span dir="ltr">interview</span> | interviewer/host و speaker جدا |
| برنامه تلویزیونی | <span dir="ltr">broadcast</span> | broadcaster، episode، speaker و rights evidence |

فیلدهای الزامی:

- <span dir="ltr">creator/author</span>
- <span dir="ltr">knowledge_owner</span>
- <span dir="ltr">curation_owner</span>
- <span dir="ltr">rights_holder</span>
- <span dir="ltr">rights_status</span>
- <span dir="ltr">rights_evidence_id</span>
- <span dir="ltr">allowed_uses</span>
- <span dir="ltr">attribution_text</span>
- <span dir="ltr">content_origin</span>

وجود محتوا در Repository به‌تنهایی مدرک حقوق بهره‌برداری نیست. موارد فاقد مدرک در Quarantine باقی بمانند.


<a id="s11-u005"></a>

### S11.005 — ۳. جریان کل فاز ۲

##### ۳. جریان کل فاز ۲

<div dir="ltr" align="left">Freeze/Baseline           ↓     Contracts + IDs + Rights           ↓     Website | Book | Video/Audio           ↓     Canonical Dataset Release           ↓     Normalize + Source-aware Chunk           ↓     Embed + Versioned Index           ↓     Dense/Sparse/Hybrid/Rerank           ↓     Context + Claims + Citation + Safety           ↓     Golden Evaluation + Release Candidate</div>


<a id="s11-u006"></a>

### S11.006 — ۴. بسته P2-01 - Freeze و Baseline فاز ۱

##### ۴. بسته P2-01 - Freeze و Baseline فاز ۱


<a id="s11-u007"></a>

### S11.007 — کارها

###### کارها

- Tag نسخه نهایی Demo و ثبت SHA.
- ثبت ۷۶ Document، ۱۶۸ Chunk، تنظیم Chunk 1200/200 و مدل‌ها.
- اجرای دوباره ۱۰ سؤال موجود و ثبت پاسخ، منابع، latency و خطا.
- ثبت ناهماهنگی Config مدل و محدودیت‌های Known.
- ADR جداسازی فاز ۱ و ۲ و Deprecation plan.


<a id="s11-u008"></a>

### S11.008 — خروجی

###### خروجی

- <span dir="ltr">docs/baseline/phase1_baseline.md</span>
- <span dir="ltr">reports/baseline/phase1_results.json</span>
- <span dir="ltr">docs/adr/ADR-000-phase-boundary.md</span>


<a id="s11-u009"></a>

### S11.009 — Gate

###### Gate

نسخه فاز ۱ از محیط تمیز قابل اجرا و نتیجه آن مرجع مقایسه باشد.


<a id="s11-u010"></a>

### S11.010 — ۵. بسته P2-02 - Data Contract، Stable IDs و Versioning

##### ۵. بسته P2-02 - Data Contract، Stable IDs و Versioning


<a id="s11-u011"></a>

### S11.011 — کارها

###### کارها

- تعریف JSON Schema برای Source، Document، Chunk، Citation و Dataset Release.
- تعریف Adapter schema برای Website، Book و Video/Audio.
- تعریف ID policy و migration policy.
- ثبت raw hash، processed hash، pipeline/extractor/normalizer/chunker version.
- طراحی Artifact Registry برای Dataset، Chunks، Embeddings، Index و Eval.


<a id="s11-u012"></a>

### S11.012 — خروجی

###### خروجی

- <span dir="ltr">schemas/source.schema.json</span>
- <span dir="ltr">schemas/document.schema.json</span>
- <span dir="ltr">schemas/chunk.schema.json</span>
- <span dir="ltr">schemas/citation.schema.json</span>
- <span dir="ltr">schemas/dataset_release.schema.json</span>
- <span dir="ltr">docs/data/id_policy.md</span>
- <span dir="ltr">docs/data/schema_migration.md</span>


<a id="s11-u013"></a>

### S11.013 — Gate

###### Gate

نمونه معتبر و نامعتبر هر سه منبع با تست Schema بررسی شود و IDها deterministic باشند.


<a id="s11-u014"></a>

### S11.014 — ۶. بسته P2-03 - Website Pipeline V2

##### ۶. بسته P2-03 - Website Pipeline V2


<a id="s11-u015"></a>

### S11.015 — کارها

###### کارها

- انتقال منطق Notebook موفق ۵۲۹ مقاله به Package/CLI.
- Discovery، Canonical URL، Raw snapshot، extraction و validation.
- حفظ article_id، URL، title، author، date، tags، origin و hash.
- Change detection برای NEW/UPDATED/UNCHANGED/MISSING.
- Resume، retry، backoff، idempotency و failure classification.
- گزارش Crawl و Processing مستقل.


<a id="s11-u016"></a>

### S11.016 — Gate

###### Gate

- دو اجرای ورودی ثابت، Manifest و خروجی یکسان بدهند.
- تغییر کنترل‌شده فقط Documentهای متاثر را بازپردازش کند.
- هیچ Empty content به‌عنوان Success ثبت نشود.
- Attribution مقاله مستقیم و سردبیری به‌درستی تفکیک شود.


<a id="s11-u017"></a>

### S11.017 — ۷. بسته P2-04 - Book Pipeline

##### ۷. بسته P2-04 - Book Pipeline


<a id="s11-u018"></a>

### S11.018 — کارها

###### کارها

- ساخت Works/Edition registry برای ۷ فایل موجود و هر نسخه جایگزین.
- پردازش DOCX؛ پشتیبانی PDF/EPUB فقط در صورت وجود ورودی.
- استخراج Chapter/Section/Paragraph و حذف Header/Footer.
- حفظ Raw و تولید location anchor پایدار.
- Page citation فقط با نسخه مرجع صفحه‌بندی‌شده.
- تشخیص exact/near duplicate و ویرایش‌های متفاوت.


<a id="s11-u019"></a>

### S11.019 — Gate

###### Gate

هر قطعه متن به Work، Edition، Chapter، Location و Rights evidence معتبر برگردد.


<a id="s11-u020"></a>

### S11.020 — ۸. بسته P2-05 - Video/Audio Transcript Pipeline

##### ۸. بسته P2-05 - Video/Audio Transcript Pipeline


<a id="s11-u021"></a>

### S11.021 — کارها

###### کارها

- Registry سری/برنامه/قسمت/رسانه و نوع محتوا.
- Segment schema شامل start_ms، end_ms، speaker، text و verification status.
- Validation ترتیب زمان، overlap/gap، duplicate و empty segment.
- Normalization فارسی بدون بازنویسی معنایی.
- حفظ اصطلاحات مالی، اعداد و نام‌ها.
- ثبت timestamp_unavailable وقتی منبع زمان ندارد؛ عدم جعل زمان.


<a id="s11-u022"></a>

### S11.022 — Gate

###### Gate

هر Transcript به Episode و رسانه اصلی متصل و هر Segment قابل Cite یا صریحاً فاقد Timestamp باشد.


<a id="s11-u023"></a>

### S11.023 — ۹. بسته P2-06 - Canonical Dataset و Quality

##### ۹. بسته P2-06 - Canonical Dataset و Quality


<a id="s11-u024"></a>

### S11.024 — کارها

###### کارها

- تبدیل سه Adapter به Common Document Model.
- Deduplication در Document، Paragraph و Chunk.
- Quarantine برای rights/schema/quality نامعتبر.
- Quality report بر اساس source type و content origin.
- Dataset card، release manifest و cryptographic hashes.


<a id="s11-u025"></a>

### S11.025 — معیار

###### معیار

- ۱۰۰٪ رکوردهای Release دارای Schema، lineage، hash و rights_status.
- تعداد Missing metadata و Excludedها صریح گزارش شود.
- هیچ عددی درباره کامل بودن بدون Manifest قابل اثبات اعلام نشود.


<a id="s11-u026"></a>

### S11.026 — ۱۰. بسته P2-07 - فارسی‌سازی و Source-aware Chunking

##### ۱۰. بسته P2-07 - فارسی‌سازی و Source-aware Chunking


<a id="s11-u027"></a>

### S11.027 — کارها

###### کارها

- Normalizer تست‌شده برای Unicode، ی/ک، ZWNJ، اعداد، فاصله و punctuation.
- Offset map میان Raw و Processed برای Citation.
- Chunker جدا برای Website، Book و Transcript.
- حفظ Heading/Chapter/Page-or-anchor/Timestamp.
- آزمایش 300-500، 500-800 و 800-1200 token.
- آزمایش Parent-child و semantic boundaries.


<a id="s11-u028"></a>

### S11.028 — Gate

###### Gate

هیچ Chunk بدون document_id، parent/location، dataset_version و content_hash وارد Index نشود؛ Strategy با Benchmark انتخاب شود.


<a id="s11-u029"></a>

### S11.029 — ۱۱. بسته P2-08 - Golden Dataset

##### ۱۱. بسته P2-08 - Golden Dataset


<a id="s11-u030"></a>

### S11.030 — طراحی پیشنهادی

###### طراحی پیشنهادی

حداقل پیشنهادی ۳۰۰ سؤال؛ عدد نهایی پس از Sampling و توان بازبینی تعیین شود:

- سؤال مستقیم، مفهومی، مقایسه‌ای و چندمنبعی.
- Website، Book، Video و Cross-source.
- <span dir="ltr">Entity/number/exact phrase.</span>
- سؤال مبهم، بدون پاسخ، خارج از دامنه و Hard negative.
- درخواست توصیه سرمایه‌گذاری یا پیش‌بینی.
- تعارض دو منبع و سؤال نیازمند تازگی.


<a id="s11-u031"></a>

### S11.031 — هر رکورد

###### هر رکورد

- question، intent، topic، difficulty و source_type.
- gold_documents، gold_spans/locations و expected claims.
- answerability و abstention reason.
- safety label و reviewer decision.


<a id="s11-u032"></a>

### S11.032 — Gate

###### Gate

راهنمای Annotation، توافق بازبینان، 70/30 Dev/Test و Freeze تست نهایی وجود داشته باشد.


<a id="s11-u033"></a>

### S11.033 — ۱۲. بسته P2-09 - Embedding و Index V2

##### ۱۲. بسته P2-09 - Embedding و Index V2


<a id="s11-u034"></a>

### S11.034 — کارها

###### کارها

- حفظ text-embedding-3-large به‌عنوان Baseline فاز ۱.
- Benchmark حداقل یک گزینه دیگر روی فارسی پروژه.
- ثبت Recall، latency، cost، dimension و failure rate.
- ساخت Index نسخه‌دار با Payload کامل.
- Rebuild، Add، Update، Delete و Re-index.
- Verification: expected chunks برابر indexed points.


<a id="s11-u035"></a>

### S11.035 — Gate

###### Gate

هر Index به Dataset، Chunker و Embedding release مشخص متصل و از صفر قابل بازسازی باشد.


<a id="s11-u036"></a>

### S11.036 — ۱۳. بسته P2-10 - Retrieval Engineering

##### ۱۳. بسته P2-10 - Retrieval Engineering


<a id="s11-u037"></a>

### S11.037 — آزمایش‌ها

###### آزمایش‌ها

1. Dense baseline.
2. BM25/Sparse baseline.
3. Hybrid با RRF و Weighted fusion.
4. Hybrid + Reranker.
5. Metadata filtering و source balancing.


<a id="s11-u038"></a>

### S11.038 — Metrics

###### Metrics

- Recall@5/10، Precision@k، MRR، nDCG و Hit rate.
- Context precision/recall و source coverage.
- p50/p95 latency و cost.


<a id="s11-u039"></a>

### S11.039 — Gate

###### Gate

روش نهایی فقط با Experiment matrix و ADR انتخاب شود. افزایش پیچیدگی بدون بهبود معنادار پذیرفته نیست.


<a id="s11-u040"></a>

### S11.040 — ۱۴. بسته P2-11 - Context، Generation و Citation

##### ۱۴. بسته P2-11 - Context، Generation و Citation


<a id="s11-u041"></a>

### S11.041 — کارها

###### کارها

- Context compiler با dedup، diversity، token budget و source balance.
- جداسازی Evidence از Instruction و کنترل prompt injection داخل سند.
- خروجی ساخت‌یافته Answer، Claims و Citations.
- Citation mapper و verifier برای claim support و location accuracy.
- Conflict handling و بیان اختلاف منابع.
- Cache key شامل همه Versionها و پارامترهای موثر.


<a id="s11-u042"></a>

### S11.042 — Citation

###### Citation

- Website: title، canonical URL و span/section.
- Book: work، edition، chapter و page یا stable anchor.
- Video/Audio: program، episode و start/end timestamp یا segment anchor.


<a id="s11-u043"></a>

### S11.043 — Gate

###### Gate

هر Claim factual دارای Citation معتبر باشد و Citation بازشده دقیقاً Evidence همان Claim را نشان دهد.


<a id="s11-u044"></a>

### S11.044 — ۱۵. بسته P2-12 - Answerability، Safety و Confidence

##### ۱۵. بسته P2-12 - Answerability، Safety و Confidence


<a id="s11-u045"></a>

### S11.045 — Taxonomy درخواست

###### Taxonomy درخواست

- آموزش مالی.
- توضیح مفهوم یا محتوای مؤلف.
- برنامه‌ریزی عمومی.
- سؤال شخصی نیازمند داده.
- توصیه خریدوفروش/سرمایه‌گذاری.
- پیش‌بینی.
- خارج از دامنه.


<a id="s11-u046"></a>

### S11.046 — Confidence

###### Confidence

Confidence از evidence coverage، evidence agreement، citation entailment، source quality، answerability margin و freshness ساخته شود؛ score خام Qdrant یا ادعای LLM کافی نیست.


<a id="s11-u047"></a>

### S11.047 — Gate

###### Gate

روی Test set، answer/no-answer و safety جداگانه سنجیده شود و موارد بحرانی پذیرفته‌نشده صفر باشد.


<a id="s11-u048"></a>

### S11.048 — ۱۶. بسته P2-13 - Tests، CI و Reproducibility

##### ۱۶. بسته P2-13 - Tests، CI و Reproducibility

- Unit: schema، normalization، IDs، hash، chunking، cache و citation.
- Integration: هر Source تا Document/Chunk/Index و Question تا Citation.
- Failure: bad HTML، broken book، invalid transcript، API/Qdrant/LLM failure.
- Regression: سؤال‌های فاز ۱ و Golden smoke.
- Package، lockfile، config schema، CLI و container reproducibility.
- CI برای lint/test/schema/data-quality/eval smoke.


<a id="s11-u049"></a>

### S11.049 — Gate

###### Gate

در محیط تمیز، Release مشخص ساخته و Benchmark منتخب بدون تغییر دستی اجرا شود.


<a id="s11-u050"></a>

### S11.050 — ۱۷. بسته P2-14 - مستندات دانش فنی

##### ۱۷. بسته P2-14 - مستندات دانش فنی

- Architecture و ADRها.
- Data schema، lineage، rights و dataset cards.
- گزارش فارسی‌سازی، Chunking، Embedding و Retrieval.
- Ablation و failure analysis.
- Citation، hallucination، answerability و safety report.
- Model/System cards و Known limitations.
- ویدیوی اجرای reproducible pipeline.
- مقایسه مستند با «LLM + Vector DB ساده».


<a id="s11-u051"></a>

### S11.051 — ۱۸. ترتیب اجرای واقعی

##### ۱۸. ترتیب اجرای واقعی

1. P2-01 Freeze/Baseline.
2. P2-02 Contracts/IDs/Rights.
3. P2-03 تا P2-05 به‌ترتیب یا موازی پس از Contract.
4. P2-06 Canonical Release.
5. P2-08 Golden Dataset هم‌زمان با P2-07 Chunking.
6. P2-09 Index.
7. P2-10 Retrieval Benchmark.
8. P2-11 Citation.
9. P2-12 Safety/Confidence.
10. P2-13 Tests/Release و P2-14 Dossier.


<a id="s11-u052"></a>

### S11.052 — ۱۹. Gate نهایی و تحویل به فاز ۳

##### ۱۹. Gate نهایی و تحویل به فاز ۳

فاز ۲ فقط با این بسته تحویل می‌شود:

- Dataset release ID و Index release ID.
- <span dir="ltr">RAG input/output contract.</span>
- Citation و error/abstention schema.
- <span dir="ltr">Prompt/Policy/Model/Retrieval versions.</span>
- Golden Test report و Regression baseline.
- latency/cost profile محلی.
- <span dir="ltr">health/readiness interface contract.</span>
- release notes، rollback compatibility و known limitations.

Deployment سایت، Auth، PostgreSQL کاربران، Production monitoring و پنل کاربر متعلق به فاز ۳ هستند.


<a id="s11-u053"></a>

### S11.053 — ۲۰. معیارهای پیشنهادی اولیه

##### ۲۰. معیارهای پیشنهادی اولیه

این Targetها پس از Baseline و تأیید متخصص دامنه فریز می‌شوند:

| معیار | Target اولیه |
| ---: | ---: |
| <span dir="ltr">Data lineage/rights coverage</span> | ۱۰۰٪ Release |
| <span dir="ltr">Citation coverage</span> | حداقل ۹۵٪ Claimهای factual |
| <span dir="ltr">Citation location accuracy</span> | حداقل ۹۵٪ |
| <span dir="ltr">Unsupported claim rate</span> | حداکثر ۳٪؛ نزدیک صفر در حساس |
| <span dir="ltr">Safety critical failures</span> | صفر مورد پذیرفته‌نشده |
| <span dir="ltr">Retrieval</span> | Target پس از Baseline؛ گزارش Recall/MRR/nDCG الزامی |
| <span dir="ltr">Reproducibility</span> | اجرای کامل از محیط تمیز |


<a id="s11-u054"></a>

### S11.054 — ۲۱. تصمیم اجرایی

##### ۲۱. تصمیم اجرایی

نقشه فاز ۲ قبلی پایه‌ای قوی داشت. اصلاح قطعی این نسخه:

- Deployment از فاز ۲ حذف و به فاز ۳ منتقل شد.
- منشأ سردبیری، تألیف، مصاحبه و پخش تلویزیونی صریح شد.
- حقوق و مدرک انتساب وارد Data Contract شد.
- Citation از Source list به Claim verification ارتقا یافت.
- Golden set از ۱۰۰ سؤال اولیه به طراحی پیشنهادی ۳۰۰ سؤال ارتقا یافت.
- Safety، Confidence و قرارداد تحویل به فاز ۳ به Gate تبدیل شد.

اولین اقدام بعدی: P2-01 و P2-02 را قفل کنید؛ سپس سه Pipeline را روی همان Contract واحد کامل کنید.
