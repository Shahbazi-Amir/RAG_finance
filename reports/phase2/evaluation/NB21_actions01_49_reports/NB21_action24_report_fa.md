# گزارش اقدام 24 — Citation و پوشش ادعا

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `USER_ACCEPTED_SCOPED_COMPLETION`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** **[پایان این دور با پذیرش محدود کاربر؛ کیفیت کامل تأیید نشده]** سنجش Citation correctness، Claim coverage و locator validity؛ تفکیک اتصال ساختاری از پشتیبانی معنایی.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**گزارش موجود در مخزن:** [reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md).

## کار انجام‌شده و نتیجه

۱۲۱۷۸ Citation ساختاریافته در ۲۵۶۰ پاسخ ثبت شده است. C106 در بستهٔ محدود، ۱۷۹ رابطه با ۱۳۶ Entails، ۴۲ Insufficient و یک Contradicts دارد. C112 از ۱۲۴ واحد نیازمند استناد: ۸۴ اتصال و شاهد کافی، ۲۴ اتصال با شاهد ناکافی، ۱۳ نامعین و سه فاقد اتصال در موجودی بررسی‌شده. نبود نشانگر inline در answer_text لایهٔ ساختاری Citation را نفی نمی‌کند.

پایان این دور با درخواست صریح کاربر و محدودیت‌های گزارش مشترک پذیرفته شده است؛ پذیرش کامل معنایی، Human Gold مستقل یا Release نتیجه نمی‌شود.

## شواهد، سل و مسیر خروجی

### NB21B.C106

پیوست گزارش مشترک، سل فیزیکی 228 در Snapshot مبنای آن گزارش:

```json
{
  "status": "DIRECT_CITATION_AND_SCOPED_GROUNDING_REVIEW_IMPORTED",
  "B05_effective_verdict_preserved": "CONTRADICTED",
  "actions_22_to_25_complete": false,
  "answer_case_count": 23,
  "claims_with_reviewed_entailed_declared_citation": 84,
  "current_claim_count": 125,
  "current_mapping_disposition_counts": {
    "CONNECTION_ABSENCE_PROVEN_IN_CHECKED_DECLARED_CLAIM_INVENTORY": 3,
    "CONNECTION_PROVEN_IN_STORED_CHECKPOINT_SCOPE": 108,
    "INDETERMINATE": 14
  },
  "direct_grounding_support_decisions_added": 10,
  "exact_prior_review_reuse_pair_count": 5,
  "formal_citation_correctness_score": null,
  "initial_31_mapping_disposition_counts": {
    "CONNECTION_ABSENCE_PROVEN_IN_CHECKED_DECLARED_CLAIM_INVENTORY": 3,
    "CONNECTION_PROVEN_IN_STORED_CHECKPOINT_SCOPE": 19,
    "INDETERMINATE": 9
  },
  "new_alignment_claim_count": 19,
  "new_api_calls": 0,
  "original_proposed_pair_review_count": 144,
  "prior_model_mapped_claims_not_accepted_for_full_scope": 5,
  "reviewed_pair_count_including_new_alignments": 179,
  "reviewed_pair_relation_counts": {
    "CONTRADICTS": 1,
    "ENTAILS": 136,
    "INSUFFICIENT": 42
  },
  "review_origin": "DIRECT_PROJECT_ASSISTANT_REVIEW",
  "independent_human_gold": false,
  "historical_verdict_files_modified": false,
  "population_extrapolation": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C106.direct_citation_review.944d79569ec75d1c46922854982cf5057985a6b9a4db259e3e5bbb13fb2c6501.json",
    "file_bytes_sha256": "944d79569ec75d1c46922854982cf5057985a6b9a4db259e3e5bbb13fb2c6501",
    "reload_validation": "PASS"
  }
}
```

### NB21B.C112

پیوست گزارش مشترک، سل فیزیکی 242 در Snapshot مبنای آن گزارش:

```json
{
  "status": "SCOPED_CITATION_REQUIREDNESS_AND_COVERAGE_REVIEWED",
  "answer_case_count": 23,
  "inventory_unit_count": 125,
  "required_citation_unit_count": 124,
  "non_separate_framing_unit_count": 1,
  "required_citation_coverage_counts": {
    "STORED_CONNECTION_WITH_SUFFICIENT_REVIEWED_EVIDENCE": 84,
    "CONNECTION_INDETERMINATE": 13,
    "STORED_CONNECTION_WITHOUT_SUFFICIENT_REVIEWED_EVIDENCE": 24,
    "CONNECTION_ABSENT_IN_CHECKED_DECLARED_INVENTORY": 3
  },
  "formal_citation_correctness_score": null,
  "formal_citation_completeness_score": null,
  "population_extrapolation": false,
  "new_api_calls": 0,
  "actions_22_to_25_complete": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C112.scoped_citation_coverage.63b4501f57d2f7c4944be46955dc44aca74632502d1741129ab7b4f19b0d366c.json",
    "file_bytes_sha256": "63b4501f57d2f7c4944be46955dc44aca74632502d1741129ab7b4f19b0d366c",
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

## محدودیت و مصرف درست

حدود گزارش مرجع و مخرج‌ها حفظ شوند. شمار پوشش، درصد صحت یا درصد زمان انجام کار نیست. رأی مدل و بازبینی دستیار، خودکار مرجع مستقل انسانی محسوب نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action24_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
