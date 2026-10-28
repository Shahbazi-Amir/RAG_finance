# گزارش اقدام 20 — Metricهای بازیابی و Sliceهای معتبر

تاریخ تدوین: ۲۷ اکتبر ۲۰۲۶. Snapshot مخزن: `5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c`.

## وضعیت و مرز

**وضعیت جاری:** `CHECKLIST_COMPLETED_IN_RECORDED_SCOPE`. اقدام در چک‌لیست فعلی تیک دارد. این فایل گزارش بازخوانی و تجمیع شاهد است؛ اجرای تازه، تیک تازه یا تغییر رأی تاریخی نیست.

**متن الزام:** محاسبه/بازتولید Recall@k، MRR و nDCG روی Development و Sliceهای معتبر؛ جداسازی rank depth و Gold mapping.

**ثبت فعلی:** [چک‌لیست پین‌شده](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md).

**وضعیت گزارش قبلی:** گزارش مستقلِ هم‌نام برای این اقدام در فهرست reports/phase2/evaluation این Snapshot یافت نشد؛ شاهد داخل چک‌لیست و نوت‌بوک موجود است. نبود گزارش مستقل، نبود اجرای قبلی نیست.

## کار انجام‌شده و نتیجه

نتایج Retrieval کلی و Sliceهای معتبر در C194/C304 و بازخوانی بعدی NB21B.C003 مبنای بستن دامنه‌دار اقدام۲۰ شده‌اند. C304 به‌تنهایی اقدام۲۰ را واجد تیک نمی‌دانست، چون Topic/Question type آن زمان نگاشت منتخب نداشتند؛ تصمیم بعدی ثبت‌شده در چک‌لیست و سپس بستن اقدام۱۰/C024 باید جدا از این خروجی تاریخی خوانده شوند. این گزارش ادعا نمی‌کند همهٔ جدول‌های قدیمی با نگاشت تازه C024 دوباره محاسبه شده‌اند.

## شواهد، سل و مسیر خروجی

سل‌ها و منابع مرتبط: C194/C304؛ NB21B.C003 و تصمیم اصلاحی ثبت‌شده در چک‌لیست.

[نوت‌بوک اصلی در Snapshot جاری](https://github.com/Shahbazi-Amir/RAG_finance/blob/5f3d3f8c3c9bc84d63799a01efbd02e9467c8d0c/notebooks/phase2/21_evaluation_and_ablation.ipynb). محتوای سل‌ها از شش بخش Export خواندنیِ tracked خوانده شده است؛ هویت Git این بخش‌ها با درخت جاری تطبیق داده شد. بایت اصل ipynb یا Artifactهای مک در این تدوین بازخوانی نشده‌اند.

### NB21-C194 — سل فیزیکی 387

خروجی ذخیره‌شدهٔ همان سل؛ Runtime تازه یا تأیید مستقل معنا نیست:

```json
{
  "status": "NB21_EXISTING_RETRIEVAL_SLICE_RESULTS_READY",
  "development_query_count": 2664,
  "all_slice_coverage_checks_pass": true,
  "source_type_summary": {
    "dense_local_cosine_100": {
      "book": {
        "query_count": 277,
        "recall_at_10": 0.6155234657039711,
        "ndcg_at_10": 0.4993943358113277,
        "mrr_at_10": 0.48259412068076324
      },
      "transcript": {
        "query_count": 1459,
        "recall_at_10": 0.3867831848297921,
        "ndcg_at_10": 0.2662635110608386,
        "mrr_at_10": 0.2679944950335629
      },
      "website": {
        "query_count": 928,
        "recall_at_10": 0.5675783388067871,
        "ndcg_at_10": 0.5057976758034003,
        "mrr_at_10": 0.5847842261904762
      }
    },
    "hybrid_depth_100": {
      "book": {
        "query_count": 277,
        "recall_at_10": 0.7888086642599278,
        "ndcg_at_10": 0.6684420848811021,
        "mrr_at_10": 0.6487808721563234
      },
      "transcript": {
        "query_count": 1459,
        "recall_at_10": 0.550045693397304,
        "ndcg_at_10": 0.4362504998777923,
        "mrr_at_10": 0.46742006375316864
      },
      "website": {
        "query_count": 928,
        "recall_at_10": 0.6831610050629447,
        "ndcg_at_10": 0.6595305425779713,
        "mrr_at_10": 0.8001056205528189
      }
    },
    "hybrid_original_pool_50": {
      "book": {
        "query_count": 277,
        "recall_at_10": 0.7888086642599278,
        "ndcg_at_10": 0.6684420848811021,
        "mrr_at_10": 0.6487808721563234
      },
      "transcript": {
        "query_count": 1459,
        "recall_at_10": 0.550045693397304,
        "ndcg_at_10": 0.4362504998777923,
        "mrr_at_10": 0.46742006375316864
      },
      "website": {
        "query_count": 928,
        "recall_at_10": 0.6831610050629447,
        "ndcg_at_10": 0.6595305425779713,
        "mrr_at_10": 0.8001056205528189
      }
    },
    "reranked_same_pool_50": {
      "book": {
        "query_count": 277,
        "recall_at_10": 0.8375451263537906,
        "ndcg_at_10": 0.7216321346409874,
        "mrr_at_10": 0.7072660592516188
      },
      "transcript": {
        "query_count": 1459,
        "recall_at_10": 0.6174091843728581,
        "ndcg_at_10": 0.520264149550968,
        "mrr_at_10": 0.5802335258983649
      },
      "website": {
        "query_count": 928,
        "recall_at_10": 0.6959962541050903,
        "ndcg_at_10": 0.6857078592893938,
        "mrr_at_10": 0.8536937260536398
      }
    },
    "sparse_frozen_100": {
      "book": {
        "query_count": 277,
        "recall_at_10": 0.740072202166065,
        "ndcg_at_10": 0.6309808625583065,
        "mrr_at_10": 0.616477565755544
      },
      "transcript": {
        "query_count": 1459,
        "recall_at_10": 0.5083790267306374,
        "ndcg_at_10": 0.41044822548946613,
        "mrr_at_10": 0.4430875137352176
      },
      "website": {
        "query_count": 928,
        "recall_at_10": 0.6438598966885605,
        "ndcg_at_10": 0.6285805145926086,
        "mrr_at_10": 0.7815548884783798
      }
    }
  },
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
  "checklist_file_updated": false,
  "network_requests": 0,
  "paid_api_calls": 0,
  "new_api_cost_toman": 0,
  "artifact": {
    "path": "artifacts/phase2/evaluation_and_ablation/work/outputs/C194.development_retrieval_slices.e1acb44554ab252591265bdaf2a047b55cb2c3e144b6cd955580a2fca5897924.json",
    "file_bytes_sha256": "e1acb44554ab252591265bdaf2a047b55cb2c3e144b6cd955580a2fca5897924",
    "bytes": 61749,
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

بستن محدود قبلی و قبول Sliceهای تشخیصی، تأیید مستقل همهٔ برچسب‌ها نیست. تغییر نگاشت ورودیِ مصرف آینده باید با نسخهٔ آن ثبت شود.

وضعیت‌های OPEN/false در خروجی تاریخی برای زمان همان اجرا حفظ شده‌اند. تصمیم‌های جدیدتر C024/C025 و گزارش‌های پایان ۲۲–۲۶ در سطح ثبت جاری مقدم‌اند؛ برای همسان‌سازی، فایل‌های تاریخی بازنویسی نمی‌شوند.

## جلوگیری از دوباره‌کاری

برای مصرف همین نتیجه، تولیدکننده از ابتدا اجرا نشود. خروجی سالم، Cache، ورودی و رأی تاریخی حفظ شوند. فقط اختلاف نسخه، خطای مؤثر یا وابستگی روشن مرحلهٔ بعد می‌تواند بررسی محدود تازه لازم کند. پیش از API، دفتر Attempt و نتیجهٔ همان وظیفه مصرف شود.

## هزینه و تغییرات این تدوین

API داوری تازه: صفر. Retry تازه: صفر. تغییر Dataset/Taxonomy/رأی: صفر. تغییر مخزن/Commit/Push: انجام نشده. این گزارش درخواست اجرای تازه یا مجوز هزینه ایجاد نمی‌کند.

## محل قرارگیری پیشنهادی

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action20_report_fa.md`

این مسیر برای واردکردن توسط مالک پیشنهاد شده است؛ هنوز در مخزن ساخته یا Push نشده است.
