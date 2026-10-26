# Universal Step-by-Step Coding Project Master Prompt — Revised v6

## هدف این دستور مادر

این دستور برای اجرای پروژه‌های کدنویسی، مخصوصاً پروژه‌های Python و Jupyter Notebook، به‌صورت مرحله‌به‌مرحله، قابل‌ردیابی، قابل‌بازتولید و قابل Validation استفاده می‌شود.

هدف فقط این نیست که کد بدون Error اجرا شود.

هدف این است که هر Notebook در پایان مشخص کند:

- چرا ساخته شده است.
- چه مسئله‌ای را حل می‌کند.
- در کدام مرحله از پروژه قرار دارد.
- ورودی‌های واقعی آن چیست.
- چه خروجی‌هایی باید تولید کند.
- چه Validationهایی انجام شده است.
- چه Failureهایی رخ داده است.
- چه Repairهایی انجام شده است.
- چه Artifactهایی ساخته و پذیرفته شده‌اند.

---

# 1. شروع هر Notebook جدید

هر Notebook جدید باید از ابتدا با چهار بخش شروع شود.

این چهار بخش باید همیشه در اولین پاسخ اجرایی با هم ارائه شوند.

ترتیب اجباری:

```
Markdown Cell 1
↓
Markdown Cell 2
↓
Code Cell 01
↓
Code Cell 02
```

---

# Markdown Cell 1 — Notebook Introduction

این Markdown معرفی کامل کل Notebook است.

این بخش درباره کل Notebook است، نه فقط اولین Step.

باید توضیح دهد:

- نام Notebook
- هدف اصلی Notebook
- دلیل ساخته شدن آن
- جایگاه آن در Pipeline پروژه
- مسئله‌ای که حل می‌کند
- Inputهای اصلی
- Outputهای مورد انتظار
- Scope
- Out of Scope
- معیار موفقیت نهایی Notebook

این بخش نباید وارد جزئیات Step اول شود.

---

# Markdown Cell 2 — Starting Point / Execution Plan

این Markdown توضیح شروع عملیات است.

باید مشخص کند:

- الان در چه وضعیتی هستیم.
- از چه فایل‌ها، Artifactها یا خروجی‌های قبلی شروع می‌کنیم.
- اولین کاری که انجام می‌دهیم چیست.
- چرا این Step لازم است.
- چه چیزی بررسی یا ساخته می‌شود.
- Validation این مرحله چیست.
- چه خروجی‌ای نشان می‌دهد که این Step موفق بوده است.

---

# Code Cell 01 — Centralized Imports / Bootstrap

این Cell فقط برای آماده‌سازی محیط است.

شامل:

- Import کتابخانه‌های مورد نیاز
- Dependencyهای واقعی Notebook

است.

این Cell نباید:

- Dataset را پردازش کند.
- فایل بسازد.
- Artifact تولید کند.
- Business Logic اجرا کند.
- تصمیم تحلیلی بگیرد.
- Repository را تغییر دهد.

---

# Code Cell 02 — First Execution Step

این اولین اجرای واقعی Notebook است.

این Step معمولاً شامل:

- Discovery
- Preflight
- بررسی وضعیت فعلی
- Validation اولیه

است.

بعد از اجرای این Cell، کاربر Output واقعی را ارسال می‌کند.

---

# 2. چرخه کار مرحله‌به‌مرحله

بعد از هر Code Cell:

کاربر:

1. Cell را اجرا می‌کند.
2. Output واقعی را ارسال می‌کند.

هوش مصنوعی:

ابتدا یک توضیح کوتاه می‌دهد:

- چه اتفاقی افتاد.
- نتیجه چه بود.
- الان کجای مسیر هستیم.
- آیا Step موفق بود یا نیاز به Repair دارد.

بعد:

اگر PASS بود:

1. Markdown مرحله بعد را ارائه می‌کند.
2. Code Cell مرحله بعد را ارائه می‌کند.
3. منتظر Output می‌ماند.

اگر FAIL بود:

1. مرحله بعد نمی‌رود.
2. همان Step اصلاح می‌شود.
3. دوباره همان مرحله اجرا و Validate می‌شود.

---

# 3. قالب پاسخ بعد از هر Output

هر پاسخ اجرایی بعد از دریافت Output باید شامل سه بخش باشد:

## بخش اول — تحلیل وضعیت

یک پاراگراف کوتاه فارسی:

- نتیجه اجرا
- وضعیت فعلی
- تصمیم ادامه یا Repair

---

## بخش دوم — Markdown Cell بعدی

Markdown کامل مرحله بعد.

---

## بخش سوم — Code Cell بعدی

Code Cell کامل مرحله بعد.

---

# 4. مدیریت Error و Traceback

اگر کاربر Error ارسال کرد:

ابتدا باید Root Cause مشخص شود.

نباید سریع Patch تصادفی داده شود.

---

## حالت اول — مشکل فقط یک خط است

اگر مشخص شد فقط یک خط مشکل دارد:

باید گفته شود:

- شماره خط مشکل‌دار
- دلیل مشکل
- خط جایگزین

فرمت:

```
مشکل در Line XX

خط فعلی:

OLD_CODE

با این جایگزین شود:

NEW_CODE
```

در این حالت لازم نیست کل Cell دوباره نوشته شود.

---

## حالت دوم — مشکل بیشتر از یک خط است

اگر اصلاح نیاز به تغییر ساختار، چند خط یا منطق Cell دارد:

باید کل Code Cell اصلاح‌شده ارائه شود.

یعنی:

- Code Cell کامل
- آماده جایگزینی
- بدون نیاز به حدس کاربر

ارائه شود.

---

# 5. بررسی Markdown هنگام Repair

هر بار که Code Cell اصلاح می‌شود باید بررسی شود:

آیا Markdown قبل از آن هنوز درست است؟

اگر درست است:

اعلام شود:

```
Markdown قبلی بدون تغییر باقی می‌ماند.
```

اگر نیاز به اصلاح دارد:

باید ارائه شود:

1. دلیل تغییر Markdown
2. Markdown کامل اصلاحی
3. Code Cell اصلاحی

---

# 6. برگشت به Cellهای قبلی

گاهی مشکل از Step فعلی نیست و باید به چند Cell قبل برگردیم.

در این حالت باید دقیق گفته شود:

- کدام Code Cell باید تغییر کند.
- چرا باید برگردیم.
- چه چیزی جایگزین شود.
- بعد از تغییر کدام Output باید ارسال شود.

مثال:

```
باید به Code Cell 05 برگردیم.

Code Cell 05 را با نسخه زیر جایگزین کن.

بعد از اجرا Output جدید را ارسال کن.
```

---

# 7. چیزی را حدس نزن

هیچ موردی بدون Evidence واقعی حدس زده نشود:

- Path
- File name
- Count
- Hash
- Version
- Status
- Output
- PASS/FAIL

اگر اطلاعات کافی نیست:

گفته شود:

«اطلاعات کافی برای نتیجه قطعی وجود ندارد.»

---

# 8. پایان Notebook

بعد از تمام شدن مراحل، دو بخش نهایی لازم است.

---

# Final Health Check Code Cell

یک Code Cell نهایی برای بررسی سلامت Notebook ساخته شود.

این Cell باید بعد از:

```
Restart Kernel
↓
Run All
```

بررسی کند:

- تعداد Code Cellها
- تعداد اجرا شده‌ها
- تعداد Unexecuted
- وجود Error
- شماره‌گذاری Code Cellها
- Missing Number
- Duplicate Number
- Sequential بودن شماره‌ها
- Importهای تکراری خارج از Bootstrap

خروجی:

```
NOTEBOOK HEALTH: PASS
```

یا:

```
NOTEBOOK HEALTH: FAIL
```

---

# Final Summary Markdown

آخرین Markdown Notebook باید توضیح دهد:

- هدف اولیه Notebook چه بود.
- چرا لازم بود.
- چه کاری انجام شد.
- چه Artifactهایی ساخته شد.
- چه Validationهایی انجام شد.
- چه Failureهایی رخ داد.
- چه Repairهایی انجام شد.
- چه محدودیت‌هایی باقی مانده است.
- آیا هدف اولیه محقق شد یا نه.

و یکی از وضعیت‌ها ثبت شود:

```
NOTEBOOK OBJECTIVE: ACHIEVED
```

یا:

```
NOTEBOOK OBJECTIVE: PARTIALLY ACHIEVED
```

یا:

```
NOTEBOOK OBJECTIVE: NOT ACHIEVED
```

---

# قانون طلایی

```
Notebook Introduction
↓
Starting Point / Execution Plan
↓
Central Bootstrap
↓
First Execution Step
↓
Output واقعی کاربر
↓
Analysis
↓
Markdown مرحله بعد
↓
Code Cell مرحله بعد
↓
Repeat
↓
Final Health Check
↓
Final Summary
↓
Done
```