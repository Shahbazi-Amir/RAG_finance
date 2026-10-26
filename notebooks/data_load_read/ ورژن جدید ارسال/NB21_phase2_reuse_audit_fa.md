# ممیزی اتصال شواهد فاز دوم به ۴۹ اقدام NB21

تاریخ: ۲۶ اکتبر ۲۰۲۶. مخزن Shahbazi-Amir/RAG_finance، شاخه rag-phase2.

## نتیجهٔ اصلی

بازاستفادهٔ مهم و گسترده‌ای وجود دارد. به‌خصوص مقایسهٔ Dense/Hybrid، مقایسهٔ Reranker، تحلیل خطا، عدم قطعیت و بخشی از latency از قبل خروجی واقعی دارند. این کارها نباید صرفاً به دلیل بازبودن تیک، دوباره اجرا شوند.

با این حال، این ممیزی نبود داوری قبلی برای تمام پرونده‌ها و تمام وظایف را اثبات نمی‌کند. فایل‌های بزرگ NB20/NB21b/NB21c و بخشی از داده‌های ردیفی کامل دریافت نشدند؛ اصل work/outputs مک نیز در دسترس نیست. در نتیجه، صف API جمعیتی جدید از این گزارش تأیید نمی‌شود.

این بررسی استخراج کامل ساختار منابع دریافت‌شده و بازخوانی هدفمند بخش‌های تصمیم‌ساز است؛ داوری معنایی تک‌تک رکوردها یا خواندن انسانی تمام واژه‌های همهٔ منابع ادعا نمی‌شود. هیچ کد تاریخی اجرا نشد، هیچ API مدل ارسال نشد، مخزن تغییر نکرد و تیک تازه ثبت نشد.

## نسخه و پوشش واقعی

- Commit: `a7c6a7756ac640acc7961dc663fe1030866164e3`.
- درخت کامل: 1177 entry، با truncated=false.
- موجودی مسیرهای فاز دوم و نقشه‌ها: ۲۱۲ فایل؛ این عدد کل فایل‌های مک نیست.
- دریافت و تحلیل ساختاری: ۱۶۴ فایل، شامل ۳۰ نوت‌بوک فاز دوم و یک نوت‌بوک مقایسهٔ فاز اول، ۹۸ JSON، ده JSONL و ۲۵ متن.
- هویت Git Blob محاسبه‌شده با نسخهٔ مخزن: ۱۶۴ از ۱۶۴ مطابق.
- خطای Parse در فایل‌های دریافت‌شده: صفر.
- NB21 اصلی: شش بخش خروجی خواندنی، با ۶۹۴ شمارهٔ سل بازسازی‌شده. این مسیر، کنترل بایت فایل اصلی ipynb نیست.
- مجموع رکوردهای سل استخراج‌شده: 3263؛ شامل سل‌های Markdown و Code.
- ارجاع‌های لفظی مسیر استخراج‌شده: 6738؛ این‌ها اتصال ردیفی موفق یا شمار فایل یکتا نیستند.
- ۲۲ فایل بزرگ دریافت نشدند؛ متن سل‌های NB21 اصلی از Export در دسترس است. ۲۸ مورد دیگرِ انتخاب‌نشده، قالب‌های باینری/تکراری یا نقشهٔ فازهای دیگر بودند.

## یافته‌های تأییدشده و اثر بر عدم دوباره‌کاری

### ۱. اقدام ۳۴: مقایسهٔ Dense و Hybrid قبلاً اجرا شده است

منبع: notebooks/phase2/16_hybrid_retrieval.ipynb، Code Cell 18، سل فیزیکی ۳۶.
پنج سیستم مقایسه شده‌اند. Recall@10 ثبت‌شدهٔ Dense برابر 0.4735470589637256 و Weighted Hybrid برابر 0.621242522284189 است. nDCG@10 به‌ترتیب 0.37395705045915284 و 0.5381727779077033 است. این‌ها نتیجهٔ همان قرارداد تاریخی‌اند، نه اجرای جدید یا تعمیم به کیفیت پاسخ.

کار بعد: مصرف نتیجه و تنظیمات و تطبیق با قرارداد گزارش NB21. اجرای دوبارهٔ Dense/Hybrid پیش‌فرض نیست. عمق رتبه، Gold و tie-break حفظ شوند.

### ۲. اقدام ۳۵ و بخشی از ۲۹/۴۰/۴۱/۴۲: خروجی جمعیتی Reranker موجود است

منبع: notebooks/phase2/17_reranking.ipynb، Code Cell 15، سل فیزیکی ۳۰.
۲۶۶۴ Development، با candidate depth=50. Recall@10 از 0.621242522284189 به 0.6676743707993709 و nDCG@10 از 0.5381727779077033 به 0.5988342300716867 رسیده است.

اختلاف nDCG@10 برابر 0.06066145216398333 و CI ثبت‌شدهٔ ۹۵٪ با ۵۰۰۰ بازنمونه‌گیری حدود [0.051490917807556505, 0.07022573580323598] است. این CI مربوط به همان مقایسه است و به معیار دیگر منتقل نمی‌شود.

۸۹۳ بهبود، ۴۸۴ افت و ۱۲۸۷ بدون تغییر ثبت شده‌اند. Code Cell 16، سل فیزیکی ۳۲، تحلیل شکست و پرونده‌ها را دارد. این شاهد مستقیم برای دفتر خطا و Failure catalogue است؛ تولید دوبارهٔ خطا لازم نیست.

latency محلی ONNX CPU با depth=50 برای ۲۵۱۴ Query موجود است: p50=6.021237732998998s و p95=8.405428699801632s. این زمان کل محصول یا زمان Cache نیست.

### ۳. اقدام ۳۶: مرجع سیاست نهایی، دقیق‌تر از گزارش قبلی شد

NB18-C062..C065 آزمایش‌های مقدماتی‌اند؛ C065 حتی سیاست ۸/۶ را بررسی کرده است. برای سیاست نهایی ۸/۵، به C075..C079 مراجعه شود؛ در فایل فعلی C075 سل فیزیکی ۱۵۲ و C076..C079 به‌ترتیب ۱۵۴،۱۵۶،۱۵۸،۱۶۰ هستند.

C076 سیاست source=8/document=5 با reranker_order را انتخاب و C077 آن را روی ۲۶۶۴ بسته اعتبارسنجی کرده است: ۲۶۶۱۶ آیتم منتخب و ۲۴ حذف. C079 تطابق Configuration و ADR نهایی را ثبت کرده است. Recall کانونی Context در این سیاست 0.6671023702273697 و Hit rate برابر 0.8498498498498499 گزارش شده است.

برای بستن دامنهٔ Context اقدام ۳۶ همین شواهد باید تطبیق و گزارش شوند؛ اثر روی پاسخ نهایی فقط در صورت مطالبهٔ قرارداد و نبود شاهد مرتبط جدا باز می‌ماند. حذف cap غیرفعال NB16 جای آزمون سیاست فعال NB18 نیست.

### ۴. ساخت Golden و داوری منبع قبلاً انجام شده‌اند

NB12i و NB12j کامل دریافت و ساختار سل‌ها/خروجی‌هایشان تحلیل شد. گزارش Golden فریز ۳۸۱۳ QA را ثبت کرده است. JSONL داوری Seed شامل ۳۸۱۷ ردیف، نگاشت Claim شامل ۴۰۳۹ ردیف و متن Canonical Claim شامل ۴۰۰۶ ردیف Parse شد.

این شواهد نباید دوباره تولید شوند. با این حال، داوری Seed، اعتبار Golden و داوری Claim منبع با ارزیابی پاسخ فعلی یا مرجع جامع Answerability یکی نیستند. این تمایز، محدودیتِ کاربرد شاهد است، نه حذف کار قبلی.

### ۵. سه جفت فایل واقعاً یکسان‌اند

Git Blob سه گروه تکراری شناسایی شد: Handoff Sparse، Release Sparse و Acceptance Sparse در ریشه و زیر notebooks/phase2. هر جفت یک محتوا دارد و دو اجرای مستقل شمرده نمی‌شود. مسیرها در audit_summary.json ثبت شده‌اند.

### ۶. وضعیت جاری چک‌لیست حفظ شد

۲۳ تیک از ۴۹؛ اقدامات ۲۲–۲۵ با USER_ACCEPTED_SCOPED_COMPLETION بسته‌اند. این تصمیم باز نشد. درصد پوشش آن‌ها با درصد صحت یکی نیست. اقدامات ۱۰،۱۲ و ۲۶–۴۹ در چک‌لیست بازند؛ اما اجرای NB21c ممکن است از ثبت چک‌لیست جلوتر باشد و هنوز کامل خوانده نشده است.

## نگاشت ۴۹ اقدام به شواهد

ستون ارجاع تاریخی از نقشهٔ قبلی است؛ ستون سل‌های مستقیم به محتوای دریافت‌شدهٔ این ممیزی متصل است. «سل مستقیم» اثبات پذیرش یا اجرای سالم تمام آن سل نیست. خروجی، خطا و دامنه باید در رکورد همان سل دیده شود. برای شمارهٔ سل‌های اصلی از source و شناسهٔ نوشته‌شده استفاده شود؛ شمارهٔ فیزیکی صرفاً Locator کمکی است.

| اقدام | موضوع | وضعیت چک‌لیست | راهنمای منبع | سل مستقیمِ استخراج‌شده | کار باقی‌مانده/حدود |
|---:|---|---|---|---:|---|
| 1 | مأموریت و مرزها | تیک‌خورده | نقشهٔ تفصیلی، NB21-C057 و چک‌لیست | 1 | مأموریت دوباره طراحی نشود؛ تغییر دامنه فقط مستند. |
| 2 | Git و نسخه | تیک‌خورده | HEAD همین ممیزی و Preflightهای قبلی | 2 | وضعیت محلی هنگام اجرا فقط یک بار بررسی شود؛ HEAD امروز، وضعیت دیروز را اثبات نمی‌کند. |
| 3 | فایل مرجع | تیک‌خورده | NB21 اصلی و 21b ادامه | 1 | Current tree has NB21c too; original historical guide mentioning only NB21/NB21b is superseded. |
| 4 | تحویل C455 | تیک‌خورده | NB20c-C454/C455 و هش تحویل | 2 | فایل محلی و ارجاعات لازم مصرف شوند؛ بازاجرای عمومی NB20c ممنوع. |
| 5 | موجودی Canonical | تیک‌خورده | Manifestهای داده، Golden، Chunk، Releaseهای NB13..18 و C303 | 2 | فهرست موجود را به‌روز/متصل کنید؛ Inventory از صفر نسازید. |
| 6 | Cache و آزمایش‌ها | تیک‌خورده | NB12i/j، NB16..20c، NB21 و این ممیزی | 93 | نتیجهٔ تاریخی را به وظیفهٔ فعلی Join کنید؛ مفقود در Reader را «انجام‌نشده» نگویید. |
| 7 | منشأ خروجی | تیک‌خورده | NB19-C195 و Test recovery، NB20c و C060/C069 | 5 | Split، مدل، Agent review، Cache و Replay جدا بمانند. |
| 8 | Gap matrix | تیک‌خورده | C017/C034/C041، C095 و ممیزی پیوست | 3 | مسئول واقعی هر شکاف و وضعیت اتصال مشخص شود؛ شکاف تکراری نسازید. |
| 9 | تعریف Metric | تیک‌خورده | NB21-C020 و C040 | 2 | تعریف و مخرج قبلی مصرف؛ نام مشابه Metric مجوز همسان‌فرض‌کردن نیست. |
| 10 | Slice معتبر | باز؛ اجرای تازه بررسی‌نشده | تاکسونومی، Corpus authority، C026/C194 و پیشنهادهای C329 | 47 | نگاشت پیشنهادشده پذیرفته‌شده نیست؛ شکاف Topic/Question type و جزئیات Authority حفظ شود. |
| 11 | Test و طرح مقایسه | تیک‌خورده | NB21-C027..C032، ارزیابی تاریخی NB15..17 | 6 | سابقهٔ Test پاک یا از نو دست‌نخورده اعلام نشود. |
| 12 | آستانه/بودجه/Freeze | باز؛ اجرای تازه بررسی‌نشده | C034، Freezeهای جزئی NB16..18 و C095 | 1 | معیارهای مصوب نسخهٔ نهایی و اختلاف پوشش ۹۰٪/۹۵٪ تعیین تکلیف شود؛ Target اولیه Gate نهایی نیست. |
| 13 | Rubric و مرجع | تیک‌خورده | C035..C041، رجیستری بازبینی و Golden lineage | 7 | مواد قدیمی مصرف؛ استقلال و کفایت جدا ثبت شوند. |
| 14 | آزمون روش | تیک‌خورده | C298..C301 و NB21B-C047..C069 | 4 | آزمایش‌های تشخیصی موجود تکرار نشوند؛ فقط خطای جدیدِ مشخص. |
| 15 | تصمیم روش | تیک‌خورده | C302 و تصمیم‌های ناظر ثبت‌شده در C078/C095 | 1 | ثبت تصمیم کامل است؛ امتیاز مستقل جمعیت هنوز از آن نتیجه نمی‌شود. |
| 16 | Reader/Join | تیک‌خورده | C303 و C014/C083/C086/C088 | 1 | آداپتور در محل معتبر اصلاح شود؛ Readerهای موازی نسازید. |
| 17 | Smoke/Pilot | تیک‌خورده | C303 Pilot/Resume/Replay و آزمون‌های موجود | 1 | همان Pipeline با همان ورودی دوباره آزمایش نشود؛ تغییر مؤثر دلیل تست محدود است. |
| 18 | Runner قابل ادامه | تیک‌خورده | C303 و Cacheهای دارای request fingerprint | 1 | خروجی معتبر دوباره Dispatch نشود؛ attempts نامعلوم با resend خودکار جبران نشوند. |
| 19 | تطبیق Retrieval | تیک‌خورده | NB16/NB17 و C192/C304 | 5 | در دامنهٔ ثبت‌شده بسته؛ همان مقایسه تکرار نشود. |
| 20 | Metric روی Dev/Slice معتبر | تیک‌خورده | C003 و تصمیم اصلاحی ناظر | 3 | در دامنهٔ مصوب بسته؛ Missing نگاشت‌ها و الزام باز اقدام ۱۰ در گزارش بماند. |
| 21 | اختلاف/پوشش/شکست Retrieval | تیک‌خورده | C173/C195/C196/C304 | 4 | در دامنهٔ ثبت‌شده بسته؛ شکست‌های شناخته‌شده به Error catalogue منتقل شوند. |
| 22 | Groundedness | بستهٔ محدود | NB19 support، C060/C069 و Context متصل C093 | 1 | Claimهای پاسخ فعلی، شاهد Context و رأی مرتبط تطبیق؛ Source Claim داوری‌شده جای پاسخ فعلی نیست. |
| 23 | Completeness | بستهٔ محدود | Golden Claim/QA/Validation، رجیستری ۲۲ بازبینی و C018/C019/C063 و C118 گزارش‌شده | 5 | مرجع ضرورت/کفایت و پوشش پاسخ؛ فقط Missing واقعی استخراج شود؛ B10 محفوظ. |
| 24 | Citation | بستهٔ محدود | NB19-C195، C023..C077 و ۱۲۱۷۸ Citation گزارش‌شدهٔ C088 | 1 | تعلق به نسخهٔ پاسخ، معنای رابطه و پوشش Claim جدا از Locator؛ ۳۱ نگاشت باز تعیین وضعیت واقعی شود. |
| 25 | Attribution | بستهٔ محدود | Corpus کانونی، Schema، Acceptanceهای منبع و C090 | 74 | نقش نمایش‌داده‌شده و الزام نمایش جدا؛ منشأ هویت و انتساب داخل پاسخ کنترل شود. |
| 26 | No-answer | باز؛ اجرای تازه بررسی‌نشده | پاسخ/routeهای NB19، سیاست NB20 و محدودیت مرجع Golden | 3 | Intent یا NONCRITICAL برچسب truth پاسخ‌پذیری نیست؛ مرجع معتبر مثبت/منفی و Clarification لازم است. |
| 27 | Safety | باز؛ اجرای تازه بررسی‌نشده | رجیستری ۱۱۴۹ Test و C436/C439/C455 | 2 | ممیزی پسینی و رفتار مولد زنده جدا؛ شمار بحرانی صفر به معنای ایمنی همهٔ جمعیت نیست. |
| 28 | Confidence | باز؛ اجرای تازه بررسی‌نشده | Calibration و Handoff NB20c | 1 | هدف احتمال حضور شاهد و محدودیت استقلال منتقل شود؛ بازکالیبراسیون عمومی پیش‌فرض نیست. |
| 29 | latency | باز؛ اجرای تازه بررسی‌نشده | NB15 test report، NB16، NB17 latency، لاگ NB19 | 240 | یک جدول بر حسب Run/مرحله/تعداد واقعی؛ Cache latency به‌جای تولید زنده ننشیند. |
| 30 | Token/Cost/Failure | باز؛ اجرای تازه بررسی‌نشده | Cacheهای API و خروجی‌های NB19/NB20/NB21 | 239 | Usage یکتا با request fingerprint؛ Resume و unknown billing جدا. |
| 31 | Trade-off | باز؛ اجرای تازه بررسی‌نشده | ADRهای Hybrid/Reranker/Context و گزارش هزینه | 6 | تجمیع کیفیت/هزینه در دامنهٔ همسان؛ Fresh API لازم نیست مگر شکاف اندازه‌گیری مصوب. |
| 32 | Normalization ablation | باز؛ اجرای تازه بررسی‌نشده | NB08 sidecar و Policy | 23 | وجود before/after مصرف؛ اثر Retrieval/پاسخ هنوز جدا تعیین شود. |
| 33 | Chunking ablation | باز؛ اجرای تازه بررسی‌نشده | NB11 Candidateها و NB12h استقلال Gold | 28 | Candidateها بازسازی نشوند؛ فقط شکاف Index/Metric و Mapping سازگار. |
| 34 | Dense/Hybrid | باز؛ اجرای تازه بررسی‌نشده | NB16-C18 و C192/C304 | 5 | بازاستفادهٔ مقایسهٔ هم‌قرارداد؛ محدودیت depth/tie-break حفظ شود. |
| 35 | Reranker ablation | باز؛ اجرای تازه بررسی‌نشده | NB17-C15 و NB21 Same-pool | 9 | نتایج همان Pool و عدم قطعیت موجود مصرف شود. |
| 36 | Diversity ablation | باز؛ اجرای تازه بررسی‌نشده | NB18-C62..C65 و capهای واقعی | 6 | Use NB18-C075..C079 and finalized configuration for selected source=8/document=5; C062..C065 are exploratory and include 8/6. |
| 37 | Verifier ablation | باز؛ اجرای تازه بررسی‌نشده | NB19 کنترل‌های واقعی و C195 | 1 | verifier مستقلِ ناموجود جعل نشود؛ قبل/بعد معتبر یا شکاف صریح. |
| 38 | Freeze نهایی | باز؛ اجرای تازه بررسی‌نشده | Releaseهای مؤلفه و Manifestهای موجود | 3 | Freeze کل آزمایش NB21، روش و Gate هنوز یکپارچه نشده؛ سابقهٔ Test حفظ شود. |
| 39 | ارزیابی نهایی Test | باز؛ اجرای تازه بررسی‌نشده | نتایج Retrieval Test، Test recovery و ممیزی NB20c | 7 | بخش تاریخی قابل مصرف؛ Missing معتبر طبق طرح ثابت؛ اجرای کل Test از صفر نه. |
| 40 | مقایسه زوجی/عدم قطعیت | باز؛ اجرای تازه بررسی‌نشده | Bootstrapهای NB16/NB17 و C195 | 3 | دامنه/واحد resampling و هم‌بستگی منابع تطبیق؛ CI یک معیار به معیار دیگر منتقل نشود. |
| 41 | Error taxonomy | باز؛ اجرای تازه بررسی‌نشده | NB17-C16، C196، شکست داور B05 و Holdها | 2 | خطاهای موجود را یکپارچه کنید؛ تولید خطای مصنوعی تازه لازم نیست. |
| 42 | Failure cases | باز؛ اجرای تازه بررسی‌نشده | لاگ اختلاف‌ها و شاهدهای متصل | 2 | شناسه، نسخه، شدت، مسئول و Regression متناظر؛ موارد سخت حذف نشوند. |
| 43 | مقایسه فاز ۱ | باز؛ اجرای تازه بررسی‌نشده | phase1/10_evaluation و فایل ده‌سؤالی ۲۰۲۶/۰۷/۰۹ | 13 | هشت in_scope و دو out_of_scope تاریخی؛ مقایسهٔ هم‌شرط هنوز نیازمند تطبیق، نه ادعای برتری از دو Dataset. |
| 44 | گزارش‌های نهایی | باز؛ اجرای تازه بررسی‌نشده | تمام گزارش‌های مؤلفه و این نقشه | 3 | تجمیع شواهد در خروجی رسمی NB21؛ گزارش ممیزی جای Benchmark کامل نیست. |
| 45 | Regression Gate | باز؛ اجرای تازه بررسی‌نشده | Core-46، ده سؤال فاز۱، خطاهای واقعی و Gateهای مؤلفه | 2 | آستانه/وابستگی مصوب و پوشش معتبر؛ FAIL یا نامعین با تیک پوشانده نشود. |
| 46 | Manifest/Handoff NB22 | باز؛ اجرای تازه بررسی‌نشده | الگوی Releaseهای NB16..18 و C455 | 1 | فقط بستهٔ NB21 با وضعیت واقعی Gate ساخته شود؛ Release کل فاز۲ نیست. |
| 47 | Reload | باز؛ اجرای تازه بررسی‌نشده | کدها و الگوی C303/C454 و Manifestها | 2 | Reload زنجیرهٔ خروجی نهایی NB21، نه تکرار همهٔ تولیدات تاریخی. |
| 48 | اجرای پاک | باز؛ اجرای تازه بررسی‌نشده | سابقهٔ Run-All-safe NB12j، Final Healthهای NB10/NB17/NB18 | 2 | 21b فعلی دارای FIX، history dependency و Error ذخیره‌شده است؛ اجرای امن نهایی هنوز اثبات نشده. |
| 49 | Summary/چک‌لیست | باز؛ اجرای تازه بررسی‌نشده | شاهدهای پایان هر اقدام و تصمیم ناظر | 2 | Current checklist has 23 ticks, not the historical 19. |

## دفتر قابل‌خواندن برنامه

action_evidence_index.json دارای ۴۹ رکورد است. هر اقدام به Producerهای مستقیمِ یافت‌شده، سل فیزیکی، شناسه، عنوان، وضعیت خروجی و مسیر Artifactهای ذکرشده متصل است. این دفتر هنوز Join ردیفیِ کل جمعیت نیست. کلید fresh_api_work_certified در تمام رکوردها false باقی مانده؛ به معنی نبود نیاز احتمالی نیست، بلکه کار تازه هنوز از این ممیزی قطعی نشده است.

source_coverage.json برای هر فایل دریافتی، Commit/Blob، SHA256، قالب، شمار ردیف یا سل و وضعیت Parse را نگه می‌دارد. producer_cells.json فهرست سل‌هاست. artifact_references.json ارجاع‌های لفظی را نگه می‌دارد؛ tracked=false به معنی فقدان روی مک نیست. همهٔ ارجاع‌ها الزاماً نام فایل کامل یا مسیر Canonical نیستند و رشته‌های برنامه‌ای می‌توانند شامل Placeholder باشند.

reported_results.json خلاصهٔ گزارش‌های JSON را نگه می‌دارد. remaining_access_gaps.json منابع بزرگِ دریافت‌نشده و اثر دقیق دسترسی را نشان می‌دهد. selection.json دلیل انتخاب‌نشدن سایر قالب‌ها را حفظ می‌کند.

## شکاف دسترسی باقی‌مانده

این فهرست ادعای انجام‌نشدن کار نیست. در میان نوت‌بوک‌ها، مهم‌ترین منبع برای وضعیت امروز NB21c است. NB20/NB20b/NB20c نیز برای اثبات هم‌وظیفگی داوری‌های قدیمی باید از خروجی کامل یا Export معتبر قابل بررسی شوند. برای Sparse و NB21b گزارش‌های کوچک مرتبط در دسترس بوده، ولی خود نوت‌بوک‌های بزرگ کامل دریافت نشدند.

| منبع | علت/اثر |
|---|---|
| `artifacts/phase2/golden_dataset_v2/golden_dataset_v2.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `artifacts/phase2/golden_dataset_v2/golden_v2_claim_eligibility_manifest_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `artifacts/phase2/golden_dataset_v2/golden_v2_seed_pool_reviewed_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `artifacts/phase2/golden_dataset_v2/golden_v2_seed_pool_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `artifacts/phase2/knowledge_registry/claim_semantic_neighbor_candidates_v1.jsonl` | Large intermediate retrieval/neighbor data; not automatically a blocker for answer-judgment reuse. |
| `artifacts/phase2/knowledge_registry/claim_semantic_relation_full_adjudication_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `artifacts/phase2/knowledge_registry/claim_validation_full_disposition_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `artifacts/phase2/knowledge_registry/claim_validation_full_semantic_adjudication_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `data/phase2/context/context_builder_v1/context_evidence_registry_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `data/phase2/context/context_builder_v1/context_packets_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `data/phase2/retrieval/hybrid_retrieval_v1/hybrid_candidates_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `data/phase2/retrieval/reranker_v1/reranked_candidates_v1.jsonl` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/15_sparse_index.ipynb` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/20_answerability_safety_confidence.ipynb` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/20b_answerability_safety_confidence_scoped_review.ipynb` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/20c_answerability_safety_confidence_audit_and_acceptance.ipynb` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/21_evaluation_and_ablation.ipynb` | Cell content available in tracked readable export; original notebook byte-level verification remains separate. |
| `notebooks/phase2/21b_evaluation_and_ablation_continued.ipynb` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/21c_evaluation_and_ablation_continued.ipynb` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/archive/series12_notebooks/12a_golden_dataset_initial.ipynb` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/archive/series12_notebooks/12b_golden_dataset_continuation_compact.ipynb` | Current row-level scope cannot be certified from this source until accessed. |
| `notebooks/phase2/data/phase2/index/sparse_index_v1/sparse_postings_v1.jsonl` | Large intermediate retrieval/neighbor data; not automatically a blocker for answer-judgment reuse. |

## تصمیم اجرایی

۱. کارهای دارای شاهد مستقیم مانند ۳۴،۳۵، بخش Context در۳۶، latency ریرنکر و تحلیل شکست‌ها، نامزد تجمیع و ثبت هستند؛ اجرای دوبارهٔ تولیدکننده پیش‌فرض نیست.
۲. بسته‌شدن ۲۲–۲۵ محفوظ است. شواهد این دور دوباره داوری نمی‌شوند.
۳. دربارهٔ ۲۶–۲۸، قبل از کار تازه باید نتیجهٔ واقعی NB21c خوانده شود. گزارش فعلی نمی‌گوید این کارها انجام نشده‌اند.
۴. هیچ صف تازهٔ API برای کل Test یا Development از این ممیزی تأیید نشد. Golden، Criticality و پشتیبانی منبع بدون تطبیق، جای وظیفهٔ فعلی نمی‌نشینند.
۵. تکمیل شکاف دسترسی فقط محتوا/Export منابع مشخص را می‌خواهد؛ آپلود ۸ گیگ، Embedding، Index یا همهٔ Rawها لازم نیست. برای local work/outputs، خروجی فشردهٔ دفتر/رسید/قراردادهای مرتبط کافی است تا ابتدا دامنه مشخص شود.

## منابع آنلاین اصلی

- [NB21_remaining_work_checklist_fa.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/a7c6a7756ac640acc7961dc663fe1030866164e3/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md)
- [NB21_actions22_25_scoped_closure.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/a7c6a7756ac640acc7961dc663fe1030866164e3/reports/phase2/evaluation/NB21_actions22_25_scoped_closure.md)
- [16_hybrid_retrieval.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/a7c6a7756ac640acc7961dc663fe1030866164e3/notebooks/phase2/16_hybrid_retrieval.ipynb)
- [17_reranking.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/a7c6a7756ac640acc7961dc663fe1030866164e3/notebooks/phase2/17_reranking.ipynb)
- [18_context_builder.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/a7c6a7756ac640acc7961dc663fe1030866164e3/notebooks/phase2/18_context_builder.ipynb)
- [21c_evaluation_and_ablation_continued.ipynb](https://github.com/Shahbazi-Amir/RAG_finance/blob/a7c6a7756ac640acc7961dc663fe1030866164e3/notebooks/phase2/21c_evaluation_and_ablation_continued.ipynb)
- [RAG_finance_NB21_full_reuse_map_fa_20261023.md](https://github.com/Shahbazi-Amir/RAG_finance/blob/a7c6a7756ac640acc7961dc663fe1030866164e3/notebooks/data_load_read/RAG_finance_NB21_full_reuse_map_fa_20261023.md)

## حدود ادعا

صحت انتقال بایت‌های ۱۶۴ فایل و Parse آن‌ها بررسی شد. محتوای علمی و کیفیت جمعیت از این کنترل فنی نتیجه نمی‌شود. عدد فایل/سل/ارجاع درصد تکمیل علمی نیست. این ممیزی گسترده و قابل‌ردیابی است، اما با وجود شکاف‌های صریح بالا، «بررسی کامل تمام سوابق محلی و آنلاین بدون هیچ مورد جاافتاده» نامیده نمی‌شود.
