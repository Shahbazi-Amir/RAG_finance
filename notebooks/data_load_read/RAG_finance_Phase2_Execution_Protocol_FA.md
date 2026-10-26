# دستورالعمل اجرایی سریع، دقیق و بدون دوباره‌کاری برای Phase 2 پروژه RAG_finance

## هدف این سند

این سند باید در ابتدای هر Chat و پیش از شروع یا ادامه‌ی هر Notebook از
Phase 2 پروژه `RAG_finance` به‌عنوان دستورالعمل اجرایی خوانده و رعایت
شود.

هدف، **افزایش سرعت مهندسی بدون کاهش کیفیت** است. سرعت نباید با حذف
Validation، کوچک‌کردن غیرموجه Benchmark، شل‌کردن Gateها، نادیده‌گرفتن خطاها
یا دور زدن نقشه‌ی اصلی پروژه به دست آید. سرعت باید از طراحی بهتر، حذف
دوباره‌کاری، استفاده صحیح از Cache و Artifact، محدودکردن Scope و کشف
زودهنگام خطاها حاصل شود.

------------------------------------------------------------------------

# 1. اصل حاکم: وفاداری کامل به نقشه‌ی اصلی

نقشه‌های رسمی Phase 2، مرجع تعیین Scope، ترتیب Notebookها، مسئولیت هر
Notebook و Definition of Done هستند.

هیچ Notebook نباید به‌دلیل آزمایش‌های جانبی، ایده‌های جدید یا توسعه‌ی
تدریجی، مسئولیت Notebookهای بعدی را به خود جذب کند.

اگر بین وضعیت فعلی Notebook و Roadmap تعارضی وجود داشت:

1.  ابتدا تعارض مشخص شود.
2.  Scope رسمی Roadmap ملاک قرار گیرد.
3.  کار تاریخی مفید حفظ شود، اما نباید Scope رسمی را تغییر دهد.
4.  کار خارج از Scope یا به Notebook رسمی خودش منتقل شود یا فقط به‌عنوان
    Experiment تاریخی ثبت شود.

**قاعده:**\
هر Notebook باید فقط مأموریت خودش را کامل کند؛ نه کمتر و نه بیشتر.

------------------------------------------------------------------------

# 2. کیفیت غیرقابل مذاکره است

برای افزایش سرعت، موارد زیر نباید حذف یا تضعیف شوند:

-   Golden Dataset و داده‌های مرجع معتبر
-   Validationهای ساختاری و معنایی موردنیاز
-   Metricهای رسمی Roadmap
-   Evidence و Source Lineage
-   Reproducibility
-   Regression Gates
-   Artifact Integrity
-   Hash / Manifest / Versioning در جاهایی که Roadmap یا معماری پروژه
    نیاز دارد
-   Failure Analysis لازم
-   Final Health Check
-   Restart Kernel → Run All نهایی در Notebookهایی که باید مستقل و قابل
    بازتولید باشند

اگر بین «سریع‌تر تمام شدن» و «اعتبار علمی/مهندسی نتیجه» تعارض ایجاد شود،
اعتبار نتیجه اولویت دارد.

------------------------------------------------------------------------

# 3. قبل از نوشتن اولین Cell، Execution Blueprint ساخته شود

پیش از شروع اجرای هر Notebook، ابتدا یک Blueprint کوتاه اما کامل تهیه
شود.

Blueprint باید مشخص کند:

-   مأموریت رسمی Notebook چیست؟
-   چه چیزهایی خارج از Scope هستند؟
-   ورودی‌های Canonical کدام‌اند؟
-   Artifactهای موردنیاز از مراحل قبل کدام‌اند؟
-   خروجی‌های این Notebook دقیقاً چه خواهند بود؟
-   چه Metricهایی باید محاسبه شوند؟
-   PASS/FAIL بر چه اساسی تعیین می‌شود؟
-   چه API یا مدل‌هایی ممکن است استفاده شوند؟
-   Cache و Checkpoint چگونه مدیریت می‌شوند؟
-   Failureهای محتمل کدام‌اند؟
-   Final Health Check چه چیزهایی را کنترل خواهد کرد؟
-   Notebook بعدی دقیقاً چه چیزی از این Notebook تحویل می‌گیرد؟

تا زمانی که این Contract روشن نشده، Full Execution شروع نشود.

------------------------------------------------------------------------

# 4. Contract ورودی و خروجی از ابتدا ثابت شود

هر Notebook باید Input Contract و Output Contract مشخص داشته باشد.

Notebook نباید به‌طور پنهانی به متغیری وابسته باشد که فقط در Kernel قبلی
وجود داشته است.

ارتباط Notebookها باید تا حد ممکن از طریق Artifactهای Versioned و قابل
Validation انجام شود، نه State موقت حافظه.

مثلاً:

`NB14 → Artifact مشخص → NB15/NB16`

بهتر از این است که Notebook بعدی فقط در صورتی کار کند که Notebook قبلی
چند دقیقه قبل در همان Kernel اجرا شده باشد.

------------------------------------------------------------------------

# 5. Artifact-first، نه Memory-first

هر نتیجه‌ای که برای مراحل بعدی مهم است باید به شکل Artifact مشخص، قابل
ردیابی و در صورت نیاز Versioned ذخیره شود.

Artifact مهم باید در صورت لزوم دارای اطلاعاتی مانند این‌ها باشد:

-   Version
-   Dataset fingerprint/hash
-   Model/config
-   Timestamp در صورت نیاز
-   Record count
-   Relevant metrics
-   Source/Lineage
-   Status
-   Manifest یا metadata لازم

Notebook بعدی باید بتواند Artifact را مستقل Load و Validate کند.

------------------------------------------------------------------------

# 6. API و عملیات گران: Checkpoint-first

هیچ عملیات گران، طولانی یا پولی نباید بدون طراحی Cache/Checkpoint اجرا
شود.

قبل از API Call:

1.  Fingerprint دقیق Input تعیین شود.
2.  Cache معتبر جست‌وجو شود.
3.  نتیجه‌ی موجود Validate شود.
4.  فقط Missing Itemها اجرا شوند.
5.  هر Batch موفق فوراً Checkpoint شود.
6.  Retry محدود و کنترل‌شده وجود داشته باشد.
7.  اجرای مجدد Notebook نباید عملیات موفق قبلی را تکرار کند.

**قاعده‌ی اصلی:**\
پرداخت یا محاسبه‌ی دوباره برای چیزی که نتیجه‌ی معتبر آن از قبل موجود است،
خطای مهندسی محسوب می‌شود مگر اینکه Recompute عمداً بخشی از آزمایش باشد.

------------------------------------------------------------------------

# 7. Full Run نهایی باید تا حد ممکن API-safe باشد

پیش از Final Restart Kernel → Run All، Cellهای پولی یا عملیات خارجی
پرریسک باید طوری طراحی شده باشند که از Checkpointهای معتبر بازسازی شوند.

اجرای نهایی نباید ناخواسته:

-   هزاران Embedding را دوباره بسازد،
-   Reranking را دوباره پولی اجرا کند،
-   LLM Callهای قبلی را تکرار کند،
-   Artifact فریز‌شده را overwrite کند.

در Final Run، هدف اثبات **Reproducibility از Artifact و Cache معتبر**
است، نه پرداخت دوباره برای همان محاسبات.

------------------------------------------------------------------------

# 8. Pilot → Validate → Full Run

هر عملیات بزرگ ابتدا روی Pilot کوچک اجرا شود.

ترتیب استاندارد:

`Smoke Test → Small Pilot → Validation → Full Execution`

Pilot باید به‌اندازه‌ای باشد که خطاهای Schema، API، Batch، Dimension،
Mapping، Cache و Logic را آشکار کند.

اما Pilot جای Full Benchmark را نمی‌گیرد.

بعد از سالم بودن Pipeline، Full Evaluation موردنیاز Roadmap باید انجام
شود.

این روش کیفیت را کم نمی‌کند؛ فقط مانع می‌شود یک باگ ساده بعد از چند ساعت
Compute یا صدها API Call کشف شود.

------------------------------------------------------------------------

# 9. Full Dataset فقط وقتی لازم است اجرا شود

Full Dataset برای نتیجه‌ی نهایی و Benchmark رسمی استفاده می‌شود؛ اما Debug
کردن نباید دائماً روی کل Dataset انجام شود.

برای Debug:

-   نمونه‌ی کوچک و نماینده استفاده شود.
-   Bug اصلاح شود.
-   تست کوچک PASS شود.
-   سپس Full Run انجام شود.

هر بار اجرای Full Dataset برای کشف Syntax Error، Schema Error یا Mapping
Error یک Anti-pattern است.

------------------------------------------------------------------------

# 10. Scope Creep ممنوع

در حین کار ممکن است ایده‌ی مفیدی برای مرحله‌ی دیگری پیدا شود.

این ایده نباید فوراً Notebook فعلی را بزرگ کند.

مثلاً:

-   NB13 مأمور Embedding Benchmark است.
-   NB14 مأمور Dense Index است.
-   NB15 مأمور Sparse Index است.
-   NB16 مأمور Hybrid Retrieval است.
-   NB17 مأمور Reranking است.

اگر هنگام NB14 ایده‌ی Reranking ایجاد شد، آن را ثبت می‌کنیم اما NB14 را به
آزمایشگاه Reranking تبدیل نمی‌کنیم.

**هر Notebook یک مسئولیت اصلی دارد.**

------------------------------------------------------------------------

# 11. Research Path و Production Path جدا بمانند

آزمایش exploratory می‌تواند مفید باشد، اما نباید با مسیر Canonical مخلوط
شود.

هر نتیجه باید مشخص کند که یکی از این‌هاست:

-   Experimental
-   Candidate
-   Accepted
-   Canonical
-   Frozen
-   Historical / Archived

یک Experiment موفق تا زمانی که Gateهای رسمی را پاس نکرده، نباید به‌عنوان
تصمیم Production معرفی شود.

------------------------------------------------------------------------

# 12. Definition of Done قبل از اجرا نوشته شود

برای هر Notebook قبل از Full Execution باید مشخص باشد چه زمانی می‌گوییم:

**این Notebook تمام شده است.**

Definition of Done باید مبتنی بر Roadmap و Artifact واقعی باشد، نه احساس
اینکه «به نظر می‌رسد کافی است».

وقتی تمام Gateهای تعریف‌شده PASS شدند:

1.  Final Health Check
2.  Restart Kernel → Run All در صورت نیاز
3.  ثبت Summary
4.  Freeze
5.  حرکت به Notebook بعدی

بعد از Freeze، آزمایش‌های خارج از Scope نباید دوباره Notebook را باز کنند
مگر دلیل مشخص مهندسی وجود داشته باشد.

------------------------------------------------------------------------

# 13. Failure باید در همان مرحله Repair شود

اگر یک Cell FAIL شد، نباید از آن عبور کرد و Notebook را ادامه داد.

قاعده:

`FAIL → Diagnose → Repair همان مرحله → Re-run → PASS → Next Step`

هیچ PASS فرضی پذیرفته نیست.

PASS فقط وقتی ثبت می‌شود که Output واقعی آن را تأیید کند.

------------------------------------------------------------------------

# 14. روش اصلاح Cellها

برای جلوگیری از سردرگمی و خطای Copy/Paste:

اگر فقط یک خط تغییر می‌کند، دقیقاً اعلام شود:

-   خط فعلی چیست؟
-   با چه خطی جایگزین شود؟

اگر بیش از یک خط یا Logic/Structure تغییر می‌کند:

-   کل Code Cell اصلاح‌شده از ابتدا تا انتها ارائه شود.

در Repair مشخص شود که Markdown قبلی بدون تغییر باقی می‌ماند یا نیاز به
اصلاح دارد.

------------------------------------------------------------------------

# 15. اجرای Notebook مرحله‌به‌مرحله باشد

در توسعه و Debug، Cellها مرحله‌به‌مرحله اجرا شوند و Output واقعی بررسی
شود.

چرخه‌ی استاندارد:

`Markdown → Code → Actual Output → Analysis → Next Step`

نباید چندین مرحله‌ی وابسته بر اساس Output فرضی جلو نوشته شوند.

این کار باعث می‌شود خطا در نزدیک‌ترین نقطه به علت اصلی شناسایی شود.

------------------------------------------------------------------------

# 16. Final Health Check از ابتدای طراحی وجود داشته باشد

Final Health Check نباید در پایان پروژه به Notebook اضافه شود؛ معیارهای
آن باید از ابتدا مشخص باشند.

بسته به Notebook، Health Check باید موارد مرتبطی مانند این‌ها را بررسی
کند:

-   همه Code Cellهای موردنیاز اجرا شده‌اند.
-   Saved Error وجود ندارد.
-   Cell Numbering صحیح و Sequential است.
-   Duplicate Code Cell Number وجود ندارد.
-   Duplicate/Unnecessary Imports کنترل شده‌اند.
-   Artifactهای لازم وجود دارند.
-   Record Countها صحیح‌اند.
-   Hash/Fingerprintها صحیح‌اند.
-   Config و Model Version مشخص‌اند.
-   API execution state مطابق Policy است.
-   Frozen Artifact overwrite نشده است.
-   خروجی‌های لازم برای Notebook بعدی وجود دارند.
-   Final Status با Output واقعی سازگار است.

------------------------------------------------------------------------

# 17. Restart Kernel → Run All آزمون استقلال Notebook است

در پایان Notebookهایی که باید مستقل و قابل بازتولید باشند، Restart
Kernel → Run All انجام شود.

این تست مشخص می‌کند آیا Notebook واقعاً مستقل است یا به State پنهان Kernel
قبلی وابسته بوده است.

اگر Run All شکست خورد، Notebook هنوز Freeze نمی‌شود.

خطا باید Repair و Run All دوباره تأیید شود.

------------------------------------------------------------------------

# 18. داده و Artifact فریز‌شده دست‌نخورده بماند

Golden Dataset، Registry، Index Snapshot یا هر Artifact فریز‌شده نباید
صرفاً برای راحتی اجرای Notebook بعدی تغییر داده شود.

اگر Notebook جدید با Artifact Canonical سازگار نیست، Notebook جدید باید
اصلاح شود؛ نه اینکه حقیقت مرجع پروژه برای سازگار شدن با کد جدید دستکاری
شود.

------------------------------------------------------------------------

# 19. Historical Notebookها و مسیر Canonical مخلوط نشوند

Notebookهای قدیمی برای Provenance و تاریخچه مفیدند، اما نباید باعث ابهام
شوند که مسیر اصلی پروژه کدام است.

در هر خانواده:

-   یک مسیر Canonical مشخص باشد.
-   نسخه‌های Superseded/Experimental در Archive بمانند.
-   Artifact نهایی مستقل از سردرگمی تاریخی قابل شناسایی باشد.

Archive به معنی حذف تاریخچه نیست؛ به معنی جداکردن تاریخچه از مسیر اجرایی
اصلی است.

------------------------------------------------------------------------

# 20. Benchmark باید روی داده‌ی واقعی پروژه باشد

تصمیم‌های اصلی مانند انتخاب Embedding، Retrieval Strategy، Reranker و
Query Rewrite نباید صرفاً بر Benchmark عمومی یا شهرت مدل تکیه کنند.

Benchmark عمومی می‌تواند اطلاعات کمکی بدهد، اما تصمیم Production باید تا
حد ممکن با:

-   Golden Dataset پروژه
-   داده فارسی پروژه
-   سه منبع اصلی پروژه
-   Queryهای واقعی یا نماینده
-   Metricهای رسمی

پشتیبانی شود.

------------------------------------------------------------------------

# 21. Metric بدون تفسیر کافی نیست

فقط تولید یک عدد کافی نیست.

برای Benchmarkهای اصلی باید مشخص شود:

-   Metric چه چیزی را اندازه می‌گیرد؟
-   Baseline چیست؟
-   Candidate چیست؟
-   بهبود یا افت کجاست؟
-   Failureها در چه نوع Query یا Source رخ می‌دهند؟
-   هزینه و Latency چه تغییری کرده؟
-   آیا نتیجه برای Promotion کافی است؟

هدف، تصمیم مهندسی مبتنی بر Evidence است؛ نه تولید جدول‌های زیاد بدون
نتیجه.

------------------------------------------------------------------------

# 22. کیفیت، هزینه و سرعت با هم دیده شوند

مدلی که کمی بهتر است اما هزینه یا Latency غیرقابل قبول دارد لزوماً انتخاب
Production نیست.

در مراحل مرتبط باید Trade-off میان این موارد ثبت شود:

-   Quality
-   Recall / Ranking quality
-   Latency
-   Cost
-   Failure rate
-   Operational complexity
-   Reproducibility

اما هیچ‌کدام نباید بدون معیار رسمی Roadmap به‌تنهایی جایگزین کیفیت شوند.

------------------------------------------------------------------------

# 23. دوباره‌کاری باید به‌عنوان Bug فرایندی دیده شود

اگر کاری چند بار تکرار شد، فقط آن را دوباره انجام ندهید؛ علت تکرار را
پیدا کنید.

نمونه‌ها:

-   API دوباره اجرا شد → Cache Policy مشکل دارد.
-   Run All شکست خورد → Hidden State وجود دارد.
-   Artifact دوباره ساخته شد → Version/Manifest مبهم است.
-   Scope چند بار عوض شد → Contract قبل از اجرا بسته نشده است.
-   Notebook بیش از حد بزرگ شد → Scope Creep رخ داده است.
-   Full Dataset چند بار برای Debug اجرا شد → Pilot Strategy ضعیف بوده
    است.

هدف این است که هر خطای پرهزینه فقط یک بار رخ دهد و بعد تبدیل به
Guardrail شود.

------------------------------------------------------------------------

# 24. هر Notebook باید Handoff واضح داشته باشد

در پایان Notebook دقیقاً ثبت شود:

-   چه چیزی ساخته شد؟
-   چه چیزی انتخاب شد؟
-   چه چیزی رد شد؟
-   Artifact Canonical کجاست؟
-   Hash/Version چیست؟
-   چه محدودیت یا Failure شناخته‌شده‌ای باقی مانده؟
-   Notebook بعدی باید چه چیزی را Load کند؟
-   آیا Notebook فعلی Frozen است؟

Notebook بعدی نباید برای فهمیدن این اطلاعات مجبور شود کل Notebook قبلی
را از ابتدا تحلیل کند.

------------------------------------------------------------------------

# 25. Summary نهایی کوتاه اما قطعی باشد

Summary نهایی باید بین سه چیز تفاوت بگذارد:

### Fact

چیزی که Output واقعی اثبات کرده است.

### Interpretation

برداشت مهندسی مبتنی بر Fact.

### Pending

چیزی که هنوز آزمایش یا تأیید نشده است.

نباید نتیجه‌ای که هنوز اجرا نشده به‌صورت Fact نوشته شود.

------------------------------------------------------------------------

# 26. ترتیب رسمی ادامه Phase 2 حفظ شود

مسیر اصلی پروژه باید طبق Roadmap رسمی ادامه پیدا کند:

`00 Environment/Baseline`\
`→ 01 Website Ingestion`\
`→ 02 Website Acceptance`\
`→ 03 Book Inventory`\
`→ 04 Book Ingestion`\
`→ 05 Transcript Inventory`\
`→ 06 Transcript Ingestion`\
`→ 07 Unified Schema & Lineage`\
`→ 08 Persian Normalization`\
`→ 09 Deduplication & Quality`\
`→ 10 Taxonomy & Knowledge Engineering`\
`→ 11 Chunking Benchmark`\
`→ 12 Golden Dataset`\
`→ 13 Embedding Benchmark`\
`→ 14 Dense Index`\
`→ 15 Sparse Index`\
`→ 16 Hybrid Retrieval`\
`→ 17 Reranking`\
`→ 18 Query Rewrite`\
`→ 19 Citation & Grounding`\
`→ 20 Evaluation Harness`\
`→ 21 Regression Suite`\
`→ 22 Performance & Cost Benchmark`\
`→ 23 Release Candidate`

تغییر این ترتیب یا ادغام مسئولیت‌ها فقط در صورت وجود دلیل مهندسی مستند و
سازگار با Roadmap مجاز است.

------------------------------------------------------------------------

# 27. پروتکل پیشنهادی اجرای هر Notebook

برای هر Notebook از این چرخه استفاده شود:

### مرحله A --- Scope Lock

Roadmap خوانده شود و مأموریت Notebook قفل شود.

### مرحله B --- Input Audit

Artifactهای ورودی و وضعیت آن‌ها بررسی شوند.

### مرحله C --- Execution Blueprint

مراحل، Metricها، API Policy، Cache و Definition of Done نوشته شوند.

### مرحله D --- Bootstrap / Preflight

محیط، مسیرها، Configها و Input Contract Validate شوند.

### مرحله E --- Smoke Test

کوچک‌ترین اجرای مفید برای کشف خطاهای بنیادی انجام شود.

### مرحله F --- Pilot

نمونه‌ی نماینده اجرا و Metric/Artifact Pipeline تأیید شود.

### مرحله G --- Full Execution

فقط پس از PASS مراحل قبل، Benchmark یا Build کامل انجام شود.

### مرحله H --- Failure Analysis

خطاهای واقعی دسته‌بندی و در صورت قرار داشتن در Scope اصلاح شوند.

### مرحله I --- Artifact Freeze

خروجی Canonical، Version، Hash، Manifest و Summary ثبت شوند.

### مرحله J --- Final Health

Notebook از نظر اجرا، Artifact، State، Cellها و API Safety بررسی شود.

### مرحله K --- Restart Kernel → Run All

در صورت الزام Reproducibility، اجرای پاک انجام شود.

### مرحله L --- Handoff

ورودی موردنیاز Notebook بعدی صریحاً ثبت شود.

------------------------------------------------------------------------

# 28. چیزهایی که برای افزایش سرعت مجاز هستند

این موارد سرعت را بالا می‌برند بدون اینکه کیفیت کم شود:

-   استفاده از Smoke Test
-   Pilot کوچک قبل از Full Run
-   Cache و Checkpoint
-   اجرای فقط Missing Itemها
-   Batch Processing صحیح
-   Parallelization امن در صورت مناسب بودن
-   Artifact reuse
-   Preflight قوی
-   Schema validation زودهنگام
-   Centralized config
-   Automated Final Health Check
-   ثبت Failureها به‌صورت Guardrail
-   Freeze کردن Scope
-   Archive کردن مسیرهای Superseded
-   جلوگیری از اجرای API در Final Run
-   ساخت Blueprint قبل از Coding

------------------------------------------------------------------------

# 29. چیزهایی که برای افزایش سرعت ممنوع هستند

این موارد «بهینه‌سازی» محسوب نمی‌شوند و نباید برای سریع‌تر شدن انجام شوند:

-   حذف Metric رسمی
-   حذف Full Benchmark لازم
-   کوچک کردن Golden Dataset نهایی بدون دلیل علمی
-   نادیده گرفتن Failure
-   اعلام PASS بدون Output واقعی
-   استفاده از Cache بدون Fingerprint/Validation
-   حذف Evidence یا Lineage
-   رد شدن از Regression Gate
-   تغییر Artifact فریز‌شده برای سازگار کردن کد
-   استفاده از نتیجه تاریخی به‌عنوان نتیجه Dataset جدید
-   اجرای مرحله بعد قبل از معتبر شدن Handoff مرحله قبل
-   حذف Final Health Check
-   حذف Run-All در جایی که Reproducibility الزام است
-   قاطی کردن Scope چند Notebook برای «زودتر تمام شدن»

------------------------------------------------------------------------

# 30. دستور کوتاه برای Assistant در ابتدای هر Chat

در شروع هر Notebook یا Chat جدید، این اصول اجرا شوند:

> نقشه رسمی Phase 2 مرجع Scope و ترتیب کار است. کیفیت، Validation،
> Golden Dataset، Evidence، Lineage، Metricها و Regression Gateها نباید
> برای افزایش سرعت حذف یا تضعیف شوند. قبل از Coding، Scope و Execution
> Blueprint را مشخص کن. از Artifact-first، Cache-first، Checkpoint-first
> و Pilot-before-Full-Run استفاده کن. هر Notebook فقط مسئول مأموریت رسمی
> خودش است و Scope Creep ممنوع است. عملیات پولی یا سنگین باید resumable
> و fingerprint-bound باشند و Final Run تا حد ممکن
> API-disabled/cache-only باشد. PASS فقط با Output واقعی ثبت شود.
> Failure در همان مرحله Repair شود. خروجی هر Notebook باید Handoff روشن،
> Artifact قابل ردیابی و Final Health Check داشته باشد. سرعت باید از
> مهندسی بهتر و حذف دوباره‌کاری حاصل شود، نه از کاهش کیفیت.

------------------------------------------------------------------------

# اصل نهایی

**هدف این پروژه «زود تمام کردن Notebookها» نیست؛ هدف ساختن یک RAG قابل
اعتماد، قابل اندازه‌گیری، قابل بازتولید و قابل انتشار است.**

اما کیفیت بالا به معنی دوباره‌کاری، اجرای چندباره‌ی API، Debug روی Full
Dataset، Scope مبهم یا Notebookهای وابسته به State پنهان نیست.

روش مطلوب این است:

**یک بار طراحی درست → یک بار اجرای کنترل‌شده → اندازه‌گیری واقعی → Repair
هدفمند → Freeze → Handoff → مرحله بعد.**

به این ترتیب سرعت بیشتر می‌شود، در حالی که استاندارد علمی و مهندسی پروژه
حفظ می‌شود.
