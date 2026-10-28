# گزارش اقدام 25 — Attribution و نقش‌ها

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `USER_ACCEPTED_SCOPED_COMPLETION`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** **[پایان این دور با پذیرش محدود کاربر؛ کیفیت کامل تأیید نشده]** سنجش Attribution correctness برای نویسندهٔ مستقیم، نویسندهٔ واقعی مقالهٔ سردبیری، نقش سردبیر و گویندهٔ واقعی.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**گزارش موجود در مخزن:** [reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md).

## کار انجام‌شده و نتیجه

کنترل عملیاتی نقش و فراداده در ۲۵۶۰ پاسخ و ۸۰۰۷۹ وقوع فیلد نقش موجود است: ۲۰۰۳۰ تطابق نقش عملیاتی، ۴۰۵۷۳ تطابق نام گویندهٔ کانونی، ۱۱۸۱۷ برچسب منبع بدون اثبات هویت و ۷۶۵۹ حفظ عدم‌قطعیت گوینده. C113 در بستهٔ ۲۳پاسخی انتساب صریح نثر نداشت؛ مخرج صحت انتساب صریح صفر است، نه امتیاز۱۰۰٪.

پایان این دور با درخواست صریح کاربر و محدودیت‌های گزارش مشترک پذیرفته شده است؛ پذیرش کامل معنایی، Human Gold مستقل یا Release نتیجه نمی‌شود.

## شواهد، سل و مسیر خروجی

### NB21B.C105

پیوست گزارش مشترک، سل فیزیکی 226 در Snapshot مبنای آن گزارش:

```json
{
  "status": "ANSWER_LEVEL_OPERATIONAL_ATTRIBUTION_RESULTS_SAVED",
  "development_queries": 2664,
  "answer_disposition_counts": {
    "STRUCTURED_DISPLAY_LAYER_UNRESOLVED": 58,
    "NO_SELECTED_ANSWER_NOT_SCORED": 46,
    "OPERATIONAL_ROLE_REPRODUCTION_CHECKS_AVAILABLE": 2560
  },
  "role_field_occurrence_count": 80079,
  "role_field_status_counts": {
    "SOURCE_LABEL_PRESERVED_PERSON_IDENTITY_NOT_ESTABLISHED": 11817,
    "CANONICAL_SPEAKER_NAME_EXACT_MATCH": 40573,
    "SOURCE_SPEAKER_UNCERTAINTY_PRESERVED": 7659,
    "OPERATIONAL_ROLE_FIELD_EXACT_MATCH": 20030
  },
  "role_status_by_source_type": {
    "book": {
      "OPERATIONAL_ROLE_FIELD_EXACT_MATCH": 11558
    },
    "transcript": {
      "SOURCE_LABEL_PRESERVED_PERSON_IDENTITY_NOT_ESTABLISHED": 11817,
      "CANONICAL_SPEAKER_NAME_EXACT_MATCH": 40573,
      "SOURCE_SPEAKER_UNCERTAINTY_PRESERVED": 7659
    },
    "website": {
      "OPERATIONAL_ROLE_FIELD_EXACT_MATCH": 8472
    }
  },
  "formal_attribution_correctness_score": null,
  "new_api_calls": 0,
  "raw_source_checks_repeated": false,
  "actions_22_to_25_complete": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C105.operational_attribution_results.97c2c9c18525ea9b198592e21171a3b5d02dc66308ced12d2d77b1d97ad6934e.json",
    "file_bytes_sha256": "97c2c9c18525ea9b198592e21171a3b5d02dc66308ced12d2d77b1d97ad6934e",
    "reload_validation": "PASS"
  }
}
```

### NB21B.C108

پیوست گزارش مشترک، سل فیزیکی 232 در Snapshot مبنای آن گزارش:

```json
{
  "status": "REQUIRED_STRUCTURED_ATTRIBUTION_PRESENCE_CHECKS_SAVED",
  "development_queries": 2664,
  "structured_citation_count": 12178,
  "member_occurrence_count": 76134,
  "member_status_counts": {
    "SOURCE_LABEL_PRESENT_IDENTITY_UNESTABLISHED": 11817,
    "CANONICAL_SPEAKER_VALUE_PRESENT": 40573,
    "SPEAKER_STATUS_PRESENT_IDENTITY_UNRESOLVED": 7659,
    "REQUIRED_ROLE_VALUES_PRESENT": 16085
  },
  "citation_member_structure_issue_counts": {},
  "answer_disposition_counts": {
    "STRUCTURED_DISPLAY_LAYER_UNRESOLVED": 58,
    "NO_SELECTED_ANSWER_NOT_SCORED": 46,
    "REQUIRED_DISPLAY_PRESENCE_CHECKS_AVAILABLE": 2560
  },
  "formal_attribution_correctness_score": null,
  "new_api_calls": 0,
  "raw_source_checks_repeated": false,
  "actions_22_to_25_complete": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C108.required_attribution_display.37bc6c0cb1fd4aa97de4f0d520632e04f15c98e94559a2eeaf12674988ae30cd.json",
    "file_bytes_sha256": "37bc6c0cb1fd4aa97de4f0d520632e04f15c98e94559a2eeaf12674988ae30cd",
    "reload_validation": "PASS"
  }
}
```

### NB21B.C233

پیوست گزارش مشترک، سل فیزیکی 482 در Snapshot مبنای آن گزارش:

```json
{
  "status": "C233_ACTION25_OFFLINE_AUDIT_ACCOUNTED",
  "action": 25,
  "population_cases": 2117,
  "case_states": {
    "INPUT_OR_EVIDENCE_HELD": 17,
    "ATTRIBUTION_CANDIDATES_REQUIRE_ROLE_VERIFICATION": 47,
    "NO_ATTRIBUTION_CUE_DETECTED_NOT_A_SEMANTIC_PASS": 2053
  },
  "input_error_counts": {
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_058eebd08a5d4cc1bacd95aa/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_06a2225ff7a4b410c1c6dda5/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_120452115973764bb3ee511e/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_2368cf0eac9bd1b2936daa2f/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_5604a5f800bb5f8ceb4fe2a7/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_56e42e3dfbdf2216e07151eb/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_6015394a513d9f3c57f87639/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_7d7120273acc70fe4d0ebb63/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_92bfcefe7a81a564423221e3/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_9536f6c35f2cea0bd008360f/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_a201c77b9345ceeb6c27dc20/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_a8016c689eb93dec5cdd52d0/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_b6433cb9d46ef3e140e84172/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_ca73b8c3239c8a64ab9b30ae/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_dae163bb9c064df98bc6c818/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_e352137e9b8a7b1d19163907/input.json'": 1,
    "[Errno 2] No such file or directory: 'artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_e55ff4e72277971020197b0a/input.json'": 1
  },
  "answer_unit_literal_evidence_counts": {},
  "explicit_locator_counts": {},
  "attribution_candidate_units": 52,
  "semantic_metric": null,
  "semantic_acceptance_established": false,
  "execution_accounting_complete": true,
  "action_closed": false,
  "closure_status": "OFFLINE_CHECKS_COMPLETE_SEMANTIC_ACCEPTANCE_OPEN",
  "new_api_calls": 0,
  "new_cost": "0 تومان",
  "old_files_modified": false,
  "old_results_relabelled": false,
  "details_path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C233.action25_offline_audit/3c35294b251d7767641fe389598fa00f01f4954fa0dbd1032b601a09747fd2d1/C233_case_results.json",
  "details_sha256": "c4877d5f3ab3237bbd0e2264fc7cb3331552eaaabb828d6d8ec5f859a5417e44",
  "remaining_verification_queue_path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C233.action25_offline_audit/3c35294b251d7767641fe389598fa00f01f4954fa0dbd1032b601a09747fd2d1/C233_remaining_verification_queue.json",
  "remaining_verification_queue_is_not_automatic_API_dispatch": true,
  "engine_sha256": "e87d6d8ee5efc8063076b89f0b1489697af664dad4a6645187e62038bed44ff3",
  "artifact_path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C233.action25_offline_audit/3c35294b251d7767641fe389598fa00f01f4954fa0dbd1032b601a09747fd2d1/report.e69a8537735e4eb678394f209ef8f3934f4b0fe00a4261af70c40230392dc535.json",
  "artifact_sha256": "e69a8537735e4eb678394f209ef8f3934f4b0fe00a4261af70c40230392dc535",
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

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action25_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
