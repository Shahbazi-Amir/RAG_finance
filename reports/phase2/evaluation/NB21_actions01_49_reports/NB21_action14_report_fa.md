# گزارش اقدام 14 — آزمون تشخیصی روش

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** مصرف آزمون‌های معتبر قبلی و آزمودن فقط شکاف واقعی روش سنجش روی Development؛ شامل شاهد اشتباه، ادعای معکوس، نقل‌قول ساختگی و پاسخ ناقص.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

دور تشخیصی C298–C301 به پایان رسیده است: ۲۴ پروندهٔ پایه با هشت مورد از هر منبع، ۱۰۴ سناریوی آماده، ۱۰۴ تطابق با انتظار فریز‌شده، ۸۲ پاسخ معنایی ذخیره‌شده و ۱۶ سناریوی HOLD. خانواده‌ها: ۸ Complete coverage، ۸ Partial coverage، ۲۲ جفت نقل‌قول، ۲۲ Positive support، ۲۲ Reversed assertion و ۲۲ Wrong evidence. این پایان دور تشخیصی است؛ طرح اولیهٔ ۱۲۰تایی کامل پاس نشده است.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C298–C301.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C299 — سل فیزیکی 600

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "schema_version": "nb21_action14_frozen_batch_review_C299_v1",
  "status": "NB21_REVIEW_FROZEN_READY_SUBSET_AVAILABLE_PLANNED_SCOPE_BLOCKED",
  "checklist_action": 14,
  "checklist_action_total": 49,
  "review_origin": "ASSISTANT_SOURCE_ONLY_REVIEW_IN_THIS_CHAT",
  "independent_expert_or_population_gold": false,
  "coverage_source_counts": {
    "book": 3,
    "transcript": 1,
    "website": 4
  },
  "planned_scenario_count": 120,
  "ready_scenario_count": 104,
  "held_scenario_count": 16,
  "ready_support_request_count": 66,
  "ready_coverage_request_count": 16,
  "maximum_semantic_requests_before_cache": 82,
  "literal_pair_count": 22,
  "literal_individual_check_count": 44,
  "expectations_frozen_before_evaluator_dispatch": true,
  "full_original_suite_can_pass_with_current_holds": false,
  "network_requests": 0,
  "paid_api_calls": 0,
  "golden_dataset_modified": false,
  "checklist_file_updated": false,
  "action_14_eligible_for_checkmark": false,
  "population_method_accepted": false,
  "held_base_cases": {
    "A14-B10": "AMBIGUOUS_TAX_QUESTION_AND_REFERENCE_REFERENT: متن بین مالیات و واجبات مالی تفکیک می‌کند؛ مرجع پیشنهادی پاسخ قابل اتکایی به سؤال موجود نیست.",
    "A14-B11": "TAUTOLOGICAL_QUESTION: سؤال نام الگو را در خود دارد و همان نام را می‌پرسد؛ برای این بسته آزمون معناداری فراهم نمی‌کند."
  },
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_action14_batch_v1/C299.frozen_batch_review.ace247f2e0a0d32c9bbae14c5a772bea64ef8fabdbaeb1b5f8a1e9fefc5afbf7.json",
    "file_bytes_sha256": "ace247f2e0a0d32c9bbae14c5a772bea64ef8fabdbaeb1b5f8a1e9fefc5afbf7",
    "bytes": 117763,
    "action": "CREATED",
    "reload_validation": "PASS"
  }
}
```

### NB21-C301 — سل فیزیکی 604

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "schema_version": "nb21_diagnostic_round_closure_C301_v1",
  "status": "NB21_ACTION14_DIAGNOSTIC_TEST_ROUND_COMPLETE",
  "checklist_action": 14,
  "checklist_action_total": 49,
  "input_bindings": {
    "execution": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_batch_execution_C300_v1/dca30461fdee984528a1a81d200cf96c981cfa51660cad51ccd1881f61cdc467/C300.batch_execution.141d313c25b2e48de670600e82496debde94040ee86bbc00c518b366c439fc27.json",
      "file_bytes_sha256": "141d313c25b2e48de670600e82496debde94040ee86bbc00c518b366c439fc27"
    },
    "frozen_review": {
      "file_bytes_sha256": "ace247f2e0a0d32c9bbae14c5a772bea64ef8fabdbaeb1b5f8a1e9fefc5afbf7",
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_action14_batch_v1/C299.frozen_batch_review.ace247f2e0a0d32c9bbae14c5a772bea64ef8fabdbaeb1b5f8a1e9fefc5afbf7.json"
    }
  },
  "completion_scope": "EXECUTION_OF_SOURCE_BOUND_FIXED_ASSERTION_AND_FIXED_REQUIREMENT_DIAGNOSTICS",
  "ready_scenario_count": 104,
  "matching_frozen_expectation_count": 104,
  "family_counts": {
    "COMPLETE_COVERAGE": 8,
    "LITERAL_QUOTE_PAIR": 22,
    "PARTIAL_COVERAGE": 8,
    "POSITIVE_SUPPORT": 22,
    "REVERSED_ASSERTION": 22,
    "WRONG_EVIDENCE": 22
  },
  "saved_semantic_responses_bound": 82,
  "held_scenario_count": 16,
  "held_scenarios_reclassified_as_pass": false,
  "original_120_scenario_plan_fully_passed": false,
  "diagnostic_references_origin": "ASSISTANT_SOURCE_ONLY_REVIEW_BEFORE_EVALUATOR_DISPATCH",
  "independent_expert_or_population_gold": false,
  "historical_tariff_estimate_for_C300_toman": 8032.271519999999,
  "actual_invoice_cost_verified": false,
  "remaining_method_scope_decisions": [
    "Official metric applicability and population coverage.",
    "Qualification of free assertion extraction and reference necessity.",
    "Semantic citation and attribution coverage.",
    "Independent reviewer requirements."
  ],
  "action_14_test_execution_complete": true,
  "action_14_eligible_for_checkmark": true,
  "action_15_eligible_for_checkmark": false,
  "population_method_accepted": false,
  "population_accuracy_estimated": false,
  "next_checklist_action": 15,
  "network_requests": 0,
  "paid_api_calls": 0,
  "previous_outputs_modified": false,
  "golden_dataset_modified": false,
  "checklist_file_updated": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C301.diagnostic_round_closure.2142c9ec320745ed3720b5313c3fc48d4b544b60c7c42f3fe174a82ba9718e56.json",
    "file_bytes_sha256": "2142c9ec320745ed3720b5313c3fc48d4b544b60c7c42f3fe174a82ba9718e56",
    "bytes": 6828,
    "action": "CREATED",
    "reload_validation": "PASS"
  }
}
```

## محدودیت و مصرف درست

مرجع تشخیصی، بازبینی دستیار پیش از Dispatch است؛ Human Gold مستقل یا برآورد دقت جمعیت نیست. ۱۶ HOLD هرگز PASS نشده‌اند.

برآورد تعرفهٔ تاریخی C300 در C301 حدود ۸٬۰۳۲ تومان است؛ هزینهٔ واقعی صورتحساب تأیید نشده. صفر API سل C301، اجرای معنایی پیشین C300 را صفر نمی‌کند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action14_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
