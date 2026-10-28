# گزارش اقدام ۲۸ — انتقال Confidence، کالیبراسیون و حدود اعتبار

تاریخ: ۲۷ اکتبر۲۰۲۶. پروژه: RAG_finance. شاخه: rag-phase2.

## ۱. وضعیت نهایی و دامنه

**وضعیت خروجی C041: ACTION28_CONFIDENCE_LIMITS_AND_CALIBRATION_TRANSFER_COMPLETE**

**دامنهٔ پایان: EXISTING_CONFIDENCE_CALIBRATION_EVIDENCE_AND_REPORTING_LIMITS**

اقدام۲۸ انتقال شواهد موجود Confidence و کالیبراسیون، حدود اعتبار مستقل و الزامات گزارش‌دهی را کامل کرده است. هدف، آموزش دوبارهٔ مدل یا اثبات احتمال صحت پاسخ نبود. تیک این اقدام، پذیرش Confidence کامل محصول یا Gate زنده نیست.

مالک پایان کار را اعلام کرده است. خروجی ذخیره‌شدهٔ C041 نیز پایان همین دامنه، عبور هر۱۹ کنترل، بررسی۱۰ Artifact و Reload=PASS را ثبت می‌کند.

## ۲. مأموریت چک‌لیست

متن اقدام۲۸: انتقال دقیق حدود Confidence، کالیبراسیون و اعتبار مستقل NB20 به گزارش و Gate؛ ثبت نیاز upstream بدون بازکردن ممیزی عمومی تازه.

این کار با مصرف منابع C404،C405،C406 وC409 تاC415 نوت‌بوک۲۰ انجام شده است. شمارهٔ اقدام‌های داخلی NB20 با شمارهٔ اقدام چک‌لیست NB21 یکی نیست؛ مثلاً C414 با عنوان داخلی action28، ورودی این انتقال است و جای اقدام۲۸ جاری به‌تنهایی معرفی نمی‌شود.

## ۳. نسخه و منشأ شواهد خوانده‌شده

- Commit اجرای ارسالی مالک: `52a07f76f78ab0802561509c3716a665d71054d0`، با پیام `28/49 in nb21 is done`.
- فایل: `notebooks/phase2/21c_evaluation_and_ablation_continued.ipynb`.
- Git Blob نوت‌بوک: `01575d6ca5934f48066d75c9e03faf620bac992e`.
- اندازهٔ فایل: 45243773 بایت.
- سل: C041؛ execution_count ذخیره‌شده:۶۲.
- Commit ثبت تیک: `64717eafea27b72e32e54ae12399efeb0d9a1b4b`.

در این تدوین، متن کامل دو سل افزوده‌شدهٔ Markdown وCode مربوط به C041 و خروجی آن‌ها از Patch همان Commit خوانده و به JSON معتبر بازسازی شد. کد نوت‌بوک اجرا نشد. این مشاهدهٔ مستقیم خروجی ذخیره‌شده است؛ خواندن دوبارهٔ بایت۱۰ Artifact روی مک، اجرای مجدد۱۹ کنترل یا تأیید مستقل معنا ادعا نمی‌شود.

## ۴. کارهای انجام‌شده

۱. خواندن منابع دقیق و کنترل هش مطابق قرارداد ثبت‌شدهٔ آن‌ها.
۲. حفظ دامنهٔ چهار مؤلفهٔ توصیفی Confidence و بررسی محدود چهارپرونده‌ای.
۳. انتقال نتیجهٔ کالیبراسیون موجود، با تفکیک بخش Fit و ارزیابی Development.
۴. ثبت هدف واقعی مدل و جلوگیری از نام‌گذاری آن به‌عنوان احتمال درستی پاسخ.
۵. ثبت بهبود و افت Metricها، بدون انتخاب گزینشی معیارهای بهترشده.
۶. ثبت محدودیت استقلال، عدم قطعیت و آستانهٔ پذیرش تاریخی.
۷. ساخت Gate ادعاهای گزارش با سیاست DENY برای ادعای ثبت‌نشده.
۸. ذخیرهٔ موجودی شواهد، Gate، محدودیت‌ها، Summary فارسی و گزارش، همراه Reload.
۹. حفظ گزارش‌های قبلی بدون پردازش یا داوری دوبارهٔ اقدامات۲۶ و۲۷.

## ۵. هدف کالیبراسیون و مخرج‌ها

هدف ثبت‌شده:

`COMPLETE_LINKED_REFERENCE_ANCHOR_IN_SELECTED_CONTEXT`

یعنی احتمال حضور کامل شاهد مرجع متصل در Context انتخاب‌شده؛ **احتمال صحت پاسخ نیست**. Raw score نیز به‌خودی‌خود احتمال معرفی نشده است.

| بخش | تعداد | دامنه |
|---|---:|---|
| Fit | ۲۰۶۲ | Development، براساس تقسیم ثبت‌شده |
| ارزیابی کنارگذاشته‌شده از Fit | ۶۰۲ | Development؛ برای Fit یا انتخاب مدل مصرف نشده است |
| جمع | ۲۶۶۴ | Development |
| Test استفاده‌شده در همین کالیبراسیون | صفر | به معنی دست‌نخورده‌بودن تاریخی Test کل پروژه نیست |

گروه‌بندی ثبت‌شده `TRANSITIVE_SHARED_REFERENCE_SOURCE_OR_EXACT_QUESTION` است. اشتراک منبع مرجع یا سؤال یکسان را کنترل کرده، اما همهٔ منابع Context بازیابی‌شده را پوشش نمی‌دهد؛ استقلال کامل منابع ادعا نشده است.

## ۶. نتایج ارزیابی موجود

مدل با Constant baseline همان آزمایش مقایسه شده است؛ اعداد زیر از خروجی ذخیره‌شده منتقل شده‌اند، نه محاسبهٔ تازهٔ Metric:

| معیار | مدل کالیبره | مبنای ثابت | مدل منهای مبنا | نتیجه |
|---|---:|---:|---:|---|
| Brier score | 0.119685034 | 0.131798568 | -0.012113534 | بهتر |
| Log loss | 0.398508601 | 0.433350290 | -0.034841689 | بهتر |
| AUC | 0.716231781 | 0.500000000 | +0.216231781 | بهتر |
| ECE؛ ده بازهٔ هم‌عرض | 0.024611707 | 0.005832482 | +0.018779225 | بدتر |

Brier، Log loss و AUC بهتر شده‌اند؛ ECE بدتر شده است. بنابراین all_metrics_improved=false محفوظ است. برای این ارزیابی تاریخی، عدم قطعیت Metricها برآورد نشده و آستانهٔ پذیرش ازپیش‌ثبت‌شده برقرار نبوده است؛ این موارد پسینی به آزمایش نسبت داده نشده‌اند.

## ۷. کنترل‌های پایان و معنای PASS

خروجی ذخیره‌شده۱۹/۱۹ کنترل موفق را ثبت می‌کند. کنترل‌ها از جمله دامنهٔ توصیفی، هدف مرجع، جدا بودن صحت پاسخ، تقسیم گروهی، شمار۲۰۶۲/۶۰۲، عدم استفاده از ارزیابی برای Fit/Selection، عدم استفاده از Test، عدم Refitting، ثبت نتیجهٔ مختلط Metricها و محدودیت‌های Gate گزارش‌دهی را بررسی کرده‌اند.

بررسی چهار مؤلفهٔ توصیفی، فقط چهار پروندهٔ source-reviewed و رفتار حالت‌های فاقد داده را پوشش می‌دهد. در منابع قبلی۱۹ آزمون فنی بدون شکست گزارش شده است؛ این۱۹ آزمون upstream با۱۹ کنترل انتقال C041 یکی نیست و هیچ‌کدام دقت معنایی کل جمعیت محسوب نمی‌شوند.

## ۸. Gate ادعاهای گزارش

نوع Gate: REPORTING_CLAIM_GATE.

ادعاهای مجاز، با Scope درست و افشای محدودیت‌های اجباری:
- HELDOUT_REFERENCE_PRESENCE_METRICS، در دامنه GROUPED_DEV_EVALUATION_602.
- SCOPED_DESCRIPTIVE_CONFIDENCE_COMPONENTS، در دامنه FOUR_SOURCE_REVIEWED_OFFLINE_CASES.
- ACTION28_EVIDENCE_TRANSFER_COMPLETE، در دامنهٔ انتقال ثبت‌شده.

سیاست ادعای ثبت‌نشده DENY است. این Gate برای کنترل ادعاهای گزارش است؛ به‌عنوان Safety verifier پاسخ، تخمین‌زن مستقل صحت پاسخ یا Gate متصل به Runtime زنده معرفی نشده است.

### محدودیت‌ها و ادعاهای نامجاز

- **L01:** هدف کالیبراسیون حضور کامل مرجع متصل در زمینه است. ادعای فاقد پشتوانه: `ANSWER_CORRECTNESS_PROBABILITY`.
- **L02:** چهار مؤلفهٔ توصیفی فقط در چهار مورد بررسی‌شده و رفتار حالت‌های فاقد داده پذیرش فنی دارند؛ اعتبار کل جمعیت ثابت نشده. ادعای فاقد پشتوانه: `POPULATION_VALIDATED_FOUR_COMPONENT_CONFIDENCE`.
- **L03:** گروه‌بندی اشتراک منبع مرجع یا سؤال یکسان را کنترل کرده؛ تمام منابع زمینهٔ بازیابی‌شده را پوشش نداده است. ادعای فاقد پشتوانه: `COMPLETE_SOURCE_INDEPENDENCE`.
- **L04:** Brier و Log Loss و AUC بهتر شده‌اند؛ ECE ده‌بازه‌ای نسبت به مبنای ثابت بدتر شده است. ادعای فاقد پشتوانه: `ALL_METRICS_IMPROVED`.
- **L05:** عدم قطعیت سنجه‌ها برآورد نشده و آستانهٔ پذیرش قبلی برای این ارزیابی ثبت نشده است. ادعای فاقد پشتوانه: `STATISTICAL_OR_THRESHOLD_ACCEPTANCE`.
- **L06:** این کالیبراسیون از Test استفاده نکرده؛ این امر به معنای دست‌نخورده‌بودن تاریخی Test در کل پروژه نیست. ادعای فاقد پشتوانه: `PROJECT_TEST_NEVER_EXPOSED`.
- **L07:** داوری‌های اقدامات ۲۶ و ۲۷ به‌خودی‌خود مرجع مستقل کالیبراسیون احتمال درستی پاسخ نیستند. ادعای فاقد پشتوانه: `INDEPENDENT_CALIBRATION_GOLD_FROM_PRIOR_JUDGMENTS`.
- **L08:** Gate این بسته برای ادعاهای گزارش است؛ اتصال آن به مسیر زندهٔ محصول و اعتبار Confidence محصول احراز نشده است. ادعای فاقد پشتوانه: `LIVE_PRODUCT_CONFIDENCE_ACCEPTANCE`.

## ۹. ورودی‌های دقیق و هش‌های ثبت‌شده

این مسیرها و SHA256ها از کد C041 خوانده شده‌اند. خروجی اجرا کنترل موفقشان را گزارش می‌کند؛ در تهیهٔ این گزارش، بایت فایل‌های روی مک دوباره خوانده نشده است.

### NB20c-C404

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action23_descriptive_output_C404_v1/C404.output.c019efac9cddb0fba6818abec4edcb83c026746046c91eda9acbd6e32fd82fb3.json`

SHA256 ثبت‌شده: `c019efac9cddb0fba6818abec4edcb83c026746046c91eda9acbd6e32fd82fb3`

### NB20c-C405

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action24_scoped_output_tests_C405_v1/C405.tests.946638ecdbe44b162cb12e0fa6a95c2e43e8b09e100552b14de8f2028067098b.json`

SHA256 ثبت‌شده: `946638ecdbe44b162cb12e0fa6a95c2e43e8b09e100552b14de8f2028067098b`

### NB20c-C406

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action23_24_scoped_completion_C406_v1/C406.decision.f33a4e4ef48e2839548b7647f1bbcb595bd8ebde4a8566d7bd9fc2981639ccdb.json`

SHA256 ثبت‌شده: `f33a4e4ef48e2839548b7647f1bbcb595bd8ebde4a8566d7bd9fc2981639ccdb`

### NB20c-C409

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action25_retrieval_baseline_C409_v1/C409.baseline.516749e3846daee8ad6da4d825a2371a77c9f5e48cd196653167b33bbd2f9115.json`

SHA256 ثبت‌شده: `516749e3846daee8ad6da4d825a2371a77c9f5e48cd196653167b33bbd2f9115`

### NB20c-C410

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action25_score_contract_C410_v1/C410.contract.70d918e07ea88049ff32b7525a5b9e63e48fb89aa5af609802a9d3230490a552.json`

SHA256 ثبت‌شده: `70d918e07ea88049ff32b7525a5b9e63e48fb89aa5af609802a9d3230490a552`

### NB20c-C411

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action26_retrieval_reference_C411_v1/C411.reference.89c3fd3e44e29b76d7e2573c4199bd0c4b62120733f22567121087c4f1818299.json`

SHA256 ثبت‌شده: `89c3fd3e44e29b76d7e2573c4199bd0c4b62120733f22567121087c4f1818299`

### NB20c-C412

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action27_grouped_partition_C412_v1/C412.partition.0db458a5a16e06bdc1d04170575039c603b7ec3be2bddcc8e0dd4d39a508761f.json`

SHA256 ثبت‌شده: `0db458a5a16e06bdc1d04170575039c603b7ec3be2bddcc8e0dd4d39a508761f`

### NB20c-C413

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action27_retrieval_calibrator_C413_v1/C413.calibrator.6db9849940b475ce522f1180c2f6fb4cb00551663db1d529703e9577d37d3e05.json`

SHA256 ثبت‌شده: `6db9849940b475ce522f1180c2f6fb4cb00551663db1d529703e9577d37d3e05`

### NB20c-C414

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action28_retrieval_evaluation_C414_v1/C414.evaluation.7f1745f542542ea973626f473cb5b564626e7e97c8d815a2e954d5a988f5c4f3.json`

SHA256 ثبت‌شده: `7f1745f542542ea973626f473cb5b564626e7e97c8d815a2e954d5a988f5c4f3`

### NB20c-C415

`artifacts/phase2/answerability_safety_confidence/work/outputs/nb20c_action25_28_scoped_completion_C415_v1/C415.decision.47e07ada9da821c0daa42aeb6c03f6924f0001029090c6f5740ba6a7f91004f8.json`

SHA256 ثبت‌شده: `47e07ada9da821c0daa42aeb6c03f6924f0001029090c6f5740ba6a7f91004f8`

## ۱۰. خروجی‌های تولیدشدهٔ C041

مسیرها و SHA256ها از خروجی ذخیره‌شدهٔ اجرای موفق نقل شده‌اند. حضور مسیر در گزارش، حضور فایل در GitHub یا کنترل مستقل بایت آن را ثابت نمی‌کند.

### گزارش اصلی

`reports/phase2/evaluation/NB21C.C041.action28_final/C041.report.910851f468de8c1e4cea8e9fcca391a199812b2ccbbfacd713926c97b3b849fc.json`

SHA256 بایت فایل، گزارش‌شده: `910851f468de8c1e4cea8e9fcca391a199812b2ccbbfacd713926c97b3b849fc`

### evidence_inventory

`reports/phase2/evaluation/NB21C.C041.action28_final/C041.evidence_inventory.3941577d7a3ad236ddc1db3756dbfb989d23dd854942d507dc482b583f8dbced.json`

SHA256 بایت فایل، گزارش‌شده: `3941577d7a3ad236ddc1db3756dbfb989d23dd854942d507dc482b583f8dbced`

### reporting_gate

`reports/phase2/evaluation/NB21C.C041.action28_final/C041.reporting_gate.aad26e00b15212b1dd6f3a4e7dfe2c1303c77c602854b7baa89799b0331a02be.json`

SHA256 بایت فایل، گزارش‌شده: `aad26e00b15212b1dd6f3a4e7dfe2c1303c77c602854b7baa89799b0331a02be`

### upstream_limitations

`reports/phase2/evaluation/NB21C.C041.action28_final/C041.upstream_limitations.7e2f5b6cee7044cb3ed3d9a463167a23175f94bf9eaac859660e8a6c0f2cb37b.json`

SHA256 بایت فایل، گزارش‌شده: `7e2f5b6cee7044cb3ed3d9a463167a23175f94bf9eaac859660e8a6c0f2cb37b`

### markdown

`reports/phase2/evaluation/NB21C.C041.action28_final/C041.summary_fa.e49e5f5cf4d498c9866d592a46ff0e0d418a211df20348386a0bbbaf7c882a82.md`

SHA256 بایت فایل، گزارش‌شده: `e49e5f5cf4d498c9866d592a46ff0e0d418a211df20348386a0bbbaf7c882a82`

## ۱۱. هزینه و عدم دوباره‌کاری

طبق خروجی و کد خوانده‌شده:
- API تازه: صفر.
- هزینهٔ API تازهٔ C041: صفر تومان.
- داوری معنایی تازه: صفر.
- Metric دوباره محاسبه نشده است.
- Calibrator دوباره Fit نشده است.
- اقدامات۲۶ و۲۷ تکرار نشده‌اند.
- منابع قبلی و Golden تغییر نکرده‌اند.
- خود C041 چک‌لیست را تغییر نداده و دستور Git اجرا نکرده است.

صفر هزینهٔ این سل، هزینهٔ تولید تاریخی منابع را صفر نمی‌کند. برای تغییر چت یا افزودن این گزارش، کالیبراسیون و داوری‌ها دوباره اجرا نشوند. تغییر واقعی هدف/نسخه/ورودی، قرارداد و آزمایش جدا می‌خواهد.

## ۱۲. ثبت تیک و تحویل

پس از تأیید پایان از سوی مالک و خواندن C041، فقط علامت اقدام۲۸ در فایل زیر از☐ به✅ تبدیل و Push شد:

`notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md`

Diff مستقل Commit ثبت تیک و بازخوانی فایل نهایی کنترل شد: یک فایل و یک خط حذف/اضافه، با تغییر فقط همان علامت. کد، نوت‌بوک، گزارش مخزن، تیک‌های دیگر و سربرگ تغییر نکردند. سربرگ قدیمی ممکن است هنوز شمار/گام قبلی را نشان دهد؛ جدول اکنون۲۸ تیک دارد و اقدام بعدی۲۹ است.

ادامهٔ چک‌لیست: اقدام۲۹، گردآوری latency مرحله‌ای و سراسری با تفکیک اجرای زنده، Cache، سخت‌افزار، warm/cold و تعداد نمونه. شواهد قبلی، از جمله latency ریرنکر، باید مصرف شوند؛ اندازه‌گیری دوباره پیش‌فرض نیست.

## ۱۳. خروجی ذخیره‌شدهٔ مبنا

```json
{
  "status": "ACTION28_CONFIDENCE_LIMITS_AND_CALIBRATION_TRANSFER_COMPLETE",
  "required_artifacts_verified": 10,
  "checks_passed": 19,
  "checks_total": 19,
  "fit_cases": 2062,
  "heldout_evaluation_cases": 602,
  "metrics": {
    "brier_score": {
      "model": 0.11968503429171104,
      "constant_baseline": 0.13179856790750388,
      "model_minus_baseline": -0.012113533615792843,
      "preferred_direction": "LOWER"
    },
    "log_loss": {
      "model": 0.39850860056686815,
      "constant_baseline": 0.4333502897982967,
      "model_minus_baseline": -0.03484168923142855,
      "preferred_direction": "LOWER"
    },
    "auc": {
      "model": 0.716231780867817,
      "constant_baseline": 0.5,
      "model_minus_baseline": 0.21623178086781703,
      "preferred_direction": "HIGHER"
    },
    "ece_10_equal_width_bins": {
      "model": 0.02461170724368839,
      "constant_baseline": 0.0058324820917020626,
      "model_minus_baseline": 0.018779225151986326,
      "preferred_direction": "LOWER"
    }
  },
  "all_metrics_improved": false,
  "action28_completed_in_reported_scope": true,
  "completion_scope": "EXISTING_CONFIDENCE_CALIBRATION_EVIDENCE_AND_REPORTING_LIMITS",
  "full_product_confidence_accepted": false,
  "new_api_calls": 0,
  "metrics_recomputed": false,
  "calibrator_refitted": false,
  "checklist_modified": false,
  "reload_validation": "PASS",
  "report": {
    "path": "reports/phase2/evaluation/NB21C.C041.action28_final/C041.report.910851f468de8c1e4cea8e9fcca391a199812b2ccbbfacd713926c97b3b849fc.json",
    "file_bytes_sha256": "910851f468de8c1e4cea8e9fcca391a199812b2ccbbfacd713926c97b3b849fc"
  },
  "outputs": {
    "evidence_inventory": {
      "path": "reports/phase2/evaluation/NB21C.C041.action28_final/C041.evidence_inventory.3941577d7a3ad236ddc1db3756dbfb989d23dd854942d507dc482b583f8dbced.json",
      "file_bytes_sha256": "3941577d7a3ad236ddc1db3756dbfb989d23dd854942d507dc482b583f8dbced"
    },
    "reporting_gate": {
      "path": "reports/phase2/evaluation/NB21C.C041.action28_final/C041.reporting_gate.aad26e00b15212b1dd6f3a4e7dfe2c1303c77c602854b7baa89799b0331a02be.json",
      "file_bytes_sha256": "aad26e00b15212b1dd6f3a4e7dfe2c1303c77c602854b7baa89799b0331a02be"
    },
    "upstream_limitations": {
      "path": "reports/phase2/evaluation/NB21C.C041.action28_final/C041.upstream_limitations.7e2f5b6cee7044cb3ed3d9a463167a23175f94bf9eaac859660e8a6c0f2cb37b.json",
      "file_bytes_sha256": "7e2f5b6cee7044cb3ed3d9a463167a23175f94bf9eaac859660e8a6c0f2cb37b"
    },
    "markdown": {
      "path": "reports/phase2/evaluation/NB21C.C041.action28_final/C041.summary_fa.e49e5f5cf4d498c9866d592a46ff0e0d418a211df20348386a0bbbaf7c882a82.md",
      "file_bytes_sha256": "e49e5f5cf4d498c9866d592a46ff0e0d418a211df20348386a0bbbaf7c882a82"
    }
  }
}
```

## ۱۴. آدرس‌ها و محل نگهداری گزارش

- [نوت‌بوک مبنا](https://github.com/Shahbazi-Amir/RAG_finance/blob/52a07f76f78ab0802561509c3716a665d71054d0/notebooks/phase2/21c_evaluation_and_ablation_continued.ipynb)
- [Commit اجرای اقدام۲۸](https://github.com/Shahbazi-Amir/RAG_finance/commit/52a07f76f78ab0802561509c3716a665d71054d0)
- [چک‌لیست پس از ثبت تیک](https://github.com/Shahbazi-Amir/RAG_finance/blob/64717eafea27b72e32e54ae12399efeb0d9a1b4b/notebooks/phase2/checklist/NB21_remaining_work_checklist_fa.md)
- [Commit صرفاً ثبت تیک](https://github.com/Shahbazi-Amir/RAG_finance/commit/64717eafea27b72e32e54ae12399efeb0d9a1b4b)

مسیر پیشنهادی برای قراردادن فایل توسط مالک:

`reports/phase2/evaluation/NB21_actions01_26_reports/NB21_action28_report_fa.md`

نام پوشهٔ قبلی برای سازگاری با گزارش‌های موجود حفظ می‌شود. این فایل گزارش در مخزن ایجاد یا Push نشده است؛ مجوز تغییر مخزن در این نوبت صرفاً برای تیک۲۸ بود.
