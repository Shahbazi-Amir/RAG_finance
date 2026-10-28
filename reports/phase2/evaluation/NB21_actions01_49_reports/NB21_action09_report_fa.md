# گزارش اقدام 09 — تعریف معیارها و مخرج‌ها

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** تعریف دقیق Metricها، مخرج، واحد تحلیل، k، روش میانگین‌گیری، Missing/Abstention و عدم قطعیت.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

C020 شانزده خانوادهٔ Metric را با واحد تحلیل، مخرج، تجمیع، k و قواعد Missing/صفرمخرج تعریف کرده است. معیارهای Hit و Recall، rank depth، اعتبار ساختاری و معنایی یکسان فرض نشده‌اند. این مرحله تعریف معیار بوده؛ آستانه و قرارداد اجرایی نهایی بعداً در اقدام۱۲/C025 ثبت شده است.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C020.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C020 — سل فیزیکی 40

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "status": "NB21_METRIC_DEFINITION_DRAFT_RELOAD_PASS",
  "checklist_action": 9,
  "checklist_action_total": 49,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C020.metric_definitions.4ff5630b473e5c49a45ac1e9e58c991db4caf16d47c7260cad66842b9abeaae6.json",
    "file_bytes_sha256": "4ff5630b473e5c49a45ac1e9e58c991db4caf16d47c7260cad66842b9abeaae6",
    "bytes": 8216,
    "action": "REUSED_IDENTICAL",
    "reload_validation": "PASS"
  },
  "metric_names": [
    "recall_at_k",
    "hit_at_k",
    "reciprocal_rank",
    "ndcg_at_k_binary",
    "groundedness",
    "answer_completeness",
    "citation_correctness",
    "claim_citation_coverage",
    "citation_locator_accuracy",
    "attribution_correctness",
    "no_answer_precision_recall_f1",
    "safety_violation_rate",
    "latency",
    "token_usage",
    "cost",
    "failure_rate"
  ],
  "action_9_eligible_for_checkmark": true,
  "acceptance_scope": "EXPLICIT_METRIC_DEFINITIONS_AND_MISSING_DATA_RULES",
  "evaluation_contract_frozen": false,
  "acceptance_thresholds_set": false,
  "pending_dependencies": {
    "population_action_mapping_and_test_exposure": 11,
    "qualified_semantic_measurement": [
      13,
      14,
      15
    ],
    "runner_and_pilot_validation": [
      16,
      17,
      18
    ],
    "slice_contract": 10,
    "thresholds_and_final_freeze": 12
  },
  "checklist_file_updated": false,
  "semantic_judgments_performed": 0,
  "new_artifact_files_written": 0,
  "paid_api_calls": 0,
  "new_api_cost_toman": 0
}
```

## محدودیت و مصرف درست

Target اولیه، Gate مصوب همیشگی نیست؛ قرارداد جاری C025 آینده‌نگر است.

وضعیت‌های OPEN/false در خروجی تاریخی برای زمان همان اجرا حفظ شده‌اند. تصمیم‌های جدیدتر C024/C025 و گزارش‌های پایان ۲۲–۲۶ در سطح ثبت جاری مقدم‌اند؛ برای همسان‌سازی، فایل‌های تاریخی بازنویسی نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action09_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
