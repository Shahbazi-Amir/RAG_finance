# گزارش اقدام 11 — Test exposure و طرح مقایسه

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** ثبت سابقهٔ دسترسی Test، قواعد Development-only، طرح مقایسهٔ زوجی و طرح شش Ablation؛ بدون تغییر قراردادهای فریز‌شدهٔ قبلی.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

C027–C032 سابقهٔ مواجههٔ Test، Development-only selection، مقایسهٔ زوجی، گروه‌بندی و شش طرح Ablation را ثبت کرده‌اند. در خروجی C032، ۲۶۶۴ پرسش Development در ۲۶۲۰ گروه و شش مقایسه ثبت شده و تمام کنترل‌های طرح پاس‌اند. C030 مرجع اصلاح‌شدهٔ هش عضویت گروه‌هاست.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C027–C032؛ گروه‌بندی C030.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C032 — سل فیزیکی 64

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "status": "NB21_COMPARISON_PLAN_RELOAD_PASS",
  "checklist_action": 11,
  "checklist_action_total": 49,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C032.comparison_and_ablation_plan.9ca95a9af817242f80b4fac7a81e06d81c28624f90caf062b7d2c86364fee2b0.json",
    "file_bytes_sha256": "9ca95a9af817242f80b4fac7a81e06d81c28624f90caf062b7d2c86364fee2b0",
    "bytes": 11866,
    "action": "REUSED_IDENTICAL",
    "reload_validation": "PASS"
  },
  "checks": {
    "six_planned_ablations": true,
    "six_control_bindings": true,
    "development_only_selection": true,
    "no_pristine_test_claim": true,
    "prior_exposure_recorded": true,
    "no_test_threshold_retuning": true,
    "paired_query_identity": true,
    "verified_group_population": true,
    "corrected_membership_binding": true,
    "grouped_paired_resampling_planned": true,
    "technical_control_checks_pass": true
  },
  "acceptance_scope": "RECORDED_TEST_EXPOSURE_DEVELOPMENT_RULES_PAIRED_COMPARISON_AND_SIX_ABLATION_PLANS",
  "ablation_count": 6,
  "development_query_count": 2664,
  "question_group_count": 2620,
  "action_11_eligible_for_checkmark": true,
  "action_10_completed": false,
  "downstream_dependencies": [
    {
      "requirement": "Complete or explicitly resolve slice gaps",
      "responsible_actions": [
        10
      ],
      "status": "OPEN"
    },
    {
      "requirement": "Thresholds, coverage gates, budget, cache contract, and evaluation blueprint",
      "responsible_actions": [
        12
      ],
      "status": "OPEN"
    },
    {
      "requirement": "Qualified semantic measurement",
      "responsible_actions": [
        13,
        14,
        15
      ],
      "status": "OPEN"
    },
    {
      "requirement": "Input joins, consumer validation, pilot, runner",
      "responsible_actions": [
        16,
        17,
        18
      ],
      "status": "OPEN"
    },
    {
      "requirement": "Per-ablation execution bindings and comparisons",
      "responsible_actions": [
        32,
        33,
        34,
        35,
        36,
        37
      ],
      "status": "OPEN"
    },
    {
      "requirement": "Final Test freeze before fresh evaluation",
      "responsible_actions": [
        38,
        39,
        40
      ],
      "status": "OPEN"
    }
  ],
  "checklist_file_updated": false,
  "evaluation_contract_frozen": false,
  "experiments_executed": 0,
  "semantic_judgments_performed": 0,
  "new_artifact_files_written": 0,
  "paid_api_calls": 0,
  "new_api_cost_toman": 0
}
```

## محدودیت و مصرف درست

طرح شش Ablation با اجرای آن‌ها فرق دارد؛ Test تاریخی دست‌نخورده معرفی نمی‌شود.

وضعیت‌های OPEN/false در خروجی تاریخی برای زمان همان اجرا حفظ شده‌اند. تصمیم‌های جدیدتر C024/C025 و گزارش‌های پایان ۲۲–۲۶ در سطح ثبت جاری مقدم‌اند؛ برای همسان‌سازی، فایل‌های تاریخی بازنویسی نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action11_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
