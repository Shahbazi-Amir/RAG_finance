# نقشهٔ واقعی اجرای فاز دوم RAG_finance

**نسخه:** P2AUD-AS-BUILT-DRAFT-V1

**وضعیت:** قابل بازبینی؛ فاقد پذیرش رسمی Release

## ۱. خلاصهٔ اجرایی

فاز دوم طبق گزارش مالک پروژه از نظر پیاده‌سازی اصلی عملاً انجام شده است. ممیزی، وجود ۲۴ نوت‌بوک اصلی و ۲۴ نوت‌بوک تکمیلی مرتبط را ثبت کرده است.

این سند سه موضوع را جدا نگه می‌دارد: **پیاده‌سازی، شواهد اجرا و پذیرش نهایی**.

بهبود کیفیت بازیابی در NB22 همچنان ادامه دارد. قرارداد Draft در NB23 ساخته شده، اما تحویل رسمی فاز سوم وابسته به پذیرش Release است.

## ۲. منابع و نسخهٔ نقشه‌ها

- **MODULAR:** `data/Road_Maps/RAG_finance_phase2_modular_notebooks_execution_plan.md`
  - SHA-256: `31b91c072cccde2fb0e0a37fe10a67ec545ede325385b743b978a60cc4869e9e`
  - وضعیت خواندن: `READ_SUCCESS`
- **OPERATIONAL:** `data/Road_Maps/RAG_finance_phase2_operational_roadmap.md`
  - SHA-256: `6f8d4502665e148cd099e0f8b811c4541d19bfaf862a2653493d0a1989b2b38c`
  - وضعیت خواندن: `READ_SUCCESS`

## ۳. نقشهٔ اجرایی NB00 تا NB23

### S01 — آماده‌سازی و Baseline

| NB | مسئولیت | بستهٔ اصلی | فرعی | نامزد گزارش | وضعیت |
|---|---|---|---:|---:|---|
| NB00 | محیط و Baseline فاز اول | P2-01 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |

### S02 — دریافت و پردازش منابع

| NB | مسئولیت | بستهٔ اصلی | فرعی | نامزد گزارش | وضعیت |
|---|---|---|---:|---:|---|
| NB01 | دریافت محتوای وب‌سایت | P2-03 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB02 | پذیرش و کنترل کیفیت وب‌سایت | P2-03 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB03 | موجودی کتاب‌ها | P2-04 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB04 | استخراج و پردازش کتاب‌ها | P2-04 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB05 | موجودی Transcript | P2-05 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB06 | پردازش Transcript | P2-05 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |

### S03 — یکپارچه‌سازی، کیفیت و Golden

| NB | مسئولیت | بستهٔ اصلی | فرعی | نامزد گزارش | وضعیت |
|---|---|---|---:|---:|---|
| NB07 | Schema مشترک و Lineage | P2-02, P2-06 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB08 | نرمال‌سازی فارسی | P2-07 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB09 | حذف تکرار و کیفیت داده | P2-06 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB10 | Taxonomy و مهندسی دانش | بدون مالک اصلی مستقل | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB11 | آزمایش Chunking | P2-07 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB12 | Golden Dataset | P2-08 | 11 | 1 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |

### S04 — Embedding و بازیابی

| NB | مسئولیت | بستهٔ اصلی | فرعی | نامزد گزارش | وضعیت |
|---|---|---|---:|---:|---|
| NB13 | Benchmark مدل Embedding | P2-09 | 1 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB14 | Dense Index | P2-09 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB15 | Sparse Index | P2-09 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB16 | Hybrid Retrieval | P2-10 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB17 | Reranking | P2-10 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB18 | Context Builder | P2-11 | 0 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |

### S05 — تولید پاسخ و ایمنی

| NB | مسئولیت | بستهٔ اصلی | فرعی | نامزد گزارش | وضعیت |
|---|---|---|---:|---:|---|
| NB19 | Generation و Citation | P2-11 | 0 | 2 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB20 | Answerability، Safety و Confidence | P2-12 | 2 | 0 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |

### S06 — ارزیابی، Release و Handoff

| NB | مسئولیت | بستهٔ اصلی | فرعی | نامزد گزارش | وضعیت |
|---|---|---|---:|---:|---|
| NB21 | Evaluation و Ablation | P2-10 | 2 | 1480 | پیاده‌سازی‌شده طبق گزارش مالک؛ پذیرش مستقل بررسی‌نشده |
| NB22 | Release و Reproducibility | P2-13, P2-14 | 7 | 213 | Checkpoint انجام‌شده؛ پذیرش کیفیت باز |
| NB23 | قرارداد تحویل فاز سوم | بدون مالک اصلی مستقل | 1 | 5 | قرارداد Draft انجام‌شده؛ تحویل رسمی باز |

## ۴. نگاشت ۱۴ بستهٔ عملیاتی

| بسته | نوت‌بوک‌های اصلی | نوت‌بوک‌های پشتیبان |
|---|---|---|
| P2-01 | NB00 | بدون مالک اصلی مستقل |
| P2-02 | NB07 | NB02, NB22 |
| P2-03 | NB01, NB02 | بدون مالک اصلی مستقل |
| P2-04 | NB03, NB04 | بدون مالک اصلی مستقل |
| P2-05 | NB05, NB06 | بدون مالک اصلی مستقل |
| P2-06 | NB07, NB09 | NB02, NB04, NB06, NB22 |
| P2-07 | NB08, NB11 | NB18 |
| P2-08 | NB12 | NB21 |
| P2-09 | NB13, NB14, NB15 | NB22 |
| P2-10 | NB16, NB17, NB21 | NB14, NB15 |
| P2-11 | NB18, NB19 | NB20 |
| P2-12 | NB20 | NB21 |
| P2-13 | NB22 | NB00, NB21, NB23 |
| P2-14 | NB22 | NB10, NB11, NB13, NB19, NB20, NB21 |

## ۵. اختلاف‌های دو نقشه

| شناسه | موضوع | نتیجهٔ مستند | تصمیم رسمی |
|---|---|---|---|
| P2AUD-RV-001 | Citation Coverage | NUMERIC_THRESHOLD_DIFFERENCE_DOCUMENTED | باز |
| P2AUD-RV-002 | ترتیب قراردادها و Schema | BASE_CONTRACT_VS_UNIFIED_SCHEMA_SCOPE | باز |
| P2AUD-RV-003 | Chunking و Golden | CONCEPTUAL_SEQUENCE_VS_ALLOWED_PARALLELISM | باز |
| P2AUD-RV-004 | مالکیت Taxonomy | MODULAR_OWNER_VS_OPERATIONAL_MAPPING_GAP | باز |
| P2AUD-RV-005 | مالکیت Handoff فاز سوم | NOTEBOOK_HANDOFF_VS_GLOBAL_DELIVERY_GATE | باز |

### منشأ و توضیح اختلاف‌ها

**P2AUD-RV-001 — Citation Coverage**

اختلاف عددی مستند میان Coverage ماژولار و معیار اولیهٔ عملیاتی؛ تعیین دامنه و معیار نهایی به قرارداد فریز‌شده وابسته است.

- `MODULAR` خط 1126: \| Claim citation coverage \| حداقل 0.90 \|
- `MODULAR` خط 825: Claim-level citation، Source-specific locator، Unsupported-claim control و Citation correctness benchmark.
- `OPERATIONAL` خط 340: \| <span dir="ltr">Citation coverage</span> \| حداقل ۹۵٪ Claimهای factual \|

**P2AUD-RV-002 — ترتیب قراردادها و Schema**

P2-02 قراردادهای پایه را پیش از Ingestion قرار می‌دهد؛ NB07 یکپارچه‌سازی Schema منابع را توضیح می‌دهد. ترتیب اجرای واقعی به‌تنهایی از این دو نقشه اثبات نمی‌شود.

- `MODULAR` خط 479: ## Notebook 07 — `07_unified_schema_and_lineage.ipynb`
- `OPERATIONAL` خط 78: ## ۵. بسته P2-02 - Data Contract، Stable IDs و Versioning
- `OPERATIONAL` خط 309: 3. P2-03 تا P2-05 به‌ترتیب یا موازی پس از Contract.

**P2AUD-RV-003 — Chunking و Golden**

نقشهٔ ماژولار ترتیب مفهومی NB11 و NB12 را نشان می‌دهد؛ نقشهٔ عملیاتی امکان پیشبرد موازی P2-07 و P2-08 را مطرح می‌کند.

- `MODULAR` خط 125: L --> M[12 Golden Dataset]
- `OPERATIONAL` خط 311: 5. P2-08 Golden Dataset هم‌زمان با P2-07 Chunking.

**P2AUD-RV-004 — مالکیت Taxonomy**

NB10 در نقشهٔ ماژولار مسئول مستقیم Taxonomy است؛ در نگاشت ۱۴ بسته، مالک عملیاتی اصلی مستقل مشخص نشده است. این موضوع به‌تنهایی نبود پیاده‌سازی نیست.

- `MODULAR` خط 555: ## Notebook 10 — `10_taxonomy_and_knowledge_engineering.ipynb`
- `MODULAR` خط 1057: \| مهندسی دانش \| Taxonomy، Competency، Expert review \| 10 \|
- `OPERATIONAL` خط 294: ## ۱۷. بسته P2-14 - مستندات دانش فنی

**P2AUD-RV-005 — مالکیت Handoff فاز سوم**

NB23 مسئول قرارداد Handoff در نقشهٔ ماژولار است؛ نقشهٔ عملیاتی تعهدات تحویل فاز سوم را در Gate سراسری دارد. Draft ساخته‌شده از پذیرش رسمی جداست.

- `MODULAR` خط 915: ## Notebook 23 — `23_phase3_handoff.ipynb`
- `MODULAR` خط 937: artifacts/phase2/releases/<release_id>/phase3_handoff_contract.json
- `OPERATIONAL` خط 318: ## ۱۹. Gate نهایی و تحویل به فاز ۳
- `OPERATIONAL` خط 323: - <span dir="ltr">RAG input/output contract.</span>

## ۶. وضعیت کیفیت و پذیرش

### NB22 — بازیابی و Release

| سنجه | نتیجهٔ تاریخی Test | هدف |
|---|---:|---:|
| Recall@10 | 0.6343 | 0.85 |
| nDCG@10 | 0.5735 | 0.75 |

**Gate تاریخی:** 2 PASS، 2 FAIL، 12 BLOCKED.

آزمایش‌های جدید 22e روی Validation به نتایج بهتری رسیده‌اند؛ اما ثبت نتیجهٔ پایدار روی نسخهٔ پذیرفته‌شده هنوز باز است.

### NB23 — تحویل فاز سوم

قرارداد Draft و آزمون‌های ساختاری تهیه شده‌اند. پذیرش رسمی Handoff وابسته به Release معتبر و اتصال نسخه‌های واقعی Producer است.

## ۷. دفتر نسخه‌های تکمیلی

### NB12

- `notebooks/phase2/archive/series12_notebooks/12a_golden_dataset_initial.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12b_golden_dataset_continuation_compact.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12c_human_review_for_author.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12d_second_human_review.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12e_golden_dataset_full_generation.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12f_author_feedback_integration.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_quality_rebuild_lab.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12g_golden_dataset_rebuild_clean.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12h_pilot_and_expansion_audit.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12i_claim_registry_and_knowledge_graph.ipynb`
- `notebooks/phase2/archive/series12_notebooks/12j_golden_dataset_v2_registry_driven_rebuild.ipynb`

### NB13

- `notebooks/phase2/13_embedding_benchmark_closure_candidate.ipynb`

### NB20

- `notebooks/phase2/20b_answerability_safety_confidence_scoped_review.ipynb`
- `notebooks/phase2/20c_answerability_safety_confidence_audit_and_acceptance.ipynb`

### NB21

- `notebooks/phase2/21b_evaluation_and_ablation_continued.ipynb`
- `notebooks/phase2/21c_evaluation_and_ablation_continued.ipynb`

### NB22

- `notebooks/phase2/22b_quality_improvement_and_acceptance.ipynb`
- `notebooks/phase2/22c_retrieval_diagnosis_and_improvement.ipynb`
- `notebooks/phase2/22d_full_corpus_retrieval_expansion.ipynb`
- `notebooks/phase2/22e_retrieval_experiment_lab_v1.ipynb`
- `notebooks/phase2/22e_retrieval_experiment_lab_v2.ipynb`
- `notebooks/phase2/22f_consolidated_retrieval_benchmark_v1.ipynb`
- `notebooks/phase2/backup_versions/22b_quality_improvement_and_acceptance.ipynb`

### NB23

- `notebooks/phase2/backup_versions/23_phase3_handoff.ipynb`

### فایل‌های کمکی خارج از دسته‌بندی NB00–NB23

- `notebooks/phase2/API_connection_diagnostics_v1.ipynb`
- `notebooks/phase2/audit/phase2_roadmap_execution_audit.ipynb`

## ۸. کارهای باقی‌مانده

۱. ثبت تصمیم دربارهٔ تفاوت قرارداد Citation Coverage.

۲. بررسی نسخهٔ نهایی نتایج NB22 و پایداری کیفیت؛ بدون بازاجرای بی‌دلیل آزمایش‌های قبلی.

۳. تعیین پذیرش رسمی Release و سپس Handoff فاز سوم.

۴. تکمیل ارجاع‌های شواهد پذیرش برای ردیف‌هایی که هنوز بررسی مستقل نشده‌اند.

۵. ثبت تصمیم نهایی دربارهٔ چهار اختلاف دیگر نقشه‌ها.

## ۹. محدودیت‌های گزارش

- این سند ممیزی READ-ONLY است.
- گزارش‌های نام‌دار، مجموعهٔ کامل شواهد پروژه نیستند.
- صفر گزارش، اثبات نبود کار نیست.
- نتایج Validation به‌تنهایی PASS نهایی نیستند.
- هیچ Gate یا Release تازه‌ای پذیرفته نشده است.
- تصمیم‌های رسمی تاریخی تغییر نکرده‌اند.