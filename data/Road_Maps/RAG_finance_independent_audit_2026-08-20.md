<div dir="rtl" align="right">

# گزارش مستقل ممیزی فنی RAG_finance

وضعیت Phase 2، معماری RAG، آمادگی محصول و مسیر دانش‌بنیان

| **Repository** | <bdi dir="ltr">Shahbazi-Amir/RAG_finance</bdi>                |
|----------------|------------------------------------------|
| **Branch**     | rag-phase2                               |
| **Commit**     | <bdi dir="ltr">96c0f0c7d09f4bff107ed71664a0c57ed09f3214</bdi> |
| **تاریخ**      | ۲۰ اوت ۲۰۲۶                              |
| **دامنه**      | ممیزی فقط‌خواندنی؛ بدون تغییر در مخزن     |

## ۱. Executive Summary

### حکم نهایی کوتاه

مسیر کلان پروژه—ساخت RAG تخصصی سواد مالی بر پایه مقاله، کتاب و Transcript—**درست و قابل دفاع است**؛ اما وضعیت فعلی مخزن هنوز یک **نمونه مهندسی/تحقیقاتی با دو نسل متفاوت** است، نه محصول Production Ready و نه پرونده آماده ارزیابی دانش‌بنیان.

مخزن دو لایه دارد:

1.  **نسل قدیمی Demo:** زنجیره کامل Embedding → Qdrant → Retrieval → Generation → Streamlit که روی ۷۶ مقاله و ۱۶۸ Chunk ساخته شده است. این لایه برای اثبات امکان‌پذیری خوب است، اما Dense-only، بدون Reranker، بدون Hybrid Search، بدون Citation در سطح ادعا و با ارزیابی بسیار کوچک است.

2.  **نسل جدید Phase 2:** Website Ingestion V2 برای ۵۲۹ مقاله با Discovery، Raw Snapshot، Hash، Validation، Stable ID، Manifest، Extraction و Quality Summary. این بخش نسبت به Demo قدیمی بسیار حرفه‌ای‌تر است، ولی هنوز Notebookمحور است و خروجی‌های اصلی آن به‌علت .gitignore داخل مخزن نیستند.

کتاب‌ها و Transcriptها به‌عنوان **ورودی داده** در Repository وجود دارند: ۷ فایل DOCX کتاب و ۲۱۳ فایل Markdown در مجموعه نهایی Transcript. بااین‌حال Pipeline استاندارد و قابل بازتولید Phase 2 برای این دو منبع، Schema رسمی، Manifest مستقل، Chunking منبع‌محور و Lineage یکپارچه هنوز وجود ندارد.

### امتیاز پیشرفت واقعی

بر اساس ۳۸ بند Roadmap ارائه‌شده و روش امتیازدهی DONE=1، PARTIAL=0.5، MISSING=0 و حذف NOT NEEDED از مخرج:

- **پیشرفت Phase 2: حدود ۳۹٪** (14.5 / 37)

- **آمادگی Production: حدود ۲۰٪**

- **آمادگی پرونده فنی دانش‌بنیان: حدود ۲۵٪**

این درصدها اندازه‌گیری مدیریتی‌اند، نه گواهی رسمی. دلیل اختلاف آن‌ها این است که داشتن داده و Notebook با داشتن محصول پایدار، قابل آزمون، قابل استقرار و قابل دفاع نزد ارزیاب یکسان نیست.

### تصمیم Go / No-Go

- ادامه پروژه: **GO**

- ارائه فوری برای ارزیابی دانش‌بنیان: **NO-GO**

- ادامه با همان معماری Demo قدیمی: **NO-GO**

- ادامه با معماری سه‌منبعی، Provenance، Hybrid Retrieval، Reranking، Citation، Safety و Evaluation: **GO**

### پنج فاصله بحرانی

1.  نبود Dataset یکپارچه و Versioned برای هر سه منبع.

2.  نبود استناد دقیق به صفحه/فصل/زمان و نبود Claim-level Citation.

3.  نبود Benchmark و Golden Dataset معتبر؛ ارزیابی فعلی فقط ۱۰ سؤال است.

4.  نبود تست، CI، Docker، Lockfile و مسیر اجرای قابل بازتولید.

5.  نبود پرونده R&D و شواهد تمایز فنی؛ در وضع فعلی ارزیاب می‌تواند پروژه را «مدل آماده + Vector DB» تلقی کند.

## ۲. روش ممیزی و سطح اطمینان شواهد

### شواهد مستقیم بررسی‌شده

- Tree کامل شاخه rag-phase2: ۹۰۴ Entry و ۷۱۳ فایل.

- Metadata مخزن، Branch و Commit head.

- README، .gitignore، <bdi dir="ltr">requirements.txt</bdi> و <bdi dir="ltr">config/settings.py.</bdi>

- کدهای <bdi dir="ltr">app.py</bdi> و ماژول‌های <bdi dir="ltr">src/embeddings</bdi>، <bdi dir="ltr">src/retrieval</bdi>، <bdi dir="ltr">src/generation</bdi>، <bdi dir="ltr">src/cache</bdi> و <bdi dir="ltr">src/pipeline.</bdi>

- Notebook جدید <bdi dir="ltr">notebooks/phase2/01_website_ingestion.ipynb</bdi> شامل ۱۷۵ Cell؛ هر ۸۲ Code Cell اجرا شده و Error ذخیره‌شده ندارد.

- Notebookهای قدیمی Preprocessing، Chunking، Embedding، Vector Store، Retrieval، Generation، Pipeline و Evaluation.

- <bdi dir="ltr">website_manifest_v1.json</bdi> با ۵۲۹ رکورد.

- فایل ارزیابی ۱۰ سؤالی و چند نمونه Transcript و اسناد بازبینی آن‌ها.

- تاریخچه Commitهای اصلی شاخه، شامل اضافه‌شدن Transcriptها و کتاب‌ها در ۲۰ اوت ۲۰۲۶.

### شواهد غیرقابل بازاجرای مستقل در این ممیزی

خروجی‌های زیر در .gitignore هستند و در Tree Commit بررسی‌شده وجود ندارند:

- <bdi dir="ltr">data/phase2/raw/</bdi>

- <bdi dir="ltr">data/phase2/interim/website_extracted_v2.json</bdi>

- <bdi dir="ltr">reports/phase2/data_quality/website_extraction_v2.json</bdi>

- <bdi dir="ltr">reports/phase2/ingestion/website_ingestion_v2.json</bdi>

- Vector Store و Embeddingهای تولیدشده

بنابراین صحت اعداد ۵۲۹/۵۲۹ از دو مدرک پشتیبانی می‌شود: خروجی‌های ذخیره‌شده داخل Notebook و فایل Manifest؛ اما Snapshotهای ignored در این ممیزی مجدداً اجرا یا Hash-verify نشدند. برای ممیزی رسمی باید Artifact Registry یا Dataset Release قابل دریافت وجود داشته باشد.

## ۳. وضعیت فعلی Repository

### ۳.۱ ساختار کلیدی

| **مسیر**                                       | **وضعیت واقعی**                                                                       | **ارزیابی**                                   |
|------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------|
| <bdi dir="ltr">README.md</bdi>                                      | معرفی مفهومی RAG؛ هنوز از مقاله و کتاب نام می‌برد و وضعیت سه‌منبعی جدید را منعکس نمی‌کند | ناقص/قدیمی                                    |
| <bdi dir="ltr">notebooks/phase2/01_website_ingestion.ipynb</bdi>    | Pipeline کامل Website V2، ۵۲۹ مقاله، Hash و Validation                                | قوی‌ترین دارایی فنی فعلی                       |
| <bdi dir="ltr">data/phase2/manifests/website_manifest_v1.json</bdi> | ۵۲۹ رکورد با Stable ID و Version                                                      | مفید ولی محدود به وب‌سایت                      |
| <bdi dir="ltr">data/books/</bdi>                                    | ۷ فایل DOCX، شامل نسخه‌های ظاهراً مشابه/بازطراحی‌شده                                     | داده موجود؛ Pipeline وجود ندارد               |
| <bdi dir="ltr">data/transcripts/final/</bdi>                        | ۲۱۳ فایل MD در ۷ مجموعه                                                               | داده ارزشمند؛ Schema و Timestamp یکنواخت نیست |
| <bdi dir="ltr">notebooks/02...10</bdi>                              | زنجیره RAG قدیمی روی ۷۶ مقاله و ۱۶۸ Chunk                                             | <bdi dir="ltr">Demo/Prototype</bdi>                                |
| <bdi dir="ltr">src/</bdi>                                           | چهار جزء اصلی RAG و Cache                                                             | کد ساده و قابل فهم؛ نه Production Grade       |
| <bdi dir="ltr">app.py</bdi>                                         | Streamlit chat، تاریخچه JSON و نمایش Source                                           | Demo UI                                       |
| <bdi dir="ltr">data/evaluation/...json</bdi>                        | ۱۰ سؤال؛ ۸ in-scope و ۲ out-of-scope                                                  | Smoke test، نه Benchmark                      |
| <bdi dir="ltr">tests/</bdi>                                         | وجود ندارد                                                                            | بحرانی                                        |
| <bdi dir="ltr">.github/workflows/</bdi>                             | وجود ندارد                                                                            | <bdi dir="ltr">CI/CD</bdi> وجود ندارد                              |
| <bdi dir="ltr">docs/</bdi>                                          | وجود ندارد                                                                            | مستندسازی معماری/عملیات وجود ندارد            |
| <bdi dir="ltr">Docker/Compose</bdi>                                 | وجود ندارد                                                                            | استقرار بازتولیدپذیر وجود ندارد               |

### ۳.۲ شاخه و تاریخچه

- Default branch مخزن main است، اما ممیزی روی rag-phase2 انجام شد.

- Head شاخه: 96c0f0c7 با پیام ogtanos aram added در ۲۰ اوت ۲۰۲۶.

- Commit قبلی f46501cc هفت فایل کتاب را اضافه کرده است.

- Commit 9e2e1ebf مجموعه‌های چهلستون/بانک ملت و فایل‌های مرتبط را اضافه کرده است.

- تاریخچه قدیمی‌تر از June–July 2026 نشان‌دهنده ساخت مرحله‌ای Demo: ingestion، chunking، embedding، Qdrant، retrieval، generation، cache، app و evaluation است.

- Branch محافظت‌شده نیست و Required Status Check ندارد.

- Commit head امضاشده/Verified نیست.

- نام و کیفیت پیام Commitها یکنواخت نیست (just، ogtanos aram added و غلط‌های نگارشی). این موضوع مانع فنی محصول نیست، اما برای پرونده قابل ممیزی و مدیریت R&D ضعیف است.

### ۳.۳ داده‌های موجود

- ۵۲۹ مقاله در Website Manifest.

- ۷ فایل DOCX کتاب؛ چند فایل ممکن است نسخه‌های متفاوت یک اثر باشند. چون Deduplication و Canonical Book Registry وجود ندارد، تعداد «اثر مستقل» از روی نام فایل قطعی نیست.

- ۲۱۳ فایل Markdown زیر <bdi dir="ltr">data/transcripts/final/</bdi>:

- asre_shirin: ۲۶

- chehelstion_finup_ketabbaz_bankmellat: ۵۵

- dar-jostojo-final-C: ۵۹، که بخشی از آن‌ها فایل‌های <bdi dir="ltr">Audit/Extracted</bdi> هستند و همگی Episode مستقل نیستند

- khane-to: ۱۳

- mq: ۸

- tarbiat-morabi: ۱۴

- uni-tehran: ۳۸

> **عدد ۲۱۳ تعداد فایل Markdown است، نه تعداد قطعی Episode مستقل. برای عدد رسمی باید Transcript Manifest ساخته شود و فایل‌های محتوایی، Audit، Candidate و Supplemental از هم تفکیک شوند.**

### ۳.۴ Website Ingestion V2

موارد مثبت:

- کشف Pagination بدون Hard-code شدن تعداد صفحات.

- ۵۲۹ مقاله یکتا و Canonical URL بر اساس article_id.

- Stable ID به شکل website:\<article_id\>.

- ذخیره Raw HTML و <bdi dir="ltr">source.json</bdi>.

- SHA-256 روی Bytes خام.

- Validation ساختاری HTML.

- Retry، Resume و رفع Root Cause خطای <bdi dir="ltr">Cookie/HTTP</bdi> 400.

- استخراج Title، Body، Author، Tags و Metadata.

- نرمال‌سازی Soft Hyphen و متن.

- گزارش خروجی Notebook: ۵۲۹ <bdi dir="ltr">Title/Body/Author/Hash</bdi> غیرخالی.

موارد منفی:

- کل Pipeline در Notebook است؛ <bdi dir="ltr">Package/CLI/Job</bdi> مستقل ندارد.

- Manifest Commit‌شده هنوز status=discovered و author=null دارد، حتی با وجود تکمیل استخراج در خروجی Notebook؛ یعنی State نهایی و Manifest همگام نیستند.

- version=1 صرفاً یک فیلد است؛ Dataset Versioning واقعی، Changelog، Parent Version و Snapshot Hash وجود ندارد.

- Incremental Update فقط Resume دانلودهای موجود را پوشش می‌دهد؛ تشخیص <bdi dir="ltr">Add/Change/Delete</bdi> و سیاست Reprocessing مستند نیست.

- گزارش‌های تولیدشده ignored و در دسترس ممیز نیستند.

- Notebook به مسیر مطلق macOS وابسته است و Reproducibility محیطی ندارد.

- Assertions و تست خودکار وجود ندارد؛ Validationها عمدتاً print هستند.

### ۳.۵ <bdi dir="ltr">Video/Transcript</bdi>

موارد مثبت:

- حجم قابل توجه متن بازبینی‌شده و Curated.

- Metadata انسانی در ابتدای بسیاری از فایل‌ها: برنامه، قسمت، موضوع، مدت، منبع و وضعیت بازبینی.

- در dar-jostojo شواهدی از <bdi dir="ltr">Raw/Machine/Reviewed/Final</bdi> و Audit اختلاف‌ها وجود دارد؛ این یک دارایی R&D ارزشمند است.

موارد منفی:

- Schema رسمی و Machine-readable واحد وجود ندارد؛ Metadata در Markdown آزاد نوشته شده است.

- Timestamp در سطح <bdi dir="ltr">Segment/Sentence</bdi> حفظ نشده و Citation زمانی قابل اتکا نیست.

- Speaker ID در بعضی مجموعه‌ها وجود دارد و در بعضی‌ها نه؛ یکنواخت نیست.

- ASR Confidence، Segment Hash، Audio Asset ID، <bdi dir="ltr">Start/End</bdi> Time و Revision Lineage عمومی وجود ندارد.

- فایل‌های Episode، Supplemental، Candidate Difference و Review در یک Tree داده‌ای کنار هم‌اند و هنوز نقش هرکدام در Knowledge Base با Manifest تعیین نشده است.

- Validator، Chunker و Quality Report اختصاصی Transcript وجود ندارد.

### ۳.۶ Book

موارد مثبت:

- فایل‌های Word در Repository حاضرند.

- نسخه‌های بازطراحی RTL می‌تواند استخراج فارسی را ساده‌تر کند.

موارد منفی:

- هیچ Book Manifest یا Canonical Work ID وجود ندارد.

- نسخه‌های مشابه یک کتاب از هم تفکیک نشده‌اند؛ Risk ورود محتوای تکراری بالاست.

- <bdi dir="ltr">Chapter/Heading</bdi> Extraction، Paragraph Anchor، <bdi dir="ltr">Page/Location</bdi> Mapping، <bdi dir="ltr">Footnote/Table</bdi> handling و Cleaning وجود ندارد.

- صفحه در DOCX پایدار نیست؛ برای Citation باید یا PDF مرجع نهایی ثبت شود، یا Anchor پایدار فصل/بخش/پاراگراف ساخته شود.

- حقوق نشر، مجوز استفاده و دامنه مجاز نمایش متن در Repository مستند نشده است.

### ۳.۷ RAG و Application قدیمی

موارد مثبت:

- اجزای Embedder، Retriever، Generator و Cache از هم جدا شده‌اند.

- Qdrant Payload شامل chunk_id، article_id، title، url و text است.

- Prompt از مدل می‌خواهد خارج از Context پاسخ ندهد.

- UI منابع بازیابی‌شده را نمایش می‌دهد.

- برای دو سؤال out-of-scope پاسخ «در منابع موجود پاسخ کافی پیدا نشد» ثبت شده است.

موارد منفی:

- RAG فعلی روی Dataset قدیمی ۷۶ مقاله/۱۶۸ Chunk است، نه Dataset سه‌منبعی جدید.

- Retrieval فقط Dense Vector Search است؛ Hybrid، <bdi dir="ltr">Sparse/BM25</bdi> و Reranking ندارد.

- Threshold بازیابی و Answerability Model وجود ندارد؛ Abstention وابسته به رفتار LLM است.

- Citation صرفاً فهرست Sourceهای Retrieval است، نه اثبات اینکه هر ادعای پاسخ توسط کدام Span پشتیبانی شده است.

- Context Builder فقط Concatenation ساده Top-k است؛ کنترل Token Budget، Diversity، Source Balance، Dedup و Conflict ندارد.

- Cache Key فقط متن Normalizeشده سؤال است؛ Dataset Version، Model Version، Prompt Version و top_k در کلید نیستند. بنابراین پاسخ قدیمی می‌تواند بعد از تغییر Knowledge Base باقی بماند.

- در مسیر Cache، داده retrieved_chunks می‌تواند با سیاست خالی‌کردن منابع در حالت Abstention ناسازگار شود.

- تاریخچه Chat در JSON مشترک ذخیره می‌شود؛ Multi-user isolation، Privacy، Retention و Concurrent write ندارد.

- هیچ Rate Limit، Auth، Audit Log، Observability یا API Contract وجود ندارد.

- ادعای پشتیبانی از ۱۵۰۰ کاربر در README هیچ Load Test یا معماری Deployment پشتیبان ندارد.

## ۴. ماتریس تطبیق با Roadmap فاز ۲

### <bdi dir="ltr">Phase 2 Foundation</bdi>

| **مورد**           | **وضعیت** | **مدرک/فاصله**                                                                     |
|--------------------|-----------|------------------------------------------------------------------------------------|
| Freeze Phase 1     | PARTIAL   | Demo قدیمی قابل مشاهده است؛ <bdi dir="ltr">Tag/Release</bdi> رسمی، Baseline Report و Freeze policy نیست |
| Baseline           | DONE      | ۷۶ مقاله/۱۶۸ Chunk برای Demo و ۵۲۹ مقاله برای Website V2 ثبت شده                   |
| Document Schema    | PARTIAL   | Schema ضمنی Website وجود دارد؛ JSON Schema مشترک سه‌منبعی نیست                      |
| Stable IDs         | PARTIAL   | Website ID مناسب است؛ <bdi dir="ltr">Book/Video</bdi> ID استاندارد نیست                                 |
| Manifest           | PARTIAL   | فقط Website Manifest وجود دارد                                                     |
| Dataset Versioning | PARTIAL   | فیلد Version هست؛ <bdi dir="ltr">Release/Hash/Parent/Changelog</bdi> نیست                               |

### <bdi dir="ltr">Website Pipeline</bdi>

| **مورد**           | **وضعیت** | **مدرک/فاصله**                                                 |
|--------------------|-----------|----------------------------------------------------------------|
| Discovery          | DONE      | ۵۲۹ مقاله و Pagination خودکار                                  |
| Raw Storage        | DONE      | HTML + <bdi dir="ltr">source.json</bdi>؛ خروجی ignored ولی اجرای Notebook ثبت شده   |
| Extraction         | DONE      | ۵۲۹ رکورد و Metadata                                           |
| Validation         | DONE      | Hash و Structure Validation؛ ۵۲۹ معتبر در خروجی Notebook       |
| Incremental Update | PARTIAL   | Resume هست؛ <bdi dir="ltr">Diff/Delete/Reprocess</bdi> policy نیست                  |
| Crawl Report       | PARTIAL   | تولید می‌شود ولی Artifact قابل ممیزی در <bdi dir="ltr">Repository/Release</bdi> نیست |
| Processing         | DONE      | Extraction و نرمال‌سازی فارسی اولیه کامل است                    |
| Chunking           | MISSING   | Chunking V2 برای ۵۲۹ مقاله وجود ندارد                          |

### <bdi dir="ltr">Video Pipeline</bdi>

| **مورد**               | **وضعیت** | **مدرک/فاصله**                                                    |
|------------------------|-----------|-------------------------------------------------------------------|
| Transcript Schema      | PARTIAL   | Metadata انسانی موجود، Contract یکنواخت و JSON Schema نیست        |
| Validation             | PARTIAL   | بازبینی انسانی وجود دارد؛ Validator خودکار و Coverage Report نیست |
| Normalization          | PARTIAL   | متن‌های نهایی پاک‌سازی شده‌اند؛ قواعد واحد و تست‌شده نیست             |
| Timestamp Preservation | MISSING   | <bdi dir="ltr">Start/End</bdi> زمان Segmentها در خروجی نهایی نیست                      |
| Chunking               | MISSING   | Pipeline اختصاصی Video وجود ندارد                                 |

### <bdi dir="ltr">Book Pipeline</bdi>

| **مورد**            | **وضعیت**  | **مدرک/فاصله**                                                             |
|---------------------|------------|----------------------------------------------------------------------------|
| <bdi dir="ltr">PDF/EPUB</bdi> Processing | NOT NEEDED | ورودی فعلی DOCX است؛ به‌جای آن <bdi dir="ltr">DOCX/PDF-reference</bdi> processing باید اضافه شود |
| Chapter Extraction  | MISSING    | Pipeline یا خروجی فصل‌بندی دیده نشد                                         |
| Page Metadata       | MISSING    | <bdi dir="ltr">Page/Location</bdi> یا Paragraph Anchor وجود ندارد                               |
| Cleaning            | MISSING    | قواعد پاک‌سازی و QA کتاب وجود ندارد                                         |
| Chunking            | MISSING    | Chunking اختصاصی کتاب وجود ندارد                                           |

### <bdi dir="ltr">Unified Dataset</bdi>

| **مورد**       | **وضعیت** | **مدرک/فاصله**                             |
|----------------|-----------|--------------------------------------------|
| Common Schema  | MISSING   | سه منبع هنوز Contract واحد ندارند          |
| Deduplication  | MISSING   | Dedup بین نسخه کتاب/مقاله/ویدیو وجود ندارد |
| Quality Report | PARTIAL   | فقط Website Quality Summary وجود دارد      |

### <bdi dir="ltr">RAG Layer</bdi>

| **مورد**        | **وضعیت** | **مدرک/فاصله**                                         |
|-----------------|-----------|--------------------------------------------------------|
| Embedding       | PARTIAL   | Demo قدیمی؛ Dataset جدید Embedding نشده                |
| Vector Database | PARTIAL   | Qdrant Demo؛ Collection versioning و migration نیست    |
| Retrieval       | PARTIAL   | Dense-only و بدون ارزیابی Retrieval                    |
| Hybrid Search   | MISSING   | <bdi dir="ltr">BM25/Sparse</bdi> وجود ندارد                                 |
| Reranking       | MISSING   | <bdi dir="ltr">Cross-encoder/LLM</bdi> reranker وجود ندارد                  |
| Context Builder | PARTIAL   | Concatenation ساده؛ <bdi dir="ltr">Budget/Diversity/Conflict</bdi> ندارد    |
| Citation        | PARTIAL   | Source list هست؛ Claim-level و <bdi dir="ltr">Page/Time</bdi> citation نیست |

### <bdi dir="ltr">Evaluation</bdi>

| **مورد**        | **وضعیت** | **مدرک/فاصله**                                                         |
|-----------------|-----------|------------------------------------------------------------------------|
| Golden Dataset  | MISSING   | ۱۰ سؤال بدون Gold <bdi dir="ltr">Evidence/Answer</bdi>                                      |
| Benchmark       | PARTIAL   | یک Smoke Test ده‌سؤالی وجود دارد                                        |
| Regression Test | MISSING   | Gate خودکار و مقایسه نسخه‌ها نیست                                       |
| Metrics         | MISSING   | فقط شمارش Reject دو سؤال؛ <bdi dir="ltr">Retrieval/Faithfulness/Citation</bdi> metrics نیست |

## ۵. بررسی معماری «Professional Financial Literacy Advisory RAG»

### <bdi dir="ltr">Multi-source Architecture</bdi>

در سطح Intent درست است، اما در پیاده‌سازی **هنوز Multi-source نیست**. سه منبع در Storage دیده می‌شوند، ولی فقط Website V2 Pipeline دارد و RAG قدیمی فقط مقالات را مصرف می‌کند. Multi-source زمانی محقق است که هر منبع Adapter مستقل داشته باشد و همه در Common Document Contract ادغام شوند.

### <bdi dir="ltr">Data Lineage</bdi>

برای وب‌سایت بخشی از Lineage وجود دارد: URL → Raw HTML → Hash → Extracted Record. برای کتاب و Transcript، Lineage یکنواخت وجود ندارد. Lineage کامل باید این زنجیره را ثبت کند:

<div dir="ltr" align="left">source asset → source version/hash → extraction run → normalization version → document ID → chunk ID → embedding model/version → index version → retrieval event → answer → cited evidence</div>

### Citation و دفاع‌پذیری

Citation فعلی واقعی و کافی نیست. نمایش عنوان/URL منابع Retrieval ثابت نمی‌کند جمله پاسخ از همان منابع آمده است. Citation حرفه‌ای باید:

- برای Website به URL + Article ID + <bdi dir="ltr">Span/Paragraph</bdi> Anchor متصل باشد.

- برای Book به <bdi dir="ltr">Work/Edition</bdi> + Chapter + Page یا Paragraph Anchor متصل باشد.

- برای Video به <bdi dir="ltr">Program/Episode</bdi> + <bdi dir="ltr">Start/End</bdi> Timestamp متصل باشد.

- هر Claim مهم پاسخ را به یک یا چند Evidence Span نگاشت کند.

- Citation Entailment را بررسی کند: آیا Evidence واقعاً Claim را پشتیبانی می‌کند؟

### کنترل Hallucination

Prompt به‌تنهایی کنترل Hallucination محسوب نمی‌شود. کنترل قابل دفاع حداقل به این اجزا نیاز دارد:

1.  Retrieval Quality Gate و حداقل Evidence Coverage.

2.  <bdi dir="ltr">Answerability/Abstention</bdi> classifier کالیبره‌شده.

3.  تولید پاسخ در قالب Claimهای قابل Cite.

4.  Citation verification یا entailment check.

5.  سیاست Conflict، Freshness و Unknown.

6.  Regression suite برای سؤال‌های خارج از دامنه، گمراه‌کننده و تزریق Prompt.

### معماری هدف پیشنهادی

1.  **Source adapters:** Website، Book و Video؛ مستقل ولی با Contract مشترک.

2.  **Immutable raw zone:** محتوا، حقوق منبع، Hash و زمان دریافت.

3.  **Canonical document layer:** Schema واحد، Stable ID، Version و Lineage.

4.  **Source-aware chunking:** فصل/پاراگراف، Topic Shift و Timestamp.

5.  **Dual index:** Dense + <bdi dir="ltr">Sparse/BM25</bdi> با فیلتر Metadata.

6.  **Reranker:** مدل مناسب فارسی یا Multilingual و آزمایش مقایسه‌ای.

7.  **Context compiler:** Dedup، <bdi dir="ltr">MMR/Diversity</bdi>، Source balance، Token budget و conflict grouping.

8.  **Grounded generation:** پاسخ آموزشی، Claim IDs و Citation اجباری.

9.  **<bdi dir="ltr">Safety/policy</bdi> layer:** مرزبندی آموزش با توصیه سرمایه‌گذاری شخصی.

10. **<bdi dir="ltr">Evaluation/observability</bdi>:** نسخه‌محور، قابل بازتولید و دارای Release Gate.

## ۶. ارزیابی آمادگی دانش‌بنیان

### معیار رسمی و دامنه اطمینان

منابع رسمی عمومی تأکید می‌کنند ارزیابی بر محصول شرکت و تشخیص کارگروه متکی است؛ آیین‌نامه اجرایی نیز مسئولیت تدوین حوزه‌ها و معیارها را به ساختار ارزیابی می‌دهد. منابع رسمی صندوق نوآوری، «سطح فناوری/پیچیدگی»، «دانش فنی» و «نمونه اولیه» را از معیارهای اصلی معرفی کرده‌اند. همچنین آخرین نسخه معیارها و فهرست کالا/خدمت باید در سامانه رسمی زمان اقدام کنترل شود.

منابع مرجع:

- آیین‌نامه اجرایی قانون حمایت از شرکت‌های دانش‌بنیان — صندوق نوآوری و شکوفایی — <bdi dir="ltr">https://www.inif.ir/-regulations-executive-law</bdi>

- اصلاح آیین‌نامه اجرایی و وظایف کارگروه — پایگاه قوانین و مقررات — <bdi dir="ltr">https://qavanin.ir/Law/TreeText/?IDS=7646595681372737421</bdi>

- توضیح رسمی صندوق درباره معیارهای سطح فناوری، دانش فنی و نمونه اولیه — <bdi dir="ltr">https://www.inif.ir/fullcontent/-/asset_publisher/YASjeuXFqbaQ/content/id/646562</bdi>

### آیا پروژه فعلی فقط «مدل آماده + Vector DB» است؟

**در Demo فعلی: تا حد زیادی بله.** اجزای اصلی، API سازگار OpenAI، Qdrant و Streamlit هستند و Retrieval نیز Dense-only است. Website Ingestion V2 و بازبینی Transcriptها نشانه‌های مهندسی اختصاصی ارزشمندند، اما هنوز به محصول نهایی متصل و با Benchmark اثبات نشده‌اند.

### وضعیت مؤلفه‌های دفاع‌پذیری

| **مؤلفه**              | **وضعیت فعلی** | **برای دفاع چه لازم است؟**                        |
|------------------------|----------------|---------------------------------------------------|
| معماری اختصاصی         | PARTIAL        | Architecture Decision Record و پیاده‌سازی سه‌منبعی  |
| Pipeline اختصاصی داده  | PARTIAL        | Website قوی؛ <bdi dir="ltr">Book/Video</bdi> باید هم‌سطح شوند           |
| Normalization فارسی    | PARTIAL        | قواعد، Corpus خطا، تست و Ablation                 |
| Data Engineering       | PARTIAL        | Orchestration، lineage، artifacts و quality gates |
| Versioning             | PARTIAL        | <bdi dir="ltr">Dataset/Index/Prompt/Model</bdi> releases               |
| Evaluation Framework   | MISSING        | Golden set، metrics، dashboards، gates            |
| Benchmark              | MISSING        | Baseline comparisons و گزارش آماری                |
| Retrieval Optimization | MISSING        | Hybrid، reranking، tuning و ablation              |
| Citation System        | PARTIAL        | Claim-level <bdi dir="ltr">page/time/span</bdi> citations              |
| Knowledge Engineering  | PARTIAL        | Taxonomy، source policy، <bdi dir="ltr">conflict/freshness</bdi>       |
| Automated Testing      | MISSING        | <bdi dir="ltr">unit/integration/data/eval/security/load</bdi>          |
| Reproducibility        | MISSING        | Docker، pinned deps، CLI، immutable artifacts     |

### ریسک‌های خاص پرونده

1.  **مالکیت و مجوز داده:** عبارت knowledge_owner=Dr. Komeil Roudi برای تمام ۵۲۹ مقاله، به‌تنهایی سند حقوقی مالکیت یا مجوز نیست. قرارداد/مجوز استفاده از مقاله، کتاب، صوت و Transcript باید جداگانه موجود باشد.

2.  **تکرار محتوا:** چند نسخه کتاب و همپوشانی مقاله/ویدیو می‌تواند Benchmark و Retrieval را مصنوعی بهبود دهد.

3.  **وابستگی به سرویس آماده:** اگر تمایز در <bdi dir="ltr">Data/Knowledge/Retrieval/Safety</bdi> اثبات نشود، پرونده ممکن است Integrator ساده تلقی شود.

4.  **نبود شواهد R&D:** Commitها تاریخچه کار را نشان می‌دهند، ولی فرضیه، آزمایش، نتیجه منفی، انتخاب معماری و مقایسه علمی ثبت نشده است.

5.  **محصول نبودن:** Notebook و Streamlit Demo به‌تنهایی نمونه محصول قابل ارزیابی سازمانی نیست.

### نتیجه دانش‌بنیان

- **قابلیت بالقوه:** دارد.

- **آمادگی فعلی برای تأیید:** کافی نیست.

- **شرط تبدیل شدن به پرونده قوی:** باید ارزش فنی حول «سامانه دانش‌محور فارسیِ قابل استناد و ایمن برای آموزش مالی» اثبات شود، نه حول استفاده از LLM و Vector DB.

## ۷. تفاوت «دستیار هوشمند سواد مالی» با «جستجوی متن»

| **جستجوی متن**                 | **دستیار هوشمند آموزشی مالی**                |
|--------------------------------|----------------------------------------------|
| چند سند مشابه برمی‌گرداند       | سؤال را تحلیل و هدف آموزشی را تشخیص می‌دهد    |
| مسئولیت صحت پاسخ ندارد         | پاسخ Grounded با Claim-level Citation می‌سازد |
| معمولاً Unknown را تشخیص نمی‌دهد | در نبود Evidence مناسب صریحاً Abstain می‌کند   |
| تفاوت آموزش/مشاوره را نمی‌فهمد  | Intent و Risk را طبقه‌بندی می‌کند              |
| Context ثابت Top-k             | Context متنوع، dedupشده و متناسب با نوع سؤال |
| بدون مسیر یادگیری              | توضیح مرحله‌ای، مثال، تمرین و پیگیری یادگیری  |
| Source list ساده               | صفحه/فصل/زمان و توضیح نقش هر منبع            |
| Score شباهت                    | Confidence کالیبره‌شده از چند سیگنال          |

### قابلیت‌های ضروری محصول

- پاسخ مستند با Citation در سطح Claim.

- تشخیص «پاسخ کافی وجود ندارد» با Threshold کالیبره‌شده.

- تفکیک Intent: آموزش عمومی، برنامه‌ریزی مالی عمومی، درخواست توصیه شخصی، پیش‌بینی بازار و معامله.

- امتناع/هشدار برای توصیه سرمایه‌گذاری شخصی بدون داده و مجوز مناسب.

- توضیح اینکه پاسخ از چه نوع منابعی ساخته شده و اختلاف منابع چیست.

- Confidence به‌صورت بالا/متوسط/پایین یا عدد کالیبره، نه Score خام Qdrant.

- ثبت Feedback، Trace و Evidence برای Audit.

- Privacy و عدم ذخیره اطلاعات حساس مالی بدون رضایت و سیاست Retention.

### روش صحیح Confidence

Confidence نباید از «اعتماد مدل» یا فقط شباهت برداری ساخته شود. پیشنهاد:

<div dir="ltr" align="left">Confidence = calibrated(retrieval coverage, evidence agreement, citation entailment, source quality, answerability margin, freshness)</div>

عدد نهایی باید روی Validation Set کالیبره شود و Reliability <bdi dir="ltr">Diagram/Brier</bdi> Score داشته باشد.

## ۸. Roadmap اصلاحی اولویت‌بندی‌شده

### P0 — ضروری؛ پیش از توسعه قابلیت‌های نمایشی بیشتر

#### P0.1 تثبیت Baseline و ساخت سند معماری

خروجی‌ها:

- <bdi dir="ltr">docs/architecture/system-context.md</bdi>

- <bdi dir="ltr">docs/architecture/data-flow.md</bdi>

- <bdi dir="ltr">docs/adr/ADR-001-multisource-contract.md</bdi>

- <bdi dir="ltr">docs/phase1-baseline.md</bdi>

- <bdi dir="ltr">Tag/Release</bdi> رسمی برای Demo قدیمی

معیار پایان: هر عضو تیم بداند Dataset قدیمی و Phase 2 جدید چه تفاوتی دارند و کدام مسیر Canonical است.

#### P0.2 ساخت Data Contract واحد

خروجی‌ها:

- <bdi dir="ltr">schemas/source_manifest.schema.json</bdi>

- <bdi dir="ltr">schemas/document.schema.json</bdi>

- <bdi dir="ltr">schemas/chunk.schema.json</bdi>

- <bdi dir="ltr">schemas/retrieval_event.schema.json</bdi>

فیلدهای حداقلی Document:

<div dir="ltr" align="left">document_id, source_type, source_id, source_version, title, language, authors, rights, canonical_uri, content_hash, extracted_at, extractor_version, quality_status, parent_document_id, location, text</div>

فیلدهای حداقلی Chunk:

<div dir="ltr" align="left">chunk_id, document_id, chunker_version, text, text_hash, start_char, end_char, heading_path, page, timestamp_start, timestamp_end, speaker, source_uri</div>

#### P0.3 تکمیل Pipeline کتاب و ویدیو

خروجی‌ها:

- <bdi dir="ltr">src/ingestion/books/</bdi>

- <bdi dir="ltr">src/ingestion/videos/</bdi>

- Manifest مستقل هر منبع

- Validation Report و Reject Queue

- Stable IDs و Lineage

معیار پایان: Run دوباره همان ورودی، خروجی Deterministic با ID و Hash یکسان بسازد.

#### P0.4 Dataset Versioning و Artifact Registry

خروجی‌ها:

- Dataset release مانند kb-2026.08.1

- <bdi dir="ltr">dataset_manifest.json</bdi> با Hash تمام اجزا

- Changelog و Parent Version

- محل Artifact خارج Git برای <bdi dir="ltr">Raw/Interim/Index</bdi>

معیار پایان: یک ممیز با یک دستور بتواند Dataset مشخص را بازیابی و Verify کند.

#### P0.5 Golden Dataset و Safety Policy

حداقل ۳۰۰ سؤال در نسخه اول:

- ۱۲۰ سؤال <bdi dir="ltr">factoid/conceptual</bdi>

- ۶۰ سؤال multi-hop

- ۴۰ سؤال <bdi dir="ltr">cross-source/conflict</bdi>

- ۳۰ سؤال out-of-scope

- ۳۰ سؤال <bdi dir="ltr">personal-advice/unsafe</bdi>

- ۲۰ سؤال <bdi dir="ltr">noisy/typo/Persian</bdi> variants

برای هر سؤال: Gold Answer، Gold Evidence Span، Source ID، Difficulty، Intent، Safety Label و Acceptable Abstention.

#### P0.6 Retrieval قابل دفاع

- <bdi dir="ltr">BM25/Sparse + Dense Hybrid.</bdi>

- Metadata filters و Source routing.

- <bdi dir="ltr">Reranker.</bdi>

- <bdi dir="ltr">Source-aware chunking.</bdi>

- Claim-level citation و Citation verifier.

- <bdi dir="ltr">Answerability gate.</bdi>

#### P0.7 تست و Reproducibility

- <bdi dir="ltr">pyproject.toml</bdi> و dependency lock.

- CLIهای idempotent؛ Notebook فقط برای توضیح/آزمایش.

- Dockerfile و Compose برای <bdi dir="ltr">App/API/Vector</bdi> DB.

- Unit، Integration، Data Contract و End-to-end tests.

- CI با <bdi dir="ltr">lint/type/test/data-smoke/eval-smoke.</bdi>

### P1 — مهم؛ برای محصول قابل ارائه و پرونده قوی

1.  API مستقل از UI با OpenAPI و Versioning.

2.  Auth، rate limit، tenant isolation و secure secret management.

3.  PostgreSQL برای <bdi dir="ltr">conversation/feedback</bdi> با consent و retention.

4.  Observability: trace هر پاسخ، نسخه <bdi dir="ltr">Dataset/Index/Prompt/Model</bdi> و cited spans.

5.  Evaluation Dashboard و Release Gate.

6.  Load Test با <bdi dir="ltr">p50/p95</bdi> latency، throughput، error rate و <bdi dir="ltr">cost/query.</bdi>

7.  Security tests: prompt injection، data exfiltration، malicious documents و PII leakage.

8.  R&D dossier شامل فرضیه‌ها، Ablationها، نتایج منفی و انتخاب مدل.

9.  Data rights register و قراردادهای محتوا.

10. Pilot واقعی با کاربران و تحلیل خطا/رضایت/یادگیری.

### P2 — بهبود و تمایز بیشتر

1.  <bdi dir="ltr">Taxonomy/Ontology</bdi> سواد مالی و Query routing موضوعی.

2.  Learning path، quiz و سنجش پیش/پس از آموزش.

3.  Personalization آموزشی بدون ورود به توصیه سرمایه‌گذاری شخصی.

4.  Conflict-aware answers و نمایش دیدگاه‌های متفاوت.

5.  Freshness-aware web recrawl و change impact analysis.

6.  مدل Embedding یا Reranker بهینه‌شده برای فارسی مالی، در صورت اثبات سود با Benchmark.

7.  Human review console برای اصلاح Evidence، Dataset و Safety cases.

## ۹. Benchmark و آزمایش‌های الزامی

### Baselineهایی که باید مقایسه شوند

1.  <bdi dir="ltr">BM25 only.</bdi>

2.  Dense only فعلی.

3.  Hybrid بدون Reranker.

4.  <bdi dir="ltr">Hybrid + Reranker.</bdi>

5.  Generic chunking در برابر source-aware chunking.

6.  بدون Normalization فارسی در برابر Normalization نسخه‌دار.

7.  بدون Citation verifier در برابر با Citation verifier.

### <bdi dir="ltr">Metrics</bdi>

**Retrieval:** Recall@<bdi dir="ltr">1/3/5/10</bdi>، MRR، nDCG@k، Hit Rate و source-diversity. **Generation:** Faithfulness، Answer Correctness، Completeness و Conciseness. **Citation:** Citation Precision، Citation <bdi dir="ltr">Recall/Coverage</bdi>، Entailment و Location Accuracy. **Abstention:** <bdi dir="ltr">Precision/Recall/F1</bdi> برای Answerable و Unanswerable، False-safe-answer rate. **Safety:** نرخ تولید توصیه شخصی نامجاز، نرخ عبور Prompt Injection و PII leakage. **Operations:** <bdi dir="ltr">p50/p95/p99</bdi> latency، throughput، error rate، availability و <bdi dir="ltr">cost/query.</bdi> **Calibration:** Brier Score، Expected Calibration Error و Reliability Diagram.

### روش علمی گزارش

- Dataset ثابت و Versioned.

- <bdi dir="ltr">Train/Dev/Test</bdi> یا <bdi dir="ltr">Development/Test</bdi> جدا.

- Bootstrap confidence interval برای اختلاف مدل‌ها.

- تحلیل خطا به تفکیک Source، Intent، Difficulty و Safety.

- ثبت Config، Seed، <bdi dir="ltr">Model/Prompt/Index</bdi> versions.

- Release فقط وقتی Regression Gate پاس شود.

## ۱۰. نمودارها و گزارش‌های لازم

### نمودارها

1.  <bdi dir="ltr">System Context Diagram.</bdi>

2.  <bdi dir="ltr">End-to-end Data Lineage Diagram.</bdi>

3.  سه Pipeline مستقل <bdi dir="ltr">Website/Book/Video</bdi> و نقطه ادغام.

4.  Dataset composition به تفکیک Source، Topic، Length و Quality.

5.  <bdi dir="ltr">Deduplication/overlap</bdi> matrix میان منابع.

6.  Retrieval benchmark chart برای Baselineها.

7.  <bdi dir="ltr">Accuracy/Faithfulness/Citation dashboard.</bdi>

8.  <bdi dir="ltr">Confidence reliability diagram.</bdi>

9.  <bdi dir="ltr">Latency/cost/throughput chart.</bdi>

10. Error taxonomy و Pareto chart.

### گزارش‌ها

- Dataset Card و Data Datasheet.

- <bdi dir="ltr">Model/System Card.</bdi>

- <bdi dir="ltr">R&D Technical Report.</bdi>

- <bdi dir="ltr">Benchmark Report.</bdi>

- <bdi dir="ltr">Safety & Responsible AI Report.</bdi>

- <bdi dir="ltr">Data Rights & Licensing Register.</bdi>

- <bdi dir="ltr">Security/Privacy Threat Model.</bdi>

- <bdi dir="ltr">Deployment/Operations Manual.</bdi>

- <bdi dir="ltr">Validation & Acceptance Report.</bdi>

- Pilot Report و User Feedback Analysis.

- Change Log و Release Notes.

## ۱۱. ساختار پیشنهادی Repository نهایی

<div dir="ltr" align="left">

```text
RAG_finance/
├── README.md
├── pyproject.toml
├── uv.lock | poetry.lock
├── Makefile
├── Dockerfile
├── docker-compose.yml
├── configs/
│ ├── ingestion/
│ ├── retrieval/
│ └── evaluation/
├── schemas/
│ ├── source_manifest.schema.json
│ ├── document.schema.json
│ └── chunk.schema.json
├── src/rag_finance/
│ ├── ingestion/{website,books,videos}/
│ ├── normalization/
│ ├── chunking/
│ ├── lineage/
│ ├── indexing/
│ ├── retrieval/
│ ├── reranking/
│ ├── context/
│ ├── generation/
│ ├── citations/
│ ├── safety/
│ ├── evaluation/
│ └── api/
├── data/
│ ├── manifests/
│ ├── samples/
│ └── README.md
├── evals/
│ ├── golden/
│ ├── adversarial/
│ └── baselines/
├── tests/
│ ├── unit/
│ ├── integration/
│ ├── data_contract/
│ └── end_to_end/
├── docs/
│ ├── architecture/
│ ├── adr/
│ ├── data/
│ ├── safety/
│ ├── operations/
│ └── knowledge_based_dossier/
├── reports/
│ ├── benchmarks/
│ ├── data_quality/
│ └── releases/
└── .github/workflows/
```

</div>

## ۱۲. فهرست مدارک لازم برای ارائه دانش‌بنیان

### مدارک محصول و فناوری

- معرفی محصول، مسئله، مشتری و ارزش پیشنهادی.

- Architecture Document و Data Flow.

- توضیح اجزای اختصاصی و اجزای Third-party.

- Technology <bdi dir="ltr">Readiness/TRL</bdi> evidence و Demo قابل بررسی.

- Datasheet محصول، API و Deployment topology.

- <bdi dir="ltr">Repo/Release/Commit</bdi> history و فهرست اعضای فنی.

### مدارک دانش فنی و R&D

- دفترچه R&D با سؤال فنی، فرضیه، آزمایش، نتیجه و تصمیم.

- گزارش ساخت Pipeline فارسی و خطاهای ویژه فارسی/<bdi dir="ltr">ASR/RTL.</bdi>

- Benchmark و Ablation Study.

- گزارش Retrieval Optimization و Citation Verification.

- مستند Reproducibility و Test reports.

- شرح دانش فنی داخلی و وابستگی‌های خارجی.

### مدارک داده و حقوق

- فهرست منابع، مالک، مجوز، تاریخ و محدودیت استفاده.

- قرارداد/اجازه استفاده از کتاب‌ها، مقالات، صوت‌ها و Transcriptها.

- Dataset Card، Manifest و Hash release.

- سیاست Privacy، Retention و حذف داده کاربر.

- سیاست امنیت و مدیریت دسترسی.

### مدارک تجاری و عملیاتی

- شرکت حقوقی، تیم، نقش‌ها و سوابق.

- نمونه قرارداد/فاکتور/Pilot در صورت نیاز نوع ارزیابی.

- بازار هدف، رقبا و تمایز کمی.

- <bdi dir="ltr">SLA/SLO</bdi>، Load Test و هزینه سرویس.

- برنامه نگهداری، پشتیبانی و به‌روزرسانی Knowledge Base.

### مدارک Safety و دامنه محصول

- تعریف دقیق «آموزش مالی» و موارد خارج از دامنه.

- سیاست عدم ارائه توصیه سرمایه‌گذاری شخصی بدون داده/مجوز.

- Risk Register و Incident Response.

- نتایج Red Team و سؤال‌های پرخطر.

- متن Disclaimer، Consent و مسیر ارجاع به متخصص انسانی.

## ۱۳. Acceptance Criteria برای پایان هر فاز

### پایان Data Foundation

- سه Manifest معتبر و Common Schema پاس‌شده.

- ۱۰۰٪ Documentها Stable ID، Hash، Rights و Lineage داشته باشند.

- Duplicateهای Exact و Near-duplicate گزارش و تعیین تکلیف شوند.

### پایان Retrieval

- Recall@5 هدف روی Test Set از قبل تعریف و پاس شود.

- Hybrid+Reranker به‌طور آماری از Dense-only بهتر باشد.

- Citation location accuracy برای هر سه منبع گزارش شود.

### پایان Safety

- نرخ پاسخ نامجاز به درخواست توصیه شخصی زیر حد مصوب تیم باشد.

- Abstention <bdi dir="ltr">precision/recall</bdi> و False-safe-answer rate پاس شوند.

- Prompt injection suite بدون نشت داده پاس شود.

### پایان Productization

- Build و Test در CI سبز.

- Deployment از محیط خالی با دستور مستند موفق.

- Trace کامل یک Answer از سؤال تا <bdi dir="ltr">Dataset/Chunk/Citation</bdi> قابل بازیابی باشد.

- Load Test ادعای ظرفیت را اثبات کند.

## ۱۴. مشکلاتی که باید فوراً اصلاح یا شفاف شوند

1.  README باید وضعیت واقعی سه منبع، Phase <bdi dir="ltr">1/2</bdi> و محدودیت Demo را توضیح دهد.

2.  دو محل Raw قدیمی <bdi dir="ltr">data/raw/...</bdi> و <bdi dir="ltr">src/ingestion/data/raw/...</bdi> باید از <bdi dir="ltr">Code/Data</bdi> separation برخوردار شوند؛ داده زیر src مناسب نیست.

3.  <bdi dir="ltr">requirements.txt</bdi> باید Version pin و Lockfile داشته باشد.

4.  مسیرهای مطلق /<bdi dir="ltr">Users/macbookpro/...</bdi> باید از Notebookها حذف و Configمحور شوند.

5.  Manifest Website باید State نهایی و Versioning واقعی را بازتاب دهد.

6.  Chat history و Cache تولیدی نباید به‌عنوان Artifact عادی Commit شوند؛ Privacy و Staleness risk دارند.

7.  Assertions و تست‌های خودکار باید جای Print-based validation را بگیرند.

8.  فایل‌های Audit Transcript نباید بدون Manifest به‌عنوان Knowledge Document وارد Index شوند.

9.  نسخه‌های کتاب باید Canonicalize و حقوق استفاده‌شان ثبت شود.

10. ادعای ظرفیت ۱۵۰۰ کاربر تا زمان Load Test از README حذف یا با برچسب Target مشخص شود.

## ۱۵. نظر نهایی Auditor

این پروژه **قابلیت تبدیل شدن به محصول دانش‌بنیان را دارد**، چون داده تخصصی فارسی، Pipeline جدید وب‌سایت، فرایند بازبینی Transcript و مسئله واقعی <bdi dir="ltr">Citation/Safety</bdi> در حوزه مالی می‌توانند پایه دانش فنی قابل دفاع باشند.

اما در وضعیت Commit بررسی‌شده:

- محصول سه‌منبعی هنوز ساخته نشده است.

- RAG موجود بیشتر یک Demo Dense RAG است.

- معیارهای علمی کیفیت و Safety اثبات نشده‌اند.

- پرونده R&D، Reproducibility و حقوق داده ناقص است.

پس جمع‌بندی حرفه‌ای این است:

> **مسیر درست است، ولی ادامه مسیر باید از «جمع‌آوری داده و تکمیل Notebook» به «مهندسی محصول قابل اندازه‌گیری، قابل استناد، قابل بازتولید و ایمن» تغییر کند.**

اولویت صحیح بعدی، Embedding کردن سریع همه داده‌ها نیست. ابتدا باید Common Schema، Stable IDs، Manifest کتاب/ویدیو، Lineage، Deduplication و Golden Dataset تکمیل شود. سپس Retrieval و Generation روی Dataset نسخه‌دار ساخته و با Benchmark مقایسه شوند.

## ضمیمه A — مسیر اجرایی پیشنهادی ۱۲ مرحله‌ای

1.  Freeze و Tag رسمی Demo قدیمی.

2.  تعریف Contract و ID policy.

3.  Book Manifest و canonicalization نسخه‌ها.

4.  Video Manifest و timestamp <bdi dir="ltr">recovery/segmentation.</bdi>

5.  انتقال Website Notebook به <bdi dir="ltr">Package/CLI.</bdi>

6.  Unified normalized documents و Quality Gate.

7.  Source-aware chunking و Dataset Release v1.

8.  <bdi dir="ltr">Dense/BM25</bdi> baselines و Golden Retrieval set.

9.  <bdi dir="ltr">Hybrid + Reranker + Context compiler.</bdi>

10. <bdi dir="ltr">Grounded generation + claim citations + safety.</bdi>

11. <bdi dir="ltr">Regression/Load/Security</bdi> tests و Observability.

12. Pilot، R&D dossier و آماده‌سازی پرونده ارزیابی.

## ضمیمه B — وضعیت Production Readiness

| **جزء**             | **Demo**      | **Production Ready**                       |
|---------------------|---------------|--------------------------------------------|
| Website ingestion   | بله           | خیر؛ Notebookمحور و Artifact غیرقابل دسترس |
| Book ingestion      | خیر           | خیر                                        |
| Video ingestion     | داده حاضر است | خیر                                        |
| Unified dataset     | خیر           | خیر                                        |
| Dense retrieval     | بله           | خیر                                        |
| <bdi dir="ltr">Hybrid/rerank</bdi>       | خیر           | خیر                                        |
| Citation            | نمایش Source  | خیر؛ Claim-level نیست                      |
| Evaluation          | Smoke test    | خیر                                        |
| Streamlit UI        | بله           | خیر                                        |
| <bdi dir="ltr">Tests/CI/Deployment</bdi> | خیر           | خیر                                        |

## ضمیمه C — اسناد Repository مشاهده‌شده

- README شاخه rag-phase2 — <bdi dir="ltr">https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/README.md</bdi>

- <bdi dir="ltr">Website Ingestion V2 Notebook — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/phase2/01_website_ingestion.ipynb</bdi>

- <bdi dir="ltr">Website Manifest v1 — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/data/phase2/manifests/website_manifest_v1.json</bdi>

- <bdi dir="ltr">RAG Pipeline — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/src/pipeline/rag_pipeline.py</bdi>

- <bdi dir="ltr">Qdrant Retriever — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/src/retrieval/qdrant_retriever.py</bdi>

- <bdi dir="ltr">Evaluation Notebook — https://github.com/Shahbazi-Amir/RAG_finance/blob/rag-phase2/notebooks/10_evaluation.ipynb</bdi>

</div>
