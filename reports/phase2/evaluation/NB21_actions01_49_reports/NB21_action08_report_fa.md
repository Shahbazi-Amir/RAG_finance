# گزارش اقدام 08 — ماتریس شکاف و مسئولیت

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** ساخت Gap matrix: موجود و قابل مصرف / نیازمند تطبیق / مفقود / فاقد اعتبار معنایی؛ تعیین مسئول رفع هر شکاف.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

C019 ماتریسی با ۱۹ ردیف الزام/شکاف و اقدام مسئول را ثبت و Reload کرده است. برای معیارها، شش Ablation، گزارش و تحویل، شاهد موجود و کار باقی‌مانده مشخص شده است. مواردی که بعداً در C024/C025 و گزارش‌های جدید بسته شده‌اند نباید از روی وضعیت قدیمی ماتریس دوباره باز شوند.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C019.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C019 — سل فیزیکی 38

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "status": "NB21_GAP_MATRIX_CHECKPOINT_RELOAD_PASS",
  "checklist_action": 8,
  "checklist_action_total": 49,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C019.input_review.8669fd3abd9b60d992f8af51556d5faf4cf550a079494b649f97ed7926d1939e.json",
    "file_bytes_sha256": "8669fd3abd9b60d992f8af51556d5faf4cf550a079494b649f97ed7926d1939e",
    "bytes": 35096,
    "action": "REUSED_IDENTICAL"
  },
  "gap_matrix": [
    {
      "existing_evidence": [
        "NB13",
        "NB16",
        "NB17",
        "persisted retrieval outputs"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Align Split, Gold mapping, rank depth and metric definitions.",
      "requirement": "Retrieval Recall / MRR / nDCG",
      "responsible_checklist_actions": [
        9,
        19,
        20,
        21
      ],
      "status": "EXISTING_RESULTS_REQUIRE_CONTRACT_ALIGNMENT"
    },
    {
      "existing_evidence": [
        "development outputs",
        "test recovery",
        "existing reviews"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Establish valid measurement and coverage; preserve nonindependence.",
      "requirement": "Groundedness / completeness",
      "responsible_checklist_actions": [
        13,
        14,
        15,
        22,
        23
      ],
      "status": "REFERENCE_VALIDITY_AND_COVERAGE_REQUIRE_ASSESSMENT"
    },
    {
      "existing_evidence": [
        "claim gates",
        "citation sidecars",
        "context evidence registry"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Separate locator integrity, semantic support and attribution.",
      "requirement": "Citation correctness / coverage / attribution",
      "responsible_checklist_actions": [
        13,
        14,
        15,
        24,
        25
      ],
      "status": "STRUCTURAL_ASSETS_PRESENT_SEMANTIC_ACCEPTANCE_OPEN"
    },
    {
      "existing_evidence": [
        "policy records",
        "recovery routing",
        "existing review summaries"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Assess existing reference eligibility before scoring or new judging.",
      "requirement": "No-answer precision / recall / F1",
      "responsible_checklist_actions": [
        8,
        13,
        15,
        26
      ],
      "status": "VALID_REFERENCE_LABELS_NOT_ESTABLISHED_BY_INSPECTED_CONTROLS"
    },
    {
      "existing_evidence": [
        "policy routing",
        "C455 stored scoped audit"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Define denominator, severity, output origin and valid reference.",
      "requirement": "Safety violation rate",
      "responsible_checklist_actions": [
        13,
        15,
        27
      ],
      "status": "SCOPED_AUDIT_AVAILABLE_LIVE_ACCEPTANCE_NOT_ESTABLISHED"
    },
    {
      "existing_evidence": [
        "C455 preserved roadmap limits",
        "NB20 checklist scope notes"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Consume existing calibration evidence within its actual target.",
      "requirement": "Confidence and calibration boundaries",
      "responsible_checklist_actions": [
        28
      ],
      "status": "UPSTREAM_SCOPE_LIMITATIONS_RECORDED"
    },
    {
      "existing_evidence": [
        "historical reports",
        "saved execution artifacts"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Separate historical generation, cache reads and fresh execution.",
      "requirement": "Latency / tokens / cost / failure",
      "responsible_checklist_actions": [
        29,
        30,
        31
      ],
      "status": "MEASUREMENT_COMPATIBILITY_AND_COVERAGE_NOT_YET_ASSESSED"
    },
    {
      "existing_evidence": [
        "existing metadata contracts",
        "Context metadata limitations"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Use actual mappings; report unavailable categories explicitly.",
      "requirement": "Source / Topic / Question type / Authority slices",
      "responsible_checklist_actions": [
        10
      ],
      "status": "CANONICAL_SLICE_MAPPING_REQUIRES_REVIEW"
    },
    {
      "existing_evidence": [
        "versioned normalization acceptance"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Find same-contract comparisons and define affected layers.",
      "requirement": "Ablation: Persian normalization",
      "responsible_checklist_actions": [
        11,
        12,
        32
      ],
      "status": "EXISTING_EVIDENCE_REQUIRES_ABLATION_CONTRACT_REVIEW"
    },
    {
      "existing_evidence": [
        "NB11 evaluation candidates",
        "current character baseline"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Locate retrieval experiments and compatible Gold mappings.",
      "requirement": "Ablation: character versus structure-aware chunking",
      "responsible_checklist_actions": [
        11,
        12,
        33
      ],
      "status": "EXISTING_EVIDENCE_REQUIRES_ABLATION_CONTRACT_REVIEW"
    },
    {
      "existing_evidence": [
        "NB16 evidence and ADR"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Align existing comparisons with the NB21 evaluation contract.",
      "requirement": "Ablation: Dense-only versus Hybrid",
      "responsible_checklist_actions": [
        11,
        12,
        34
      ],
      "status": "EXISTING_EVIDENCE_REQUIRES_ABLATION_CONTRACT_REVIEW"
    },
    {
      "existing_evidence": [
        "NB17 evidence and frozen candidate outputs"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Align candidate depth, ordering and metric definitions.",
      "requirement": "Ablation: without Reranker",
      "responsible_checklist_actions": [
        11,
        12,
        35
      ],
      "status": "EXISTING_EVIDENCE_REQUIRES_ABLATION_CONTRACT_REVIEW"
    },
    {
      "existing_evidence": [
        "NB16 evidence",
        "NB18 configuration and ADR"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Identify the active Context policy and actual changed outputs.",
      "requirement": "Ablation: without source diversity",
      "responsible_checklist_actions": [
        11,
        12,
        36
      ],
      "status": "EXISTING_EVIDENCE_REQUIRES_ABLATION_CONTRACT_REVIEW"
    },
    {
      "existing_evidence": [
        "NB19 claim gates and citation artifacts"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Identify the implemented verifier and valid comparison scope.",
      "requirement": "Ablation: without citation verifier",
      "responsible_checklist_actions": [
        11,
        12,
        37
      ],
      "status": "EXISTING_EVIDENCE_REQUIRES_ABLATION_CONTRACT_REVIEW"
    },
    {
      "existing_evidence": [
        "NB19 development manifest/release/acceptance v4"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Inspect original run metadata before model-specific claims.",
      "requirement": "Development generation model provenance",
      "responsible_checklist_actions": [
        7,
        8,
        16
      ],
      "status": "EXECUTED_MODEL_NOT_SPECIFIED_IN_INSPECTED_CONTROLS"
    },
    {
      "existing_evidence": [
        "historical phase-1 evaluation identified in repository inspection"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Locate local baseline and establish comparable questions and metrics.",
      "requirement": "Phase-1 comparison",
      "responsible_checklist_actions": [
        43
      ],
      "status": "COMPARABLE_SCOPE_NOT_YET_ESTABLISHED"
    },
    {
      "existing_evidence": [
        "1149 saved Test records",
        "historical Test exposure declarations"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Record prior exposure and freeze plan before fresh Test evaluation.",
      "requirement": "Final Test evaluation",
      "responsible_checklist_actions": [
        11,
        12,
        38,
        39,
        40
      ],
      "status": "NEW_EVALUATION_CONTRACT_NOT_FROZEN"
    },
    {
      "existing_evidence": [
        "roadmap targets",
        "documented target differences"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Resolve approved thresholds and upstream dependencies explicitly.",
      "requirement": "Regression and acceptance thresholds",
      "responsible_checklist_actions": [
        12,
        45
      ],
      "status": "CURRENT_ACCEPTANCE_CONTRACT_REQUIRES_RESOLUTION"
    },
    {
      "existing_evidence": [
        "verified inputs",
        "reuse sources",
        "provenance registration"
      ],
      "new_api_requirement": "NOT_DETERMINED_REUSE_FIRST",
      "remaining_work": "Produce reports, reload validation and scoped handoff after evaluation.",
      "requirement": "Benchmark reports / handoff / reproducibility",
      "responsible_checklist_actions": [
        41,
        42,
        44,
        46,
        47,
        48,
        49
      ],
      "status": "NB21_DELIVERABLES_PENDING"
    }
  ],
  "action_8_eligible_for_checkmark": true,
  "checklist_file_updated": false,
  "evaluation_configuration_frozen": false,
  "upstream_product_acceptance_changed": false,
  "reload_validation": "PASS",
  "new_artifact_files_written": 0,
  "existing_artifacts_overwritten": false,
  "semantic_judgments_performed": 0,
  "paid_api_calls": 0,
  "new_api_cost_toman": 0
}
```

## محدودیت و مصرف درست

ثبت Gap matrix، انجام همهٔ کارهای داخل آن نیست؛ وضعیت تاریخ تهیهٔ هر ردیف حفظ شود.

وضعیت‌های OPEN/false در خروجی تاریخی برای زمان همان اجرا حفظ شده‌اند. تصمیم‌های جدیدتر C024/C025 و گزارش‌های پایان ۲۲–۲۶ در سطح ثبت جاری مقدم‌اند؛ برای همسان‌سازی، فایل‌های تاریخی بازنویسی نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action08_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
