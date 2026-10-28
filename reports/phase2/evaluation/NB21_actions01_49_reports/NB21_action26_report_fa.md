# گزارش اقدام 26 — No-answer و تصمیم پاسخ‌دهی

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `HISTORICAL_TEST_MODEL_REFERENCE_DECISION_EVALUATION`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** **[پایان ارزیابی در دامنهٔ Test تاریخی و مرجع مدل؛ محدودیت‌ها محفوظ]** سنجش No-answer precision/recall/F1 و خطاهای پاسخ/خودداری براساس مرجع معتبر؛ Clarification جدا گزارش شود.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**گزارش موجود در مخزن:** [reports/phase2/evaluation/NB21_action26_final_summary.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/reports/phase2/evaluation/NB21_action26_final_summary.md).

## کار انجام‌شده و نتیجه

متن گزارش موجود، با همان دامنه و منشأ، در ادامه نقل می‌شود. دستور ادامهٔ تاریخی داخل نقل‌قول، وضعیت جاری را عوض نمی‌کند؛ ادامهٔ امروز از اقدام۲۷ است:

# اقدام ۲۶ — پایان ارزیابی و گزارش

وضعیت: **کامل در دامنهٔ Test تاریخی و داوری مدل**؛ ثبت به درخواست صریح مالک مخزن.

این گزارش از خروجی اجرای C018 ارسالی مالک بازنویسی شده است. فایل کامل ردیفی روی دستگاه کاربر با این ثبت بازخوانی نشده؛ مسیر و هش گزارش‌شده در [خلاصهٔ ماشینی](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/reports/phase2/evaluation/NB21_action26_final_summary.json) محفوظ است.

| نتیجه | تعداد |
| --- | ---: |
| کل Test | ۱۱۴۹ |
| داوری قابل‌مصرف | ۱۱۳۶ |
| MODEL_CORRECT | ۱۰۹۳ |
| MODEL_INCORRECT | ۳۱ |
| MODEL_UNDETERMINED | ۱۲ |
| خروجی غیرقابل‌مصرف | ۱۳ |

پوشش داوری: ۹۸٫۸۷٪. توافق درستی تصمیم در موارد تعیین‌شده: ۹۷٫۲۴٪. این اعداد صحت مستقل جمعیت یا عملکرد مولد زنده را ثابت نمی‌کنند.

| معیار رفتار، مشروط به مرجع مدل | Precision | Recall | F1 |
| --- | ---: | ---: | ---: |
| خودداری لازم | ۴۲٫۸۶٪ | ۱۰۰٪ | ۶۰٪ |
| اجازهٔ پاسخ محتوایی | ۹۹٫۷۲٪ | ۹۸٫۷۱٪ | ۹۹٫۲۱٪ |

مخرج هر دو مقایسهٔ دودویی ۱۱۳۱ است: ۱۳ خروجی غیرقابل‌مصرف و ۵ مورد خارج از نگاشت دودویی کنار گذاشته شده‌اند. ۱۶ خودداری اضافی شامل ۱۴ سؤال پاسخ‌پذیر و ۲ سؤال نیازمند روشن‌سازی است. Clarification با نبود پاسخ یکی نشده است.

هزینهٔ شناخته‌شده بر مبنای تعرفهٔ تاریخی با احتساب C012: **۶۸۵٬۱۱۰ تومان**؛ ذخیرهٔ برنامه‌ریزی هزینهٔ نامعلوم: **۱۱۵٬۱۰۹ تومان**؛ ذخیره، پرداخت تأییدشده نیست. این ثبت API تازه ندارد.

تیک اقدام ۲۶ پایان ارزیابی و گزارش با حفظ ۳۱ خطا، ۱۲ مورد نامعین و ۱۳ خروجی غیرقابل‌مصرف است. آستانهٔ پذیرش کیفیت یا تأیید Release از این تیک نتیجه نمی‌شود. اقدام ۲۷ جداگانه به Safety می‌پردازد.

## شواهد، سل و مسیر خروجی

خلاصهٔ ماشینی مرجع، برای حفظ دقیق مخرج و تعریف وضعیت‌ها:

```json
{
  "schema_version": "nb21_action26_repository_summary_v1",
  "status": "ACTION26_OFFLINE_EVALUATION_REPORT_COMPLETE",
  "provenance": {
    "basis": "C018 execution output supplied by repository owner in this conversation",
    "raw_report_bytes_independently_reloaded": false,
    "repository_head_reviewed": "5a75fe1216d01f12234c8a1f68a9515991775b3b",
    "original_report_path": "reports/phase2/evaluation/NB21C.C018.action26_final/C018.report.3d860b1077a63b4ad78f9f7ea828840e2fd2ae2cb7d7e60197c2ada141cef500.json",
    "original_report_sha256_reported": "3d860b1077a63b4ad78f9f7ea828840e2fd2ae2cb7d7e60197c2ada141cef500",
    "reload_validation_reported": "PASS"
  },
  "population_count": 1149,
  "locally_valid_judgments": 1136,
  "decision_counts": {
    "MODEL_CORRECT": 1093,
    "MODEL_INCORRECT": 31,
    "MODEL_UNDETERMINED": 12,
    "EXECUTION_OR_INPUT_UNRESOLVED": 13
  },
  "rates": {
    "valid_judgment_coverage": 0.9886858137510879,
    "determined_judgment_coverage": 0.9782419495213229,
    "model_correct_fraction_of_all_cases": 0.9512619669277633,
    "model_correct_rate_among_determined_judgments": 0.9724199288256228,
    "model_correct_rate_among_all_valid_judgments": 0.9621478873239436,
    "these_are_not_independent_population_accuracy": true
  },
  "expected_by_observed_behavior": {
    "ABSTENTION_REQUIRED": {
      "ABSTENTION_ONLY": 12
    },
    "ANSWER_SUPPORTED": {
      "SUBSTANTIVE_RESPONSE": 935,
      "ABSTENTION_ONLY": 8
    },
    "BOUNDED_ANSWER_SUPPORTED": {
      "SUBSTANTIVE_RESPONSE": 139,
      "ABSTENTION_ONLY": 6
    },
    "CLARIFICATION_REQUIRED": {
      "CLARIFICATION_ONLY": 26,
      "MIXED": 4,
      "SUBSTANTIVE_RESPONSE": 3,
      "ABSTENTION_ONLY": 2
    },
    "UNDETERMINED": {
      "ABSTENTION_ONLY": 1
    }
  },
  "abstention_metrics": {
    "scope": "CONDITIONAL_ON_EVALUABLE_MODEL_REFERENCE",
    "confusion_matrix": {
      "TP": 12,
      "FP": 16,
      "FN": 0,
      "TN": 1103
    },
    "evaluated_case_count": 1131,
    "precision": 0.42857142857142855,
    "recall": 1,
    "f1": 0.6,
    "broad_binary_agreement": 0.9858532272325375
  },
  "answer_decision_metrics": {
    "scope": "CONDITIONAL_ON_EVALUABLE_MODEL_REFERENCE",
    "confusion_matrix": {
      "TP": 1074,
      "FP": 3,
      "FN": 14,
      "TN": 40
    },
    "evaluated_case_count": 1131,
    "precision": 0.9972144846796658,
    "recall": 0.9871323529411765,
    "f1": 0.9921478060046189,
    "broad_binary_agreement": 0.9849690539345711
  },
  "binary_metric_exclusions": {
    "unreadable": 13,
    "other_valid_cases_outside_binary_mapping": 5,
    "explanation": "4 MIXED observations and 1 UNDETERMINED expected behavior; semantic-decision unknown and binary behavior evaluability are separate dimensions."
  },
  "costs": {
    "semantic_rounds_historical_tariff_known_cost_toman": 671239,
    "semantic_rounds_unknown_cost_planning_reserve_toman": 113584,
    "C012_historical_tariff_known_cost_toman": 13871,
    "C012_unknown_cost_planning_reserve_toman": 1525,
    "all_recorded_work_historical_tariff_known_cost_toman": 685110,
    "all_recorded_work_unknown_cost_planning_reserve_toman": 115109,
    "cost_is_verified_invoice": false,
    "unknown_reserve_is_not_confirmed_payment": true,
    "new_api_cost_toman": 0
  },
  "completion": {
    "action": 26,
    "evaluation_and_reporting_complete": true,
    "action_26_completed_in_reported_scope": true,
    "completion_scope": "HISTORICAL_TEST_MODEL_REFERENCE_DECISION_EVALUATION",
    "all_1149_initial_semantic_attempts_accounted": true,
    "corrective_219_round_finished": true,
    "unreadable_results_preserved": 13,
    "semantic_undetermined_results_preserved": 12,
    "formal_quality_gate_pass": null,
    "independent_reference_accuracy_established": false,
    "live_generator_performance_established": false,
    "new_api_calls": 0
  },
  "limitations": [
    "Historical exposed Test; model reference is not independent ground truth.",
    "930 previous valid results and 206 valid corrective results use different output contracts; no retrospective blind evaluation claimed.",
    "Completion records evaluation and reporting; it does not assert every model answer correct or Release acceptance.",
    "Row-level raw reports remain referenced artifacts; this repository summary does not replace their byte identities."
  ]
}
```

## محدودیت و مصرف درست

حدود گزارش مرجع و مخرج‌ها حفظ شوند. شمار پوشش، درصد صحت یا درصد زمان انجام کار نیست. رأی مدل و بازبینی دستیار، خودکار مرجع مستقل انسانی محسوب نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action26_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
