# گزارش اقدام 23 — Completeness پاسخ

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `USER_ACCEPTED_SCOPED_COMPLETION`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** **[پایان این دور با پذیرش محدود کاربر؛ کیفیت کامل تأیید نشده]** سنجش Completeness پاسخ در برابر مطالب لازمِ مرجع؛ جداسازی آن از حضور شاهد در Context.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**گزارش موجود در مخزن:** [reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md).

## کار انجام‌شده و نتیجه

صف ۲۱۱۷تایی C230: ۱۰۷۳ مثبت قبلی، ۳۲۲ Acceptable با معیار جدید، ۹۳ Answer gap، ۱۴ Question ambiguous، دو Evidence insufficient، یک Review required، ۱۷ Input/evidence held و ۵۹۵ خروجی داور غیرقابل‌مصرف. ۱۵۰۵ نتیجهٔ قابل‌گزارش و ۱۳۹۵ مثبت با سیاست‌های متفاوت داریم؛ ۵۹۵ خروجی معیوب داور، ۵۹۵ پاسخ غلط نیست. هزینهٔ معلوم نقل‌شده ۷۱۴٬۱۴۰ تومان و ذخیرهٔ نامعلوم ۱۱٬۶۶۷ تومان است؛ صورتحساب مستقل تأیید نشده.

پایان این دور با درخواست صریح کاربر و محدودیت‌های گزارش مشترک پذیرفته شده است؛ پذیرش کامل معنایی، Human Gold مستقل یا Release نتیجه نمی‌شود.

## شواهد، سل و مسیر خروجی

### NB21B.C228

پیوست گزارش مشترک، سل فیزیکی 472 در Snapshot مبنای آن گزارش:

```json
{
  "status": "C228_REVISED_POLICY_REVIEW_ACCOUNTED_NOT_GOLD",
  "population_cases": 2117,
  "previous_MODEL_FULL_preserved_not_rechecked": 1073,
  "remaining_cases": 1044,
  "revised_review_counts": {
    "INPUT_OR_EVIDENCE_HELD": 17,
    "ANSWER_GAP": 93,
    "HTTP_OR_OUTPUT_HELD": 595,
    "ACCEPTABLE": 322,
    "QUESTION_AMBIGUOUS": 14,
    "EVIDENCE_INSUFFICIENT": 2,
    "REVIEW_REQUIRED": 1
  },
  "accounting_total": 2117,
  "recorded_attempts": 1027,
  "elapsed_minutes": 13.4,
  "run_known_cost": "127,661 تومان",
  "run_unknown_or_inflight_reserve": "0 تومان",
  "overall_known_cost": "714,140 تومان",
  "overall_unknown_reserve": "11,667 تومان",
  "cost_is_verified_invoice": false,
  "automatic_retries": 0,
  "old_files_modified": false,
  "automatic_relabeling_of_old_results": false,
  "independent_population_accuracy_established": false,
  "question_ambiguity_not_counted_as_answer_failure": true,
  "grounding_action22_not_closed_by_this_review": true,
  "action23_closed": false,
  "interrupted": false,
  "stop_reasons": [],
  "artifact_path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C228.semantic_sufficiency_remaining1044/93b8738ed74a8408b09e1ee0798e4e29de984ac396ac00945963f06656d51056/report.05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc.json",
  "artifact_sha256": "05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc",
  "reload_validation": "PASS"
}
```

### NB21B.C230

پیوست گزارش مشترک، سل فیزیکی 476 در Snapshot مبنای آن گزارش:

```json
{
  "status": "C230_OFFLINE_RECOVERY_ACCOUNTED_MODEL_RESULTS_NOT_GOLD",
  "parent_C228_sha256": "05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc",
  "population_cases": 2117,
  "held_outputs_examined": 595,
  "recovery_counts": {
    "REMAINS_HELD": 595
  },
  "raw_text_shapes": {
    "OTHER_TEXT_PREFIX": 588,
    "STARTS_WITH_OBJECT": 5,
    "STARTS_WITH_ARRAY": 1
  },
  "recovered_model_verdicts": {},
  "remaining_error_counts_nonexclusive": {
    "NO_COMPLETE_JSON_OBJECT_NO_REPAIR": 588,
    "FIELDS": 5,
    "VERDICT": 5,
    "TEXT:reason_fa": 5,
    "TEXT:essential_meaning_fa": 5,
    "TEXT:missing_meaning_fa": 5,
    "TEXT:reference_issue_fa": 5,
    "REASON_REQUIRED": 5,
    "GROUNDING_FLAG": 5,
    "IDS_NOT_LIST:source_span_ids": 5,
    "IDS_NOT_LIST:answer_span_ids": 5,
    "COMPLETE_JSON_CONTRACT_NOT_VALID": 5,
    "INCOMPLETE_OR_NONSTOP_NO_REPAIR": 1,
    "MULTIPLE_DISTINCT_JSON_OBJECTS_REVIEW_REQUIRED": 1
  },
  "population_partition": {
    "PREVIOUS_MODEL_FULL_NOT_RECHECKED": 1073,
    "INPUT_OR_EVIDENCE_HELD": 17,
    "ACCEPTABLE": 322,
    "C228_OUTPUT_STILL_HELD": 595,
    "ANSWER_GAP": 93,
    "QUESTION_AMBIGUOUS": 14,
    "EVIDENCE_INSUFFICIENT": 2,
    "REVIEW_REQUIRED": 1
  },
  "positive_model_results_under_mixed_policies": 1395,
  "positive_model_result_percent": 65.9,
  "positive_result_percent_is_not_accuracy": true,
  "recovered_results_are_model_judgments_not_human_gold": true,
  "semantic_quality_improvement_proven": false,
  "recovery_records_path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C230.offline_judge_output_recovery/05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc/C230_recovery_records.json",
  "recovery_records_sha256": "897d4a7d8c0260f1f0cfba31ea38f4716ec93ca635263e5401d728cc1698cb10",
  "new_api_calls": 0,
  "new_cost": "0 تومان",
  "overall_known_cost_as_reported_by_C228": "714,140 تومان",
  "overall_unknown_reserve_as_reported_by_C228": "11,667 تومان",
  "old_files_modified": false,
  "json_content_repaired": false,
  "missing_content_invented": false,
  "old_labels_overwritten": false,
  "action23_closed": false,
  "artifact_path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C230.offline_judge_output_recovery/05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc/report.264259ac134341058684f59ccee427881d722235372402fe2dc2eca0f3976c14.json",
  "artifact_sha256": "264259ac134341058684f59ccee427881d722235372402fe2dc2eca0f3976c14",
  "reload_validation": "PASS"
}
```

## محدودیت و مصرف درست

حدود گزارش مرجع و مخرج‌ها حفظ شوند. شمار پوشش، درصد صحت یا درصد زمان انجام کار نیست. رأی مدل و بازبینی دستیار، خودکار مرجع مستقل انسانی محسوب نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action23_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
