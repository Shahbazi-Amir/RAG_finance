# گزارش اقدام 19 — تطبیق بازوهای Retrieval

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** تطبیق نتایج Dense، Sparse، Hybrid و Reranker موجود روی ورودی و تعریف Metric همسان.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

C192 پنج بازوی بازیابی روی ۲۶۶۴ Development را در جدول واحد ثبت کرده و C304 تطابق جدول‌های Cache با ورودی‌های C303 را تأیید کرده است. Dense/Sparse/Hybrid/Reranker با قرارداد و عمق رتبهٔ خودشان مصرف می‌شوند. نیازی به اجرای دوبارهٔ موتور برای تکرار همان جدول معتبر نیست.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C192/C304 و NB16/NB17.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C192 — سل فیزیکی 383

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "schema_version": "nb21_retrieval_comparison_C192_v1",
  "status": "NB21_FIVE_ARM_DEVELOPMENT_TABLE_READY",
  "checklist_actions": [
    19,
    20,
    21
  ],
  "checklist_action_total": 49,
  "input_bindings": {
    "dense_local_cosine_100": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_cached_dense_v1/cce675c281a5094d80bd617c7cc934f5fbf4bd447837ab65d594ef35032780b0/development_rankings.2f0acbf9bc6c2a2c2b4364c225ee311a4e697a0da1b26c1a23e60cdbe55667a1.json",
      "file_bytes_sha256": "2f0acbf9bc6c2a2c2b4364c225ee311a4e697a0da1b26c1a23e60cdbe55667a1"
    },
    "sparse_frozen_100": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_frozen_sparse_v1/aa638442bb1577b6dfee1fddc8917296f861ac8386f21bce05163a37016d0acd/development_rankings.2ef9cac3f743ce8536931d5ebac1fbb5aea0b9b7f9bc375c530f79a754274884.json",
      "file_bytes_sha256": "2ef9cac3f743ce8536931d5ebac1fbb5aea0b9b7f9bc375c530f79a754274884"
    },
    "hybrid_depth_100": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_local_retrieval_metrics_v1/ba7be2442f0e5257237c0572cdcb6926a21b6afbfa234b09fdf79f5ced54211c/hybrid_depth_100.b9d58ff625075bbe3bb54a7fd2491e5353bb12c36ffea24433fe4e61ccc23e3f.json",
      "file_bytes_sha256": "b9d58ff625075bbe3bb54a7fd2491e5353bb12c36ffea24433fe4e61ccc23e3f"
    },
    "hybrid_original_pool_50": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_local_retrieval_metrics_v1/ba7be2442f0e5257237c0572cdcb6926a21b6afbfa234b09fdf79f5ced54211c/hybrid_original_pool_50.ea282e6d8d1514934fde614503b162cc645fdba2cf3ecb6ef2e3f404347d3156.json",
      "file_bytes_sha256": "ea282e6d8d1514934fde614503b162cc645fdba2cf3ecb6ef2e3f404347d3156"
    },
    "reranked_same_pool_50": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/nb21_local_retrieval_metrics_v1/ba7be2442f0e5257237c0572cdcb6926a21b6afbfa234b09fdf79f5ced54211c/reranked_same_pool_50.15eec9299c9ca1428d3f11b022d678087e50b4a8eb733586524f63d522ca4c65.json",
      "file_bytes_sha256": "15eec9299c9ca1428d3f11b022d678087e50b4a8eb733586524f63d522ca4c65"
    }
  },
  "gold_mapping_binding": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C165.development_locator_gold_mapping.9349af309791a2f14d4d094562162d78727b7ab16b217615462050a84af6d124.json",
    "file_bytes_sha256": "9349af309791a2f14d4d094562162d78727b7ab16b217615462050a84af6d124"
  },
  "schema_adapters": {
    "dense_local_cosine_100": "NESTED_METRICS",
    "sparse_frozen_100": "NESTED_METRICS",
    "hybrid_depth_100": "DIRECT_ROW_METRICS",
    "hybrid_original_pool_50": "DIRECT_ROW_METRICS",
    "reranked_same_pool_50": "DIRECT_ROW_METRICS"
  },
  "development_query_count": 2664,
  "all_arm_query_id_sets_match": true,
  "aggregation": "MACRO_PER_QUERY_WITH_AVAILABILITY_COUNTS",
  "summaries": {
    "dense_local_cosine_100": {
      "hit_at_k:k=5": {
        "macro_mean": 0.521021021021021,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=5": {
        "macro_mean": 0.39137262262262257,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=5": {
        "macro_mean": 0.3441948979972235,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "hit_at_k:k=10": {
        "macro_mean": 0.609984984984985,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=10": {
        "macro_mean": 0.4735470589637256,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=10": {
        "macro_mean": 0.3739455468479943,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_10": {
        "macro_mean": 0.40066152461985793,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_50": {
        "macro_mean": 0.41037127769468706,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_100": {
        "macro_mean": 0.41114801916014126,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      }
    },
    "sparse_frozen_100": {
      "hit_at_k:k=5": {
        "macro_mean": 0.6786786786786787,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=5": {
        "macro_mean": 0.5128710555793888,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=5": {
        "macro_mean": 0.4855041074074556,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "hit_at_k:k=10": {
        "macro_mean": 0.743993993993994,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=10": {
        "macro_mean": 0.5796647838314506,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=10": {
        "macro_mean": 0.50936500655395,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_10": {
        "macro_mean": 0.5790209852709853,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_50": {
        "macro_mean": 0.5852859413787405,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_100": {
        "macro_mean": 0.58579916164883,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      }
    },
    "hybrid_depth_100": {
      "hit_at_k:k=5": {
        "macro_mean": 0.7117117117117117,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=5": {
        "macro_mean": 0.5469027062777063,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=5": {
        "macro_mean": 0.5115595588576384,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "hit_at_k:k=10": {
        "macro_mean": 0.7856606606606606,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=10": {
        "macro_mean": 0.621242522284189,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=10": {
        "macro_mean": 0.5381727779077033,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_10": {
        "macro_mean": 0.6021682396682396,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_50": {
        "macro_mean": 0.6077657488576085,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_100": {
        "macro_mean": 0.6082169141249909,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      }
    },
    "hybrid_original_pool_50": {
      "hit_at_k:k=5": {
        "macro_mean": 0.7117117117117117,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=5": {
        "macro_mean": 0.5469027062777063,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=5": {
        "macro_mean": 0.5115595588576384,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "hit_at_k:k=10": {
        "macro_mean": 0.7856606606606606,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=10": {
        "macro_mean": 0.621242522284189,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=10": {
        "macro_mean": 0.5381727779077033,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_10": {
        "macro_mean": 0.6021682396682396,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_50": {
        "macro_mean": 0.6077657488576085,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_100": {
        "macro_mean": null,
        "eligible_query_count": 0,
        "unavailable_query_count": 2664
      }
    },
    "reranked_same_pool_50": {
      "hit_at_k:k=5": {
        "macro_mean": 0.7916666666666666,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=5": {
        "macro_mean": 0.5977872217455551,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=5": {
        "macro_mean": 0.5732765152763587,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "hit_at_k:k=10": {
        "macro_mean": 0.8498498498498499,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "recall_at_k:k=10": {
        "macro_mean": 0.6676743707993709,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "ndcg_at_k_binary:k=10": {
        "macro_mean": 0.5988342300716867,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_10": {
        "macro_mean": 0.6887016480766481,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_50": {
        "macro_mean": 0.6913267208948901,
        "eligible_query_count": 2664,
        "unavailable_query_count": 0
      },
      "rr_at_100": {
        "macro_mean": null,
        "eligible_query_count": 0,
        "unavailable_query_count": 2664
      }
    }
  },
  "no_gold_hit_query_counts": {
    "dense_local_cosine_100": {
      "no_gold_hit_at_5": 1276,
      "no_gold_hit_at_10": 1039
    },
    "sparse_frozen_100": {
      "no_gold_hit_at_5": 856,
      "no_gold_hit_at_10": 682
    },
    "hybrid_depth_100": {
      "no_gold_hit_at_5": 768,
      "no_gold_hit_at_10": 571
    },
    "hybrid_original_pool_50": {
      "no_gold_hit_at_5": 768,
      "no_gold_hit_at_10": 571
    },
    "reranked_same_pool_50": {
      "no_gold_hit_at_5": 555,
      "no_gold_hit_at_10": 400
    }
  },
  "same_pool_paired_comparison": {
    "baseline": "hybrid_original_pool_50",
    "comparison": "reranked_same_pool_50",
    "candidate_pool_size": 50,
    "metrics": {
      "hit_at_k:k=5": {
        "mean_reranker_minus_hybrid": 0.07995495495495496,
        "paired_query_count": 2664,
        "unavailable_pair_count": 0
      },
      "recall_at_k:k=5": {
        "mean_reranker_minus_hybrid": 0.0508845154678488,
        "paired_query_count": 2664,
        "unavailable_pair_count": 0
      },
      "ndcg_at_k_binary:k=5": {
        "mean_reranker_minus_hybrid": 0.0617169564187203,
        "paired_query_count": 2664,
        "unavailable_pair_count": 0
      },
      "hit_at_k:k=10": {
        "mean_reranker_minus_hybrid": 0.06418918918918919,
        "paired_query_count": 2664,
        "unavailable_pair_count": 0
      },
      "recall_at_k:k=10": {
        "mean_reranker_minus_hybrid": 0.046431848515181846,
        "paired_query_count": 2664,
        "unavailable_pair_count": 0
      },
      "ndcg_at_k_binary:k=10": {
        "mean_reranker_minus_hybrid": 0.06066145216398341,
        "paired_query_count": 2664,
        "unavailable_pair_count": 0
      },
      "rr_at_10": {
        "mean_reranker_minus_hybrid": 0.08653340840840841,
        "paired_query_count": 2664,
        "unavailable_pair_count": 0
      },
      "rr_at_50": {
        "mean_reranker_minus_hybrid": 0.08356097203728165,
        "paired_query_count": 2664,
        "unavailable_pair_count": 0
      },
      "rr_at_100": {
        "mean_reranker_minus_hybrid": null,
        "paired_query_count": 0,
        "unavailable_pair_count": 2664
      }
    },
    "uncertainty_estimated": false,
    "statistical_significance_assessed": false
  },
  "relevance_target": "CHUNK_CONTAINS_MEMBER_WITH_IDENTICAL_SOURCE_LOCATOR",
  "dense_variant": "LOCAL_EXACT_COSINE_CHUNK_ID_TIE_BREAK",
  "historical_qdrant_parity_established": false,
  "cross_engine_deltas_are_strict_ablation_effects": false,
  "slice_benchmark_completed": false,
  "semantic_quality_established": false,
  "regression_acceptance_assessed": false,
  "action_19_eligible_for_checkmark": false,
  "action_20_eligible_for_checkmark": false,
  "action_21_eligible_for_checkmark": false,
  "checklist_file_updated": false,
  "new_retrieval_executed": false,
  "new_test_queries_evaluated": false,
  "network_requests": 0,
  "paid_api_calls": 0,
  "new_api_cost_toman": 0,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C192.development_retrieval_comparison.7f8c85de9f91b8a552a49739c7f68891d4517a0d4404b1c2372d1b6dbc08d00c.json",
    "file_bytes_sha256": "7f8c85de9f91b8a552a49739c7f68891d4517a0d4404b1c2372d1b6dbc08d00c",
    "bytes": 9808,
    "action": "CREATED",
    "reload_validation": "PASS"
  }
}
```

### NB21-C304 — سل فیزیکی 610

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "schema_version": "nb21_retrieval_package_C304_v1",
  "status": "NB21_RETRIEVAL_TABLES_ALIGNED_REQUIRED_SLICE_MAPPING_OPEN",
  "checklist_actions": [
    19,
    20,
    21
  ],
  "checklist_action_total": 49,
  "development_query_count": 2664,
  "retrieval_arm_count": 5,
  "all_cached_metric_tables_match_C303": true,
  "open_slice_gaps": [
    {
      "family": "topic",
      "reason": "No validated query-to-topic mapping selected from inspected sources; frozen taxonomy alone is insufficient.",
      "status": "NOT_ASSESSED_NO_CANONICAL_MAPPING",
      "unassigned_development_query_count": 2664
    },
    {
      "family": "question_type",
      "reason": "No validated fixed question-type mapping selected; raw question_intent is not adopted as that mapping.",
      "status": "NOT_ASSESSED_NO_CANONICAL_MAPPING",
      "unassigned_development_query_count": 2664
    }
  ],
  "slice_contract_structure": {
    "schema_version": "nb21_slice_contract_draft_C026_v1",
    "top_level_fields": [
      "action_10_eligible_for_checkmark",
      "checklist_action",
      "checklist_action_total",
      "coverage",
      "evaluation_contract_frozen",
      "input_file_hashes",
      "membership_policy",
      "new_api_cost_toman",
      "open_gaps",
      "paid_api_calls",
      "population_query_count",
      "query_slice_rows",
      "schema_version",
      "semantic_judgments_performed",
      "split",
      "status",
      "upstream_product_acceptance_changed"
    ]
  },
  "failure_arithmetic_checks": {
    "transition_denominator": true,
    "baseline_miss_count": true,
    "reranker_miss_count": true,
    "net_hit_gain": true,
    "miss_partition_denominator": true,
    "same_pool_identity": true,
    "hit_delta_matches_count_delta": true
  },
  "hit_at_10_transitions": {
    "HIT_GAINED": 219,
    "HIT_LOST": 48,
    "HIT_RETAINED": 2045,
    "MISS_RETAINED": 352
  },
  "reranker_miss_categories": {
    "GOLD_IN_POOL_50_BUT_OUTSIDE_RERANKED_TOP_10": 127,
    "GOLD_OUTSIDE_POOL_50_BUT_IN_HYBRID_TOP_100": 86,
    "NO_GOLD_IN_HYBRID_TOP_100": 187
  },
  "net_hit_gain_count": 171,
  "actions_eligible_for_checkmark": {
    "19": true,
    "20": false,
    "21": true
  },
  "next_checklist_action": 20,
  "next_required_work": "RESOLVE_REQUIRED_TOPIC_AND_QUESTION_TYPE_MAPPING_GAPS",
  "metrics_recomputed": false,
  "new_retrieval_executed": false,
  "network_requests": 0,
  "paid_api_calls": 0,
  "checklist_file_updated": false,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C304.retrieval_package.bf078b985c16666005f4932aee1fc1a1140028342c404ab9c865651e18615d66.json",
    "file_bytes_sha256": "bf078b985c16666005f4932aee1fc1a1140028342c404ab9c865651e18615d66",
    "bytes": 12032,
    "action": "CREATED",
    "reload_validation": "PASS"
  }
}
```

## محدودیت و مصرف درست

مقایسه با rank depth، Gold mapping یا tie-break متفاوت ادعای کنترل‌شدهٔ یکسان نیست.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action19_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
