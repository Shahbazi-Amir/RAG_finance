<div dir="rtl" align="right">

# قرارداد اجرایی NB23 — تحویل نسخه‌پذیر و تعویض‌پذیر از فاز دوم به سوم

**پروژه:** `Shahbazi-Amir/RAG_finance`  
**شاخهٔ مبنای مطالعه:** `rag-phase2`  
**نوت‌بوک مصرف‌کننده:** `notebooks/phase2/23_phase3_handoff.ipynb`  
**محل قرارگیری این قرارداد:** `notebooks/phase2/checklist/NB23_version_switchable_handoff_execution_contract_fa.md`  
**تاریخ:** ۲۹ اکتبر ۲۰۲۶  
**وضعیت:** قرارداد طراحی/اجرا؛ ایجاد این فایل به‌تنهایی به معنی اجرای NB23 یا پذیرش Release نیست.

## ۱. توافق اصلی

NB23 یک نوت‌بوک **واحد** با **۱۰ اقدام رسمی چک‌لیست** است؛ نوت‌بوک جدا برای NB22A و NB22B ساخته نمی‌شود. ورودی آن یک **مرجع صریح، نسخه‌دار و قابل‌تعویض** به بستهٔ Handoff/Release فاز دوم است. در هر اجرا فقط یک مرجع مؤثر انتخاب می‌شود و تمام خروجی‌های NB23 باید با هویت همان مرجع تولید شوند.

هدف این است که ابتدا با checkpoint موجود NB22A، قراردادها، Adapterها، نمونه‌ها و آزمون‌های ساختاری NB23 را در حالت Draft بسازیم و بعد از آماده‌شدن یک نسخهٔ دیگر (ازجمله NB22B)، **فقط `NB23_SOURCE_REF` در سل تنظیمات نوت‌بوک تغییر کند** و `Restart Kernel → Run All`، همان ۱۰ اقدام را برای ورودی جدید دوباره ارزیابی کند. هیچ مسیر، هش یا نام Release قدیمی نباید در سل‌های پایین‌دست hard-code بماند.

تعویض یک‌خطی **مشروط به وجود Adapter معتبر برای Schema نسخهٔ جدید** است. تغییر ناسازگار و ناشناخته نباید با تبدیل حدسی، انتخاب خودکار آخرین نسخه یا جعل مقادیر دور زده شود؛ باید خطای سازگاری صریح تولید کند تا یک Adapter نسخه‌دار افزوده شود. این شرط مانع طراحی یک نوت‌بوک واحد نیست.

## ۲. مرجع انتخاب‌شده و منشأ واقعی

مرجع اولیهٔ شناخته‌شده در چک‌لیست NB23، خروجی C054 نوت‌بوک ۲۲ است:

```text
reports/phase2/release/NB22.C054.quality_disposition/C054.supplemented_NB23_handoff.f41ed8f332785201ec29a7e9ca6c7f60c122730044419d5b833745fca17c059f.json
```

این رشته یک **مسیر اعلام‌شده در سند** است، نه تأیید اینکه فایل روی GitHub یا مک در همین محل وجود دارد. در اجرای محلی، سل C002 وجود و محتوای آن را بدون نوشتن کنترل می‌کند. اگر فایل در محل دیگری است، مقدار `NB23_SOURCE_REF` به مسیر **واقعی نسبی به ریشهٔ مخزن** تغییر داده شود؛ سل پایین‌دست نباید تغییر کند. اگر فایل قابل‌دسترسی نبود، وارد حالت `SOURCE_NOT_FOUND` می‌شویم، نه اینکه نسخه یا پذیرش صوری بسازیم.

ورودی NB22B زمانی قابل‌انتخاب است که ایجنت مربوط، Manifest/Handoff واقعی و نسخه‌دار تحویل دهد. **NB22B فقط به دلیل جدیدتر بودن، خودکار به مرجع اصلی تبدیل نمی‌شود.** انتخاب دستی و صریح مرجع، مبنای اجرای جدید است. وضعیت کیفیت و پذیرش از رکورد واقعی همان نسخه خوانده می‌شود.

## ۳. تفکیک اساسی وضعیت‌ها و Gateها

| سطح | معنی | آیا با NB22A قابل انجام است؟ |
| --- | --- | --- |
| `SOURCE_DISCOVERED` | فایل واقعی ورودی خوانده و هش و ساختار آن کنترل شده است | در صورت دسترسی به فایل، بله |
| `PROFILE_NORMALIZED` | Adapter با Schema شناسایی‌شده خروجی داخلی را بدون حدس ساخته است | پس از مشاهدهٔ Schema، بله |
| `CONTRACT_TESTED` | Schema و Fixtures مثبت/منفی، Resolver و اتصال نسخه‌ها واقعاً آزموده شده‌اند | در دامنهٔ موجود، بله |
| `DRAFT_HANDOFF` | بستهٔ تحویل فنی، با محدودیت‌ها و Gateهای باز آماده شده است | بله |
| `ACCEPTED_RELEASE_HANDOFF` | Release واقعی پذیرفته شده، همهٔ الزامات رسمی و Gateهای مؤثر گذرانده شده‌اند | خیر؛ NB22A فعلاً `accepted=false` گزارش شده است |

ساخته‌شدن Contract، قبولی Test ساختاری، دریافت checkpoint و **پذیرش Release** چهار واقعیت جدا هستند. `accepted_for_phase3=true` یا `release_id` پذیرفته‌شده بدون شاهد واقعی ساخته نمی‌شود. اگر NB22B هم Gate کیفیت را رد کند، NB23 باید با همان کد گزارش عدم‌آمادگی درست تولید کند.

## ۴. معماری داخلی ثابت

```text
NB23_SOURCE_REF  (تنها انتخابگر نسخه در C002)
  └─ Source Reader (relative-path + byte SHA256 + JSON/schema inspection)
      └─ Versioned Source Adapter Registry (NB22A / NB22B / ...)
          └─ Canonical NB23 Input Snapshot + source fingerprint
              ├─ Action 01: Release receipt and acceptance evidence
              ├─ Actions 02–05: Request / Response / Citation / status contracts
              ├─ Action 06: full version trace and release lock
              ├─ Actions 07–08: fixtures / negative tests / compatibility
              ├─ Action 09: sample conversations and consumer guide
              └─ Action 10: draft or accepted readiness decision and handoff
```

**Adapter فقط تفاوت شکل داده را تطبیق می‌دهد، نه معنای داده را تغییر می‌دهد.** فیلد غایب `UNKNOWN`/`MISSING`/`BLOCKED` در قرارداد مشتق می‌گیرد؛ به‌جای خالی‌بودن، `PASS`، صفر یا نام مدل ساخته نمی‌شود. Adapter باید نسخه، Schema ورودی، نگاشت فیلدها و Validation/Provenance خود را داشته باشد. کد Adapter نباید داخل Artifact/JSON وارد و اجرا شود. منبع خارجی غیرقابل‌اثبات در نتیجهٔ جداگانهٔ `UNVERIFIED_EXTERNAL_DEPENDENCY` حفظ می‌شود.

### هویت غیرقابل‌تعارض نسخه

ورودی هر اجرا با حداقل این‌ها پیگیری شود: `source_ref` نسبی، `raw_byte_sha256`، `source_schema_version`/`artifact_type` واقعی، Adapter version، `release_id` اگر واقعاً وجود دارد، `manifest_sha256` و `acceptance_decision_ref` اگر منبع معرفی می‌کند، و `configuration_fingerprint`. **هش بایت فایل، هش JSON کانونی، هش منطقی سند و Git blob با هم یکسان فرض نمی‌شوند.**

## ۵. محل خروجی و حفظ نسخه‌ها

- خروجی‌های مشتق NB23 به فضای **مجزای هر `source_fingerprint`** می‌روند؛ ترجیحاً مسیر کاری نسخه‌دار و content-addressed تحت `artifacts/phase2/phase3_handoff/` پس از کنترل واقعیت مسیرهای مخزن.
- خروجی اصلی NB22A/NB22B، Golden، Split، Index، Raw، مدل، فایل‌های `.env` و رأی تاریخی **دست‌نخورده** می‌مانند.
- بدون `release_id` واقعاً تخصیص‌یافته و تأیید پذیرش، فایل رسمی در `artifacts/phase2/releases/<release_id>/phase3_handoff_contract.json` ساخته یا ادعا نمی‌شود؛ فقط خروجی Draft در مسیر جدا ذخیره می‌شود.
- خروجی‌های مهم در همان filesystem با tempfile، flush/fsync و انتشار اتمی ذخیره و از دیسک Reload می‌شوند. اگر مسیر مقصد قبلاً با بایت متفاوت وجود دارد، به‌جای overwrite، توقف و گزارش تعارض انجام می‌شود.
- Manifest و Handoff با ترتیب بدون چرخهٔ هش ساخته می‌شوند: source/adapter → canonical snapshot → schemas/fixtures/tests → readiness decision → handoff.
- خروجی جدید نسخهٔ قبلی را overwrite نمی‌کند؛ امکان مقایسهٔ نسخه، rollback و replay مستقل باقی می‌ماند. NB23 خود rollback محصول را اجرا نمی‌کند.

## ۶. رفتار Run All و شبکه

- `Restart Kernel → Run All` باید با محیط تمیز و بدون متغیر Kernel قبلی کار کند. Imports و تنظیمات در سل‌های نخست، و خواندن از دیسک و بررسی Hash در بسته‌های مرتبط انجام شود.
- **پیش‌فرض API پولی صفر، دانلود خودکار مدل صفر، تغییر مخزن صفر** است. NB23 وظیفهٔ تولید/داوری جدید پاسخ یا بهبود موتور را ندارد.
- خطای یک Fixture یا پرونده باید ردیف مشخص با منشأ داشته باشد؛ خطای مشترک Reader، Schema، Hash یا Gate مؤثر باید ادامهٔ وابسته را متوقف کند. موارد سالم حفظ شوند.
- از کاربر درخواست اجرای مجدد NB19/NB20/NB21/NB22 برای آماده‌سازی نوت‌بوک نمی‌شود. شواهد موجود بازاستفاده و اختلاف نسخه صریح گزارش می‌شود.
- کنترل مثبت/منفی و خطای واقعی باید قابل شکست باشد؛ تست همیشه-PASS ممنوع است. Final Health فقط یک‌بار در پایان و جدا از Preflightها اجرا شود.
- **Run All برای نسخهٔ Draft می‌تواند سالم باشد ولی تصمیم رسمی آن `NOT_READY_FOR_ACCEPTED_HANDOFF` باشد؛ این یک نتیجهٔ معتبر است، نه خطای اجرا.**

## ۷. نقشهٔ اقدام‌محور NB23

| اقدام | زیرکارها | خروجی/معیار پایان | با Candidate فعلی |
| --- | ---: | --- | --- |
| ۱. دریافت نسخه و احراز پذیرش | ۵ | رسید مرجع، Manifest، Hash، وضعیت واقعی پذیرش | دریافت Candidate و گزارش Draft؛ پذیرش رسمی باز |
| ۲. Request Schema | ۵ | JSON Schema نسخه‌دار و تست مثبت/منفی مطابق قابلیت واقعی | قابل ساخت |
| ۳. Response Schema | ۵ | متن، Claims، Citation، status، Version/Confidence بدون فیلد جعلی | قابل ساخت |
| ۴. Citation و Attribution | ۵ | رزولوشن Website/Book/Transcript، نقش نویسنده/سردبیر/گوینده و Locator | قابل ساخت در دامنهٔ شواهد واقعی |
| ۵. وضعیت‌ها و خطاها | ۵ | نگاشت enumهای واقعی و Fixtureهای answer/no-answer/clarification/safety | قابل ساخت مشروط به Producer |
| ۶. Version Trace | ۵ | binding به Dataset/Chunk/Index/Retrieval/Prompt/Model/Policy/Eval | قابل ساخت؛ Missing صریح |
| ۷. Contract Fixtures و تست‌ها | ۵ | آزمون‌های مثبت، منفی، مرزی، dangling reference و Schema | قابل اجرا |
| ۸. Backward Compatibility | ۵ | ماتریس نسخه‌ها؛ Adapter/migration برای اختلاف واقعی | قابل طراحی/تست در دامنهٔ موجود |
| ۹. نمونه و راهنمای مصرف | ۵ | نمونه‌های دارای منشأ و راهنمای فارسی Phase3 Module00 | قابل ساخت به‌عنوان Draft |
| ۱۰. Readiness و تحویل | ۶ | Reload، Gate و سند Draft یا Accepted بر اساس واقعیت | Draft اکنون؛ Accepted بعد از تأیید Release |

هر اقدام قبل از اجرا با زیرکارها، کار انجام‌شده، شکاف و تعداد بستهٔ لازم مشخص شود. یک Markdown فارسی RTL و یک Python Cell کامل و شماره‌دار برای هر بستهٔ لازم؛ بدون افزونگی Preflight. نتیجهٔ Stage با بسته‌شدن اقدام و پذیرش Release اشتباه نشود.

## ۸. معیار سازگاری نسخه‌ها

اگر ورودی جدید شناسهٔ واقعی Release، قرارداد Citation، فیلدهای الزامی، enum، نوع داده، Nullability یا روابط Claim/Citation را تغییر داد، نتیجه باید یکی از موارد `COMPATIBLE`، `ADAPTER_REQUIRED`، `BREAKING` یا `NOT_COMPARABLE_NO_REAL_REFERENCE` با دلیل و شاهد باشد. Adapter فقط با Mapping صریح و آزمون مؤثر اضافه می‌شود. انتخاب نسخهٔ جدید به‌خودی‌خود اثبات سازگاری نیست.

**تضمین طراحی:** هستهٔ NB23 برای تعویض نسخه ثابت می‌ماند؛ تنها مرجع ورودی عوض می‌شود **به شرط** آنکه Adapter مناسب Schema جدید از قبل وجود داشته باشد. در غیر این صورت Runner با گزارش دقیق توقف می‌کند و بدون تغییر ۱۰ اقدام، Adapter پشتیبان همان Schema تکمیل می‌شود.

## ۹. استقلال NB22B و قواعد Git

کار بهبود در NB22B توسط ایجنت دیگر و مستقل پیش می‌رود. هیچ تغییر مستقیم در فایل‌ها، پوشه‌ها یا خروجی ایجنت از NB23 مجاز نیست. کار محلی موازی باید پوشه/Worktree جدا داشته باشد و هر Merge/Pull فقط با اقدام آگاهانهٔ کاربر انجام شود.

**قرارداد همین چت:** دستیار GitHub/مخزن را **فقط می‌خواند**؛ هیچ `commit`، `push`، `update_file`، ساخت شاخه، تغییر چک‌لیست یا حذف در مخزن انجام نمی‌دهد. دستیار فایل قرارداد و سل‌ها/نسخهٔ قابل دانلود را در چت تحویل می‌دهد. **کاربر فایل‌ها را خودش در مخزن محلی جایگذاری، اجرا، Save و در صورت تمایل Git می‌کند** و خروجی را ارسال می‌کند.

## ۱۰. پذیرش فنی و تحویل به Module00 فاز سوم

- کنترل نسخهٔ ورودی و خطوط منشأ، JSON Schemaها و negative tests، قواعد Locator/Attribution، Version trace، compatibility، فایل‌های لازم، Reload و Test fixture باید با مسیر و شمار واقعی مستند شوند.
- معیارهای Quality و Release باید از Manifest/Gate همان نسخه مصرف شوند؛ FAIL/BLOCKED یا تعویق حذف نشوند. نبود پذیرش رسمی در NB22A به PASS تبدیل نشود.
- برای Module00 فقط یک **بستهٔ قابل مصرف و نسخه‌دار** ارائه می‌شود: Contractها، نمونه‌ها، provenance، locks/refs، known limitations و گزارش Readiness. استقرار، احراز هویت، DB، UI و پذیرش خود Module00 وظیفهٔ NB23 نیستند.
- در پایان وضعیت هدف Notebook می‌تواند `ACHIEVED_IN_DRAFT_SCOPE` همراه `FORMAL_HANDOFF_BLOCKED`, یا `ACCEPTED_FOR_PHASE3_HANDOFF` با شاهد کامل باشد. تنها حالت دوم مجوز ادعای تحویل رسمی است.

## ۱۱. مراجع و دستور شروع

- [چک‌لیست ده‌اقدامی NB23](NB23_phase3_handoff_checklist_fa.md)
- [چک‌لیست NB22A](NB22A_remaining_work_checklist_fa.md)
- [چک‌لیست NB22B](NB22B_quality_improvement_checklist_fa.md)
- `data/Road_Maps/RAG_finance_phase2_operational_roadmap.md`
- `data/Road_Maps/RAG_finance_phase3_modular_execution_plan.md`، Module 00
- چهار فایل مبنای همکاری که در چت ارائه شده‌اند؛ در صورت اختلاف نسخه، دستور جدید کاربر و شاهد اجرایی جدید مقدم‌اند.

**اولین اجرای عملی:** Markdown معرفی، Markdown نقطهٔ شروع، C001 واردکردن Imports، C002 بررسی فقط‌خواندنی مرجع انتخاب‌شده. پس از مشاهدهٔ خروجی C002، Schema واقعی Source Adapter اقدام ۱ تثبیت می‌شود؛ نه با حدس.

</div>
