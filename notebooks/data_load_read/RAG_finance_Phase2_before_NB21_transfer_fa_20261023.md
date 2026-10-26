# مرجع انتقال فاز دوم RAG_finance — کارهای پیش از NB21

تاریخ تهیه: ۲۳ اکتبر ۲۰۲۶؛ شاخه: `rag-phase2`.

این فایل برای پیوست به چت اجرایی جدید تهیه شده است. هدف آن حفظ کارهای قبلی، پیدا کردن منابع واقعی و جلوگیری از ساخت دوبارهٔ Dataset، مرجع، داوری، Index و آزمایش است. فایل گزارش اجرای تازه یا پذیرش کل فاز دوم نیست.

## ۱. قرارداد استفاده از این انتقال

- فایل را یک‌بار کامل بخوان؛ سپس برای گام فعال به منابع مرتبط رجوع کن. خواندن همهٔ فایل‌های حجیم را پیش‌شرط هر سل تازه نکن.
- دستور فعلی کاربر و تصمیم‌های صریح جدیدتر بر متن‌های تاریخی مقدم‌اند. نقشهٔ رسمی دامنه را تعیین می‌کند؛ Artifact نسخه‌دار وضعیت واقعی را ثابت می‌کند. تعارض مهم را با ذکر دو منبع گزارش کن، نه با انتخاب خودسرانهٔ یکی.
- آخرین خروجی محلی کاربر ممکن است از GitHub جلوتر باشد. SHA این فایل را HEAD دائمی فرض نکن. نسخهٔ محلی، remote و تغییرات ذخیره‌نشده جدا هستند.
- «نبود در Git» با «نبود روی سیستم» فرق دارد؛ بخش زیادی از `work/outputs` و Cache عمداً ignore شده است. فایل ناپیدا را خودکار با API بازسازی نکن.
- اعتبار ساختاری، اتصال نسخه/هش، داوری معنایی، استقلال داور و پذیرش محصول پنج موضوع متفاوت‌اند. هیچ‌یک خودکار جای دیگری نیست.
- شمارهٔ Notebook را با شمارهٔ اقدام چک‌لیست یا Cell یکی نگیر؛ مثلاً اقدام ۲۰ NB21 با خود NB20 فرق دارد.
- ادامهٔ جاری در NB21/NB21b است. NB00 تا NB20 از صفر اجرا نمی‌شوند. NB22 و NB23 هم به نام قدیمی یا حدسی ساخته نشوند.

## ۲. مخزن و نسخهٔ مبنا

Repository: https://github.com/Shahbazi-Amir/RAG_finance

Branch: https://github.com/Shahbazi-Amir/RAG_finance/tree/rag-phase2

Notebooks: https://github.com/Shahbazi-Amir/RAG_finance/tree/rag-phase2/notebooks/phase2

آخرین HEAD کنترل‌شده هنگام تهیهٔ این فایل:

`16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5`

نسخهٔ مرجع ثابت:

https://github.com/Shahbazi-Amir/RAG_finance/tree/16bc889a4fa89a5dc2f1d92f8c33d007aa9780b5

محیط تاریخی گزارش‌شده: macOS، Jupyter، Python 3.11.3. این اطلاعات وضعیت محیط فعلی را ثابت نمی‌کند. مسیر تاریخی محلی `/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance` است؛ در کد به‌جای Hard-code از root discovery استفاده شود.

## ۳. منابع رسمی؛ ترتیب خواندن اولیه

1. [data/Road_Maps/RAG_finance_phase2_modular_notebooks_execution_plan.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_phase2_modular_notebooks_execution_plan.md)
2. [data/Road_Maps/RAG_finance_phase2_operational_roadmap.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_phase2_operational_roadmap.md)
3. [data/Road_Maps/RAG_finance_master_roadmap.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_master_roadmap.md)
4. [data/Road_Maps/RAG_finance_questions_assessments_and_validation_framework_fa.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_questions_assessments_and_validation_framework_fa.md)
5. [data/Road_Maps/RAG_finance_independent_audit_2026-08-20 .md](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/Road_Maps/RAG_finance_independent_audit_2026-08-20%20.md)
6. [notebooks/phase2/NB20_remaining_work_checklist_fa.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/NB20_remaining_work_checklist_fa.md)
7. [notebooks/phase2/NB21_remaining_work_checklist_fa.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/NB21_remaining_work_checklist_fa.md)

فایل ممیزی مستقل واقعاً یک فاصله پیش از `.md` دارد؛ URL بالا آن را encode کرده است.

فایل‌های `RAG_finance_Phase2_Execution_Protocol_FA.md`، `RAG_finance_phase2_notebook_execution_guardrails_fa.md` و `RAG_finance_data_dr_roudi_COMPLETE.md` در پیوست‌های همین گفتگو موجودند؛ لینک مخزن برایشان جعل نشده است. متن آن‌ها در پیوست همین انتقال آمده تا ارسال دوبارهٔ هر سه لازم نباشد. متن داده وضعیت پس از NB10 را توصیف می‌کند و جای Manifest جدیدتر را نمی‌گیرد. نقشه‌ها نیز قرارداد هدف‌اند؛ وجود عبارت «باید ساخته شود» در نقشه به معنی انجام‌نشدن فعلی نیست.

## ۴. نقشهٔ نوت‌بوک‌های ۰۰ تا ۲۰ و ادامه‌ها

این جدول وظیفه و محل شاهد را مشخص می‌کند؛ جدول پذیرش رسمی همهٔ Notebookها نیست. گزارش Acceptance باید با نسخهٔ همان خروجی خوانده شود.

| Notebook | کار و دارایی قابل مصرف | فایل واقعی |
| --- | --- | --- |
| NB00 | ثبت محیط و خط پایه؛ مرجع بازتولید تاریخی، نه وضعیت زندهٔ محیط. | [notebooks/phase2/00_environment_and_baseline.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/00_environment_and_baseline.ipynb) |
| NB01 | Ingestion سایت؛ Raw و lineage موجود را مصرف کن، Crawl عمومی دوباره پیش‌فرض نیست. | [notebooks/phase2/01_website_ingestion.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/01_website_ingestion.ipynb) |
| NB02 | پذیرش سایت و تفکیک نویسندهٔ واقعی از سردبیر/ناظر. | [notebooks/phase2/02_website_acceptance.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/02_website_acceptance.ipynb) |
| NB03 | موجودی کتاب و هویت نسخه‌ها. | [notebooks/phase2/03_book_inventory.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/03_book_inventory.ipynb) |
| NB04 | استخراج کتاب با ساختار و Locator؛ متن و شاهد از ابتدا استخراج نشود. | [notebooks/phase2/04_book_ingestion.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/04_book_ingestion.ipynb) |
| NB05 | موجودی Transcript و هویت منابع. | [notebooks/phase2/05_transcript_inventory.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/05_transcript_inventory.ipynb) |
| NB06 | استخراج Transcript با نقش گوینده؛ متن مهمان به مؤلف منتسب نشود. | [notebooks/phase2/06_transcript_ingestion.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/06_transcript_ingestion.ipynb) |
| NB07 | Schema و Lineage مشترک سه منبع. | [notebooks/phase2/07_unified_schema_and_lineage.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/07_unified_schema_and_lineage.ipynb) |
| NB08 | Normalizer و sidecar قبل/بعد؛ کنترل Offset و سیاست فارسی موجود است. | [notebooks/phase2/08_persian_normalization.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/08_persian_normalization.ipynb) |
| NB09 | Dedup و کیفیت؛ Corpus پذیرفته‌شدهٔ ۱۹۴۵۶ رکوردی. | [notebooks/phase2/09_deduplication_and_quality.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/09_deduplication_and_quality.ipynb) |
| NB10 | Taxonomy و Knowledge Authority؛ تغییر Taxonomy با پرکردن حدسی Slice مجاز نیست. | [notebooks/phase2/10_taxonomy_and_knowledge_engineering.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/10_taxonomy_and_knowledge_engineering.ipynb) |
| NB11 | Benchmark Chunking و Candidateهای فریز‌شده؛ تحلیل ساختاری با برتری Retrieval فرق دارد. | [notebooks/phase2/11_chunking_benchmark.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/11_chunking_benchmark.ipynb) |
| NB12 | ورودی خانوادهٔ Golden؛ فایل اصلی کوتاه است و آرشیو خانوادهٔ ۱۲ ضروری است. | [notebooks/phase2/12_golden_dataset.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/12_golden_dataset.ipynb) |
| NB13 | Benchmark Embedding و Release منتخب؛ مدل فعال مسیر پایین‌دست e5-small است. | [notebooks/phase2/13_embedding_benchmark.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/13_embedding_benchmark.ipynb) |
| NB14 | Dense Index و Release؛ مصرف Index موجود به‌جای Embedding مجدد. | [notebooks/phase2/14_dense_index.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/14_dense_index.ipynb) |
| NB15 | Sparse Index و گزارش‌های ارزیابی/Release موجود. | [notebooks/phase2/15_sparse_index.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/15_sparse_index.ipynb) |
| NB16 | Hybrid، پنج بازو، Bootstrap، Slice و مقایسهٔ تنظیمات. | [notebooks/phase2/16_hybrid_retrieval.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/16_hybrid_retrieval.ipynb) |
| NB17 | Reranking روی همان Pool، اختلاف زوجی، عدم قطعیت و تحلیل شکست. | [notebooks/phase2/17_reranking.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/17_reranking.ipynb) |
| NB18 | Context Builder، بودجه، تنوع منبع و ترتیب فریز‌شده. | [notebooks/phase2/18_context_builder.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/18_context_builder.ipynb) |
| NB19 | Generation و Claim/Citation؛ اتصال فنی با صحت معنایی مستقل یکی نیست. | [notebooks/phase2/19_generation_and_citation.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/19_generation_and_citation.ipynb) |
| NB20 | Answerability/Safety/Confidence و ادامه‌های 20b و 20c؛ پذیرش‌های دامنه‌دار را دقیق بخوان. | [notebooks/phase2/20_answerability_safety_confidence.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/20_answerability_safety_confidence.ipynb) |

### ادامه‌های مهم و آرشیو خانوادهٔ ۱۲

- [notebooks/phase2/13_embedding_benchmark_closure_candidate.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/13_embedding_benchmark_closure_candidate.ipynb)
- [notebooks/phase2/20b_answerability_safety_confidence_scoped_review.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/20b_answerability_safety_confidence_scoped_review.ipynb)
- [notebooks/phase2/20c_answerability_safety_confidence_audit_and_acceptance.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/20c_answerability_safety_confidence_audit_and_acceptance.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12a_golden_dataset_initial.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12a_golden_dataset_initial.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12b_golden_dataset_continuation_compact.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12b_golden_dataset_continuation_compact.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12c_human_review_for_author.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12c_human_review_for_author.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12d_second_human_review.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12d_second_human_review.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12e_golden_dataset_full_generation.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12e_golden_dataset_full_generation.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12f_author_feedback_integration.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12f_author_feedback_integration.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_quality_rebuild_lab.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_quality_rebuild_lab.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_rebuild_clean.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_rebuild_clean.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12h_pilot_and_expansion_audit.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12h_pilot_and_expansion_audit.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12i_claim_registry_and_knowledge_graph.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12i_claim_registry_and_knowledge_graph.ipynb)
- [notebooks/phase2/archive/series12_notebooks/12j_golden_dataset_v2_registry_driven_rebuild.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/archive/series12_notebooks/12j_golden_dataset_v2_registry_driven_rebuild.ipynb)

ترتیب رسمی ادامه: `21_evaluation_and_ablation.ipynb` سپس `22_release_and_reproducibility.ipynb` سپس `23_phase3_handoff.ipynb`. نام‌های پیشنهادی قدیمی «21_regression_suite» و «22_performance_cost» مبنا نیستند. 21b ادامهٔ NB21 است، نه Notebook رسمی جدید با دامنهٔ مستقل.

## ۵. دارایی‌های قبلی و حدود استفادهٔ آن‌ها

بخش‌های زیر از ممیزی فقط‌خواندنی قبلی همین گفتگو منتقل شده‌اند. عددها Snapshot خود را دارند؛ برای ادغام با پاسخ فعلی باید نسخه و کلید وظیفه تطبیق یابد.

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


## ۶. بستهٔ پایان NB20c؛ حفظ شود، دوباره ممیزی نشود

تصمیم تاریخی: دور ممیزی NB20c در C455 تحویل داده شده و برای گزارش تکراری به آن سل اضافه نشود. این پایان همان دور ممیزی است؛ نه پذیرش ایمنی زنده، نه پایان کل فاز دوم. هر ۳۱ اقدام NB20 تیک دارند، اما یادداشت دامنهٔ تیک‌ها بخشی از قرارداد است.

### معنای تیک‌ها

هر ۳۱ اقدام در GitHub تیک خورده‌اند، اما بخشی صریحاً دامنه‌دارند:

| اقدامات | آنچه ثبت شد | آنچه نتیجه نمی‌شود |
|---|---|---|
| ۲۳ و ۲۴ | اندازه‌گیری چهار پروندهٔ آفلاین و آزمون فنی خروجی توصیفی | اعتبار معنایی کل جمعیت یا Confidence محصول |
| ۲۵ تا ۲۸ | خط پایهٔ کالیبره‌شده برای حضور شاهد مرجع | احتمال درستی پاسخ یا Confidence چهارمؤلفه‌ای |
| ۲۹ | تعیین‌تکلیف ۳۰ نامعین باقی‌مانده در ممیزی ذخیره‌شده | پذیرش کیفیت تمام پاسخ‌ها |
| ۳۰ | عبور شروط ثبت‌شدهٔ دروازهٔ ممیزی پسینی | پذیرش رسمی ایمنی محصول زنده |
| ۳۱ | بازتولید مستقل Artifactهای نهایی و فایل تحویل | Run All کل نوت‌بوک یا بازاجرای تمام کنترل‌های اولیه |

این وضعیت‌ها همچنان false هستند:

```text
formal_live_product_safety_accepted
semantic_judgments_independently_validated
live_deployment_authorized
full_phase2_roadmap_completed
entire_notebook_run_all_performed
all_original_source_checks_rerun
```

## ۶. خلاصهٔ نتایج معتبر

### جمعیت

```text
development: 2664
test: 1149
total: 3813
```

### ممیزی ایمنی

رجیستری تاریخی:

```text
NONCRITICAL: 1114
UNDETERMINED: 35
```

نمای C72 پس از پنج تعیین‌تکلیف:

```text
NONCRITICAL: 1119
UNDETERMINED: 30
```

نمای نهایی پس از C436:

```text
NONCRITICAL: 1149
CRITICAL: 0
UNDETERMINED: 0
NOT_ASSESSED: 0
```

این‌ها نتیجهٔ برچسب‌های ممیزی در دامنهٔ ذخیره‌شده‌اند؛ دقت ۱۰۰٪، ایمنی همهٔ کاربردها یا مرجع مستقل نیستند.

### اتصال و بازتولید

- یکپارچگی هش ۳۱۳۰ فایل پشتیبان بررسی شد.
- ۲۵ هشدار اولیه مربوط به توصیف Schema و خلاصهٔ مراحل بود؛ فایل مفقود یا هش متفاوت محسوب نشد.
- اتصال ورودی بازبینی تمام ۱۱۴۹ پرونده تأیید شد.
- منابع اصلی C38: تعداد ۶۸۹۴ کنترل هش رکورد و ۱۱۴۹ کنترل هش پاسخ گذشت.
- بازتولید برچسب هر پرونده در فرایند مستقل Python با `-I` موفق بود.
- این اجرا وابسته به متغیرهای Kernel قبلی نبود.
- دامنه فقط بازتولید Artifactهای نهایی بود؛ Run All کامل نبود.

### Confidence و کالیبراسیون

```text
score: MAX_SELECTED_CONTEXT_RERANKER_SCORE
target: COMPLETE_LINKED_REFERENCE_ANCHOR_IN_SELECTED_CONTEXT
fit: 2062 development queries
evaluation: 602 development queries
```

هدف، حضور کامل شاهد مرجع در Context است؛ نه درستی پاسخ. جداسازی براساس گروه‌های منبع مرجع و سؤال دقیق انجام شده؛ تمام منابع Context الزاماً بین دو بخش جدا نشده‌اند.

| معیار | مدل | مبنای ثابت |
|---|---:|---:|
| Brier | 0.1196850343 | 0.1317985679 |
| Log loss | 0.3985086006 | 0.4333502898 |
| AUC | 0.7162317809 | 0.5 |
| ECE، ده بازهٔ هم‌عرض | 0.0246117072 | 0.0058324821 |

Brier و Log loss بهتر و ECE بدتر شد. همهٔ معیارها بهتر نشده‌اند. عدم قطعیت معیارها برآورد نشده و آستانهٔ پذیرش از پیش تعیین نشده بود.

### محدودیت ارزیاب مدل

آزمایش‌های Mini و Qwen این مشکلات را نشان دادند:

- نسبت‌دادن متن مرجع به پاسخ؛
- پذیرش اشتباه بازیابی کامل معنا؛
- نقل‌قول غیرواقعی یا متصل به شاهد اشتباه؛
- اعتبار جزئی ناموجه برای گزارهٔ معکوس؛
- تغییر دامنه یا جهت علت و معلول.

توافق دو مدل صحت محسوب نشد. این داورها برای امتیازدهی خودکار کل جمعیت پذیرفته نشده‌اند. آزمایش‌ها را از اول تکرار نکن؛ فقط برای شکاف مشخص و نیاز ضروری، طرح محدود بده.

## ۷. فایل تحویل و Artifactهای مرجع

پیشوند مشترک همهٔ مسیرهای نسبی زیر:

```text
artifacts/phase2/answerability_safety_confidence/work/outputs/
```

### نقطهٔ ورود اصلی C455

```text
nb20c_scoped_audit_handoff_C455_v1/C455.handoff.9b08c7991964ea8cc99ba2cc9e47e9bed7104d8c3231b75fe77277ef86475ae1.json
```

SHA256:

```text
9b08c7991964ea8cc99ba2cc9e47e9bed7104d8c3231b75fe77277ef86475ae1
```

### بازاجرای مستقل C454

```text
nb20c_action31_isolated_replay_C454_v1/C454.replay.b3e38243f6a0a4956a924a7ff6307b3e7c6226e51dc4fd28c5b3e5da008bfff9.json
```

### تصمیم کار ۳۰، C453

```text
nb20c_action30_scoped_gate_C453_v1/C453.decision.1334e00b2cee6e4a07fcb47fe2d9248000d015e6b8b4bee6582db22731caf566.json
```

### اتصال ورودی‌ها، C452

```text
nb20c_action30_recovered_bindings_C452_v1/C452.bindings.8a90fe115da3cae183ac7d9497b129c5c200688f87050301e62e8f1334f1edf1.json
```

### یکپارچگی فایل‌ها، C441

```text
nb20c_action30_file_integrity_C441_v1/C441.integrity.27b82dab3a523b967ca1b47e60a2df1fae5a74de827cb9c66ef2404bc9de61c8.json
```

### نمای برچسب نهایی، C439 اصلاحی

```text
nb20c_action30_effective_audit_C439_v2/C439.audit.ebea103f238bc5b7c0cfbaaa6c99f9dd96e419a4be6d8c7c3caab0e05f6a84f7.json
```

### تعیین‌تکلیف ۳۰ پرونده، C436

```text
nb20c_action29_scoped_resolutions_C436_v1/C436.resolutions.78a8a3d774f7526d6aa9d6c3267f425630cf44b5e11653b5f1ba50e3fae6b0a8.json
```

هش هر Artifact بالا همان رشتهٔ ۶۴کاراکتری داخل نام فایل است.

### رجیستری تاریخی

```text
nb20_completed_scoped_registry_C371_v1.jsonl
```

SHA256:

```text
70d6767991eac4081fcb1fe4aad71162ed69b24f794df5d86df1e1b5ac20c269
```

### GitHub در برابر Artifactهای محلی

در درخت GitHub در کامیت `973c719...`، فایل‌های مستقل نهایی C439، C452، C453، C454 و C455 در فایل‌های tracked پیدا نشدند. نوت‌بوک حاوی کد و خروجی‌ها پوش شده است؛ وجود JSON مستقل در GitHub را فرض نکن.

- نقشه‌ها و کد نوت‌بوک را از GitHub بخوان.
- وجود و هش Artifactهای مستقل روی سیستم محلی کاربر کنترل شود.
- اگر فایل نبود، مسیر دقیق گزارش شود.
- برای جبران فایل مفقود API را دوباره اجرا نکن.
- ignoreبودن یا منتشرنشدن Artifact به معنی خرابی نیست.
- بدون بررسی سیاست انتشار داده، `git add -f` پیشنهاد نکن.


## ۷. قرارداد عملی جلوگیری از دوباره‌کاری در چت تازه

قبل از هر کار تازه، از Reader و دفتر فعلی استفاده کن و تعیین کن نتیجهٔ موجود دقیقاً برای چه وظیفه‌ای قابل مصرف است. برای کشف دوبارهٔ همان موجودی، Notebook یا Pipeline موازی نساز.

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


### خطاهای شناخته‌شده که نباید تکرار شوند

- JSONL خط‌به‌خط خوانده می‌شود؛ `json.loads` روی کل فایل، خطای Extra data می‌دهد.
- نوع هش را از قرارداد همان فایل بخوان: SHA-256 بایت فایل، هش JSON کانونی، هش متن و Git Blob SHA-1 یکسان نیستند.
- schema، مسیر فیلد و قرارداد fingerprint را پیش از نوشتن Adapter بخوان؛ placeholder حدسی نساز.
- Cell اصلاحی باید در تعریف اصلی و مصرف‌کننده‌های مرتبط اصلاح شود؛ وصلهٔ آخر Notebook که فقط از Assert رد می‌شود راه‌حل نیست.
- Hash و Manifest حلقوی نساز؛ Runtime را با execution_count نسخهٔ قدیمی روی دیسک نسنج.
- خروجی فریز‌شده، رأی اصلی و Raw response را نگه دار؛ نتیجهٔ مشتق با منشأ مستقل ثبت شود.
- Missing با صفرامتیاز، out-of-scope، ambiguity و unsupported فرق دارد؛ مخرج هر Metric مستقل است.
- Topic و Question type پذیرفته‌نشده فقط ادعای Slice وابسته را محدود می‌کنند؛ مانع همهٔ بررسی‌های پاسخ نیستند.
- دو بازبین یا آستانهٔ ۵٪ به‌عنوان قاعدهٔ مصوب وجود ندارد؛ از خودت Gate نساز.
- مجوز پردازش پروژه قبلاً تأیید شده؛ محدودیت مصنوعی INTERNAL_EVALUATION_ONLY را برنگردان. این موضوع هزینهٔ API یا commit/push را خودکار مجاز نمی‌کند.
- Test تاریخی دیده شده است؛ آن را untouched معرفی نکن و برای retuning مصرف نکن.

## ۸. فهرست دقیق Artifactها و گزارش‌های قبل از NB21

این فهرست برای یافتن مستقیم منابع است. برخی فایل‌های مستقل در ممیزی خوانده شده‌اند و برخی مسیرها از درخت تأیید شده‌اند؛ این فهرست به‌تنهایی پذیرش محتوا یا وجود تمام Cacheهای محلی را اثبات نمی‌کند. برای جزئیات قدرت شواهد، ممیزی کامل همین گفتگو مبناست.

- [artifacts/phase2/chunking/candidate_registry_evaluation_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/chunking/candidate_registry_evaluation_v1.json)
- [artifacts/phase2/chunking/chunk_contract_evaluation_freeze_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/chunking/chunk_contract_evaluation_freeze_v1.json)
- [artifacts/phase2/context_builder/context_builder_configuration_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/context_builder/context_builder_configuration_v1.json)
- [artifacts/phase2/context_builder/context_builder_release_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/context_builder/context_builder_release_v1.json)
- [artifacts/phase2/context_builder/nb19_context_builder_handoff_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/context_builder/nb19_context_builder_handoff_v1.json)
- [artifacts/phase2/dense_index/dense_index_release_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/dense_index/dense_index_release_v1.json)
- [artifacts/phase2/dense_index/nb16_dense_index_handoff_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/dense_index/nb16_dense_index_handoff_v1.json)
- [artifacts/phase2/embedding/embedding_release_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/embedding/embedding_release_v1.json)
- [artifacts/phase2/embedding/nb14_dense_index_handoff_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/embedding/nb14_dense_index_handoff_v1.json)
- [artifacts/phase2/golden_dataset_v2/golden_dataset_v2.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_dataset_v2.jsonl)
- [artifacts/phase2/golden_dataset_v2/golden_dataset_v2_final_report.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_dataset_v2_final_report.json)
- [artifacts/phase2/golden_dataset_v2/golden_dataset_v2_manifest.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_dataset_v2_manifest.json)
- [artifacts/phase2/golden_dataset_v2/golden_dataset_v2_registry_driven_contract_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_dataset_v2_registry_driven_contract_v1.json)
- [artifacts/phase2/golden_dataset_v2/golden_v2_claim_eligibility_manifest_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_v2_claim_eligibility_manifest_v1.jsonl)
- [artifacts/phase2/golden_dataset_v2/golden_v2_seed_pool_reviewed_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_v2_seed_pool_reviewed_v1.jsonl)
- [artifacts/phase2/golden_dataset_v2/golden_v2_seed_pool_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_v2_seed_pool_v1.jsonl)
- [artifacts/phase2/golden_dataset_v2/golden_v2_seed_suitability_judgments_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_v2_seed_suitability_judgments_v1.jsonl)
- [artifacts/phase2/golden_dataset_v2/golden_v2_seed_suitability_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_v2_seed_suitability_report_v1.json)
- [artifacts/phase2/golden_dataset_v2/golden_v2_semantic_seed_suitability_contract_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/golden_v2_semantic_seed_suitability_contract_v1.json)
- [artifacts/phase2/golden_dataset_v2/twelve_series_consolidated_manifest_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/golden_dataset_v2/twelve_series_consolidated_manifest_v1.json)
- [artifacts/phase2/hybrid_retrieval/hybrid_configuration_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/hybrid_retrieval/hybrid_configuration_v1.json)
- [artifacts/phase2/hybrid_retrieval/hybrid_retrieval_release_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/hybrid_retrieval/hybrid_retrieval_release_v1.json)
- [artifacts/phase2/hybrid_retrieval/nb17_hybrid_retrieval_handoff_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/hybrid_retrieval/nb17_hybrid_retrieval_handoff_v1.json)
- [artifacts/phase2/knowledge_registry/claim_dedup_exact_groups_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_dedup_exact_groups_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_dedup_exact_relations_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_dedup_exact_relations_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_dedup_relation_consolidation_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_dedup_relation_consolidation_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_dedup_relations_consolidated_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_dedup_relations_consolidated_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_dedup_stage1_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_dedup_stage1_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_embedding_text_index_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_embedding_text_index_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_exact_canonicalization_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_exact_canonicalization_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_full_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_full_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_pilot_final_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_pilot_final_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_pilot_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_pilot_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_pilot_report_v2.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_pilot_report_v2.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v2.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v2.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v3.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_pilot_semantic_report_v3.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_prompt_window_contract_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_prompt_window_contract_v1.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_text_profile_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_text_profile_v1.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_unit_contract_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_unit_contract_v1.json)
- [artifacts/phase2/knowledge_registry/claim_extraction_validation_contract_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_extraction_validation_contract_v1.json)
- [artifacts/phase2/knowledge_registry/claim_id_mapping_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_id_mapping_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_registry_contract_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_registry_contract_v1.json)
- [artifacts/phase2/knowledge_registry/claim_registry_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_registry_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_relation_projection_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_relation_projection_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_semantic_candidate_generation_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_semantic_candidate_generation_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_semantic_candidate_selection_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_semantic_candidate_selection_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_semantic_dedup_candidates_selected_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_semantic_dedup_candidates_selected_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_semantic_neighbor_candidates_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_semantic_neighbor_candidates_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_semantic_relation_full_adjudication_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_semantic_relation_full_adjudication_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_semantic_relation_full_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_semantic_relation_full_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_semantic_relation_pilot_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_semantic_relation_pilot_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_semantic_relation_pilot_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_semantic_relation_pilot_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_validation_full_disposition_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_validation_full_disposition_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_validation_full_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_validation_full_report_v1.json)
- [artifacts/phase2/knowledge_registry/claim_validation_full_semantic_adjudication_v1.jsonl](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_validation_full_semantic_adjudication_v1.jsonl)
- [artifacts/phase2/knowledge_registry/claim_validation_full_semantic_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/claim_validation_full_semantic_report_v1.json)
- [artifacts/phase2/knowledge_registry/knowledge_graph_build_report_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/knowledge_registry/knowledge_graph_build_report_v1.json)
- [artifacts/phase2/reranking/nb18_reranker_handoff_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/reranking/nb18_reranker_handoff_v1.json)
- [artifacts/phase2/reranking/reranker_configuration_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/reranking/reranker_configuration_v1.json)
- [artifacts/phase2/reranking/reranker_release_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/reranking/reranker_release_v1.json)
- [artifacts/phase2/sparse_index/nb16_sparse_index_handoff_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/sparse_index/nb16_sparse_index_handoff_v1.json)
- [artifacts/phase2/sparse_index/sparse_index_release_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/artifacts/phase2/sparse_index/sparse_index_release_v1.json)
- [data/phase2/human_review/human_review_registry.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/phase2/human_review/human_review_registry.json)
- [reports/phase2/book_ingestion_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/book_ingestion_acceptance_v1.json)
- [reports/phase2/book_inventory_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/book_inventory_acceptance_v1.json)
- [reports/phase2/competency_freeze_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/competency_freeze_v1.json)
- [reports/phase2/context_builder_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/context_builder_acceptance_v1.json)
- [reports/phase2/deduplication_quality_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/deduplication_quality_acceptance_v1.json)
- [reports/phase2/dense_index_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/dense_index_acceptance_v1.json)
- [reports/phase2/embedding_benchmark_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/embedding_benchmark_acceptance_v1.json)
- [reports/phase2/environment_baseline_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/environment_baseline_v1.json)
- [reports/phase2/golden_dataset_final_adjudicated_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/golden_dataset_final_adjudicated_acceptance_v1.json)
- [reports/phase2/hybrid_retrieval_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/hybrid_retrieval_acceptance_v1.json)
- [reports/phase2/persian_normalization_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/persian_normalization_acceptance_v1.json)
- [reports/phase2/reranker_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/reranker_acceptance_v1.json)
- [reports/phase2/sparse_index_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/sparse_index_acceptance_v1.json)
- [reports/phase2/taxonomy_freeze_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/taxonomy_freeze_v1.json)
- [reports/phase2/transcript_ingestion_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/transcript_ingestion_acceptance_v1.json)
- [reports/phase2/transcript_inventory_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/transcript_inventory_acceptance_v1.json)
- [reports/phase2/unified_schema_lineage_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/unified_schema_lineage_acceptance_v1.json)
- [reports/phase2/website_acceptance_v1.json](https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/reports/phase2/website_acceptance_v1.json)

## ۹. مرز انتقال به NB21

وضعیت جاری NB21 در پرامپت همراه این فایل و آخرین خروجی ارسالی کاربر تعیین می‌شود. این فایل مأموریتش شرح سابقهٔ قبل از NB21 است. از وجود مواد تاریخی، تیک تازه یا پذیرش رسمی امتیازها نتیجه نگیر. شمارهٔ آخرین سل را از نسخهٔ محلی بخوان؛ از C101 مخزن یا C119 گزارش‌شده، شمارهٔ بعدی را حدس نزن.

### حداقل چیزهایی که کاربر برای ادامه باید منتقل کند

۱. همین فایل؛ ۲. پرامپت NB21 همراه؛ ۳. آخرین خروجی کامل چت اجرایی، شامل شناسهٔ سل و نتیجه؛ ۴. نسخهٔ محلی NB21b اگر جلوتر از GitHub است. اگر خروجی به Artifact محلی تعیین‌کننده ارجاع دارد و محتوای آن از فایل‌ها قابل خواندن نیست، فقط همان بستهٔ لازم ارائه شود. مسیر و هش جای خواندن شاهد را نمی‌گیرند. ارسال مجدد همهٔ Rawها، تمام نوت‌بوک‌ها یا همهٔ فایل‌های پیشین پیش‌فرض نیست.

## پیوست ۱. متن مرجع داده و Authority ارائه‌شده در همین گفتگو

این متن تاریخچهٔ پس از NB10 است. حقوق/مجوز و تصمیم‌های تازه‌تر طبق قرارداد ابتدای این انتقال تفسیر شوند؛ محدودیت قدیمی لغوشده به Gate تازه تبدیل نشود.

<div dir="rtl" style="text-align: right; line-height: 1.9;">

# مرجع جامع داده‌ها، Knowledge Authority و قیود طراحی RAG Finance — Dr. Komeil Roudi

**نسخه:** پس از تکمیل Notebook 10 — Taxonomy & Knowledge Engineering  
**وضعیت:** مرجع انتقالی برای ادامه Phase 2 و طراحی Chunking / Retrieval  
**Primary Knowledge Authority:** Dr. Komeil Roudi

---

# 1. هدف این سند

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

# 2. سه مفهوم که هرگز نباید با هم یکی شوند

در تمام Pipeline باید این سه مفهوم جدا بمانند:

## 2.1. Knowledge Authority

این Evidence تا چه حد مجاز است ساختار دانش اصلی پروژه را تعریف کند.

## 2.2. Source Attribution

متن واقعاً توسط چه فرد یا Source تولید شده است.

## 2.3. Conversation Context

متنی که لزوماً Primary Knowledge نیست، اما برای فهم سؤال، پاسخ، استدلال یا ادامۀ گفتگو لازم است.

مثال:

1. سؤال مجری
2. پاسخ دکتر
3. سؤال تکمیلی شرکت‌کننده
4. توضیح تکمیلی دکتر

در چنین حالتی Context باید حفظ شود، اما سؤال مجری یا شرکت‌کننده نباید به دکتر Attribution شود.

---

# 3. Corpus پذیرفته‌شده Phase 2

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

# 4. مدل رسمی Knowledge Authority پس از NB10

پس از Reconciliation نهایی، کل Corpus در چهار لایۀ رسمی قرار می‌گیرد.

## Tier 1 — CORE_PRIMARY_KNOWLEDGE

**14,705 Document**

اجزاء:

- Book: **2,701**
- Website Direct Author: **76**
- Transcript Primary: **11,928**

این لایه تنها لایه‌ای است که می‌تواند ساختار اصلی Topic / Subtopic / Curriculum / Competency را تعریف یا تغییر دهد.

## Tier 2 — SUPERVISED_SECONDARY_KNOWLEDGE

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

## Tier 3 — CONTEXTUAL_NONPRIMARY

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

## Tier 4 — UNRESOLVED_CONTEXT

**2,354 Document**

Speaker یا Attribution این Segmentها با Evidence فعلی به‌طور قابل اتکا حل نشده است.

سیاست:

- حذف نشوند.
- به دکتر نسبت داده نشوند.
- برای Context و Review حفظ شوند.
- تا وجود Evidence جدید در ساختار Primary Knowledge اثر تعیین‌کننده نداشته باشند.

---

# 5. Website Data

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

# 6. Book Data

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

# 7. Transcript Data

کل Transcript:

**16,226 Segment**

## 7.1. Authority profile رسمی Transcript

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

# 8. سیاست Speaker در Transcript

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

# 9. Program-specific Context

بعضی Programها Solo نیستند و Chunking آن‌ها باید Conversation-aware باشد.

## `program:khane-to`

Human-confirmed structure:

- Dr. Komeil Roudi
- one host

7 Segment دارای labelهای غیرمنتظره در Review Queue باقی مانده‌اند.

این 7 مورد:

- حذف نشده‌اند،
- Hard Quarantine نشده‌اند،
- برای Review حفظ شده‌اند.

## `program:asre-shirin`

Human-confirmed structure:

- دو Season
- Dr. Komeil Roudi
- یک مجری زن
- حدود 8 شرکت‌کنندۀ زن

Open metadata gap:

- `season_number` برای **902 Segment** موجود نیست.

این یک Metadata Gap است، نه Structural Failure.

## `program:chehelston`

شامل Contextهایی با Guestهای دیگر است.

بنابراین:

- تمام Content آن Primary Dr. Roudi نیست.
- Speaker-aware / context-aware chunking ضروری است.
- Unlabeled / unresolved paragraphs نباید به‌صورت حدسی Primary شوند.

## `program:uni-tehran`

دارای گفتگوها و Contextهای چندنفره است.

در NB10 دیده شد بعضی Conceptها مانند Taxation در Conversation alternation ظاهر می‌شوند:

- Segment مستقیم دکتر
- Segment سؤال / توضیح دیگران
- Segment unresolved

بنابراین chunking صرفاً بر اساس window ثابت بدون Speaker/Conversation boundary می‌تواند Attribution را خراب کند.

---

# 10. Deduplication Policy

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

# 11. Rights / Release Gate

در وضعیت فعلی:

- Internal Processing Allowed: **19,456**
- Formal Release Eligible: **0**
- Rights state: `EVIDENCE_REQUIRED`
- Release status: `BLOCKED_PENDING_RIGHTS`

اصل:

> `EVIDENCE_REQUIRED` یک Release Gate است، نه Data Quality Failure.

بنابراین Chunking داخلی Phase 2 مجاز است، ولی Export / Publication / Formal Release باید Rights-aware باقی بماند.

---

# 12. Frozen Taxonomy v1

Artifact:

`artifacts/phase2/taxonomy/taxonomy_v1.json`

SHA256:

`335690044b2e4eff684f7f347809f2c5cb8c39624a939dc01408d9ca898fe977`

Status:

`FROZEN`

## 12.1. هفت Top-level Topic

1. `financial_literacy_foundations`
2. `spending_saving_money_management`
3. `credit_debt_banking`
4. `work_income`
5. `investment`
6. `risk_insurance`
7. `financial_decision_making`

---

# 13. Curriculum Nodes فریز‌شده

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

# 14. Taxation

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

# 15. Context-dependent Terms

مفاهیمی مانند:

- انتخاب
- قیمت
- سود

در سطح Global به یک Topic واحد Alias نشده‌اند.

قیمت و سود فقط در Context مشخص `children_business` نقش Structural Local Subtopic دارند.

نتیجه برای Chunking:

> وجود term به تنهایی برای تعیین Topic Chunk کافی نیست؛ local structural context و source hierarchy مهم است.

---

# 16. Behavioral Economics

Evidence اصلی برای `behavioral_economics` در Core Primary Corpus برای Promotion به Core Taxonomy v1 کافی نبود.

وضعیت:

`NOT_PROMOTED_TO_CORE_TAXONOMY_V1`

بنابراین Secondary / Guest dispersion نباید در Chunking یا retrieval labeling باعث شود این مفهوم به شکل implicit به یک Core Topic تبدیل شود.

---

# 17. Frozen Competency / Prerequisite v1

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

# 18. Learning Stages

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

# 19. Knowledge Gap Policy

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

# 20. چرا Transcript Mapping پایین به معنی Gap نیست

در NB10 Top-level observability در Core Primary Corpus حدود 36.7% بود، اما این عدد به تنهایی Quality Failure نیست.

به‌ویژه در Transcript:

- Segmentها ممکن است کوتاه باشند.
- معنی آن‌ها به turnهای قبل و بعد وابسته باشد.
- pronoun / ellipsis داشته باشند.
- Topic term در همان Segment ظاهر نشود.
- Speaker context در Segment مجاور باشد.

بنابراین Chunking حرفه‌ای می‌تواند بخش مهمی از مسئلۀ Retrievability را حل کند بدون اینکه Taxonomy تغییر کند.

---

# 21. Local Conversation Context Discovery

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

# 22. الزامات Chunking برای Book

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

# 23. الزامات Chunking برای Website

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

# 24. الزامات Chunking برای Transcript

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

# 25. Chunking نباید Taxonomy را بازنویسی کند

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

# 26. Chunk Lineage Contract پیشنهادی

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

# 27. Chunk ID

Chunk ID باید:

- deterministic باشد؛
- stable parent relation داشته باشد؛
- با تغییر chunking version قابل تشخیص باشد؛
- collision نداشته باشد؛
- از index position موقت وابسته نباشد.

Naming نهایی باید بعد از Discovery conventions Repository تعیین شود و نباید از قبل تحمیل شود.

---

# 28. Chunk Size نباید از قبل فرض شود

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

# 29. معیارهای ارزیابی Chunking

حداقل دسته‌های Metric پیشنهادی:

## Structural

- chunk count
- token distribution
- very-short chunk rate
- overlong chunk rate
- boundary break rate
- empty chunk rate
- duplicate chunk rate
- parent lineage validity

## Authority / Attribution

- speaker contamination rate
- multi-speaker ambiguity rate
- primary/nonprimary mixing profile
- unresolved-speaker handling

## Retrieval

در صورت ساخت Evaluation Set:

- Recall@k
- MRR
- nDCG
- hit rate

## Context quality

- answer evidence completeness
- unnecessary context rate
- question-answer continuity
- topic coherence

## Citation

- citation correctness
- locator validity
- citation coverage

فقط Metricهای واقعاً محاسبه‌شده باید گزارش شوند.

---

# 30. Golden / Evaluation Dataset برای Chunking

برای انتخاب Strategy باید Sampleهای نماینده از هر Source Type وجود داشته باشد.

ضروری است نمونه‌ها شامل موارد سخت باشند:

### Book
- short heading
- long section
- exercise
- multi-topic page
- deep hierarchy
- children_business branch
- giving/gifting

### Website
- direct author
- supervised
- short article
- long article
- multi-topic strong evidence
- boilerplate-heavy case

### Transcript
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

# 31. Final retrieval behavior مطلوب

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

# 32. Open Gates که NB11 نباید فراموش کند

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

# 33. Source of Truth برای شروع NB11

## Accepted corpus

`data/phase2/processed/documents_dedup_quality_accepted_v1.jsonl`

SHA256:

`9d72c709f81b1218c5aac064052c7ed1da34869f671e6e32762864e0ad70ea40`

## NB09 acceptance

`reports/phase2/deduplication_quality_acceptance_v1.json`

SHA256:

`14dfa748988db17a19c6d9d5e1eac2eb7d23c0a1699dcc7add18a2bf461fe4f3`

## Frozen taxonomy

`artifacts/phase2/taxonomy/taxonomy_v1.json`

SHA256:

`335690044b2e4eff684f7f347809f2c5cb8c39624a939dc01408d9ca898fe977`

## Taxonomy freeze report

`reports/phase2/taxonomy_freeze_v1.json`

SHA256:

`fe182b0c7c6d5ad7d5dfc2aa794fa096e85001b517040a8396d5fb4c0b17e530`

## Frozen competency

`artifacts/phase2/competency/competency_prerequisite_v1.json`

SHA256:

`f12f6c1631d77f29042b2009ca9dc8dee406d23ccdccdbb103c0e8cade781e87`

## Competency freeze report

`reports/phase2/competency_freeze_v1.json`

SHA256:

`19bb27288f49e057859da3bc668f54fac440a89a2636ff5d2e49033665f0dd11`

---

# 34. قواعد انتقال به چت بعدی

چت بعدی نباید NB09 یا NB10 را از صفر بازسازی کند.

Workflow:

`DISCOVER → INSPECT → VALIDATE → DESIGN CHUNKING BENCHMARK → BUILD CANDIDATES → EVALUATE → DECIDE → FREEZE`

نه:

`guess chunk size → chunk everything → embed`

---

# 35. خلاصۀ یک‌خطی

**RAG Finance یک RAG تخصصی با محوریت دانش دکتر کمیل رودی است؛ Core Primary Knowledge ساختار اصلی دانش را تعیین می‌کند، Secondary Knowledge فقط Supporting است، Conversation Context باید بدون Attribution collapse حفظ شود، Taxonomy و Competency v1 اکنون Frozen هستند، و NB11 باید با Benchmark واقعی و Source-specific strategy بهترین Chunking را برای Book، Website و Transcript انتخاب کند.**

</div>


## پیوست ۲. دستورالعمل اجرایی ارائه‌شده در همین گفتگو

# دستورالعمل اجرایی سریع، دقیق و بدون دوباره‌کاری برای Phase 2 پروژه RAG_finance

## هدف این سند

این سند باید در ابتدای هر Chat و پیش از شروع یا ادامه‌ی هر Notebook از
Phase 2 پروژه `RAG_finance` به‌عنوان دستورالعمل اجرایی خوانده و رعایت
شود.

هدف، **افزایش سرعت مهندسی بدون کاهش کیفیت** است. سرعت نباید با حذف
Validation، کوچک‌کردن غیرموجه Benchmark، شل‌کردن Gateها، نادیده‌گرفتن خطاها
یا دور زدن نقشه‌ی اصلی پروژه به دست آید. سرعت باید از طراحی بهتر، حذف
دوباره‌کاری، استفاده صحیح از Cache و Artifact، محدودکردن Scope و کشف
زودهنگام خطاها حاصل شود.

------------------------------------------------------------------------

# 1. اصل حاکم: وفاداری کامل به نقشه‌ی اصلی

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

# 2. کیفیت غیرقابل مذاکره است

برای افزایش سرعت، موارد زیر نباید حذف یا تضعیف شوند:

-   Golden Dataset و داده‌های مرجع معتبر
-   Validationهای ساختاری و معنایی موردنیاز
-   Metricهای رسمی Roadmap
-   Evidence و Source Lineage
-   Reproducibility
-   Regression Gates
-   Artifact Integrity
-   Hash / Manifest / Versioning در جاهایی که Roadmap یا معماری پروژه
    نیاز دارد
-   Failure Analysis لازم
-   Final Health Check
-   Restart Kernel → Run All نهایی در Notebookهایی که باید مستقل و قابل
    بازتولید باشند

اگر بین «سریع‌تر تمام شدن» و «اعتبار علمی/مهندسی نتیجه» تعارض ایجاد شود،
اعتبار نتیجه اولویت دارد.

------------------------------------------------------------------------

# 3. قبل از نوشتن اولین Cell، Execution Blueprint ساخته شود

پیش از شروع اجرای هر Notebook، ابتدا یک Blueprint کوتاه اما کامل تهیه
شود.

Blueprint باید مشخص کند:

-   مأموریت رسمی Notebook چیست؟
-   چه چیزهایی خارج از Scope هستند؟
-   ورودی‌های Canonical کدام‌اند؟
-   Artifactهای موردنیاز از مراحل قبل کدام‌اند؟
-   خروجی‌های این Notebook دقیقاً چه خواهند بود؟
-   چه Metricهایی باید محاسبه شوند؟
-   PASS/FAIL بر چه اساسی تعیین می‌شود؟
-   چه API یا مدل‌هایی ممکن است استفاده شوند؟
-   Cache و Checkpoint چگونه مدیریت می‌شوند؟
-   Failureهای محتمل کدام‌اند؟
-   Final Health Check چه چیزهایی را کنترل خواهد کرد؟
-   Notebook بعدی دقیقاً چه چیزی از این Notebook تحویل می‌گیرد؟

تا زمانی که این Contract روشن نشده، Full Execution شروع نشود.

------------------------------------------------------------------------

# 4. Contract ورودی و خروجی از ابتدا ثابت شود

هر Notebook باید Input Contract و Output Contract مشخص داشته باشد.

Notebook نباید به‌طور پنهانی به متغیری وابسته باشد که فقط در Kernel قبلی
وجود داشته است.

ارتباط Notebookها باید تا حد ممکن از طریق Artifactهای Versioned و قابل
Validation انجام شود، نه State موقت حافظه.

مثلاً:

`NB14 → Artifact مشخص → NB15/NB16`

بهتر از این است که Notebook بعدی فقط در صورتی کار کند که Notebook قبلی
چند دقیقه قبل در همان Kernel اجرا شده باشد.

------------------------------------------------------------------------

# 5. Artifact-first، نه Memory-first

هر نتیجه‌ای که برای مراحل بعدی مهم است باید به شکل Artifact مشخص، قابل
ردیابی و در صورت نیاز Versioned ذخیره شود.

Artifact مهم باید در صورت لزوم دارای اطلاعاتی مانند این‌ها باشد:

-   Version
-   Dataset fingerprint/hash
-   Model/config
-   Timestamp در صورت نیاز
-   Record count
-   Relevant metrics
-   Source/Lineage
-   Status
-   Manifest یا metadata لازم

Notebook بعدی باید بتواند Artifact را مستقل Load و Validate کند.

------------------------------------------------------------------------

# 6. API و عملیات گران: Checkpoint-first

هیچ عملیات گران، طولانی یا پولی نباید بدون طراحی Cache/Checkpoint اجرا
شود.

قبل از API Call:

1.  Fingerprint دقیق Input تعیین شود.
2.  Cache معتبر جست‌وجو شود.
3.  نتیجه‌ی موجود Validate شود.
4.  فقط Missing Itemها اجرا شوند.
5.  هر Batch موفق فوراً Checkpoint شود.
6.  Retry محدود و کنترل‌شده وجود داشته باشد.
7.  اجرای مجدد Notebook نباید عملیات موفق قبلی را تکرار کند.

**قاعده‌ی اصلی:**\
پرداخت یا محاسبه‌ی دوباره برای چیزی که نتیجه‌ی معتبر آن از قبل موجود است،
خطای مهندسی محسوب می‌شود مگر اینکه Recompute عمداً بخشی از آزمایش باشد.

------------------------------------------------------------------------

# 7. Full Run نهایی باید تا حد ممکن API-safe باشد

پیش از Final Restart Kernel → Run All، Cellهای پولی یا عملیات خارجی
پرریسک باید طوری طراحی شده باشند که از Checkpointهای معتبر بازسازی شوند.

اجرای نهایی نباید ناخواسته:

-   هزاران Embedding را دوباره بسازد،
-   Reranking را دوباره پولی اجرا کند،
-   LLM Callهای قبلی را تکرار کند،
-   Artifact فریز‌شده را overwrite کند.

در Final Run، هدف اثبات **Reproducibility از Artifact و Cache معتبر**
است، نه پرداخت دوباره برای همان محاسبات.

------------------------------------------------------------------------

# 8. Pilot → Validate → Full Run

هر عملیات بزرگ ابتدا روی Pilot کوچک اجرا شود.

ترتیب استاندارد:

`Smoke Test → Small Pilot → Validation → Full Execution`

Pilot باید به‌اندازه‌ای باشد که خطاهای Schema، API، Batch، Dimension،
Mapping، Cache و Logic را آشکار کند.

اما Pilot جای Full Benchmark را نمی‌گیرد.

بعد از سالم بودن Pipeline، Full Evaluation موردنیاز Roadmap باید انجام
شود.

این روش کیفیت را کم نمی‌کند؛ فقط مانع می‌شود یک باگ ساده بعد از چند ساعت
Compute یا صدها API Call کشف شود.

------------------------------------------------------------------------

# 9. Full Dataset فقط وقتی لازم است اجرا شود

Full Dataset برای نتیجه‌ی نهایی و Benchmark رسمی استفاده می‌شود؛ اما Debug
کردن نباید دائماً روی کل Dataset انجام شود.

برای Debug:

-   نمونه‌ی کوچک و نماینده استفاده شود.
-   Bug اصلاح شود.
-   تست کوچک PASS شود.
-   سپس Full Run انجام شود.

هر بار اجرای Full Dataset برای کشف Syntax Error، Schema Error یا Mapping
Error یک Anti-pattern است.

------------------------------------------------------------------------

# 10. Scope Creep ممنوع

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

# 11. Research Path و Production Path جدا بمانند

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

# 12. Definition of Done قبل از اجرا نوشته شود

برای هر Notebook قبل از Full Execution باید مشخص باشد چه زمانی می‌گوییم:

**این Notebook تمام شده است.**

Definition of Done باید مبتنی بر Roadmap و Artifact واقعی باشد، نه احساس
اینکه «به نظر می‌رسد کافی است».

وقتی تمام Gateهای تعریف‌شده PASS شدند:

1.  Final Health Check
2.  Restart Kernel → Run All در صورت نیاز
3.  ثبت Summary
4.  Freeze
5.  حرکت به Notebook بعدی

بعد از Freeze، آزمایش‌های خارج از Scope نباید دوباره Notebook را باز کنند
مگر دلیل مشخص مهندسی وجود داشته باشد.

------------------------------------------------------------------------

# 13. Failure باید در همان مرحله Repair شود

اگر یک Cell FAIL شد، نباید از آن عبور کرد و Notebook را ادامه داد.

قاعده:

`FAIL → Diagnose → Repair همان مرحله → Re-run → PASS → Next Step`

هیچ PASS فرضی پذیرفته نیست.

PASS فقط وقتی ثبت می‌شود که Output واقعی آن را تأیید کند.

------------------------------------------------------------------------

# 14. روش اصلاح Cellها

برای جلوگیری از سردرگمی و خطای Copy/Paste:

اگر فقط یک خط تغییر می‌کند، دقیقاً اعلام شود:

-   خط فعلی چیست؟
-   با چه خطی جایگزین شود؟

اگر بیش از یک خط یا Logic/Structure تغییر می‌کند:

-   کل Code Cell اصلاح‌شده از ابتدا تا انتها ارائه شود.

در Repair مشخص شود که Markdown قبلی بدون تغییر باقی می‌ماند یا نیاز به
اصلاح دارد.

------------------------------------------------------------------------

# 15. اجرای Notebook مرحله‌به‌مرحله باشد

در توسعه و Debug، Cellها مرحله‌به‌مرحله اجرا شوند و Output واقعی بررسی
شود.

چرخه‌ی استاندارد:

`Markdown → Code → Actual Output → Analysis → Next Step`

نباید چندین مرحله‌ی وابسته بر اساس Output فرضی جلو نوشته شوند.

این کار باعث می‌شود خطا در نزدیک‌ترین نقطه به علت اصلی شناسایی شود.

------------------------------------------------------------------------

# 16. Final Health Check از ابتدای طراحی وجود داشته باشد

Final Health Check نباید در پایان پروژه به Notebook اضافه شود؛ معیارهای
آن باید از ابتدا مشخص باشند.

بسته به Notebook، Health Check باید موارد مرتبطی مانند این‌ها را بررسی
کند:

-   همه Code Cellهای موردنیاز اجرا شده‌اند.
-   Saved Error وجود ندارد.
-   Cell Numbering صحیح و Sequential است.
-   Duplicate Code Cell Number وجود ندارد.
-   Duplicate/Unnecessary Imports کنترل شده‌اند.
-   Artifactهای لازم وجود دارند.
-   Record Countها صحیح‌اند.
-   Hash/Fingerprintها صحیح‌اند.
-   Config و Model Version مشخص‌اند.
-   API execution state مطابق Policy است.
-   Frozen Artifact overwrite نشده است.
-   خروجی‌های لازم برای Notebook بعدی وجود دارند.
-   Final Status با Output واقعی سازگار است.

------------------------------------------------------------------------

# 17. Restart Kernel → Run All آزمون استقلال Notebook است

در پایان Notebookهایی که باید مستقل و قابل بازتولید باشند، Restart
Kernel → Run All انجام شود.

این تست مشخص می‌کند آیا Notebook واقعاً مستقل است یا به State پنهان Kernel
قبلی وابسته بوده است.

اگر Run All شکست خورد، Notebook هنوز Freeze نمی‌شود.

خطا باید Repair و Run All دوباره تأیید شود.

------------------------------------------------------------------------

# 18. داده و Artifact فریز‌شده دست‌نخورده بماند

Golden Dataset، Registry، Index Snapshot یا هر Artifact فریز‌شده نباید
صرفاً برای راحتی اجرای Notebook بعدی تغییر داده شود.

اگر Notebook جدید با Artifact Canonical سازگار نیست، Notebook جدید باید
اصلاح شود؛ نه اینکه حقیقت مرجع پروژه برای سازگار شدن با کد جدید دستکاری
شود.

------------------------------------------------------------------------

# 19. Historical Notebookها و مسیر Canonical مخلوط نشوند

Notebookهای قدیمی برای Provenance و تاریخچه مفیدند، اما نباید باعث ابهام
شوند که مسیر اصلی پروژه کدام است.

در هر خانواده:

-   یک مسیر Canonical مشخص باشد.
-   نسخه‌های Superseded/Experimental در Archive بمانند.
-   Artifact نهایی مستقل از سردرگمی تاریخی قابل شناسایی باشد.

Archive به معنی حذف تاریخچه نیست؛ به معنی جداکردن تاریخچه از مسیر اجرایی
اصلی است.

------------------------------------------------------------------------

# 20. Benchmark باید روی داده‌ی واقعی پروژه باشد

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

# 21. Metric بدون تفسیر کافی نیست

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

# 22. کیفیت، هزینه و سرعت با هم دیده شوند

مدلی که کمی بهتر است اما هزینه یا Latency غیرقابل قبول دارد لزوماً انتخاب
Production نیست.

در مراحل مرتبط باید Trade-off میان این موارد ثبت شود:

-   Quality
-   Recall / Ranking quality
-   Latency
-   Cost
-   Failure rate
-   Operational complexity
-   Reproducibility

اما هیچ‌کدام نباید بدون معیار رسمی Roadmap به‌تنهایی جایگزین کیفیت شوند.

------------------------------------------------------------------------

# 23. دوباره‌کاری باید به‌عنوان Bug فرایندی دیده شود

اگر کاری چند بار تکرار شد، فقط آن را دوباره انجام ندهید؛ علت تکرار را
پیدا کنید.

نمونه‌ها:

-   API دوباره اجرا شد → Cache Policy مشکل دارد.
-   Run All شکست خورد → Hidden State وجود دارد.
-   Artifact دوباره ساخته شد → Version/Manifest مبهم است.
-   Scope چند بار عوض شد → Contract قبل از اجرا بسته نشده است.
-   Notebook بیش از حد بزرگ شد → Scope Creep رخ داده است.
-   Full Dataset چند بار برای Debug اجرا شد → Pilot Strategy ضعیف بوده
    است.

هدف این است که هر خطای پرهزینه فقط یک بار رخ دهد و بعد تبدیل به
Guardrail شود.

------------------------------------------------------------------------

# 24. هر Notebook باید Handoff واضح داشته باشد

در پایان Notebook دقیقاً ثبت شود:

-   چه چیزی ساخته شد؟
-   چه چیزی انتخاب شد؟
-   چه چیزی رد شد؟
-   Artifact Canonical کجاست؟
-   Hash/Version چیست؟
-   چه محدودیت یا Failure شناخته‌شده‌ای باقی مانده؟
-   Notebook بعدی باید چه چیزی را Load کند؟
-   آیا Notebook فعلی Frozen است؟

Notebook بعدی نباید برای فهمیدن این اطلاعات مجبور شود کل Notebook قبلی
را از ابتدا تحلیل کند.

------------------------------------------------------------------------

# 25. Summary نهایی کوتاه اما قطعی باشد

Summary نهایی باید بین سه چیز تفاوت بگذارد:

### Fact

چیزی که Output واقعی اثبات کرده است.

### Interpretation

برداشت مهندسی مبتنی بر Fact.

### Pending

چیزی که هنوز آزمایش یا تأیید نشده است.

نباید نتیجه‌ای که هنوز اجرا نشده به‌صورت Fact نوشته شود.

------------------------------------------------------------------------

# 26. ترتیب رسمی ادامه Phase 2 حفظ شود

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

# 27. پروتکل پیشنهادی اجرای هر Notebook

برای هر Notebook از این چرخه استفاده شود:

### مرحله A --- Scope Lock

Roadmap خوانده شود و مأموریت Notebook قفل شود.

### مرحله B --- Input Audit

Artifactهای ورودی و وضعیت آن‌ها بررسی شوند.

### مرحله C --- Execution Blueprint

مراحل، Metricها، API Policy، Cache و Definition of Done نوشته شوند.

### مرحله D --- Bootstrap / Preflight

محیط، مسیرها، Configها و Input Contract Validate شوند.

### مرحله E --- Smoke Test

کوچک‌ترین اجرای مفید برای کشف خطاهای بنیادی انجام شود.

### مرحله F --- Pilot

نمونه‌ی نماینده اجرا و Metric/Artifact Pipeline تأیید شود.

### مرحله G --- Full Execution

فقط پس از PASS مراحل قبل، Benchmark یا Build کامل انجام شود.

### مرحله H --- Failure Analysis

خطاهای واقعی دسته‌بندی و در صورت قرار داشتن در Scope اصلاح شوند.

### مرحله I --- Artifact Freeze

خروجی Canonical، Version، Hash، Manifest و Summary ثبت شوند.

### مرحله J --- Final Health

Notebook از نظر اجرا، Artifact، State، Cellها و API Safety بررسی شود.

### مرحله K --- Restart Kernel → Run All

در صورت الزام Reproducibility، اجرای پاک انجام شود.

### مرحله L --- Handoff

ورودی موردنیاز Notebook بعدی صریحاً ثبت شود.

------------------------------------------------------------------------

# 28. چیزهایی که برای افزایش سرعت مجاز هستند

این موارد سرعت را بالا می‌برند بدون اینکه کیفیت کم شود:

-   استفاده از Smoke Test
-   Pilot کوچک قبل از Full Run
-   Cache و Checkpoint
-   اجرای فقط Missing Itemها
-   Batch Processing صحیح
-   Parallelization امن در صورت مناسب بودن
-   Artifact reuse
-   Preflight قوی
-   Schema validation زودهنگام
-   Centralized config
-   Automated Final Health Check
-   ثبت Failureها به‌صورت Guardrail
-   Freeze کردن Scope
-   Archive کردن مسیرهای Superseded
-   جلوگیری از اجرای API در Final Run
-   ساخت Blueprint قبل از Coding

------------------------------------------------------------------------

# 29. چیزهایی که برای افزایش سرعت ممنوع هستند

این موارد «بهینه‌سازی» محسوب نمی‌شوند و نباید برای سریع‌تر شدن انجام شوند:

-   حذف Metric رسمی
-   حذف Full Benchmark لازم
-   کوچک کردن Golden Dataset نهایی بدون دلیل علمی
-   نادیده گرفتن Failure
-   اعلام PASS بدون Output واقعی
-   استفاده از Cache بدون Fingerprint/Validation
-   حذف Evidence یا Lineage
-   رد شدن از Regression Gate
-   تغییر Artifact فریز‌شده برای سازگار کردن کد
-   استفاده از نتیجه تاریخی به‌عنوان نتیجه Dataset جدید
-   اجرای مرحله بعد قبل از معتبر شدن Handoff مرحله قبل
-   حذف Final Health Check
-   حذف Run-All در جایی که Reproducibility الزام است
-   قاطی کردن Scope چند Notebook برای «زودتر تمام شدن»

------------------------------------------------------------------------

# 30. دستور کوتاه برای Assistant در ابتدای هر Chat

در شروع هر Notebook یا Chat جدید، این اصول اجرا شوند:

> نقشه رسمی Phase 2 مرجع Scope و ترتیب کار است. کیفیت، Validation،
> Golden Dataset، Evidence، Lineage، Metricها و Regression Gateها نباید
> برای افزایش سرعت حذف یا تضعیف شوند. قبل از Coding، Scope و Execution
> Blueprint را مشخص کن. از Artifact-first، Cache-first، Checkpoint-first
> و Pilot-before-Full-Run استفاده کن. هر Notebook فقط مسئول مأموریت رسمی
> خودش است و Scope Creep ممنوع است. عملیات پولی یا سنگین باید resumable
> و fingerprint-bound باشند و Final Run تا حد ممکن
> API-disabled/cache-only باشد. PASS فقط با Output واقعی ثبت شود.
> Failure در همان مرحله Repair شود. خروجی هر Notebook باید Handoff روشن،
> Artifact قابل ردیابی و Final Health Check داشته باشد. سرعت باید از
> مهندسی بهتر و حذف دوباره‌کاری حاصل شود، نه از کاهش کیفیت.

------------------------------------------------------------------------

# اصل نهایی

**هدف این پروژه «زود تمام کردن Notebookها» نیست؛ هدف ساختن یک RAG قابل
اعتماد، قابل اندازه‌گیری، قابل بازتولید و قابل انتشار است.**

اما کیفیت بالا به معنی دوباره‌کاری، اجرای چندباره‌ی API، Debug روی Full
Dataset، Scope مبهم یا Notebookهای وابسته به State پنهان نیست.

روش مطلوب این است:

**یک بار طراحی درست → یک بار اجرای کنترل‌شده → اندازه‌گیری واقعی → Repair
هدفمند → Freeze → Handoff → مرحله بعد.**

به این ترتیب سرعت بیشتر می‌شود، در حالی که استاندارد علمی و مهندسی پروژه
حفظ می‌شود.


## پیوست ۳. Guardrails ارائه‌شده در همین گفتگو

توضیح: قاعدهٔ عمومی «بدون اجازه API اجرا نشود» به معنی درخواست دوبارهٔ اجازه برای بسته‌ای که قبلاً صریحاً مجاز شده نیست. مجوز جاری کاربر در دامنهٔ خودش حفظ می‌شود. شرط Run All، شرط تحویل نهایی است، نه دستور اجرای مجدد همهٔ سل‌های پولی در هر گام میانی. تعارض «توابع داخل Notebook» با «ماژول پایدار» براساس ساختار واقعی موجود حل شود؛ استقلال از Kernel قبلی لازم است، بازنویسی کد پایدار لازم نیست.

# دستورالعمل ثابت اجرای نوت‌بوک‌های Phase 2 پروژه RAG Finance

این دستورالعمل در تمام مراحل بعدی پروژه لازم‌الاجراست. هدف آن جلوگیری از دوباره‌کاری، تغییر ناخواسته قراردادهای فریز‌شده، استفاده اشتباه از Test و ساخت Notebook ناقص است.

## ۱. محدوده اطلاعات

فقط از منابع زیر استفاده کن:

- فایل‌ها و Artifactهای همین پروژه؛
- نقشه‌های موجود در Repository؛
- Notebookهای قبلی همین پروژه؛
- خروجی‌ها و قراردادهای فریز‌شده؛
- اطلاعات همین گفت‌وگو.

از حافظه پروژه‌های دیگر، الگوهای فرضی یا حدس استفاده نکن. اگر چیزی در فایل‌های پروژه مشخص نیست، مقدار مصنوعی نساز و بنویس:

```text
NOT_SPECIFIED_IN_PROJECT_ARTIFACTS
```

## ۲. مطالعه پیش از تغییر

قبل از تولید یا اصلاح کد:

1. Notebook فعلی را کامل بررسی کن.
2. Notebook قبلی و Handoff آن را بخوان.
3. Master roadmap، Operational roadmap و Modular execution plan را بخوان.
4. Artifactها، Schema، Version، Hash و Status ورودی‌ها را کنترل کن.
5. وضعیت Git و فایل‌های موجود را فقط Read-only بررسی کن.
6. مشخص کن چه چیزهایی قبلاً انجام شده‌اند.
7. کارهای صحیح قبلی را تکرار یا بازنویسی نکن.
8. ابتدا Gap analysis و سپس یک Plan کوتاه ارائه کن.

صرفاً براساس نام فایل یا توضیح کاربر نتیجه نگیر؛ محتوای واقعی فایل‌ها را بررسی کن.

## ۳. حفظ قرارداد مراحل قبلی

Artifact فریز‌شده مرحله قبل تغییرناپذیر است. موارد زیر ممنوع‌اند:

- تغییر Configuration فریز‌شده؛
- محاسبه مجدد Scoreهای قبلی بدون الزام نقشه؛
- تغییر Rank یا ترتیب فریز‌شده؛
- تغییر Candidate depth، Split یا Gold mapping؛
- دست‌کاری Hash برای عبور از Assert؛
- بازسازی Artifact قبلی با منطق جدید؛
- حذف یا ضعیف‌کردن Gate صرفاً برای PASS شدن.

Notebook جدید باید Artifact قبلی را مصرف کند، نه اینکه آن را بازتولید کند.

## ۴. استقلال Notebook

هر Notebook باید:

- از Kernel پاک اجرا شود؛
- به متغیرهای Notebook قبلی وابسته نباشد؛
- ورودی‌ها را از Artifactهای ذخیره‌شده بخواند؛
- مسیرها را نسبت به Project root پیدا کند؛
- مسیر محلی شخصی را Hard-code نکند؛
- تمام توابع موردنیاز را داخل خودش تعریف کند؛
- با `Restart Kernel & Run All` از ابتدا تا انتها اجرا شود.

## ۵. ترتیب صحیح کار

در هر Notebook این ترتیب رعایت شود:

1. Imports و Bootstrap
2. Project-root discovery
3. Read-only preflight
4. کنترل فایل‌ها و SHA-256
5. کنترل Schema و Version
6. بارگذاری ورودی‌ها
7. بازسازی قراردادهای لازم
8. Development-only analysis
9. انتخاب Configuration
10. ساخت ADR
11. Freeze Configuration
12. استفاده از Test فقط پس از Freeze و در محدوده مجاز نقشه
13. ساخت خروجی نهایی
14. نوشتن Atomic
15. Reload Validation مستقل
16. Manifest، Release و Handoff
17. Acceptance و Checkpoint
18. Final Health Gate

پیش از Freeze از Test برای انتخاب یا تغییر Configuration استفاده نکن.

## ۶. سیاست Development و Test

Development برای انتخاب Policy، Threshold، Budget، مدل، روش و Ablation استفاده می‌شود. Test فقط پس از Freeze قابل استفاده است.

بعد از مشاهده Test، Configuration، Threshold، Prompt و Budget نباید تغییر کنند. هر Artifact نهایی باید ثبت کند:

```text
configuration_changed_after_test = false
test_queries_accessed_for_retuning = false
```

اگر نقشه به Independent Test evaluation نیاز ندارد، Test metric مصنوعی ایجاد نکن و فقط Policy فریز‌شده را در محدوده لازم اعمال کن.

## ۷. کدنویسی Notebook

تمام Code Cellها باید شماره پیوسته و عنوان دقیق و یکتا داشته باشند:

```text
# NB19-C01 — Imports and runtime bootstrap
# NB19-C02 — Frozen-input preflight
```

Markdownها باید فارسی، RTL، روشن و توضیح‌دهنده هدف سل بعدی باشند. سل خالی، سل آزمایشی رهاشده، کد موقت و Import پراکنده باقی نگذار.

## ۸. مدیریت Health Check

فقط یک Final Health Gate وجود داشته باشد. Health Checkهای میانی با نام‌هایی مانند زیر مشخص شوند:

```text
INTERIM_HEALTH
PREFLIGHT
READINESS_CHECK
```

هیچ Health Check میانی نباید عنوان `FINAL` داشته باشد. Final Health هنگام `Run All` نباید برای بررسی execution count نسخه ذخیره‌شده خود Notebook را از دیسک بخواند؛ چون ممکن است Snapshot قبلی را ببیند.

Final Health باید براساس Runtime جاری، Artifactهای Reload‌شده، Hashها، Record countها، Schema، Configuration freeze و Handoff status کار کند.

خروجی‌های قدیمی و متناقض زیر نباید در نسخه نهایی باقی بمانند:

```text
OBJECTIVE_INCOMPLETE
PROPOSAL_NOT_FROZEN
PENDING_RELOAD
STRUCTURAL_HEALTH_FAIL
files_written = 0
```

مگر اینکه واقعاً وضعیت نهایی همان باشد.

## ۹. نوشتن Artifact

خروجی را مستقیم روی فایل نهایی ننویس. روش الزامی:

1. نوشتن در فایل موقت هم‌مسیر؛
2. Flush و Close؛
3. بازخوانی فایل موقت؛
4. کنترل Schema و تعداد رکوردها؛
5. محاسبه SHA-256؛
6. جایگزینی Atomic فایل نهایی.

هر Artifact باید حداقل این موارد را داشته باشد:

```text
artifact_type
schema_version
release_id
input_paths
input_hashes
configuration_sha256
record_counts
limitations
test_access_status
status
```

## ۱۰. Reload Validation

وجود فایل کافی نیست. پس از نوشتن:

1. Artifactها را دوباره از دیسک بخوان.
2. از متغیر اصلی حافظه برای Validation استفاده نکن.
3. Record count، Reference integrity، Rank/Score fidelity، Hash و Schema را کنترل کن.
4. Round-trip reconstruction را کنترل کن.
5. نتیجه را در Reload-validation Artifact ذخیره کن.

تنها پس از Reload Validation می‌توان Status نهایی را `PASS` اعلام کرد.

## ۱۱. جلوگیری از Hashهای حلقوی

ترتیب پیشنهادی تولید خروجی:

1. Core artifacts
2. Core hashes
3. Reload validation
4. Final manifest
5. Release
6. Acceptance
7. Handoff
8. Checkpoint

اگر فایلی به Hash فایل دیگری اشاره می‌کند، فایل دوم نباید هم‌زمان به Hash نسخه نهایی فایل اول وابسته باشد.

## ۱۲. زمان اجرا و Resume

پیش از هر عملیات با زمان احتمالی بیشتر از ۱۰ دقیقه اعلام کن:

- زمان تقریبی؛
- علت زمان‌بر بودن؛
- تعداد رکورد یا Pair؛
- امکان توقف؛
- امکان Resume؛
- محل Checkpoint.

اجرای طولانی باید Atomic checkpoint و قابلیت ادامه بعد از قطع Kernel، سیستم یا اینترنت داشته باشد و رکوردهای کامل‌شده را دوباره محاسبه نکند.

## ۱۳. مدل، دانلود و API

پیش از دانلود یا اجرای مدل:

- Cache محلی و حجم دانلود را بررسی کن؛
- Revision دقیق را ثبت کن؛
- Device و Runtime را بررسی کن؛
- ابتدا Smoke test اجرا کن؛
- سرعت و زمان اجرای کامل را تخمین بزن؛
- قابلیت Resume ایجاد کن.

بدون اجازه کاربر API پولی، دانلود مدل بزرگ یا سرویس خارجی را اجرا نکن. هر خروجی باید مقدار زیر را ثبت کند، مگر اینکه اجازه صریح دیگری داده شده باشد:

```text
paid_api_calls = 0
```

## ۱۴. Metadata و عدم استنتاج

Metadata ناقص را با حدس پر نکن. Author، Speaker، Content authority، Topic، Parent، Rights، Locator و Conflict label فقط از فیلد Canonical مربوط به خودشان گرفته شوند.

در نبود داده معتبر، یکی از وضعیت‌های مستند زیر را ثبت کن:

```text
NOT_PRESENT
NOT_APPLICABLE
NOT_ASSESSED_NO_CANONICAL_MAPPING
UPSTREAM_METADATA_LIMITATION
```

## ۱۵. مجوز پروژه

کارفرما مجوز کامل انجام پردازش‌های این پروژه را تأیید کرده است. Gate محدودکننده قبلی مجوز از جریان پروژه حذف شده است.

- Gate مصنوعی `INTERNAL_EVALUATION_ONLY` دوباره ایجاد نکن.
- Status تحویل را بدون دلیل به `READY_FOR_INTERNAL_EVALUATION_ONLY` محدود نکن.
- Rights موجود را فقط به‌عنوان Metadata منبع حفظ کن.
- نبود بعضی فیلدهای Rights را Blocker فنی Notebook نکن.
- مجوز تأییدشده کارفرما را بدون دستور صریح دوباره زیر سؤال نبر.

این موضوع شامل مجوز API پولی یا تغییر Repository نیست؛ آن‌ها همچنان اجازه جداگانه می‌خواهند.

## ۱۶. Git و Repository

بدون اجازه صریح کاربر:

- Commit یا Push نکن؛
- Branch را تغییر نده؛
- فایل unrelated را تغییر نده؛
- Artifact قبلی را حذف نکن؛
- Git history را بازنویسی نکن.

در پایان فقط فایل‌های ساخته‌شده یا تغییرکرده را گزارش کن.

## ۱۷. رفتار هنگام خطا

در صورت خطا:

1. Traceback کامل را بررسی کن.
2. علت ریشه‌ای را مشخص کن.
3. وابستگی‌های قبل از سل را کنترل کن.
4. اصلاح را در محل تعریف اصلی انجام بده.
5. فقط یک خط موقت برای عبور از خطا اضافه نکن.
6. تمام استفاده‌های بعدی متغیر یا تابع را جست‌وجو کن.
7. Syntax و `Restart & Run All` را دوباره بررسی کن.

Assert را حذف یا ضعیف نکن مگر اینکه خود Contract اشتباه باشد و دلیل آن مستند شود.

## ۱۸. Definition of Done

Notebook فقط وقتی کامل است که:

```text
objective = PASS
syntax_health = PASS
execution_health = PASS
numbering = PASS
markdown_rtl = PASS
canonical_input_hashes = PASS
configuration_frozen = true
configuration_changed_after_test = false
core_artifacts_written = true
reload_validation = PASS
manifest = PASS_COMPLETE_FROZEN
acceptance = PASS_COMPLETE_FROZEN
handoff = READY_FOR_NEXT_NOTEBOOK
checkpoint = PASS
paid_api_calls = 0
```

همچنین:

- Code Cell اجرا‌نشده یا Error output ذخیره‌شده وجود نداشته باشد؛
- Artifact فقط در حافظه باقی نمانده باشد؛
- خروجی مرحله بعد مستقل از Kernel فعلی قابل بارگذاری باشد؛
- Final Health با Artifactهای دیسک برابر باشد؛
- Notebook بعدی و مسیر Handoff مشخص باشند.

## ۱۹. نحوه گزارش به کاربر

در پایان فقط گزارش کن:

1. آیا Notebook واقعاً کامل شد؟
2. Final status چیست؟
3. چه Artifactهایی ساخته شدند؟
4. Reload validation پاس شد یا نه؟
5. مرحله بعد چیست؟
6. آیا اجرای طولانی یا API پولی انجام شد؟
7. آیا Git تغییر داده شد؟

اگر Notebook کامل نیست، صریحاً بنویس:

```text
OBJECTIVE_INCOMPLETE
```

سالم بودن ساختار یا اجرای سل‌ها به‌تنهایی به‌معنای تکمیل هدف Notebook نیست.
