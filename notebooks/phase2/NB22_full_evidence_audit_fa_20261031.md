# ممیزی جامع نوت‌بوک‌های خانوادهٔ NB22 — گزارش مبتنی بر فایل‌های ارسالی

**تاریخ بررسی:** ۳۱ اکتبر ۲۰۲۶  
**دامنه:** هفت فایل مشخص‌شده در پیوست، خواندن ساختاری تمام سل‌های کد و Markdown و خروجی‌های ذخیره‌شده؛ بدون اجرای محاسبات اصلی، بدون درخواست API، بدون تغییر Git یا Golden.  
**مرز اعتبار:** هش‌های ذکرشده در گزارش‌ها «ادعای ثبت‌شده در Notebook» هستند، مگر آنکه مستقلاً بایت Artifact محلی قابل دسترس بوده باشد. در این بررسی فایل‌های `ipynb` ارسالی به‌صورت بایت خوانده و SHA-256 آن‌ها محاسبه شد، اما Artifactهای مستقل در ماشین کاربر بازخوانی نشدند.

## جمع‌بندی تصمیم‌ساز

- **نتیجهٔ واقعی مثبت:** NB22B انتخاب `cached_rrf_k10_w0.75` را با بهبود Development تثبیت کرد (Recall@10 از 66.77% به 67.30% و nDCG@10 از 59.88% به 60.70%). ارزیابی Test تاریخی روی ۱۱۴۹ مورد Recall را از 63.43% به 64.18% و nDCG را از 57.35% به 58.03% رساند. هر دو پایین‌تر از آستانه‌های آزمایش ماندند.
- **نتیجهٔ واقعی مثبت:** NB22C روی داده‌های Development رتبه‌بندی را از Recall 67.30% به 67.79% و nDCG 60.70% به 60.87% رساند. NB22D کاندیداهای Lexical را روی کل ۲۶۶۴ Development محاسبه کرد و Recall Full-Dev را از 67.79% به 68.35% و nDCG را از 60.87% به 61.16% رساند؛ همچنان FAIL مطلق.
- **نتیجهٔ مثبت محدود BGE:** در NB22E v2، C019 با BGE Top40 روی ۶۰ سؤال دیده‌شدهٔ Development، Recall@10=85.14% و nDCG@10=77.63% ثبت کرده است؛ این فقط آزمایش روی همان ۶۰ مورد است. C017 با Top20 به 83.06%/76.23% رسیده بود.
- **عدم تکرار BGE:** C021 روی ۶۰ سؤال دیگر با تنظیم Top40 فریز‌شده، Recall از 81.25% به 81.25% و nDCG از 72.53% به 72.14% رسید؛ Hit از 95% به 93.33% کاهش یافت. C022 تصمیم `KEEP_BASELINE_NO_AUTOMATIC_REPLACEMENT` ثبت کرد.
- **آزمون بزرگ و تجمیعی موجود:** NB22F واقعاً ۲۶۶۴ سؤال را در Fit=1507، Validation=533، Check=624 تفکیک و چند روش Dense/Word/Char/RRF/Linear را مقایسه کرد. برندهٔ Validation همان `baseline` شد؛ در Check=624، Recall@10=69.60% و nDCG@10=60.38%. آزمون مستقل Release نیست؛ بخش Book فقط یک کامپوننت منبع دارد.
- **آزمون بزرگ دوم:** NB22E C035 آزمایش Window Retrieval را با همان تفکیک انجام داده و Baseline را نگه داشته؛ در فایل ذخیره‌شده خروجی COMPLETE هست اما execution_count این سل خالی است، پس سلامت Runtime مستقل از خروجی اثبات نمی‌شود.
- **شکاف اثبات‌شده:** NB22E C037 روی ۵۳۳ Validation، سقف Top100=79.03% و سقف Pool کامل=91.80% و اتحاد Word/Char (به‌عنوان سقف ظرفیت)=92.99% گزارش می‌کند؛ انتخاب ۱۰۰ کاندیدای باکیفیت هنوز حل نشده است. C038 shortlist یادگرفته‌شده=80.51%, C039 boundary-aware=78.53%, C045 RRF=79.58%. هیچ‌یک به ۸۵% نمی‌رسند؛ RRF حتی برای Website افت دارد.
- **هشدار Gold:** C042 اتصال واقعی Locator و متن را برای ۵۳۳ سؤال بررسی کرده (۱۰۳۳ اتصال، ۵۷۱ با span کامل و ۴۶۲ بدون span کامل). C043 با تعریف *متفاوت* ارتباط، روی ۵۳۱ سؤال قابل‌مقایسه Recall تشخیصی=83.73%, nDCG=70.32%, Hit=84.37% به‌دست آورده؛ این بهبود موتور نیست و معیار فریز‌شده را جایگزین نمی‌کند.
- **بازبینی کوچکِ واقعی:** C044 بستهٔ ۲۹سؤالی/۷۲ اتصال ایجاد کرد. اجرای C046 از خروجی مستقلی که کاربر در همین چت فرستاد: ۲۹ API، ۲۶ رأی مکانیکی معتبر/۶۵ اتصال، ۳ HOLD. این خروجی در فایل `NB22E v2(6)` درج/اجرا نشده؛ کد C046 در آخر فایل ارسالی خالی است. C047 هم اجرا نشده است.
- **پذیرش:** NB22A گزارش‌های انتشار، بایت، Manifest و Checkpoint را در دامنهٔ خود ساخته و کنتر‌ل کرده؛ C047 آن نوت‌بوک Release را صراحتاً نپذیرفته است. NB22B نیز ۱۴ اقدام را مستند کرده ولی شروط معنایی و Product/Release هنوز باز هستند. هیچ نتیجه‌ای پذیرش رسمی فاز دوم ایجاد نمی‌کند.

## نمودار تصمیم (فقط همان جمعیت و روش)

| اجرای واقعی | جمعیت/دامنه | Recall@10 قبل → بعد | nDCG@10 قبل → بعد | حکم |
|---|---|---|---|---|
| NB22B Dev | ۲۶۶۴ Dev | 66.77 → 67.30٪ | 59.88 → 60.70٪ | رشد محدود |
| NB22B Test تاریخی | ۱۱۴۹ Test مشاهده‌شده | 63.43 → 64.18٪ | 57.35 → 58.03٪ | رشد محدود، FAIL |
| NB22C | ۲۶۶۴ Dev، انتخاب در زیرمجموعهٔ Validation | 67.30 → 67.79٪ | 60.70 → 60.87٪ | رشد محدود |
| NB22D | ۲۶۶۴ Dev، Pool توسعه‌یافته | 67.79 → 68.35٪ | 60.87 → 61.16٪ | رشد محدود، FAIL |
| NB22E C010 ONNX400 | ۶۰ Dev دیده‌شده | 78.89 → 76.94٪ | 69.05 → 69.50٪ | افت Recall/Hit |
| NB22E C017 BGE Top20 | ۶۰ Dev اول | 78.89 → 83.06٪ | 69.05 → 76.23٪ | خوب ولی Recall زیر ۸۵٪ |
| NB22E C019 BGE Top40 | همان ۶۰ Dev | 78.89 → 85.14٪ | 69.05 → 77.63٪ | عبور عددی فقط در نمونهٔ دیده‌شده |
| NB22E C021 BGE Top40 ثابت | ۶۰ Dev دیگر | 81.25 → 81.25٪ | 72.53 → 72.14٪ | عدم تکرار، افت nDCG/Hit |
| NB22E C035 Window | Check=624 Dev | 69.60 → 69.60٪ | 60.38 → 60.38٪ | Baseline منتخب |
| NB22F F008 | Check=624 Dev | 69.60 → 69.60٪ | 60.38 → 60.38٪ | Baseline منتخب |

**تفاوت جمعیت‌ها:** اعداد ۶۰سؤالی، ۱۲۰سؤالی، ۵۳۳سؤالی، ۶۲۴سؤالی، ۲۶۶۴سؤالی و ۱۱۴۹ Test نمی‌توانند به‌عنوان یک سیر زمانی واحد جمع شوند. برای هر مقایسه باید جمعیت، نسخه Gold، روش انتخاب، baseline و عمق ثابت باشد.

## خطاها و مرزهای واقعی

1. NB22E v1 به‌دلیل `INSUFFICIENT_DISTINCT_SOURCE_COMPONENTS:book` در Setup مسدود شد؛ اجرای موفق Reranker در آن ثبت نشده است.
2. NB22E v2 یک `KeyboardInterrupt` ذخیره‌شده در C009 دارد. خروجی موفق بعدی می‌تواند معتبر باشد، ولی آن خطای قدیمی حذف/پنهان نشده است.
3. در NB22E v2 کد C035 خروجی `COMPLETE` دارد، ولی `execution_count` برابر `null` است؛ این ناسازگاری نمای ذخیره‌شده است، نه به‌تنهایی اثبات اجرای ناموفق.
4. NB22E v2 آخرین سل C046 را خالی نشان می‌دهد، درحالی‌که خروجی اجرای C046 در چت جدا فرستاده شده است؛ این دو باید در تجمیع آینده به‌صورت دو منشأ مجزا ثبت شوند.
5. NB22F و C035 دارای Validation و Check درون Development هستند و برچسب‌های تاریخی احتمالاً قبلاً مشاهده شده‌اند؛ آزمون «independent holdout release» نامیده نشوند.
6. در تمام نوت‌بوک‌های ارسالی، خود فایل‌های Notebook از نظر JSON و نحو Python کنترل شدند؛ به‌جز استثناهای اجرایی فوق، خطای Parse/Syntax مشاهده نشد. صحت اجرای زندهٔ API، بایت تمام Artifactهای محلی، و معنای مستقل Gold در این ممیزی **تأیید نشده** است.

## مسیر منطقی بعد از این ممیزی

**تا ارائهٔ تصمیم، اجرای سل و API جدید لازم نیست.** اول نتایج ذخیره‌شدهٔ NB22F و C035 و C037 را مبنای مشترک قرار دهید؛ روش شکست‌خوردهٔ C045 یا ONNX400 را بی‌دلیل تکرار نکنید. اگر مسیر بهبود از سر گرفته شد، یک تغییر عملی و Gold-blind در candidate retrieval/selection لازم است که روی همان جمعیت Validation و Check، با حفظ Baseline و ثبت ناموفق‌ها، اثر مستقل از صرفِ سقف Oracle را نشان دهد. مسئلهٔ کفایت معنایی Gold باید جدا و با منشأ روشن پیگیری شود، نه با دستکاری شاخص برای قبولی.

---

## جزئیات آزمایش‌های محاسباتی که نباید دوباره اجرا شوند

- NB22E C010: یک آزمایش کامل ONNX400/Fusion بر ۶۰ سؤال Development، **۲۴٬۰۰۰ جفت امتیازدهی محلی تازه**؛ Recall از 78.89% به 76.94% کاهش یافت و علت افت غالباً جابه‌جایی شاهدهای Transcript توسط خود مدل بود. زمان اجرا حدود ۳۸۸۱ ثانیه برای مسیر ثبت‌شده (مقایسهٔ زمان با مسیرهای Cacheدار منصفانه نیست).
- NB22E C019: BGE Top40 روی ۶۰ سؤال اول، **۱۲۰۰ جفت تازه** با امکان مصرف Cache؛ عبور عددی 85.14/77.63 فقط روی نمونهٔ دیده‌شده.
- NB22E C021: BGE Top40 فریز‌شده روی ۶۰ سؤال دیگر، **۲۴۰۰ جفت تازه**؛ رشد همانند نمونهٔ انتخابی تکرار نشد.
- NB22E C027: BGE Top100 + RRF ثابت، **۷۲۰۰ جفت تازه**؛ دو جمعیت ۶۰تایی: در اول Recall=83.89%/nDCG=75.37% و در دوم Recall=82.08%/nDCG=74.17%؛ هیچ‌کدام همزمان هدف 85/75 را تأمین نکردند. اجرای Pure-BGE Top100 در همان گزارش روی جمعیت اول 85.14%/76.84% و روی دوم 82.92%/72.72% ثبت شده است. این نتایج از Cache همان آزمایش‌اند، اجرای عمومی ۲۶۶۴سؤالی نیستند.
- NB22E C033: مقایسهٔ دوباره بر **۱۲۰ سؤال مشترک** (توصیفی، نه holdout مستقل): Baseline=80.07% Recall و 70.79% nDCG؛ BGE+RRF Top40=82.99% و 74.75%؛ Top100 تقریباً برابر. این جدول برای *مقایسهٔ کنترل‌شدهٔ همان جمعیت* ارزشمند است اما به 85/75 نمی‌رسد.
- NB22E C034: یادگیری ترکیب وزن‌دار BGE/انباشت Cached، Fit=60، Validation=26، Check=34. در Validation، nDCG برای Weighted Ridge بهتر شد (79.39% در برابر Top40=75.43%)؛ ولی در Check، Top40=76.89% و Weighted Ridge=75.32% شد، با Recall یکسان 84.31%. تعمیم بهبود Validation اثبات نشد.
- NB22E C035: Window-only در ۵۳۳ Validation نسبت به Baseline افت شدیدی داشت (Recall 54.94% در برابر 66.52%). ترکیب Window+Baseline نیز Recall=63.18% پایین‌تر بود. برندهٔ ثبت‌شده Baseline است؛ Check=624 همین برنده را تأیید کرده، نه کیفیت مطلوب را.
- NB22E C040: آزمایش تشخیصی Gold-conditioned روی ۶ سؤال به‌صورت ذخیره‌شده **۶/۶ کامل**، ۷۴۱ جفت محلی تازه و بازیابی ۳ شاهد از ۱۰ شاهد عمیق به Top10؛ چون Gold در ساخت Pool تشخیصی دخیل است، نتیجه برای خط تولید قابل‌استفاده نیست.
- NB22E C042–C044: این‌ها بررسی **اعتبار اتصال Gold به شواهد** هستند، نه بهبود موتور. در C043 با تعریف تشخیصی جدید Recall به 83.73% رسید، اما Hit از 86.06% به 84.37% افت کرد؛ معیار تاریخی نباید جایگزین شود.
- NB22E C045: انتخاب Gold-blind با RRF روی کل ۵۳۳ Validation، Top100 از 79.03% به 79.58% رسید؛ ۱۸ بهتر، ۱۷ بدتر، ۴۹۸ برابر؛ Website اندکی افت کرد و روش با `CAPACITY_SCREEN_FAIL_NO_NEW_BGE` رد شد.

**استفادهٔ مجدد:** اجرای مجدد این سل‌ها صرفاً برای «دیدن نتیجه» لازم نیست. دریافت دوبارهٔ Cacheها، دانلود مدل یا درخواست دوبارهٔ ۲۹ API C046 نیز ضرورت اثبات‌شده ندارد.

## پیوست: ممیزی سل‌به‌سل نسخه‌های ارسالی

در این جدول، هر ردیف یک Code Cell واقعی است. متن Markdown و Code در ساختار فایل خوانده و کل خروجی‌های متنی بررسی و اندیس‌گذاری شده‌اند. ستون `status` از خروجی همان سل استخراج شده؛ حالت `بدون JSON روشن` به معنی انجام‌نشدن نیست. `saved_count` فقط شمارهٔ اجرای ذخیره‌شدهٔ همان فایل است؛ مستقل‌بودن Run All را اثبات نمی‌کند.

### NB22 — `22_release_and_reproducibility(1).ipynb`

- SHA256 بایت فایل پیوست: `2a7a1d4c11418bb6008e202c38d5d845092d5a8bd20c9f734a1631e770e4acbd`. تعداد کل سل‌ها: 117؛ کد: 58؛ Markdown: 59.

| سل فیزیکی (از ۰) | شناسه/عنوان موجود در کد | اجرای ذخیره‌شده | وضعیت ذخیره‌شده | توضیح ساختاری |
|---:|---|---:|---|---|
| 1 | `# NB21-C001 — Centralized standard-library imports for NB21.` | 1 | `—` |  |
| 3 | `# NB22-C02 — Read-only final-handoff preflight` | 2 | `READONLY_PREFLIGHT_COMPLETED_NOT_ACCEPTANCE` |  |
| 5 | `# NB22-C03 — Consume NB21 summary and direct handoff package` | 3 | `PRIOR_DOCUMENTED_WORK_PRESERVED_NOT_REAUDITED` |  |
| 7 | `# NB22-C04 — Action 05: persist the requirement-to-evidence ledger` | 4 | `ACTION05_EVIDENCE_MAPPING_WRITTEN_AND_RELOADED` |  |
| 9 | `# NB22-C05 — Action 06, package 1: targeted acceptance evidence` | 5 | `ACTION06_PACKAGE1_EVIDENCE_ASSEMBLED_NOT_ACCEPTANCE` |  |
| 11 | `# NB22-C06 — Action 06: package-level acceptance reconciliation` | 6 | `PACKAGE_EVIDENCE_RECONCILIATION_RECORDED_REVIEW_PENDING` |  |
| 13 | `# NB22-C07 — Finalize action 06 in the inspected evidence scope` | 7 | `ACTION06_RECONCILIATION_COMPLETE_IN_INSPECTED_SCOPE` |  |
| 15 | `# NB22-C08 — Action 07: collect declared versions with provenance` | 8 | `DECLARED_VERSIONS_COLLECTED_CANONICAL_SELECTION_PENDING` |  |
| 17 | `# NB22-C09 — Action 07: qualify version observations` | 9 | `VERSION_INVENTORY_QUALIFIED_WITH_EXPLICIT_BINDING_GAPS` |  |
| 19 | `# NB22-C10 — Action 07: connect declared metadata to existing provenance` | 10 | `EXISTING_VERSION_BINDINGS_ASSEMBLED` |  |
| 21 | `# NB22-C11 — Direct metadata bindings for action 07` | 11 | `DIRECT_METADATA_BINDINGS_READY_FOR_SCOPE_DECISION` |  |
| 23 | `# NB22-C12 — Action 07: bind producer manifests and scoped rubric` | 12 | `REFERENCED_METADATA_BOUND` |  |
| 25 | `# NB22-C13 — Close the action 07 inventory with explicit provenance gaps` | 13 | `ACTION07_VERSION_INVENTORY_RECORDED_WITH_EXPLICIT_GAPS` |  |
| 27 | `# NB22-C14 — Action 08: bind reference paths to observed consumers` | 14 | `REFERENCE_PATHS_RECORDED_WITH_EXPLICIT_PENDING_BINDINGS` |  |
| 29 | `# NB22-C15 — Action 09: stream byte hashes for six explicit assets` | 15 | `FILE_BYTES_MATCH_DECLARED_VALUE` |  |
| 31 | `# NB22-C16 — Action 09: configuration bindings and component manifests` | 16 | `COMPONENT_MANIFEST_AND_CONFIG_CHECKS_RECORDED` |  |
| 33 | `# NB22-C17 — Reconcile reranker configuration hash semantics` | 17 | `RERANKER_HASH_DEFINITION_EVIDENCE_ASSEMBLED` |  |
| 35 | `# NB22-C18 — Reconcile reranker payload hash with producer serialization` | 19 | `RERANKER_CONFIG_PAYLOAD_HASH_VERIFIED` |  |
| 37 | `# NB22-C19 — Action 09: physical index file byte verification` | 20 | `FILE_BYTES_MATCH_DECLARED_VALUE` |  |
| 39 | `# NB22-C20 — Consume bound index-validation evidence without rerunning tests` | 21 | `INDEX_IDENTITIES_AND_BOUND_REPORTS_ACCOUNTED` |  |
| 41 | `# NB22-C21 — Action 10: streamed JSONL structure and manifest counts` | 22 | `STRUCTURE_AND_BOUND_COUNTS_CHECKED` |  |
| 43 | `# NB22-C22 — Action 10: structural identity and reference integrity` | 23 | `CHECKED_IDENTITY_AND_REFERENCE_RELATIONS_PASS` |  |
| 45 | `# NB22-C23 — Action 10: consume existing reload-validation evidence` | 24 | `COUNT_AND_EXISTING_RELOAD_EVIDENCE_RECORDED` |  |
| 47 | `# NB22-C24 — Bind reused validation evidence and inventory restore assets` | 25 | `REUSED_VALIDATION_BOUND_AND_INITIAL_RESTORE_ASSETS_LISTED` |  |
| 49 | `# NB22-C25 — Action 11: offline snapshot and targeted cache inventory` | 26 | `SNAPSHOT_AND_TARGETED_CACHES_ACCOUNTED` |  |
| 51 | `# NB22-C26 — Action 12: initial candidate manifest from existing receipts` | 27 | `DRAFT_CANDIDATE_MANIFEST_WITH_OPEN_DEPENDENCIES` |  |
| 53 | `# NB22-C27 — Evidence-backed cards and corrected derived manifest` | 30 | `DRAFT_CANDIDATE_WITH_CARDS_AND_OPEN_DEPENDENCIES` |  |
| 55 | `# NB22-C28 — Action 18: evidence index, release notes and rollback status` | 31 | `DRAFT_WITH_EVIDENCE_INDEX_AND_OPEN_DEPENDENCIES` |  |
| 57 | `# NB22-C29 — Action 19: offline runtime facts and bounded restore plan` | 32 | `BOUNDED_OFFLINE_RESTORE_PLAN_PREPARED` |  |
| 59 | `# NB22-C30 — Action 20: isolated candidate restore and validate-only` | 33 | `ISOLATED_CANDIDATE_AND_DENSE_SNAPSHOT_RESTORE_PASS` |  |
| 61 | `# NB22-C31 — Action 21: explicit consolidation and clean-execution scope` | 34 | `CONSOLIDATION_SCOPE_RECORDED_NOT_EXECUTED` |  |
| 63 | `def nb22_c32_run():` | 35 | `RECENT_CODE_PRESENT_IN_SAVED_NOTEBOOK` |  |
| 65 | `def nb22_c33_run(c31):` | 36 | `SCOPED_SCAN_HAS_REVIEW_CANDIDATES` |  |
| 67 | `def nb22_c34_run(c33):` | 37 | `FINDINGS_GROUPED_CONTEXT_REVIEW_PENDING` |  |
| 69 | `def nb22_c35_run(c33, c34):` | 38 | `MASKED_SOURCE_CONTEXT_READY_FOR_REVIEW` |  |
| 71 | `def nb22_c36_run(c35):` | 39 | `ALL_CACHED_SOURCE_CONTEXTS_GROUPED` |  |
| 73 | `def nb22_c37_run(c33):` | 41 | `SEVEN_DERIVED_NOTEBOOK_COPIES_WRITTEN_AND_RELOADED` |  |
| 75 | `def nb22_c38_run(c28, c37):` | 42 | `PACKAGE_SCAN_HAS_REVIEW_CANDIDATES` |  |
| 77 | `def nb22_c39_run(c38):` | 43 | `TWO_DOCUMENTATION_VIEWS_WRITTEN_OR_REUSED` |  |
| 79 | `def nb22_c40_run(c38, c39):` | 44 | `ELEVEN_RELATIVE_REFERENCE_BINDINGS_ESTABLISHED` |  |
| 81 | `def nb22_c41_run(c40):` | 45 | `ISOLATED_RELATIVE_REFERENCE_VALIDATION_PASS` |  |
| 83 | `def nb22_c42_run(c28, c30, c37, c38, c39, c40, c41):` | 46 | `EXPANDED_LOCAL_DRAFT_WITH_OPEN_RELEASE_REQUIREMENTS` |  |
| 85 | `def nb22_c43_run(c03, c06):` | 47 | `CACHED_NB21_JSONL_REFERENCES_EXTRACTED` |  |
| 87 | `def nb22_c44_run(c03):` | 48 | `EXACT_CACHED_BINDING_SECTIONS_EXTRACTED` |  |
| 89 | `# NB22-C045 — Action 24: consolidated documentation export` | 49 | `ACTION24_DOCUMENTATION_EXPORT_COMPLETE_IN_DECLARED_SCOPE` |  |
| 91 | `# NB22-C046 — Action 25: atomic checkpoint manifest and independent reload` | 50 | `ACTION25_LOCAL_CHECKPOINT_WRITE_AND_RELOAD_COMPLETE` |  |
| 93 | `# NB22-C047 — Action 26: evidence-based final release gate` | 51 | `ACTION26_GATE_RECORDED_RELEASE_NOT_ACCEPTED` |  |
| 95 | `# NB22-C048 — Action 27: record checkpoint disposition and actual acceptance` | 52 | `ACTION27_VERIFIED_LOCAL_CHECKPOINT_RECORDED_RELEASE_NOT_ACCEPTED` |  |
| 97 | `# NB22-C049 — Action 28: evidence/status handoff for NB23` | 53 | `HANDOFF_PREPARED_WITH_UNACCEPTED_RELEASE_INPUT` |  |
| 99 | `# NB22-C050 — Existing quality evidence audit, corrected root resolution` | 55 | `EXISTING_EVIDENCE_AUDIT_RECORDED` |  |
| 101 | `# NB22-C051 — Quality evidence review, package 1 of 3` | 56 | `QUALITY_REVIEW_PACKAGE1_CLASSIFICATION_COMPLETE` |  |
| 103 | `# NB22-C052 — Quality evidence review, package 2 of 3` | 57 | `QUALITY_REVIEW_PACKAGE2_CONTEXT_CHECK_RECORDED` |  |
| 105 | `# NB22-C053 — Quality evidence review, package 3 of 3` | 58 | `THREE_PACKAGE_QUALITY_EVIDENCE_REVIEW_COMPLETE_IN_SCOPE` |  |
| 107 | `# NB22-C054 — Consolidate quality findings into the handoff and next-work plan` | 59 | `QUALITY_EVIDENCE_RECONCILED_PRIOR_NONACCEPTANCE_PRESERVED` |  |
| 109 | `# NB22-C055 — Retrieval verification, package 1 of 2` | 60 | `RETRIEVAL_BINDINGS_AND_PRODUCER_FORMULAS_RECORDED` |  |
| 111 | `# NB22-C056 — Independent retrieval metric verification, package 2 of 2` | 61 | `INDEPENDENT_RECOMPUTATION_MATCHES_RECORDED_METRICS` |  |
| 113 | `# NB22-C057 — Exact blocked-metric decisions and acceptance contract` | 62 | `EXACT_BLOCKED_DECISIONS_AND_CONTRACT_CONNECTED` |  |
| 115 | `# NB22-C058 — Final acceptance work inventory and cached retrieval diagnostics` | 63 | `VERIFICATION_AND_REMAINING_WORK_INVENTORY_COMPLETE` |  |

### NB22B — `22b_quality_improvement_and_acceptance(2).ipynb`

- SHA256 بایت فایل پیوست: `8e37c2f87b9e4e1195a7ad4011c8d7297ccfe69228deaccf6572d260ccefb063`. تعداد کل سل‌ها: 39؛ کد: 18؛ Markdown: 21.

| سل فیزیکی (از ۰) | شناسه/عنوان موجود در کد | اجرای ذخیره‌شده | وضعیت ذخیره‌شده | توضیح ساختاری |
|---:|---|---:|---|---|
| 3 | `# NB22B-C001 — Imports only; no model, file write, download or API call.` | 1 | `—` |  |
| 5 | `# NB22B-C002 — Explicit pinned inputs and complete checklist.` | 2 | `READ_ONLY_PREFLIGHT_COMPLETE` |  |
| 7 | `# NB22B-C003 — Shared validated mechanics; no historical notebook execution.` | 3 | `—` |  |
| 9 | `# NB22B-C004 — Action 1: scope, lineage and acceptance boundaries.` | 4 | `SCOPE_AND_PRIOR_DECISION_BOUND` |  |
| 11 | `# NB22B-C005 — Action 2: versioned inputs, caches and test boundary.` | 5 | `INPUTS_AND_EVALUATION_BOUNDARY_RECORDED` |  |
| 13 | `# NB22B-C006 — Action 3: exact Development pool/rank diagnostics.` | 6 | `DEVELOPMENT_DIAGNOSTICS_COMPLETE` |  |
| 15 | `# NB22B-C007 — Action 4: freeze bounded experiment before candidate scores.` | 7 | `BOUNDED_DEVELOPMENT_PLAN_FROZEN` |  |
| 17 | `# NB22B-C008 — Action 5: cached rank fusion and cache-only local depth expansion.` | 8 | `CACHED_EXPERIMENTS_EXECUTED_WITH_EXPLICIT_LOCAL_RUNTIME_STATUS` |  |
| 19 | `# NB22B-C009 — Action 6: paired Development selection and source-component uncertainty.` | 9 | `DEVELOPMENT_HYPOTHESIS_SELECTED` |  |
| 21 | `# NB22B-C010 — Action 7: reuse exact response/claim/requirement evidence.` | 10 | `SEMANTIC_GAP_REVIEW_PARTIAL_OR_GATED_WITH_PRIOR_SUPPORT_REUSED` | API=58 |
| 23 | `# NB22B-C011 — Action 8: link, locator, coverage and attribution accounting.` | 11 | `LINK_LOCATOR_AND_CURRENT_MODEL_SCOPE_MEASUREMENTS_RECORDED` |  |
| 25 | `# NB22B-C012 — Action 9: exact existing no-answer evidence, without Test policy tuning.` | 12 | `HISTORICAL_ABSTENTION_REPRODUCED_SCOPED_F1_BELOW_TARGET` |  |
| 27 | `# NB22B-C013 — Action 10: safety coverage and preserved issue/regression dispositions.` | 13 | `SAFETY_AND_REGRESSION_EVIDENCE_REUSED_WITH_OPEN_QUALIFICATION` |  |
| 29 | `# NB22B-C014 — Action 11: actual-runtime boundary and operational measurement qualification.` | 14 | `PRODUCT_RUNTIME_AND_JUDGE_BOUNDARIES_RECORDED` |  |
| 31 | `# NB22B-C015 — Action 12: frozen-candidate historical evaluation; genuine independence remains separate.` | 15 | `HISTORICAL_COMPARISON_RECORDED_INDEPENDENT_PRODUCT_EVALUATION_OPEN` |  |
| 33 | `# NB22B-C016 — Action 13: producer/source identity, environment and publication scope.` | 16 | `DERIVATIVE_PRODUCER_BOUND_FULL_PRODUCT_CLOSURE_OPEN` |  |
| 35 | `# NB22B-C017 — Action 14: independently reload generated evidence and record actual acceptance.` | 17 | `EXPERIMENT_AND_EVIDENCE_REPORT_COMPLETE_ACCEPTANCE_NOT_ESTABLISHED` |  |
| 38 | `selection = S["memory"].get("selection", {})` | 18 | `—` |  |

### NB22C — `22c_retrieval_diagnosis_and_improvement(2).ipynb`

- SHA256 بایت فایل پیوست: `e658b973c057d945add9a9f7c96c6a98b36aae1b2fca70cf958925df4de7315c`. تعداد کل سل‌ها: 20؛ کد: 9؛ Markdown: 11.

| سل فیزیکی (از ۰) | شناسه/عنوان موجود در کد | اجرای ذخیره‌شده | وضعیت ذخیره‌شده | توضیح ساختاری |
|---:|---|---:|---|---|
| 2 | `# NB22C-C001 — Imports only; standard library, no file/network/model operations.` | 1 | `—` |  |
| 4 | `# NB22C-C002 — Read-only bootstrap and explicit configuration.` | 2 | `—` |  |
| 6 | `# NB22C-C003 — Shared mechanics; no historical notebook is executed.` | 3 | `—` |  |
| 8 | `# NB22C-C004 — Action 1: bind exact prior results and Development inputs.` | 4 | `COMPLETE_IN_SCOPE` |  |
| 10 | `# NB22C-C005 — Action 2: coverage ceilings, rank losses and source components.` | 5 | `COMPLETE_IN_SCOPE` |  |
| 12 | `# NB22C-C006 — Action 3: freeze bounded hypotheses before candidate evaluation.` | 6 | `COMPLETE_IN_SCOPE` |  |
| 14 | `# NB22C-C007 — Action 4: execute cached-rank experiments and freeze one winner.` | 7 | `COMPLETE_IN_SCOPE` |  |
| 16 | `# NB22C-C008 — Action 5: assess one frozen candidate on internal validation.` | 8 | `COMPLETE_IN_SCOPE` |  |
| 18 | `# NB22C-C009 — Action 6: concrete final decision, unresolved work and evidence.` | 9 | `COMPLETE_IN_SCOPE` |  |

### NB22D — `22d_full_corpus_retrieval_expansion(3).ipynb`

- SHA256 بایت فایل پیوست: `fff5bd072a4977820882045451b61d66f8621ef9a4918775e4534800f0ae1480`. تعداد کل سل‌ها: 18؛ کد: 8؛ Markdown: 10.

| سل فیزیکی (از ۰) | شناسه/عنوان موجود در کد | اجرای ذخیره‌شده | وضعیت ذخیره‌شده | توضیح ساختاری |
|---:|---|---:|---|---|
| 2 | `# NB22D-C001 — Imports only; standard library, no file/network/model operations.` | 1 | `—` |  |
| 4 | `# NB22D-C002 — Explicit offline experiment, no dispatch or inference fallback.` | 2 | `—` |  |
| 6 | `# NB22D-C003 — Shared mechanics; no historical notebook is executed.` | 3 | `—` |  |
| 8 | `# NB22D-C004 — Action 1: exact corpus, Golden and NB22C retained candidate.` | 4 | `COMPLETE_IN_SCOPE` |  |
| 10 | `# NB22D-C005 — Action 2: freeze a corpus-wide retrieval change.` | 5 | `COMPLETE_IN_SCOPE` |  |
| 12 | `# NB22D-C006 — Action 3: full corpus lexical retrieval, checkpointed per query.` | 6 | `COMPLETE_IN_SCOPE` | q=2664 |
| 14 | `# NB22D-C007 — Action 4: choose coverage and ranking candidates on tuning only.` | 7 | `COMPLETE_IN_SCOPE` |  |
| 16 | `# NB22D-C008 — Action 5: internal validation and visible acceptance tables.` | 8 | `COMPLETE_IN_SCOPE` |  |

### NB22E v1 — `22e_retrieval_experiment_lab_v1(3).ipynb`

- SHA256 بایت فایل پیوست: `35b814de0a10ca3e7db1b7c4dbf24ca35dcdde99eecc6b8a2c952e8cf90bddca`. تعداد کل سل‌ها: 18؛ کد: 8؛ Markdown: 10.

| سل فیزیکی (از ۰) | شناسه/عنوان موجود در کد | اجرای ذخیره‌شده | وضعیت ذخیره‌شده | توضیح ساختاری |
|---:|---|---:|---|---|
| 2 | `# NB22E-C001 — Imports only; standard library, no file/network/model operations.` | 1 | `—` |  |
| 4 | `# NB22E-C002 — Shared settings, exact inputs, engine and frozen pilot.` | 2 | `—` |  |
| 6 | `# NB22E-C003 — Independent complete route: baseline_D` | 3 | `BLOCKED_SETUP` |  |
| 8 | `# NB22E-C004 — Independent complete route: onnx200` | 4 | `BLOCKED_SETUP` |  |
| 10 | `# NB22E-C005 — Independent complete route: onnx400` | 5 | `BLOCKED_SETUP` |  |
| 12 | `# NB22E-C006 — Independent complete route: onnx800` | 6 | `BLOCKED_SETUP` |  |
| 14 | `# NB22E-C007 — Independent complete route: onnx400_fusion` | 7 | `BLOCKED_SETUP` |  |
| 16 | `# NB22E-C008 — Compare identical complete pilot cohorts; no full-run dispatch.` | 8 | `BLOCKED_SETUP` | q=0 |

### NB22E v2 — `22e_retrieval_experiment_lab_v2(6).ipynb`

- SHA256 بایت فایل پیوست: `c3387465e2eaa8fefe2928483a16832b90cc5ff8fbd2d3d89ab0115a83c887c7`. تعداد کل سل‌ها: 94؛ کد: 47؛ Markdown: 47.

| سل فیزیکی (از ۰) | شناسه/عنوان موجود در کد | اجرای ذخیره‌شده | وضعیت ذخیره‌شده | توضیح ساختاری |
|---:|---|---:|---|---|
| 2 | `# NB22E-C001 — Imports only; standard library, no file/network/model operations.` | 1 | `—` |  |
| 4 | `# NB22E-C002 — Shared settings, exact inputs, engine and frozen pilot.` | 2 | `—` |  |
| 6 | `# NB22E-C003 — Independent complete route: baseline_D` | 3 | `COMPLETE` | q=12 |
| 8 | `# NB22E-C004 — Independent complete route: onnx200` | 4 | `PARTIAL_HELD_NOT_ELIGIBLE` | q=0 |
| 10 | `# NB22E-C005 — Independent complete route: onnx400` | 5 | `PARTIAL_HELD_NOT_ELIGIBLE` | q=0 |
| 12 | `# NB22E-C006 — Independent complete route: onnx800` | 6 | `PARTIAL_HELD_NOT_ELIGIBLE` | q=0 |
| 14 | `# NB22E-C007 — Independent complete route: onnx400_fusion` | 7 | `PARTIAL_HELD_NOT_ELIGIBLE` | q=0 |
| 16 | `# NB22E-C008 — Compare identical complete pilot cohorts; no full-run dispatch.` | 8 | `COMPLETE` | q=12 |
| 18 | `# NB22E-C009 — آزمایش یکپارچه با نسخهٔ مستقل امتیازهای محلی` | 41 | `—` | خطای ذخیره‌شده: KeyboardInterrupt |
| 20 | `# NB22E-C010 — Action 3: frozen onnx400_fusion on 60 additional Development queries.` | 10 | `COMPLETE` | q=60 |
| 22 | `# NB22E-C011 — Action 4: offline diagnosis and bounded rank-only experiments.` | 11 | `—` |  |
| 24 | `# NB22E-C012 — Local tokenizer/evidence-position audit; no model inference.` | 12 | `COMPLETE_IN_SCOPE` |  |
| 26 | `# NB22E-C013 — Export contrastive cases from existing files/cache only.` | 13 | `COMPLETE_IN_SCOPE` |  |
| 28 | `# NB22E-C014 — Offline model/runtime inventory; no inference or downloads.` | 14 | `COMPLETE_IN_SCOPE` |  |
| 30 | `# C015 v2 — Local model verification only` | 16 | `PINNED_FILES_VERIFIED_NOT_EXECUTED` |  |
| 32 | `# C016 v3 — Verified project passages + bounded local BGE CPU pilot` | 19 | `PILOT_COMPLETE` |  |
| 34 | `# C017 v1 — BGE reranks baseline Top20; resumable local scoring.` | 20 | `COMPLETE` | local_pairs=1200؛ q=60 |
| 35 | `print(json.dumps(C017, ensure_ascii=False, indent=2))` | 21 | `COMPLETE` | local_pairs=1200؛ q=60 |
| 37 | `# C018 v1 — Offline candidate-depth ceilings; no model inference.` | 22 | `COMPLETE` | q=60 |
| 39 | `# C019 v1 — Extend BGE Top20 to Top40, preserving the score contract/cache.` | 23 | `COMPLETE` | local_pairs=1200؛ q=60 |
| 41 | `# C020 v2 — Freeze BGE Top40 and reserve a new Dev cohort.` | 26 | `METHOD_FROZEN_COHORT_RESERVED` |  |
| 43 | `# C021 v1 — Verified NB22D replay + frozen BGE Top40 on reserved Dev60.` | 27 | `COMPLETE` | local_pairs=2400؛ q=60 |
| 45 | `# C022 v2 — Correct offline audit of both BGE Top40 cohorts.` | 30 | `COMPLETE` | decision=KEEP_BASELINE_NO_AUTOMATIC_REPLACEMENT |
| 47 | `# C023 v1 — One fixed, rank-only fusion experiment.` | 31 | `COMPLETE` | decision=EXPLORATORY_CANDIDATE_ONLY_REQUIRES_SEPARATE_VALIDATION |
| 49 | `# C024 v1 — Offline Top40 coverage and ranking-gap decomposition.` | 32 | `COMPLETE` |  |
| 51 | `# C025 v1 — Offline candidate coverage across 120 Dev questions.` | 33 | `COMPLETE` | q=120 |
| 53 | `# C026 v1 — Preserve baseline Top40; add up to 60 pool candidates` | 34 | `COMPLETE` |  |
| 55 | `# C027 v1 — Baseline Top100 -> BGE -> fixed equal-weight RRF(k=60).` | 35 | `COMPLETE` | local_pairs=7200 |
| 57 | `# C028 v1 — Final scoped reporting; no inference or model loading.` | 36 | `COMPLETE` |  |
| 59 | `# C029 v1 — Protected Top40 + alternating word/char candidates.` | 37 | `COMPLETE` |  |
| 61 | `# C030 v1 — Bounded local inventory of semantic-retrieval code and files.` | 38 | `COMPLETE_IN_SCOPE` |  |
| 63 | `# C031 v1 — Cached E5 vectors -> direct semantic rankings -> coverage.` | 39 | `COMPLETE` |  |
| 65 | `# C032 v1 — Scoped decision record and open-work ledger.` | 40 | `COMPLETE` |  |
| 67 | `# C033 v1 — Common-question comparison using existing E/F artifacts.` | 42 | `COMPLETE` |  |
| 69 | `# C034 v1 — Learn baseline/BGE combination from existing Top100 scores.` | 43 | `COMPLETE` |  |
| 71 | `# C035 v2 — Complete window-retrieval experiment with resumable caching.` | — | `COMPLETE` | Output ذخیره‌شده ولی ExecutionCount خالی |
| 73 | `# C036 v1 — Coverage ceiling, validated cache counts, and runtime estimate.` | 45 | `COMPLETE` | decision=NEITHER_TOP40_NOR_TOP100_CAN_MEET_RECALL_TARGET;DO_NOT_START_BGE_FOR_TARGET_ACCEPTANCE_ON_THESE؛ q=533 |
| 75 | `# C037 v1 — Offline coverage and witness-rank diagnosis on Dev validation533.` | 46 | `COMPLETE` | q=533 |
| 77 | `# C038 v1 — Protected Top40 + existing F ridge shortlist.` | 47 | `COMPLETE` |  |
| 79 | `# C039 v1 — Boundary-aware shortlist training.` | 48 | `COMPLETE` |  |
| 81 | `# C040 v1 — Gold-conditioned diagnostic of BGE ranking ability.` | 50 | `COMPLETE` | local_pairs=741 |
| 83 | `# C041 v1 — Text/input inspection pack for C040's six diagnostic cases.` | 51 | `COMPLETE` | q=6 |
| 85 | `# C042 v1 — Exact locator/span-to-chunk audit; no label changes.` | 52 | `COMPLETE_IN_SCOPE` | q=533 |
| 87 | `# C043 v1 — Diagnostic metric sensitivity to exact-span chunk membership.` | 53 | `COMPLETE_IN_SCOPE` |  |
| 89 | `# C044 v1 — One consolidated semantic-review packet.` | 54 | `COMPLETE` |  |
| 91 | `# NB22E-C045 — Frozen label-blind Top100 RRF (schema repair)` | 56 | `COMPLETE_IN_SCOPE` | decision=CAPACITY_SCREEN_FAIL_NO_NEW_BGE؛ q=533 |
| 93 | `بدون متن` | — | `—` | سل بدون اجرای ذخیره‌شده |

### NB22F — `22f_consolidated_retrieval_benchmark_v1(2).ipynb`

- SHA256 بایت فایل پیوست: `8d08726f1fe894224b3a035309a2210c600f6c518f86e3e387dabc4c18961efb`. تعداد کل سل‌ها: 18؛ کد: 8؛ Markdown: 10.

| سل فیزیکی (از ۰) | شناسه/عنوان موجود در کد | اجرای ذخیره‌شده | وضعیت ذخیره‌شده | توضیح ساختاری |
|---:|---|---:|---|---|
| 2 | `import os, json, math, hashlib, time, tempfile, collections, re, unicodedata, io, platform` | 1 | `—` |  |
| 4 | `verified=read(C056);dfinal=read(D_FINAL);bindings=verified["input_file_receipts"]` | 2 | `—` |  |
| 6 | `parent={q:q for q in IDS}` | 3 | `—` |  |
| 8 | `handoff=read({"path":"artifacts/phase2/embedding/nb14_dense_index_handoff_v1.json","sha256":"77eb9f34e36f` | 4 | `—` |  |
| 10 | `FEATURE_NAMES=['dense_cosine','baseline_rr','word_rr','char_rr','hybrid_rr','word_coverage','numeric_cove` | 5 | `COMPLETE` |  |
| 12 | `require(FEATURES_READY,"RUN_F005_UNTIL_COMPLETE")` | 6 | `—` |  |
| 14 | `ROUTES=['baseline','dense_only','word_char_rrf','dense_word_char_rrf','linear_ridge','pairwise_linear']` | 7 | `—` |  |
| 16 | `frozen=read(FREEZE);require(frozen['winner']==WINNER,'SELECTION_CHANGED')` | 8 | `EXPERIMENT_COMPLETE` |  |
