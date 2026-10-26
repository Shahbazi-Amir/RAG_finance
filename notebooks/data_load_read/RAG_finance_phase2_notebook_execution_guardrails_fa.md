# دستورالعمل ثابت اجرای نوت‌بوک‌های Phase 2 پروژه RAG Finance

این دستورالعمل در تمام مراحل بعدی پروژه لازم‌الاجراست. هدف آن جلوگیری از دوباره‌کاری، تغییر ناخواسته قراردادهای فریز‌شده، استفاده اشتباه از Test و ساخت Notebook ناقص است.

## ۱. محدوده اطلاعات

فقط از منابع زیر استفاده کن:

- فایل‌ها و Artifactهای همین پروژه؛
- نقشه‌های موجود در Repository؛
- Notebookهای قبلی همین پروژه؛
- خروجی‌ها و قراردادهای فریز‌شده؛
- اطلاعات همین گفت‌وگو.

از حافظه پروژه‌های دیگر، الگوهای فرضی یا حدس استفاده نکن. اگر چیزی در فایل‌های پروژه مشخص نیست، مقدار مصنوعی نساز و بنویس:

```text
NOT_SPECIFIED_IN_PROJECT_ARTIFACTS
```

## ۲. مطالعه پیش از تغییر

قبل از تولید یا اصلاح کد:

1. Notebook فعلی را کامل بررسی کن.
2. Notebook قبلی و Handoff آن را بخوان.
3. Master roadmap، Operational roadmap و Modular execution plan را بخوان.
4. Artifactها، Schema، Version، Hash و Status ورودی‌ها را کنترل کن.
5. وضعیت Git و فایل‌های موجود را فقط Read-only بررسی کن.
6. مشخص کن چه چیزهایی قبلاً انجام شده‌اند.
7. کارهای صحیح قبلی را تکرار یا بازنویسی نکن.
8. ابتدا Gap analysis و سپس یک Plan کوتاه ارائه کن.

صرفاً براساس نام فایل یا توضیح کاربر نتیجه نگیر؛ محتوای واقعی فایل‌ها را بررسی کن.

## ۳. حفظ قرارداد مراحل قبلی

Artifact فریز‌شده مرحله قبل تغییرناپذیر است. موارد زیر ممنوع‌اند:

- تغییر Configuration فریز‌شده؛
- محاسبه مجدد Scoreهای قبلی بدون الزام نقشه؛
- تغییر Rank یا ترتیب فریز‌شده؛
- تغییر Candidate depth، Split یا Gold mapping؛
- دست‌کاری Hash برای عبور از Assert؛
- بازسازی Artifact قبلی با منطق جدید؛
- حذف یا ضعیف‌کردن Gate صرفاً برای PASS شدن.

Notebook جدید باید Artifact قبلی را مصرف کند، نه اینکه آن را بازتولید کند.

## ۴. استقلال Notebook

هر Notebook باید:

- از Kernel پاک اجرا شود؛
- به متغیرهای Notebook قبلی وابسته نباشد؛
- ورودی‌ها را از Artifactهای ذخیره‌شده بخواند؛
- مسیرها را نسبت به Project root پیدا کند؛
- مسیر محلی شخصی را Hard-code نکند؛
- تمام توابع موردنیاز را داخل خودش تعریف کند؛
- با `Restart Kernel & Run All` از ابتدا تا انتها اجرا شود.

## ۵. ترتیب صحیح کار

در هر Notebook این ترتیب رعایت شود:

1. Imports و Bootstrap
2. Project-root discovery
3. Read-only preflight
4. کنترل فایل‌ها و SHA-256
5. کنترل Schema و Version
6. بارگذاری ورودی‌ها
7. بازسازی قراردادهای لازم
8. Development-only analysis
9. انتخاب Configuration
10. ساخت ADR
11. Freeze Configuration
12. استفاده از Test فقط پس از Freeze و در محدوده مجاز نقشه
13. ساخت خروجی نهایی
14. نوشتن Atomic
15. Reload Validation مستقل
16. Manifest، Release و Handoff
17. Acceptance و Checkpoint
18. Final Health Gate

پیش از Freeze از Test برای انتخاب یا تغییر Configuration استفاده نکن.

## ۶. سیاست Development و Test

Development برای انتخاب Policy، Threshold، Budget، مدل، روش و Ablation استفاده می‌شود. Test فقط پس از Freeze قابل استفاده است.

بعد از مشاهده Test، Configuration، Threshold، Prompt و Budget نباید تغییر کنند. هر Artifact نهایی باید ثبت کند:

```text
configuration_changed_after_test = false
test_queries_accessed_for_retuning = false
```

اگر نقشه به Independent Test evaluation نیاز ندارد، Test metric مصنوعی ایجاد نکن و فقط Policy فریز‌شده را در محدوده لازم اعمال کن.

## ۷. کدنویسی Notebook

تمام Code Cellها باید شماره پیوسته و عنوان دقیق و یکتا داشته باشند:

```text
# NB19-C01 — Imports and runtime bootstrap
# NB19-C02 — Frozen-input preflight
```

Markdownها باید فارسی، RTL، روشن و توضیح‌دهنده هدف سل بعدی باشند. سل خالی، سل آزمایشی رهاشده، کد موقت و Import پراکنده باقی نگذار.

## ۸. مدیریت Health Check

فقط یک Final Health Gate وجود داشته باشد. Health Checkهای میانی با نام‌هایی مانند زیر مشخص شوند:

```text
INTERIM_HEALTH
PREFLIGHT
READINESS_CHECK
```

هیچ Health Check میانی نباید عنوان `FINAL` داشته باشد. Final Health هنگام `Run All` نباید برای بررسی execution count نسخه ذخیره‌شده خود Notebook را از دیسک بخواند؛ چون ممکن است Snapshot قبلی را ببیند.

Final Health باید براساس Runtime جاری، Artifactهای Reload‌شده، Hashها، Record countها، Schema، Configuration freeze و Handoff status کار کند.

خروجی‌های قدیمی و متناقض زیر نباید در نسخه نهایی باقی بمانند:

```text
OBJECTIVE_INCOMPLETE
PROPOSAL_NOT_FROZEN
PENDING_RELOAD
STRUCTURAL_HEALTH_FAIL
files_written = 0
```

مگر اینکه واقعاً وضعیت نهایی همان باشد.

## ۹. نوشتن Artifact

خروجی را مستقیم روی فایل نهایی ننویس. روش الزامی:

1. نوشتن در فایل موقت هم‌مسیر؛
2. Flush و Close؛
3. بازخوانی فایل موقت؛
4. کنترل Schema و تعداد رکوردها؛
5. محاسبه SHA-256؛
6. جایگزینی Atomic فایل نهایی.

هر Artifact باید حداقل این موارد را داشته باشد:

```text
artifact_type
schema_version
release_id
input_paths
input_hashes
configuration_sha256
record_counts
limitations
test_access_status
status
```

## ۱۰. Reload Validation

وجود فایل کافی نیست. پس از نوشتن:

1. Artifactها را دوباره از دیسک بخوان.
2. از متغیر اصلی حافظه برای Validation استفاده نکن.
3. Record count، Reference integrity، Rank/Score fidelity، Hash و Schema را کنترل کن.
4. Round-trip reconstruction را کنترل کن.
5. نتیجه را در Reload-validation Artifact ذخیره کن.

تنها پس از Reload Validation می‌توان Status نهایی را `PASS` اعلام کرد.

## ۱۱. جلوگیری از Hashهای حلقوی

ترتیب پیشنهادی تولید خروجی:

1. Core artifacts
2. Core hashes
3. Reload validation
4. Final manifest
5. Release
6. Acceptance
7. Handoff
8. Checkpoint

اگر فایلی به Hash فایل دیگری اشاره می‌کند، فایل دوم نباید هم‌زمان به Hash نسخه نهایی فایل اول وابسته باشد.

## ۱۲. زمان اجرا و Resume

پیش از هر عملیات با زمان احتمالی بیشتر از ۱۰ دقیقه اعلام کن:

- زمان تقریبی؛
- علت زمان‌بر بودن؛
- تعداد رکورد یا Pair؛
- امکان توقف؛
- امکان Resume؛
- محل Checkpoint.

اجرای طولانی باید Atomic checkpoint و قابلیت ادامه بعد از قطع Kernel، سیستم یا اینترنت داشته باشد و رکوردهای کامل‌شده را دوباره محاسبه نکند.

## ۱۳. مدل، دانلود و API

پیش از دانلود یا اجرای مدل:

- Cache محلی و حجم دانلود را بررسی کن؛
- Revision دقیق را ثبت کن؛
- Device و Runtime را بررسی کن؛
- ابتدا Smoke test اجرا کن؛
- سرعت و زمان اجرای کامل را تخمین بزن؛
- قابلیت Resume ایجاد کن.

بدون اجازه کاربر API پولی، دانلود مدل بزرگ یا سرویس خارجی را اجرا نکن. هر خروجی باید مقدار زیر را ثبت کند، مگر اینکه اجازه صریح دیگری داده شده باشد:

```text
paid_api_calls = 0
```

## ۱۴. Metadata و عدم استنتاج

Metadata ناقص را با حدس پر نکن. Author، Speaker، Content authority، Topic، Parent، Rights، Locator و Conflict label فقط از فیلد Canonical مربوط به خودشان گرفته شوند.

در نبود داده معتبر، یکی از وضعیت‌های مستند زیر را ثبت کن:

```text
NOT_PRESENT
NOT_APPLICABLE
NOT_ASSESSED_NO_CANONICAL_MAPPING
UPSTREAM_METADATA_LIMITATION
```

## ۱۵. مجوز پروژه

کارفرما مجوز کامل انجام پردازش‌های این پروژه را تأیید کرده است. Gate محدودکننده قبلی مجوز از جریان پروژه حذف شده است.

- Gate مصنوعی `INTERNAL_EVALUATION_ONLY` دوباره ایجاد نکن.
- Status تحویل را بدون دلیل به `READY_FOR_INTERNAL_EVALUATION_ONLY` محدود نکن.
- Rights موجود را فقط به‌عنوان Metadata منبع حفظ کن.
- نبود بعضی فیلدهای Rights را Blocker فنی Notebook نکن.
- مجوز تأییدشده کارفرما را بدون دستور صریح دوباره زیر سؤال نبر.

این موضوع شامل مجوز API پولی یا تغییر Repository نیست؛ آن‌ها همچنان اجازه جداگانه می‌خواهند.

## ۱۶. Git و Repository

بدون اجازه صریح کاربر:

- Commit یا Push نکن؛
- Branch را تغییر نده؛
- فایل unrelated را تغییر نده؛
- Artifact قبلی را حذف نکن؛
- Git history را بازنویسی نکن.

در پایان فقط فایل‌های ساخته‌شده یا تغییرکرده را گزارش کن.

## ۱۷. رفتار هنگام خطا

در صورت خطا:

1. Traceback کامل را بررسی کن.
2. علت ریشه‌ای را مشخص کن.
3. وابستگی‌های قبل از سل را کنترل کن.
4. اصلاح را در محل تعریف اصلی انجام بده.
5. فقط یک خط موقت برای عبور از خطا اضافه نکن.
6. تمام استفاده‌های بعدی متغیر یا تابع را جست‌وجو کن.
7. Syntax و `Restart & Run All` را دوباره بررسی کن.

Assert را حذف یا ضعیف نکن مگر اینکه خود Contract اشتباه باشد و دلیل آن مستند شود.

## ۱۸. Definition of Done

Notebook فقط وقتی کامل است که:

```text
objective = PASS
syntax_health = PASS
execution_health = PASS
numbering = PASS
markdown_rtl = PASS
canonical_input_hashes = PASS
configuration_frozen = true
configuration_changed_after_test = false
core_artifacts_written = true
reload_validation = PASS
manifest = PASS_COMPLETE_FROZEN
acceptance = PASS_COMPLETE_FROZEN
handoff = READY_FOR_NEXT_NOTEBOOK
checkpoint = PASS
paid_api_calls = 0
```

همچنین:

- Code Cell اجرا‌نشده یا Error output ذخیره‌شده وجود نداشته باشد؛
- Artifact فقط در حافظه باقی نمانده باشد؛
- خروجی مرحله بعد مستقل از Kernel فعلی قابل بارگذاری باشد؛
- Final Health با Artifactهای دیسک برابر باشد؛
- Notebook بعدی و مسیر Handoff مشخص باشند.

## ۱۹. نحوه گزارش به کاربر

در پایان فقط گزارش کن:

1. آیا Notebook واقعاً کامل شد؟
2. Final status چیست؟
3. چه Artifactهایی ساخته شدند؟
4. Reload validation پاس شد یا نه؟
5. مرحله بعد چیست؟
6. آیا اجرای طولانی یا API پولی انجام شد؟
7. آیا Git تغییر داده شد؟

اگر Notebook کامل نیست، صریحاً بنویس:

```text
OBJECTIVE_INCOMPLETE
```

سالم بودن ساختار یا اجرای سل‌ها به‌تنهایی به‌معنای تکمیل هدف Notebook نیست.
