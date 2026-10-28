# گزارش اقدام 21 — اختلاف و شکست بازیابی

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** ثبت اختلاف‌ها، پوشش ورودی، شکست‌های بازیابی و حدود مقایسه؛ رفع اختلافِ محاسباتی پیش از ادامه.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

C195 مقایسهٔ زوجی/گروهی و C196/C304 شکست‌های Retrieval را تطبیق داده‌اند. انتقال Hit@10: ۲۱۹ به‌دست‌آمده، ۴۸ ازدست‌رفته، ۲۰۴۵ حفظ‌شده و ۳۵۲ Miss حفظ‌شده؛ سود خالص ۱۷۱ است. ۴۰۰ Miss ریرنکر به ۱۲۷ Gold داخل Pool50 و خارجTop10، ۸۶ خارجPool50 و داخلHybridTop100 و ۱۸۷ فاقدGold درHybridTop100 تقسیم شده‌اند. تمام کنترل‌های حسابی C304 پاس‌اند.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C173/C195/C196/C304.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C195 — سل فیزیکی 389

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "status": "NB21_DEVELOPMENT_PAIRED_GROUP_INTERVALS_READY",
  "development_query_count": 2664,
  "question_group_count": 2620,
  "bootstrap_replicates": 10000,
  "undefined_replicate_count": 0,
  "point_estimates_match_C192": true,
  "intervals": {
    "hit_at_k:k=5": {
      "mean_reranker_minus_hybrid": 0.07995495495495496,
      "percentile_95_lower": 0.06578885559445401,
      "percentile_95_upper": 0.09411378559936263,
      "degenerate_interval": false,
      "paired_query_count": 2664,
      "unavailable_pair_count": 0
    },
    "recall_at_k:k=5": {
      "mean_reranker_minus_hybrid": 0.05088451546784879,
      "percentile_95_lower": 0.03907969270303363,
      "percentile_95_upper": 0.06292344350351732,
      "degenerate_interval": false,
      "paired_query_count": 2664,
      "unavailable_pair_count": 0
    },
    "ndcg_at_k_binary:k=5": {
      "mean_reranker_minus_hybrid": 0.061716956418720416,
      "percentile_95_lower": 0.05111052469561152,
      "percentile_95_upper": 0.0724787771235065,
      "degenerate_interval": false,
      "paired_query_count": 2664,
      "unavailable_pair_count": 0
    },
    "hit_at_k:k=10": {
      "mean_reranker_minus_hybrid": 0.06418918918918919,
      "percentile_95_lower": 0.052393069052406496,
      "percentile_95_upper": 0.07600198962804958,
      "degenerate_interval": false,
      "paired_query_count": 2664,
      "unavailable_pair_count": 0
    },
    "recall_at_k:k=10": {
      "mean_reranker_minus_hybrid": 0.04643184851518183,
      "percentile_95_lower": 0.03623709532360841,
      "percentile_95_upper": 0.05669975437590614,
      "degenerate_interval": false,
      "paired_query_count": 2664,
      "unavailable_pair_count": 0
    },
    "ndcg_at_k_binary:k=10": {
      "mean_reranker_minus_hybrid": 0.060661452163983456,
      "percentile_95_lower": 0.051185199401089974,
      "percentile_95_upper": 0.06996134755664722,
      "degenerate_interval": false,
      "paired_query_count": 2664,
      "unavailable_pair_count": 0
    },
    "rr_at_10": {
      "mean_reranker_minus_hybrid": 0.08653340840840848,
      "percentile_95_lower": 0.07352691905311241,
      "percentile_95_upper": 0.09931223529122515,
      "degenerate_interval": false,
      "paired_query_count": 2664,
      "unavailable_pair_count": 0
    },
    "rr_at_50": {
      "mean_reranker_minus_hybrid": 0.08356097203728176,
      "percentile_95_lower": 0.07081787300914556,
      "percentile_95_upper": 0.0961181511117413,
      "degenerate_interval": false,
      "paired_query_count": 2664,
      "unavailable_pair_count": 0
    }
  },
  "regression_acceptance_assessed": false,
  "checklist_file_updated": false,
  "network_requests": 0,
  "paid_api_calls": 0,
  "new_api_cost_toman": 0,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C195.development_paired_group_bootstrap.658cb1edda0daa825a9d050ef9a2026a50a2f52095febe2b3131c1959e1ab939.json",
    "file_bytes_sha256": "658cb1edda0daa825a9d050ef9a2026a50a2f52095febe2b3131c1959e1ab939",
    "bytes": 5635,
    "action": "CREATED",
    "reload_validation": "PASS"
  }
}
```

### NB21-C196 — سل فیزیکی 391

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "schema_version": "nb21_retrieval_failure_partition_C196_v1",
  "status": "NB21_RETRIEVAL_FAILURE_PARTITION_READY",
  "checklist_action": 21,
  "checklist_action_total": 49,
  "input_bindings": {
    "joined_rankings": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C166.joined_development_retrieval_inputs.71ffa7d27eb47dac2b54d60963198d95cc31cb21b9b0c5ee7c11c666d8b7bfd5.json",
      "file_bytes_sha256": "71ffa7d27eb47dac2b54d60963198d95cc31cb21b9b0c5ee7c11c666d8b7bfd5"
    },
    "comparison": {
      "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C192.development_retrieval_comparison.7f8c85de9f91b8a552a49739c7f68891d4517a0d4404b1c2372d1b6dbc08d00c.json",
      "file_bytes_sha256": "7f8c85de9f91b8a552a49739c7f68891d4517a0d4404b1c2372d1b6dbc08d00c"
    }
  },
  "joined_row_field": "retrieval_inputs",
  "development_query_count": 2664,
  "same_pool_identity_verified": true,
  "transition_counts": {
    "HIT_RETAINED": 2045,
    "HIT_GAINED": 219,
    "HIT_LOST": 48,
    "MISS_RETAINED": 352
  },
  "baseline_top_10_miss_count": 571,
  "reranker_top_10_miss_count": 400,
  "net_hit_gain_count": 171,
  "reranker_miss_category_counts": {
    "GOLD_IN_POOL_50_BUT_OUTSIDE_RERANKED_TOP_10": 127,
    "GOLD_OUTSIDE_POOL_50_BUT_IN_HYBRID_TOP_100": 86,
    "NO_GOLD_IN_HYBRID_TOP_100": 187
  },
  "reranker_miss_category_denominator": 400,
  "counts_match_C192": true,
  "relevance_target": "CHUNK_CONTAINS_MEMBER_WITH_IDENTICAL_SOURCE_LOCATOR",
  "categories_establish_semantic_failure_causes": false,
  "regression_acceptance_assessed": false,
  "action_21_eligible_for_checkmark": false,
  "checklist_file_updated": false,
  "new_retrieval_executed": false,
  "new_test_queries_evaluated": false,
  "network_requests": 0,
  "paid_api_calls": 0,
  "new_api_cost_toman": 0,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C196.development_retrieval_failure_partition.a063ce76b477de4527df84cfd4fc5c9a8ce266487fd4417a7712cfe60b8039c8.json",
    "file_bytes_sha256": "a063ce76b477de4527df84cfd4fc5c9a8ce266487fd4417a7712cfe60b8039c8",
    "bytes": 715916,
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

تحلیل شکست Retrieval، علت همهٔ خطاهای پاسخ یا کیفیت استناد/انتساب را ثابت نمی‌کند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action21_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
