# گزارش اقدام 17 — Smoke و Pilot

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** Smoke و Pilot کوچک Development برای Metric، اتصال شناسه، denominator، Missing، Resume و Cache؛ اصلاح همان مرحله در صورت FAIL.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

در C303، Pilot مستقل ۱۲ ردیفی و کنترل‌های Smoke پاس شده‌اند؛ سپس Resume مستقل کل ۲۶۶۴ ردیف را پوشش داده است. تمام فازها یک هویت Engine دارند، پوشش strata مشاهده‌شده و شمارش Missing کنترل شده و وابستگی به Kernel قبلی حذف شده است.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C303.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C303 — سل فیزیکی 608

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "schema_version": "nb21_engine_package_C303_v1",
  "status": "NB21_BOUND_INPUT_ENGINE_PACKAGE_TECHNICAL_PASS",
  "checklist_actions": [
    16,
    17,
    18
  ],
  "checklist_action_total": 49,
  "completion_scope": "TECHNICAL_READ_JOIN_AND_CACHE_HANDLING_OF_BOUND_DEVELOPMENT_INPUTS_WITH_EXPLICIT_MISSING_AND_BLOCKED_STATES",
  "checks": {
    "all_phases_same_engine_identity": true,
    "pilot_covers_observed_strata": true,
    "full_development_join": true,
    "resume_accounts_for_every_row": true,
    "replay_writes_zero_rows": true,
    "replay_reuses_every_row": true,
    "replay_row_index_identical": true,
    "answer_partition_preserved": true,
    "all_smoke_checks_pass": true,
    "all_phases_kernel_independent": true,
    "no_network_or_paid_calls": true
  },
  "development_query_count": 2664,
  "answer_available_count": 2618,
  "answer_missing_count": 46,
  "citation_count": 10532,
  "retrieval_arm_count": 5,
  "pilot_query_count": 12,
  "phase_artifacts": {
    "pilot": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_engine_rows_C303_v1/ff878700247047117b087bf118ab06dad6e1c30ce69da92dfec693c411d6694e/phase_report.7fabf87261b51d99478066382e3a33af905b7b897bccd53afb6ee306d998788e.json",
      "file_bytes_sha256": "7fabf87261b51d99478066382e3a33af905b7b897bccd53afb6ee306d998788e"
    },
    "resume": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_engine_rows_C303_v1/ff878700247047117b087bf118ab06dad6e1c30ce69da92dfec693c411d6694e/phase_report.081641bb469570beb0e2c86f2ea8087b0bc945202be2cf17bbc54e646b39fa21.json",
      "file_bytes_sha256": "081641bb469570beb0e2c86f2ea8087b0bc945202be2cf17bbc54e646b39fa21"
    },
    "replay": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_engine_rows_C303_v1/ff878700247047117b087bf118ab06dad6e1c30ce69da92dfec693c411d6694e/phase_report.41bb0254e35b4ff02fdf5066d9d67f10ea8739e9ee128c101c294badd57bc8aa.json",
      "file_bytes_sha256": "41bb0254e35b4ff02fdf5066d9d67f10ea8739e9ee128c101c294badd57bc8aa"
    }
  },
  "row_index_binding": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_engine_rows_C303_v1/ff878700247047117b087bf118ab06dad6e1c30ce69da92dfec693c411d6694e/row_index.74794942c8043ae2cfa6daedcca5aba4a0c3e865dcd7bae5e4fdf3f95d562a03.json",
    "file_bytes_sha256": "74794942c8043ae2cfa6daedcca5aba4a0c3e865dcd7bae5e4fdf3f95d562a03"
  },
  "implementation_binding": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_cache_only_engine_C303_v1/C303.engine.6949b823367f64e8a2ca24e541d0f08a097b3bf0da87bb0e29ee4aec8678ee09.py",
    "file_bytes_sha256": "6949b823367f64e8a2ca24e541d0f08a097b3bf0da87bb0e29ee4aec8678ee09"
  },
  "manifest_binding": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_cache_only_engine_C303_v1/C303.manifest.b2d8f6adcee80a25cf17d4c0f9e5cf47d1681b66d3ea2775bc4ab99bb07182f5.json",
    "file_bytes_sha256": "b2d8f6adcee80a25cf17d4c0f9e5cf47d1681b66d3ea2775bc4ab99bb07182f5"
  },
  "remaining_upstream_gaps": [
    "46 frozen-core queries lack selected bound answer text.",
    "No Development Policy/Confidence run is selected.",
    "Official population semantic metrics remain unqualified.",
    "Claim/citation identity joins do not establish alignment to the selected answer text or semantic correctness."
  ],
  "actions_eligible_for_checkmark": {
    "16": true,
    "17": true,
    "18": true
  },
  "official_semantic_evaluation_complete": false,
  "population_method_accepted": false,
  "new_retrieval_or_per_query_metric_execution": false,
  "network_requests": 0,
  "paid_api_calls": 0,
  "evidence_code_executed": false,
  "golden_dataset_modified": false,
  "checklist_file_updated": false,
  "fresh_test_evaluation_performed": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C303.engine_package.63a75c45bc05c46a418d475110d80f039a1b818c9c901840b779855babac828d.json",
    "file_bytes_sha256": "63a75c45bc05c46a418d475110d80f039a1b818c9c901840b779855babac828d",
    "bytes": 3449,
    "reload_validation": "PASS"
  }
}
```

## محدودیت و مصرف درست

پایلوت فنی و آزمون Kernel، اعتبار معنایی داور و کیفیت پاسخ را اثبات نمی‌کنند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action17_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
