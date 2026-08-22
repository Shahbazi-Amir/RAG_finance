<div dir="rtl" align="right">

# نقشه عملیاتی فاز ۴ RAG_finance

**Assessment، Learning، Planning، Progress و Admin Panel**

| <span dir="ltr">Repository</span> | <span dir="ltr">Shahbazi-Amir/RAG_finance</span> |
| ---: | ---: |
| Branch مبنا | <span dir="ltr">rag-phase2</span> |
| Commit ممیزی | <span dir="ltr">96c0f0c7d09f4bff107ed71664a0c57ed09f3214</span> |
| تاریخ نسخه | ۲۱ اوت ۲۰۲۶ |
| دامنه | مربی شخصی سواد مالی و پنل مدیریت گسترده |

## ۱. شرط ورود

- فاز ۳ Production و پایدار باشد.
- Auth، consent، isolation و حذف/Export داده کار کند.
- Conversation و RAG trace قابل اتکا باشد.
- RAG فاز ۲ Citation/Safety regression gate داشته باشد.
- مسئول تأیید محتوای مالی و Policy مشخص باشد.

## ۲. مرز محصول

### داخل فاز ۴

- آموزش و توضیح سواد مالی.
- سنجش دانش، رفتار و وضعیت مالی تعریف‌شده.
- بودجه، بدهی، پس‌انداز و هدف‌گذاری آموزشی.
- برنامه اقدام و پیگیری.
- ارجاع موارد پیچیده یا پرریسک.

### خارج از Scope پایه

- پیش‌بینی بازار.
- سیگنال خریدوفروش.
- مدیریت خودکار دارایی.
- انتقال وجه یا معامله.
- توصیه سرمایه‌گذاری شخصی بدون چارچوب و مجوز مستقل.

## ۳. چرخه اصلی کاربر

<div dir="ltr" align="left">Consent       ↓     Baseline Assessment       ↓     Financial Snapshot       ↓     Gap Explanation + Evidence       ↓     Learning Path + Action Plan       ↓     Chat + Tools + Check-ins       ↓     Reassessment       ↓     Progress Report / Human Referral</div>

## ۴. معماری هوشمندی

| موتور | مسئولیت | نباید انجام دهد |
| ---: | ---: | ---: |
| <span dir="ltr">RAG Engine</span> | پاسخ و منبع از دانش مؤلف | ساخت Claim بدون Evidence |
| <span dir="ltr">Assessment Engine</span> | سؤال، Scoring و سطح‌بندی نسخه‌دار | امتیازدهی آزاد توسط LLM |
| <span dir="ltr">Planning Engine</span> | قواعد و برنامه اقدام قطعی | محاسبه حساس با متن آزاد |
| <span dir="ltr">Conversation Engine</span> | سؤال روشن‌کننده، توضیح و لحن | تغییر نتیجه Rules |
| <span dir="ltr">Safety Router</span> | intent، محدودیت و referral | عبور خاموش از Policy |

## ۵. بسته P4-01 - Product Model و Taxonomy

### کارها

- تعریف Domain taxonomy: درآمد، هزینه، بودجه، بدهی، پس‌انداز، هدف، ریسک، رفتار و تصمیم.
- تبدیل منابع سه‌گانه به Learning objects.
- تعریف competency، prerequisite و سطح دشواری.
- تعریف outcomeهای آموزشی و actionهای مجاز.
- تعریف Policy مرز آموزش، برنامه‌ریزی و توصیه سرمایه‌گذاری.

### خروجی

- taxonomy.yaml
- competency_model.yaml
- learning_object.schema.json
- docs/product/safety_boundary.md

### Gate

هر سؤال آزمون، محتوا و Action به competency و Evidence معتبر متصل باشد.

## ۶. بسته P4-02 - Onboarding، Consent و Financial Profile

### داده حداقلی

- اهداف و اولویت‌ها.
- بازه درآمد و هزینه؛ ثبت دقیق فقط در صورت نیاز.
- بدهی، پس‌انداز و تعهدات به‌صورت ساخت‌یافته.
- ترجیح یادگیری و زمان در دسترس.
- consentهای جدا برای personalization و analytics.

### اصول

- progressive disclosure؛ همه داده‌ها در شروع اجباری نباشد.
- purpose limitation و retention مشخص.
- امکان ویرایش، حذف و توقف personalization.
- Snapshot نسخه‌دار؛ تاریخچه تغییرات بدون overwrite.

### Gate

کاربر بداند هر داده چرا گرفته می‌شود و حذف/پس‌گرفتن رضایت واقعاً اثر کند.

## ۷. بسته P4-03 - Assessment Engine

### ابعاد

- دانش مفهومی.
- رفتار و عادت.
- نگرش/اعتمادبه‌نفس.
- توان مدیریت جریان نقد.
- بدهی و تعهدات.
- پس‌انداز و تاب‌آوری.
- هدف‌گذاری و برنامه‌ریزی.

### طراحی فنی

- item bank نسخه‌دار.
- question/option/scoring schema.
- assessment form و adaptive routing در صورت اثبات.
- scoring rules قطعی، explainable و تست‌شده.
- confidence و missing-data handling.
- pre/post comparable versions.

استفاده از چارچوب‌های بیرونی فقط پس از بررسی مجوز، ترجمه حرفه‌ای و اعتبارسنجی ایرانی انجام شود؛ کپی مستقیم قابل قبول نیست.

### اعتبارسنجی

- content review توسط متخصص.
- cognitive interview و آزمون فهم.
- pilot item analysis.
- reliability و sensitivity to change.
- fairness بررسی‌شده برای گروه‌های تعریف‌شده.

### Gate

Score توسط LLM تولید نشود؛ نسخه، فرمول و پاسخ‌های موثر بر نتیجه قابل توضیح باشند.

## ۸. بسته P4-04 - Rules و Financial Calculators

### ابزارهای پایه

- cash-flow summary.
- emergency buffer indicator.
- debt burden و payment priority framework.
- savings goal calculator.
- goal feasibility و scenario comparison.
- budget allocation rule sets.

### قواعد

- ورودی، واحد، فرمول، rounding، missing data و exception صریح.
- rule version و effective date.
- unit/property-based tests.
- explanation template با Evidence.
- متخصص دامنه Rule release را تأیید کند.

### Gate

LLM فقط نتیجه Engine را توضیح دهد؛ حق تغییر عدد، اولویت یا هشدار را نداشته باشد.

## ۹. بسته P4-05 - Personalization و Learning Path

### ورودی

- assessment gaps.
- goals و financial snapshot.
- محتوای تکمیل‌شده.
- ترجیح و زمان کاربر.
- safety constraints.

### خروجی

- سطح فعلی و سه اولویت.
- Learning path مرحله‌ای.
- مقاله/فصل/ویدیو منتخب با دلیل انتخاب.
- micro-lesson، سؤال مرور و تمرین.
- next-best-action قابل توضیح.

### روش

ابتدا Rules-based و قابل توضیح؛ الگوریتم adaptive فقط پس از داده و آزمایش کافی.

### Gate

برای هر توصیه آموزشی، reason code و source/competency linkage ثبت شود.

## ۱۰. بسته P4-06 - Action Plan و Check-in

### قابلیت‌ها

- برنامه ۷ یا ۳۰ روزه.
- action item کوچک، deadline و reminder preference.
- ثبت Done/Skipped/Blocked.
- سؤال روشن‌کننده و مانع انجام.
- بازتنظیم برنامه با حفظ تاریخچه.
- escalation برای فشار بدهی یا ریسک تعریف‌شده.

### Gate

برنامه با Goal، Rule version و Evidence متصل و تغییرات آن Audit شود.

## ۱۱. بسته P4-07 - Conversation Coach

### رفتار

- استفاده از وضعیت مرحله‌ای کاربر بدون افشای داده غیرضروری.
- توضیح «چرا این پیشنهاد» و «چه منبعی».
- پرسیدن داده مفقود پیش از شخصی‌سازی.
- پیشنهاد محتوا یا ابزار مناسب، نه فقط متن طولانی.
- تشخیص تناقض داده و درخواست تأیید.
- عدم استفاده از حافظه آزاد خارج از Profile نسخه‌دار.

### خروجی ساخت‌یافته

- answer.
- claims/citations.
- used_profile_fields.
- rule_outputs.
- confidence components.
- suggested_learning/action.
- safety decision.

### Gate

هر پاسخ شخصی audit trace داشته و داده کاربر دیگری یا داده حذف‌شده را استفاده نکند.

## ۱۲. بسته P4-08 - Safety، Risk و Human Referral

### دسته‌ها

- normal education.
- needs clarification.
- insufficient data.
- high-impact personal decision.
- investment/trading request.
- distress/debt crisis marker.
- complaint یا suspected harm.

### رفتار

- محدودیت شفاف و غیرمبهم.
- ارائه آموزش عمومی به‌جای توصیه ممنوع.
- ارجاع با reason code و priority.
- human review queue با حداقل داده لازم.
- ثبت outcome و بازخورد برای Policy evaluation.

### Gate

تمام مسیرهای پرریسک Test case و owner انسانی مشخص داشته باشند.

## ۱۳. بسته P4-09 - پنل مدیریت محتوا و دانش

- Source/Document/Release و rights status.
- صف quarantine و data quality.
- taxonomy، competency و learning object.
- assessment/item/scoring versions.
- rule/policy/prompt versions و approvals.
- citation broken-link و stale-content review.
- publish، rollback و audit history.

مدیر نباید Raw SQL، Secret یا دسترسی نامحدود PII داشته باشد.

## ۱۴. بسته P4-10 - پنل عملیات کاربر و مشاور

- user support با masked data و least privilege.
- consent/deletion/export status.
- flagged conversation و referral queue.
- امکان note ساخت‌یافته با audit.
- assignment، SLA و resolution outcome.
- عدم نمایش عمومی اطلاعات مالی کامل مگر با مجوز نقش و علت.

### Gate

تمام مشاهده و تغییر مدیریتی audit event داشته و دسترسی نقش‌ها با تست منفی کنترل شود.

## ۱۵. بسته P4-11 - Analytics و Outcome

### قیف

- onboarding completion.
- assessment completion.
- first learning object.
- first action plan.
- action completed در ۷ روز.
- reassessment.
- retained learner.

### کیفیت

- groundedness و citation correctness.
- no-answer و policy violation.
- assessment reliability.
- plan acceptance و override.
- user-rated helpfulness.

### اثر

- تغییر score قبل/بعد.
- competency mastery.
- action completion.
- تغییر شاخص‌های cash-flow/debt فقط در کاربران مربوط و با تعریف روشن.

### Gate

Dashboard از eventهای نسخه‌دار ساخته و Vanity metric مانند تعداد پیام معیار اصلی اعلام نشود.

## ۱۶. بسته P4-12 - Experiment و Pilot

### طراحی پایلوت

- cohort و معیار ورود مشخص.
- baseline و follow-up window.
- primary/secondary outcomes.
- dropout و missing data.
- qualitative interviews.
- incident و harm review.

### آزمایش‌های نمونه

- مسیر عمومی در برابر مسیر مبتنی بر Assessment.
- explanation کوتاه در برابر تفصیلی.
- content-only در برابر content + action.
- reminder opt-in variants.
- human referral flow.

### Gate

ادعای «بهبود سواد مالی» فقط با داده قبل/بعد و روش تحلیل مستند مطرح شود.

## ۱۷. بسته P4-13 - Tests و Release

- assessment/scoring golden tests.
- calculator unit/property tests.
- personalization reason-code tests.
- profile isolation و consent revocation.
- end-to-end Assess→Plan→Reassess.
- safety/adversarial و human referral.
- accessibility/RTL.
- analytics event integrity.
- backward compatibility با نسخه‌های قدیمی assessment/rules.

## ۱۸. مدل داده اصلی

- financial_profiles و financial_snapshots.
- income_items، expense_items، debts و savings.
- assessments، assessment_versions، items، answers و scores.
- competencies، learning_objects و completions.
- goals، action_plans، action_items و check_ins.
- rule_sets، calculator_runs و explanations.
- risk_flags، referrals، assignments و outcomes.
- admin_actions و approval_records.

## ۱۹. ترتیب اجرا

1. P4-01 Taxonomy و Policy.
2. P4-02 Profile/Consent extension.
3. P4-03 Assessment.
4. P4-04 Rules/Calculators.
5. P4-05 Learning path.
6. P4-06 Action/Check-in.
7. P4-07 Conversation integration.
8. P4-08 Safety/Referral.
9. P4-09 و P4-10 Admin.
10. P4-11 Analytics.
11. P4-12 Pilot.
12. P4-13 Release.

## ۲۰. شواهد دانش فنی فاز ۴

- Domain taxonomy و Knowledge graph/competency model.
- روش طراحی و اعتبارسنجی Assessment فارسی.
- Rule engine، calculator specifications و test evidence.
- Personalization algorithm، reason codes و Ablation.
- Safety taxonomy، referral outcomes و harm review.
- longitudinal outcome model و pilot report.
- Human-in-the-loop architecture.
- versioning و lineage از Profile/Rule/Evidence تا پاسخ.

## ۲۱. Gate نهایی

- چرخه Assess→Learn→Act→Reassess کامل باشد.
- Assessment و Rules قطعی، نسخه‌دار و توضیح‌پذیر باشند.
- مسیر آموزشی به Corpus و competency متصل باشد.
- پاسخ شخصی used-data و source explanation داشته باشد.
- پنل Admin با RBAC، approval و audit کار کند.
- Safety و referral روی سناریوهای پرریسک پاس شود.
- پایلوت و گزارش Outcome وجود داشته باشد.

## ۲۲. تصمیم محصولی

فاز ۲ «دانش قابل اعتماد» می‌سازد. فاز ۳ «دسترسی قابل اعتماد» می‌سازد. فاز ۴ «تغییر قابل اندازه‌گیری» می‌سازد.

اگر فاز ۴ فقط چند فرم کنار چت اضافه کند، محصول همچنان یک سیستم جست‌وجوی متن باقی می‌ماند. اگر Assessment، Rules، Learning path، Action و Outcome طبق این نقشه اجرا شوند، محصول به مربی واقعی سواد مالی تبدیل می‌شود.

</div>
