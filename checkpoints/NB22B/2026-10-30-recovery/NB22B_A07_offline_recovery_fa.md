<div dir="rtl" align="right">

## NB22B — اصلاح آفلاین قالب پاسخ‌های اقدام ۷

### گزارش

تمام ۱۱۴۹ اتصال ورودی، درخواست و شناسهٔ کش بررسی شد؛ برای ۱۰۹۱ تلاش ثبت‌شده، اتصال پاسخ خام و رسید نیز بررسی شد. ۴۳۸ پاسخ قبلاً معتبر بودند. با حذف فقط فیلد metadata با نام `schema_version` و مقدار دقیق `NB22B_GAP_REVIEW_OUTPUT_V1` از نمای اعتبارسنجی، ۴۰۵ پاسخ دیگر همهٔ کنترل‌های سخت‌گیرانهٔ قبلی را گذراندند. پاسخ خام، رأی، نقل‌قول، شناسه، نیازمندی و دلایل تغییری نکردند. مجموع پاسخ‌های معتبر محلی اکنون ۸۴۳ است؛ این عدد دقت معنایی یا پذیرش محصول نیست.

۲۴۷ پاسخ هنوز نگه داشته می‌شوند؛ ۵۶ خروجی پایان کامل ندارند و ۱۹۱ مورد ایراد ساختار، پوشش یا تطبیق شاهد دارند. ۵۸ درخواست اصلاً ارسال نشده و ۱ مورد HTTP504 دارد. هیچ موردی خودکار دوباره ارسال نمی‌شود. دلیلِ موجودنبودن فیلد reason_fa با متن ساختگی پر نمی‌شود.

### کار و زیرکار

کار: بازیابی پاسخ‌های موجود و ثبت گزارش مشتق اقدام ۷، بدون API.

۱. خاموش‌کردن ارسال پولی و مسیر داوری/تولید تازه؛ در پایان نیز خاموش می‌ماند.
۲. افزودن adapter محدود برای فیلد نسخهٔ شناخته‌شده؛ سایر نقص‌ها همچنان رد می‌شوند.
۳. اجرای مجدد فقط اقدام ۷ از کش و کنترل همهٔ شناسه‌ها، هش‌ها، پوشش‌ها و نقل‌قول‌ها.
۴. ذخیرهٔ گزارش جدید بدون تغییر فایل‌های تاریخی و کنترل صفر بودن افزایش شمارندهٔ API.

**اجرا:** کد زیر را در یک سل جدید، دقیقاً بعد از اقدام ۷ و قبل از اقدام ۸، در همان نوت‌بوک و همان کرنل اجرا کنید. سل‌های ۱ تا ۶ یا محاسبهٔ چندساعته را تکرار نکنید. اجرای این سل به ادامهٔ کرنل فعلی نیاز دارد؛ نوت‌بوک تعمیر را در کرنل جدا باز نکنید. اگر بعداً Run All نسخهٔ اصلی را بزنید، تنظیمات آغازین آن می‌توانند API را دوباره فعال کنند؛ این سل تعویض نسخهٔ اصلی نوت‌بوک نیست.

پس از اجرا، خروجی بازیابی ارسال شود. زیرکار۷٫۵ و تصمیم پذیرش همچنان باید بر اساس شواهد واقعی بررسی شوند. برای نتیجه‌های تازهٔ اقدام۸به‌بعد، آن سل‌ها باید پس از بازیابی اجرا شوند؛ خروجی قبلی آن‌ها خودکار به‌روز نمی‌شود.

</div>

```python
# NB22B — بازیابی آفلاین A07؛ در همان کرنل و پس از اقدام ۷ اجرا شود.
# هیچ درخواست شبکه‌ای ارسال نمی‌شود؛ ارسال پولی برای ادامه نیز خاموش می‌ماند.
required_names = ('CONFIG', 'S', 'GAP_REVIEW_SCHEMA', 'validate_gap_review',
                  'action07', 'run_action', 'save_json', 'json')
missing_names = [name for name in required_names if name not in globals()]
if missing_names:
    raise RuntimeError('Run this cell in the original NB22B kernel after action 7: ' + ', '.join(missing_names))

# یک بار ذخیره شود؛ اجرای دوبارهٔ سل، wrapper تو در تو ایجاد نمی‌کند.
if '_nb22b_strict_gap_validator_before_envelope_recovery' not in globals():
    _nb22b_strict_gap_validator_before_envelope_recovery = validate_gap_review

def nb22b_validate_gap_review_envelope_recovery(data, result):
    normalized = result
    removed_schema_version = None
    expected = set(GAP_REVIEW_SCHEMA)
    if (isinstance(result, dict)
            and set(result) == expected | {'schema_version'}
            and result.get('schema_version') == 'NB22B_GAP_REVIEW_OUTPUT_V1'):
        # فقط metadata شناخته‌شده؛ هیچ رأی، نقل‌قول، دلیل یا شناسه‌ای اصلاح نمی‌شود.
        normalized = {key: value for key, value in result.items() if key != 'schema_version'}
        removed_schema_version = result['schema_version']
    checked = _nb22b_strict_gap_validator_before_envelope_recovery(data, normalized)
    if removed_schema_version is not None:
        checked = {**checked, 'offline_format_adapter': {
            'version': 'NB22B_KNOWN_SCHEMA_VERSION_ENVELOPE_V1',
            'removed_envelope_field': 'schema_version',
            'recorded_envelope_value': removed_schema_version,
            'all_original_semantic_checks_reexecuted': True,
            'semantic_content_changed': False,
            'raw_response_modified': False}}
    return checked

# ثابت‌ماندن request و task identity: پرامپت و کلیدهای کش تغییر نمی‌کنند.
CONFIG['paid_model_dispatch'] = False
CONFIG['semantic_review']['enabled'] = False
CONFIG['product_execution']['enabled'] = False
validate_gap_review = nb22b_validate_gap_review_envelope_recovery
_nb22b_calls_before_recovery = S['new_api_calls']
A07 = run_action(7, action07)
if S['new_api_calls'] != _nb22b_calls_before_recovery:
    raise RuntimeError('OFFLINE_RECOVERY_UNEXPECTED_API_COUNTER_CHANGE')
_nb22b_recovered_states = S['memory'].get('gap_review_states', {})
_nb22b_recovered_count = sum(
    row.get('status') == 'LOCALLY_VALID_MODEL_GAP_REVIEW'
    and 'offline_format_adapter' in row
    for row in _nb22b_recovered_states.values())
_nb22b_offline_receipt = save_json('A07.offline_envelope_recovery', {
    'status': 'OFFLINE_ENVELOPE_RECOVERY_COMPLETE',
    'adapter_version': 'NB22B_KNOWN_SCHEMA_VERSION_ENVELOPE_V1',
    'recovered_valid_cached_reviews': _nb22b_recovered_count,
    'valid_reviews_total': sum(row.get('status') == 'LOCALLY_VALID_MODEL_GAP_REVIEW'
                              for row in _nb22b_recovered_states.values()),
    'new_api_calls': 0,
    'raw_cache_modified': False,
    'original_historical_reports_modified': False,
    'semantic_verdicts_changed': False,
    'paid_dispatch_left_disabled': True,
    'release_acceptance_granted': False,
})
print(json.dumps({'offline_recovery_output': _nb22b_offline_receipt,
                  'recovered_cached_reviews': _nb22b_recovered_count,
                  'new_api_calls': 0, 'paid_dispatch_left_disabled': True},
                 ensure_ascii=False, indent=2))

```
