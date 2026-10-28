# گزارش اقدام 13 — Rubric و موجودی مرجع

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** بررسی Rubric، پاسخ/شاهد مرجع و استقلال داوری برای Groundedness، completeness، citation و attribution.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

C035–C041 Rubric و حضور مرجع‌ها و استقلال ثبت‌شده را بررسی کرده‌اند. برای ۲۶۶۴ سؤال Development، سؤال، پاسخ مرجع، شناسه/نقل‌قول/Locator شاهد و سند وجود دارد. داشتن فیلد مرجع با صحت معنا یا جامعیت آن یکی نشده است. حمایت تاریخی Recovery غیرمستقل و بازبینی‌های محدود با حدود واقعی نگه داشته شده‌اند.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C035–C041؛ Rubric هم‌راستا C040.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C041 — سل فیزیکی 82

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "schema_version": "nb21_reference_review_checkpoint_C041_v1",
  "status": "NB21_REFERENCE_REVIEW_CHECKPOINT_RELOAD_PASS",
  "checklist_action": 13,
  "checklist_action_total": 49,
  "acceptance_scope": "REVIEW_OF_RUBRIC_REFERENCE_AVAILABILITY_AND_RECORDED_INDEPENDENCE",
  "input_bindings": {
    "aligned_rubric": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C040.metric_aligned_assessment_rubric.7351ce0a46e80064a08045350d3f9fe9da2c173c2f443c59b3648b3012c7c9f6.json",
      "file_bytes_sha256": "7351ce0a46e80064a08045350d3f9fe9da2c173c2f443c59b3648b3012c7c9f6"
    },
    "existing_review_census": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C037.review_metadata_census.e3abffce4ae6684c10d575026be0991a4f01acdbad44979b4c2eaa464c0d96af.json",
      "file_bytes_sha256": "e3abffce4ae6684c10d575026be0991a4f01acdbad44979b4c2eaa464c0d96af"
    },
    "golden": {
      "path": "artifacts/phase2/golden_dataset_v2/golden_dataset_v2.jsonl",
      "file_bytes_sha256": "b9ca18e710686ddca48a25c637840b716adb306717cafd8ec7c96ce9e182e6f2"
    }
  },
  "development_query_count": 2664,
  "reference_field_coverage": {
    "document_ids_missing_or_empty": 0,
    "document_ids_present": 2664,
    "evidence_ids_missing_or_empty": 0,
    "evidence_ids_present": 2664,
    "evidence_locators_missing_or_empty": 0,
    "evidence_locators_present": 2664,
    "evidence_quotes_missing_or_empty": 0,
    "evidence_quotes_present": 2664,
    "expected_answer_missing_or_empty": 0,
    "expected_answer_present": 2664,
    "nondevelopment_id_filter_only": 1149,
    "question_missing_or_empty": 0,
    "question_present": 2664
  },
  "findings": [
    {
      "area": "Groundedness and citation support",
      "finding": "Existing recovery support is explicitly nonindependent; retain as historical/descriptive evidence, not an automatically qualified independent reference."
    },
    {
      "area": "Completeness",
      "finding": "Reference-answer presence is counted below. Qualified required-information units and their adequacy remain unvalidated; presence alone does not establish coverage."
    },
    {
      "area": "Attribution",
      "finding": "Canonical metadata coverage was recorded in C026. Authority tiers and raw speaker labels do not by themselves validate every emitted attribution assertion."
    },
    {
      "area": "User review",
      "finding": "The inspected file contains two limited-scope records with independence_verified=false and verified_ground_truth=false; other reviews are not declared absent."
    }
  ],
  "reference_field_presence_proves_semantic_validity": false,
  "reference_coordinates_validated": false,
  "independent_reference_accepted": false,
  "semantic_measurement_method_accepted": false,
  "complete_population_scoring_authorized": false,
  "next_dependencies": {
    "reuse_valid_method_tests_and_pilot_real_gaps": 14,
    "accepted_method_and_coverage_decision": 15,
    "input_join_and_coordinate_validation": 16
  },
  "action_13_eligible_for_checkmark": true,
  "blanket_semantic_rereview_required": false,
  "historical_c455_acceptance_changed": false,
  "semantic_judgments_performed": 0,
  "paid_api_calls": 0,
  "new_api_cost_toman": 0,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C041.reference_review_checkpoint.89e33877111d1204111f8a0b383c44ef0755b57537cc9ec24ba4bc66ca0303ba.json",
    "file_bytes_sha256": "89e33877111d1204111f8a0b383c44ef0755b57537cc9ec24ba4bc66ca0303ba",
    "bytes": 812753,
    "action": "REUSED_IDENTICAL",
    "reload_validation": "PASS"
  },
  "checklist_file_updated": false,
  "quality_metrics_computed": false,
  "new_artifact_files_written": 0
}
```

## محدودیت و مصرف درست

در زمان C041 کنترل تمام مختصات منبع و پذیرش مرجع مستقل برقرار نبود؛ کنترل محدود بعدی به جمعیت تعمیم داده نشود.

وضعیت‌های OPEN/false در خروجی تاریخی برای زمان همان اجرا حفظ شده‌اند. تصمیم‌های جدیدتر C024/C025 و گزارش‌های پایان ۲۲–۲۶ در سطح ثبت جاری مقدم‌اند؛ برای همسان‌سازی، فایل‌های تاریخی بازنویسی نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action13_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
