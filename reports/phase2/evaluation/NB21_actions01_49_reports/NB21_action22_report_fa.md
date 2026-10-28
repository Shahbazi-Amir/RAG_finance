# گزارش اقدام 22 — Groundedness پاسخ

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `USER_ACCEPTED_SCOPED_COMPLETION`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** **[پایان این دور با پذیرش محدود کاربر؛ کیفیت کامل تأیید نشده]** سنجش Groundedness پاسخ و Claimها با روش معتبر اقدام ۱۵.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**گزارش موجود در مخزن:** [reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md).

## کار انجام‌شده و نتیجه

C122/C123، ۶۶۰۵ Claim در ۲۵۶۰ پاسخ را با آرای ذخیره‌شده ۶۱۷۲ Supported، ۲۵۵ Partial، ۱۰۳ Unsupported و ۷۵ Uncertain ثبت کرده‌اند. تنها ۱۰۴۴ واحد در ۸۱۹ پاسخ در روش بررسی‌شده هم اتصال لفظی یکتا و هم اتصال Context داشته‌اند. C111 برای بستهٔ مستقیم ۲۳پاسخی/۱۲۵ادعا: ۱۰۳ پشتیبانی‌شده، ۲۰ بدون پشتیبانی، یک متعارض و یک بررسی‌نشده. B05 محفوظ است.

پایان این دور با درخواست صریح کاربر و محدودیت‌های گزارش مشترک پذیرفته شده است؛ پذیرش کامل معنایی، Human Gold مستقل یا Release نتیجه نمی‌شود.

## شواهد، سل و مسیر خروجی

### NB21B.C111

پیوست گزارش مشترک، سل فیزیکی 240 در Snapshot مبنای آن گزارش:

```json
{
  "status": "SCOPED_REVIEWED_GROUNDING_LEDGER_MERGED",
  "answer_case_count": 23,
  "claim_count": 125,
  "effective_verdict_counts": {
    "SUPPORTED": 103,
    "NOT_SUPPORTED": 20,
    "NOT_ASSESSED": 1,
    "CONTRADICTED": 1
  },
  "overlaid_claim_count": 30,
  "reused_C107_decision_count": 95,
  "reviewed_citation_support_conflict_count": 0,
  "remaining_not_assessed_claim_ids": [
    "golden_v2_candidate_4b3dbd833a57bbc16b7bc6e6:A001"
  ],
  "not_assessed_scored_as_zero": false,
  "B05_effective_verdict": "CONTRADICTED",
  "formal_groundedness_score": null,
  "population_extrapolation": false,
  "new_api_calls": 0,
  "actions_22_to_25_complete": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C111.merged_reviewed_grounding.581f6ccb33fda2b5ceffdd5046b80969922e722995abf1497c49a0af23193e0b.json",
    "file_bytes_sha256": "581f6ccb33fda2b5ceffdd5046b80969922e722995abf1497c49a0af23193e0b",
    "reload_validation": "PASS"
  }
}
```

### NB21B.C122

پیوست گزارش مشترک، سل فیزیکی 262 در Snapshot مبنای آن گزارش:

```json
{
  "status": "BOUND_VERIFIER_AND_SUPPORT_MATERIALS_CONNECTED",
  "development_queries": 2664,
  "case_status_counts": {
    "PREVIOUSLY_UNRESOLVED_CHAIN_PRESERVED": 58,
    "NO_SELECTED_ANSWER_NOT_SCORED": 46,
    "CURRENT_ANSWER_AND_STORED_VERIFIER_CHAIN_LINKED": 2560
  },
  "C120_53_case_status_counts": {
    "CURRENT_ANSWER_AND_STORED_VERIFIER_CHAIN_LINKED": 50,
    "PREVIOUSLY_UNRESOLVED_CHAIN_PRESERVED": 3
  },
  "linked_checkpoint_claim_count": 6605,
  "linked_checkpoint_citation_count": 12178,
  "answers_with_linked_raw_support": 2549,
  "chain_recheck_error_count": 0,
  "chain_recheck_error_examples": [],
  "historical_model_verdicts_preserved": true,
  "semantic_acceptance_changed": false,
  "broad_project_rescan": false,
  "new_api_calls": 0,
  "actions_22_to_25_complete": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C122.bound_verifier_reuse.c8758caf3c9ba94b6ee971a39505ab0269a56ff6c7e02b4cd07a6e6a0c502258.json",
    "file_bytes_sha256": "c8758caf3c9ba94b6ee971a39505ab0269a56ff6c7e02b4cd07a6e6a0c502258",
    "reload_validation": "PASS"
  }
}
```

### NB21B.C123

پیوست گزارش مشترک، سل فیزیکی 264 در Snapshot مبنای آن گزارش:

```json
{
  "status": "STORED_MODEL_DECISIONS_CONSUMED_WITH_ALIGNMENT_LIMITS",
  "development_queries": 2664,
  "answer_status_counts": {
    "PREVIOUSLY_UNRESOLVED_CHAIN_PRESERVED": 58,
    "NO_SELECTED_ANSWER_NOT_SCORED": 46,
    "STORED_MODEL_DECISIONS_CONSUMED_WITH_SCOPE": 2560
  },
  "consumed_checkpoint_claim_count": 6605,
  "stored_model_verdict_counts": {
    "SUPPORTED": 6172,
    "PARTIALLY_SUPPORTED": 255,
    "UNSUPPORTED": 103,
    "UNCERTAIN": 75
  },
  "claim_route_counts": {
    "STORED_MODEL_DECISION_BOTH_BINDINGS_PENDING": 141,
    "STORED_MODEL_DECISION_CONTEXT_BINDING_PENDING": 22,
    "MODEL_ESTIMATE_LITERAL_UNIT_CONTEXT_BOUND": 1044,
    "STORED_MODEL_DECISION_ANSWER_ALIGNMENT_PENDING": 5398
  },
  "literal_context_bound_model_verdict_counts": {
    "SUPPORTED": 965,
    "PARTIALLY_SUPPORTED": 42,
    "UNCERTAIN": 14,
    "UNSUPPORTED": 23
  },
  "answers_with_literal_context_bound_units": 819,
  "declared_citation_pair_counts": {
    "EVIDENCE_SELECTED_BY_STORED_SUPPORT": 10746,
    "EVIDENCE_NOT_SELECTED_BY_STORED_SUPPORT": 1432
  },
  "raw_derived_status_difference_count": 34,
  "raw_support_not_parsed_case_count": 11,
  "reviewed_decisions_overwritten": false,
  "new_api_calls": 0,
  "broad_project_rescan": false,
  "actions_22_to_25_complete": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C123.consumed_model_decisions.901511ebff2f8c7c3472639705a749c0740646f8444369d522862a03a578177a.json",
    "file_bytes_sha256": "901511ebff2f8c7c3472639705a749c0740646f8444369d522862a03a578177a",
    "reload_validation": "PASS"
  }
}
```

## محدودیت و مصرف درست

حدود گزارش مرجع و مخرج‌ها حفظ شوند. شمار پوشش، درصد صحت یا درصد زمان انجام کار نیست. رأی مدل و بازبینی دستیار، خودکار مرجع مستقل انسانی محسوب نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action22_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
