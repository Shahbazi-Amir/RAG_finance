<div dir="rtl" align="right">

# تعیین تکلیف تجمیعی اقدامات ۲۲ تا ۲۵ — NB21

تاریخ: ۲۶ اکتبر ۲۰۲۶. مبنا: کد و خروجی ذخیره‌شدهٔ هر دو نوت‌بوک در شاخهٔ rag-phase2، Commit: `679b753f27f6d6ce11629609acbfdf3df248b0bc`.

این گزارش بازخوانی کد و خروجی‌های پوش‌شده است؛ اجرای دوبارهٔ API، دسترسی به تمام Artifactهای محلی مک، یا تأیید مستقل آرای مدل نیست. فایل‌های شواهد محلی که در خروجی نوت‌بوک نام برده شده‌اند، صرف نام‌بردن دوباره اعتبارسنجی نشده‌اند.

## اصلاح نتیجه‌گیری قبلی

اقدامات ۲۲، ۲۴ و ۲۵ از صفر نیستند. گزارش‌های C231 تا C233 فقط غربالگری محدود بودند و نباید جای نتایج معنایی و ساختاری قبلی قرار گیرند. خصوصاً نبود استناد در متن answer_text، با نبود Citation ساختاریافته برابر نیست.

## دامنه‌ها

- Development کامل: ۲۶۶۴ پرسش.
- ۲۵۶۰ پاسخ دارای اتصال زنجیرهٔ تولید و Citation؛ ۵۸ اتصال حل‌نشده؛ ۴۶ پاسخ منتخب مفقود در دفتر تاریخی.
- صف اجرای Completeness اخیر: ۲۱۱۷ پرونده، زیرجمعیت؛ برابر کل Development نیست.
- بستهٔ مستقیم تشخیصی: ۲۳ پاسخ با ۱۲۵ ادعا. مخرج ادعا، رابطهٔ استناد، نقش و پرونده قابل جایگزینی با هم نیستند.

## اقدام ۲۲ — پشتیبانی پاسخ از منبع

شاهد جمعیتی C122/C123: ۶۶۰۵ ادعای Checkpoint در ۲۵۶۰ پاسخ مصرف شده‌اند. آرای ذخیره‌شدهٔ مدل: ۶۱۷۲ SUPPORTED، ۲۵۵ PARTIALLY_SUPPORTED، ۱۰۳ UNSUPPORTED و ۷۵ UNCERTAIN.

از این تعداد، ۱۰۴۴ واحد در ۸۱۹ پاسخ هم اتصال لفظی یکتا به پاسخ و هم اتصال Context تولید داشته‌اند: ۹۶۵ پشتیبانی‌شده، ۴۲ جزئی، ۲۳ بدون پشتیبانی و ۱۴ نامعین. برای ۵۳۹۸ واحد اتصال معنایی به پاسخ هنوز در این روش اثبات نشده؛ ۲۲ واحد اتصال Context می‌خواهند و ۱۴۱ واحد هر دو اتصال را. نبود تطابق لفظی به‌تنهایی خطای استخراج نیست.

شاهد بازبینی مستقیم C111 در بستهٔ ۲۳پاسخی: ۱۰۳ ادعا پشتیبانی‌شده، ۲۰ بدون پشتیبانی، یک متعارض و یک بررسی‌نشده. نتیجهٔ C107 قدیمی‌تر است و نباید جای جمع‌بندی C111 استفاده شود. تعارض B05 حفظ می‌شود.

تعیین تکلیف: ارزیابی تاریخی مدل موجود و قابل گزارش با محدودیت اتصال؛ امتیاز صحت کل پاسخ‌های جمعیت ثابت نشده است. آزمون روش از ابتدا تکرار نشود.

## اقدام ۲۳ — کفایت پاسخ

آخرین دفتر C230 از ۲۱۱۷ پرونده: ۱۰۷۳ نتیجهٔ مثبت قبلی بازبینی‌نشده، ۳۲۲ پذیرفته‌شده با معیار جدید، ۹۳ نقص طبق مدل، ۱۴ سؤال مبهم، ۲ مورد شواهد ناکافی، یک نیازمند بررسی، ۱۷ ورودی در دسترس نیست، ۵۹۵ خروجی داور جدید غیرقابل‌مصرف.

۱۳۹۵ نتیجهٔ مثبت، ۶۵٫۹٪ این صف است؛ دقت جمعیت نیست و معیارهای قدیم/جدید یکسان نبوده‌اند. خروجی ناموفق داور به معنای پاسخ غلط نیست؛ سوابق پیشین آن موارد محفوظ است. نمونهٔ انسانی بیست‌تایی و اصلاح معیار، تأیید انسانی تمام جمعیت نیست.

تعیین تکلیف: دور اجرا و بازیابی ثبت شده؛ ارسال مجدد عمومی یا پرامپت‌آزمایی تازه از این گزارش نتیجه نمی‌شود. محدودیت اعتبار ارزیاب همراه نتیجه باقی می‌ماند.

## اقدام ۲۴ — استناد

C122 تعداد ۱۲۱۷۸ Citation ساختاریافته را در ۲۵۶۰ پاسخ متصل ثبت کرده است. نتیجهٔ C232 دربارهٔ نبود نشانگر داخل متن پاسخ، این Citationها را نفی نمی‌کند.

C106 در بستهٔ ۲۳پاسخی، ۱۷۹ رابطهٔ بررسی‌شده دارد: ۱۳۶ ENTAILS، ۴۲ INSUFFICIENT و یک CONTRADICTS. شمار اتصال ادعاهای جاری: ۱۰۸ مشخص، ۱۴ نامعین و سه فاقد متناظر در فهرست بررسی‌شده.

C112 از ۱۲۵ واحد، ۱۲۴ واحد را نیازمند استناد شمرده: ۸۴ دارای اتصال و شاهد کافی، ۲۴ دارای اتصال با شاهد ناکافی، ۱۳ اتصال نامعین و سه فاقد اتصال در موجودی بررسی‌شده. یک واحد چارچوب‌بندی جداگانه نیازمند استناد مستقل نبوده است.

تعیین تکلیف: اتصال ساختاری جمعیتی و ارزیابی معنایی محدود موجود است؛ ۱۷۹ رابطه را به ۱۲۱۷۸ Citation تعمیم نمی‌دهیم. صحت معنایی کل جمعیت هنوز ثابت نشده است.

## اقدام ۲۵ — انتساب

C105/C108 پیش از غربالگری C233، کنترل عملیاتی نقش‌ها را در ۲۵۶۰ پاسخ ثبت کرده‌اند: ۸۰۰۷۹ وقوع فیلد نقش، شامل ۲۰۰۳۰ تطابق فیلد عملیاتی، ۴۰۵۷۳ تطابق نام گویندهٔ کانونی، ۱۱۸۱۷ برچسب منبع بدون اثبات هویت و ۷۶۵۹ مورد حفظ عدم‌قطعیت گوینده.

این‌ها تعداد اشخاص یا پرونده‌های مستقل نیستند. C090 تعداد ۶۹۰ جفت مسیر/هش منبع و ۷۶۱۳۴ وقوع فراداده را کنترل کرده است؛ تطابق با فراداده جای تأیید مستقل هویت واقعی نیست.

در بستهٔ تشخیصی C113، ۲۳ پاسخ انتساب صریح منبع در نثر نداشتند؛ مخرج صحت انتساب صریح صفر است، نه امتیاز ۱۰۰٪. C233 در صف ۲۱۱۷تایی، ۵۲ قطعه در ۴۷ پرونده را با نشانهٔ لفظی پیدا کرده؛ این غربالگری تمام انتساب‌های ضمنی را پوشش نمی‌دهد.

تعیین تکلیف: بازتولید نقش/فراداده بررسی شده؛ صحت هویت واقعی و انتساب صریح کل پاسخ‌ها پذیرفته نشده است. شروع دوباره از صفر توجیه ندارد.

## تصمیم اجرایی مشترک

- گزارش‌های تاریخی بالا مرجع باشند؛ C231–C233 آن‌ها را جایگزین نکنند.
- این دورِ جمع‌آوری و جمع‌بندی بسته‌بندی شود؛ هیچ API تازه‌ای اجرا نشده و در این گزارش مجوز ارسال جدید ایجاد نمی‌شود.
- اصلاح پاسخ یا بهبود کیفیت، کار جداگانه است؛ شکست ارزیاب یا محدودیت پوشش به‌عنوان خطای پاسخ شمرده نشود.
- وضعیت بسته: «نتایج موجود تجمیع و محدودیت‌ها ثبت شد؛ پذیرش کامل معنایی باز است». این عنوان چهار تیک PASS نیست.
- کارهای مستقل بعدی NB21 قابل ادامه‌اند؛ Release نهایی باید این محدودیت‌ها را در Gate خود ببیند. این گزارش چک‌لیست مخزن را تغییر نداده است.

## منشأ قابل بازخوانی

- [21_evaluation_and_ablation.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/679b753f27f6d6ce11629609acbfdf3df248b0bc/notebooks/phase2/21_evaluation_and_ablation.ipynb) — Git blob `4405d634de02e8e95df717a4f727bade2ea730e7`، SHA256 `1a0a006922ca8698af77b29f959a5c0eb3edb76881c8f2627a9b258da9352a94`.
- [21b_evaluation_and_ablation_continued.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/679b753f27f6d6ce11629609acbfdf3df248b0bc/notebooks/phase2/21b_evaluation_and_ablation_continued.ipynb) — Git blob `d41877ae9d39132f88153295a2449720f99b7da6`، SHA256 `d4d40bb241e26704db30f3dfb69b1b44ce2a23371935c52782d6aa51b00fd84c`.

## پیوست: خلاصه‌های اصلیِ استخراج‌شده از خروجی نوت‌بوک

</div>

```json
{
  "C105": {
    "notebook_cell_1based": 226,
    "report": {
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
  },
  "C106": {
    "notebook_cell_1based": 228,
    "report": {
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
  },
  "C108": {
    "notebook_cell_1based": 232,
    "report": {
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
  },
  "C111": {
    "notebook_cell_1based": 240,
    "report": {
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
  },
  "C112": {
    "notebook_cell_1based": 242,
    "report": {
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
  },
  "C122": {
    "notebook_cell_1based": 262,
    "report": {
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
  },
  "C123": {
    "notebook_cell_1based": 264,
    "report": {
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
  },
  "C228": {
    "notebook_cell_1based": 472,
    "report": {
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
      "artifact_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C228.semantic_sufficiency_remaining1044/93b8738ed74a8408b09e1ee0798e4e29de984ac396ac00945963f06656d51056/report.05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc.json",
      "artifact_sha256": "05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc",
      "reload_validation": "PASS"
    }
  },
  "C230": {
    "notebook_cell_1based": 476,
    "report": {
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
      "recovery_records_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C230.offline_judge_output_recovery/05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc/C230_recovery_records.json",
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
      "artifact_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C230.offline_judge_output_recovery/05481414b6a9d67044a2395392094243695ea665fe9302e28c5bc7202ba878fc/report.264259ac134341058684f59ccee427881d722235372402fe2dc2eca0f3976c14.json",
      "artifact_sha256": "264259ac134341058684f59ccee427881d722235372402fe2dc2eca0f3976c14",
      "reload_validation": "PASS"
    }
  },
  "C231": {
    "notebook_cell_1based": 478,
    "report": {
      "status": "C231_ACTION22_OFFLINE_AUDIT_ACCOUNTED",
      "action": 22,
      "population_cases": 2117,
      "case_states": {
        "INPUT_OR_EVIDENCE_HELD": 17,
        "MECHANICAL_EVIDENCE_CHECK_COMPLETED": 2100
      },
      "input_error_counts": {
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_058eebd08a5d4cc1bacd95aa/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_06a2225ff7a4b410c1c6dda5/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_120452115973764bb3ee511e/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_2368cf0eac9bd1b2936daa2f/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_5604a5f800bb5f8ceb4fe2a7/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_56e42e3dfbdf2216e07151eb/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_6015394a513d9f3c57f87639/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_7d7120273acc70fe4d0ebb63/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_92bfcefe7a81a564423221e3/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_9536f6c35f2cea0bd008360f/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_a201c77b9345ceeb6c27dc20/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_a8016c689eb93dec5cdd52d0/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_b6433cb9d46ef3e140e84172/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_ca73b8c3239c8a64ab9b30ae/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_dae163bb9c064df98bc6c818/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_e352137e9b8a7b1d19163907/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_e55ff4e72277971020197b0a/input.json'": 1
      },
      "answer_unit_literal_evidence_counts": {
        "NO_LITERAL_MATCH_SEMANTIC_REVIEW_REQUIRED": 4177,
        "EXACT_TEXT_IN_SOURCE": 57,
        "NORMALIZED_TEXT_IN_SOURCE": 4,
        "TOO_SHORT_FOR_LITERAL_CHECK": 75
      },
      "explicit_locator_counts": {},
      "attribution_candidate_units": 0,
      "semantic_metric": null,
      "semantic_acceptance_established": false,
      "execution_accounting_complete": true,
      "action_closed": false,
      "closure_status": "OFFLINE_CHECKS_COMPLETE_SEMANTIC_ACCEPTANCE_OPEN",
      "new_api_calls": 0,
      "new_cost": "0 تومان",
      "old_files_modified": false,
      "old_results_relabelled": false,
      "details_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C231.action22_offline_audit/893232ea36efbf9bcaa04849004a792f70fec5230b1124c6c2cf6eda1ac72e1d/C231_case_results.json",
      "details_sha256": "bd98803d77bc9b0f0c1c2fa844cc1c61f622a3af17c290dac95e35400995a85f",
      "remaining_verification_queue_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C231.action22_offline_audit/893232ea36efbf9bcaa04849004a792f70fec5230b1124c6c2cf6eda1ac72e1d/C231_remaining_verification_queue.json",
      "remaining_verification_queue_is_not_automatic_API_dispatch": true,
      "engine_sha256": "e87d6d8ee5efc8063076b89f0b1489697af664dad4a6645187e62038bed44ff3",
      "artifact_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C231.action22_offline_audit/893232ea36efbf9bcaa04849004a792f70fec5230b1124c6c2cf6eda1ac72e1d/report.e17e0aae4664306b4199e9f55354e4b534ef094fe2a3476ce5f57cc6618686c0.json",
      "artifact_sha256": "e17e0aae4664306b4199e9f55354e4b534ef094fe2a3476ce5f57cc6618686c0",
      "reload_validation": "PASS"
    }
  },
  "C232": {
    "notebook_cell_1based": 480,
    "report": {
      "status": "C232_ACTION24_OFFLINE_AUDIT_ACCOUNTED",
      "action": 24,
      "population_cases": 2117,
      "case_states": {
        "INPUT_OR_EVIDENCE_HELD": 17,
        "NO_SUPPORTED_INLINE_MARKER_FOUND": 2100
      },
      "input_error_counts": {
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_058eebd08a5d4cc1bacd95aa/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_06a2225ff7a4b410c1c6dda5/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_120452115973764bb3ee511e/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_2368cf0eac9bd1b2936daa2f/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_5604a5f800bb5f8ceb4fe2a7/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_56e42e3dfbdf2216e07151eb/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_6015394a513d9f3c57f87639/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_7d7120273acc70fe4d0ebb63/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_92bfcefe7a81a564423221e3/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_9536f6c35f2cea0bd008360f/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_a201c77b9345ceeb6c27dc20/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_a8016c689eb93dec5cdd52d0/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_b6433cb9d46ef3e140e84172/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_ca73b8c3239c8a64ab9b30ae/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_dae163bb9c064df98bc6c818/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_e352137e9b8a7b1d19163907/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_e55ff4e72277971020197b0a/input.json'": 1
      },
      "answer_unit_literal_evidence_counts": {},
      "explicit_locator_counts": {},
      "attribution_candidate_units": 0,
      "semantic_metric": null,
      "semantic_acceptance_established": false,
      "execution_accounting_complete": true,
      "action_closed": false,
      "closure_status": "OFFLINE_CHECKS_COMPLETE_SEMANTIC_ACCEPTANCE_OPEN",
      "new_api_calls": 0,
      "new_cost": "0 تومان",
      "old_files_modified": false,
      "old_results_relabelled": false,
      "details_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C232.action24_offline_audit/ee486d73f2bd934ea9851a1810010a59a6b2476e6a8029d1b891b29713768f21/C232_case_results.json",
      "details_sha256": "bb90f87fc412d8976bf32f425234099849affb96b3522bd293ddcd810dabaa8d",
      "remaining_verification_queue_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C232.action24_offline_audit/ee486d73f2bd934ea9851a1810010a59a6b2476e6a8029d1b891b29713768f21/C232_remaining_verification_queue.json",
      "remaining_verification_queue_is_not_automatic_API_dispatch": true,
      "engine_sha256": "e87d6d8ee5efc8063076b89f0b1489697af664dad4a6645187e62038bed44ff3",
      "artifact_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C232.action24_offline_audit/ee486d73f2bd934ea9851a1810010a59a6b2476e6a8029d1b891b29713768f21/report.f9f985f9e2094dce4b3791148a0455bc8aa027679c25c4c79339fdd7b8ff1d39.json",
      "artifact_sha256": "f9f985f9e2094dce4b3791148a0455bc8aa027679c25c4c79339fdd7b8ff1d39",
      "reload_validation": "PASS"
    }
  },
  "C233": {
    "notebook_cell_1based": 482,
    "report": {
      "status": "C233_ACTION25_OFFLINE_AUDIT_ACCOUNTED",
      "action": 25,
      "population_cases": 2117,
      "case_states": {
        "INPUT_OR_EVIDENCE_HELD": 17,
        "ATTRIBUTION_CANDIDATES_REQUIRE_ROLE_VERIFICATION": 47,
        "NO_ATTRIBUTION_CUE_DETECTED_NOT_A_SEMANTIC_PASS": 2053
      },
      "input_error_counts": {
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_058eebd08a5d4cc1bacd95aa/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_06a2225ff7a4b410c1c6dda5/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_120452115973764bb3ee511e/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_2368cf0eac9bd1b2936daa2f/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_5604a5f800bb5f8ceb4fe2a7/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_56e42e3dfbdf2216e07151eb/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_6015394a513d9f3c57f87639/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_7d7120273acc70fe4d0ebb63/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_92bfcefe7a81a564423221e3/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_9536f6c35f2cea0bd008360f/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_a201c77b9345ceeb6c27dc20/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_a8016c689eb93dec5cdd52d0/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_b6433cb9d46ef3e140e84172/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_ca73b8c3239c8a64ab9b30ae/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_dae163bb9c064df98bc6c818/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_e352137e9b8a7b1d19163907/input.json'": 1,
        "[Errno 2] No such file or directory: '/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C206.population_three_passes/fb68235184e7c7107d626cc5ea967262509977d739430741c3acb7971621abf2/cases/golden_v2_candidate_e55ff4e72277971020197b0a/input.json'": 1
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
      "details_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C233.action25_offline_audit/3c35294b251d7767641fe389598fa00f01f4954fa0dbd1032b601a09747fd2d1/C233_case_results.json",
      "details_sha256": "c4877d5f3ab3237bbd0e2264fc7cb3331552eaaabb828d6d8ec5f859a5417e44",
      "remaining_verification_queue_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C233.action25_offline_audit/3c35294b251d7767641fe389598fa00f01f4954fa0dbd1032b601a09747fd2d1/C233_remaining_verification_queue.json",
      "remaining_verification_queue_is_not_automatic_API_dispatch": true,
      "engine_sha256": "e87d6d8ee5efc8063076b89f0b1489697af664dad4a6645187e62038bed44ff3",
      "artifact_path": "/Users/macbookpro/AMIR_DATA/00_WORKS/01_PROJECTS/RAG-projects/RAG_finance/artifacts/phase2/evaluation_and_ablation/work/outputs/NB21B.C233.action25_offline_audit/3c35294b251d7767641fe389598fa00f01f4954fa0dbd1032b601a09747fd2d1/report.e69a8537735e4eb678394f209ef8f3934f4b0fe00a4261af70c40230392dc535.json",
      "artifact_sha256": "e69a8537735e4eb678394f209ef8f3934f4b0fe00a4261af70c40230392dc535",
      "reload_validation": "PASS"
    }
  }
}
```
