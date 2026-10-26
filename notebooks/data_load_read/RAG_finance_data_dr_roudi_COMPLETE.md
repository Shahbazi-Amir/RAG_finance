<div dir="rtl" style="text-align: right; line-height: 1.9;">

# مرجع جامع داده‌ها، Knowledge Authority و قیود طراحی RAG Finance — Dr. Komeil Roudi

**نسخه:** پس از تکمیل Notebook 10 — Taxonomy & Knowledge Engineering  
**وضعیت:** مرجع انتقالی برای ادامه Phase 2 و طراحی Chunking / Retrieval  
**Primary Knowledge Authority:** Dr. Komeil Roudi

---

# 1. هدف این سند

این سند مرجع ثابت برای درک ماهیت داده‌های پروژه `RAG_finance` و نحوۀ استفاده از آن‌ها در مراحل بعدی RAG است.

هدف پروژه ساخت یک Knowledge Base عمومی مالی نیست. هدف، ساخت یک RAG تخصصی است که:

- دانش مستقیم دکتر کمیل رودی را در بالاترین سطح Authority نگه دارد؛
- محتوای تحت نظارت ایشان را به‌عنوان Secondary Evidence حفظ کند؛
- سؤال‌ها، مجری‌ها، مهمان‌ها و شرکت‌کنندگان را برای Context نگه دارد؛
- هیچ محتوایی را فقط به دلیل حضور در Corpus به دکتر نسبت ندهد؛
- Lineage، Source Identity، Attribution، Rights و Locator را در تمام مراحل حفظ کند؛
- در Retrieval و Generation بتواند میان «دانش مستقیم دکتر»، «دانش تحت نظارت»، «Context مکالمه» و «Context حل‌نشده» تفاوت واقعی ایجاد کند.

اصل مرکزی پروژه:

> **Primary Knowledge Structure باید از Core Primary Corpus استخراج شود و پراکندگی Secondary / Guest / Contextual content نباید ساختار دانش اصلی را بازطراحی کند.**

---

# 2. سه مفهوم که هرگز نباید با هم یکی شوند

در تمام Pipeline باید این سه مفهوم جدا بمانند:

## 2.1. Knowledge Authority

این Evidence تا چه حد مجاز است ساختار دانش اصلی پروژه را تعریف کند.

## 2.2. Source Attribution

متن واقعاً توسط چه فرد یا Source تولید شده است.

## 2.3. Conversation Context

متنی که لزوماً Primary Knowledge نیست، اما برای فهم سؤال، پاسخ، استدلال یا ادامۀ گفتگو لازم است.

مثال:

1. سؤال مجری
2. پاسخ دکتر
3. سؤال تکمیلی شرکت‌کننده
4. توضیح تکمیلی دکتر

در چنین حالتی Context باید حفظ شود، اما سؤال مجری یا شرکت‌کننده نباید به دکتر Attribution شود.

---

# 3. Corpus پذیرفته‌شده Phase 2

Artifact اصلی پذیرفته‌شده:

`data/phase2/processed/documents_dedup_quality_accepted_v1.jsonl`

تعداد کل:

**19,456 Document**

SHA256:

`9d72c709f81b1218c5aac064052c7ed1da34869f671e6e32762864e0ad70ea40`

توزیع Source Type:

| Source Type | تعداد |
|---|---:|
| Website | 529 |
| Book | 2,701 |
| Transcript | 16,226 |
| **Total** | **19,456** |

این Dataset برای Internal Phase 2 Processing پذیرفته شده است.

نکتۀ مهم:

> Processing Acceptance با Formal Release Eligibility یکی نیست.

---

# 4. مدل رسمی Knowledge Authority پس از NB10

پس از Reconciliation نهایی، کل Corpus در چهار لایۀ رسمی قرار می‌گیرد.

## Tier 1 — CORE_PRIMARY_KNOWLEDGE

**14,705 Document**

اجزاء:

- Book: **2,701**
- Website Direct Author: **76**
- Transcript Primary: **11,928**

این لایه تنها لایه‌ای است که می‌تواند ساختار اصلی Topic / Subtopic / Curriculum / Competency را تعریف یا تغییر دهد.

## Tier 2 — SUPERVISED_SECONDARY_KNOWLEDGE

**453 Document**

این لایه شامل Websiteهایی است که نویسندۀ مستقیم آن‌ها دکتر نیست، اما تحت نظارت / سردبیری / تأیید علمی ایشان منتشر شده‌اند.

کاربرد:

- Supporting Evidence
- Coverage Extension
- Retrieval Support
- Terminology Support
- Cross-check

اما:

> Tier 2 نباید Primary Taxonomy را override یا reshape کند.

## Tier 3 — CONTEXTUAL_NONPRIMARY

**1,944 Document**

عمدتاً شامل:

- Host
- Guest
- Participant
- Other explicit non-primary speaker
- Human-confirmed secondary guest

کاربرد:

- سؤال
- Context
- مقایسه
- Dialogue reconstruction
- فهم پاسخ دکتر

اما:

> نباید به‌عنوان دیدگاه مستقیم دکتر ارائه شود.

## Tier 4 — UNRESOLVED_CONTEXT

**2,354 Document**

Speaker یا Attribution این Segmentها با Evidence فعلی به‌طور قابل اتکا حل نشده است.

سیاست:

- حذف نشوند.
- به دکتر نسبت داده نشوند.
- برای Context و Review حفظ شوند.
- تا وجود Evidence جدید در ساختار Primary Knowledge اثر تعیین‌کننده نداشته باشند.

---

# 5. Website Data

کل Website:

**529**

تقسیم رسمی:

- Direct Author / Primary: **76**
- Editorial Supervision / Secondary: **453**

اصل:

> Direct Author و Editorial Supervision دو سطح Evidence متفاوت هستند.

برای Retrieval پاسخ‌هایی مانند «نظر دکتر چیست؟» یا «دکتر چه می‌گوید؟»، Direct Author باید بر Secondary اولویت داشته باشد.

453 مقالۀ تحت نظارت همچنان ارزشمند هستند، اما نباید به شکل «نوشتۀ مستقیم دکتر» Citation یا Generation شوند.

---

# 6. Book Data

کل Book Documentها:

**2,701**

کتاب‌ها از قوی‌ترین منابع Primary Corpus هستند.

در طراحی RAG باید بین مفاهیم زیر تفاوت حفظ شود:

`Work != Edition != File`

موارد مهمی که باید در Chunking و Retrieval حفظ شوند:

- Work ID
- Edition ID در صورت وجود
- Heading Path
- Section / Chapter relation
- Page / stable locator فقط اگر واقعاً معتبر باشد
- Source lineage
- Parent / child structural relation
- document_id
- raw/source relation

کتاب‌ها فقط مجموعه‌ای از Paragraphهای مستقل نیستند؛ ساختار آموزشی و ترتیب Headingها در NB10 برای کشف Curriculum استفاده شده است.

بنابراین:

> Chunking کتاب نباید Heading hierarchy را نابود کند.

---

# 7. Transcript Data

کل Transcript:

**16,226 Segment**

## 7.1. Authority profile رسمی Transcript

- `PRIMARY_CANONICAL_ATTRIBUTION`: **11,209**
- `PRIMARY_EXPLICIT_SOURCE_MARKER`: **718**
- `PRIMARY_HUMAN_CONFIRMED_OVERLAY`: **1**
- `SECONDARY_HUMAN_CONFIRMED_OVERLAY`: **1**
- `NONPRIMARY_EXPLICIT_CONTEXT`: **1,943**
- `UNRESOLVED_SPEAKER_CONTEXT`: **2,354**

Transcript Primary Total:

**11,928**

Transcript Contextual Non-primary Total:

**1,944**

Unresolved:

**2,354**

---

# 8. سیاست Speaker در Transcript

Canonical Speaker اصلی پروژه:

`Dr. Komeil Roudi`

ولی Canonical Attribution فقط با Evidence ثبت می‌شود.

قواعد:

1. Unknown Speaker inference ممنوع است.
2. Speaker label با Canonical Identity یکی نیست.
3. Alias فقط در Scope واقعی Program معتبر است.
4. Guest / Host / Participant باید هویت مستقل داشته باشند.
5. سؤال و Context نباید صرفاً به دلیل نزدیک بودن به پاسخ دکتر، به دکتر نسبت داده شود.
6. Human-confirmed overlays باید از Parser attribution قابل تفکیک بمانند.
7. Chunking نباید مرز Speaker را به شکل مخرب Merge کند.

اصل:

> **Preserve Context, do not collapse Attribution.**

---

# 9. Program-specific Context

بعضی Programها Solo نیستند و Chunking آن‌ها باید Conversation-aware باشد.

## `program:khane-to`

Human-confirmed structure:

- Dr. Komeil Roudi
- one host

7 Segment دارای labelهای غیرمنتظره در Review Queue باقی مانده‌اند.

این 7 مورد:

- حذف نشده‌اند،
- Hard Quarantine نشده‌اند،
- برای Review حفظ شده‌اند.

## `program:asre-shirin`

Human-confirmed structure:

- دو Season
- Dr. Komeil Roudi
- یک مجری زن
- حدود 8 شرکت‌کنندۀ زن

Open metadata gap:

- `season_number` برای **902 Segment** موجود نیست.

این یک Metadata Gap است، نه Structural Failure.

## `program:chehelston`

شامل Contextهایی با Guestهای دیگر است.

بنابراین:

- تمام Content آن Primary Dr. Roudi نیست.
- Speaker-aware / context-aware chunking ضروری است.
- Unlabeled / unresolved paragraphs نباید به‌صورت حدسی Primary شوند.

## `program:uni-tehran`

دارای گفتگوها و Contextهای چندنفره است.

در NB10 دیده شد بعضی Conceptها مانند Taxation در Conversation alternation ظاهر می‌شوند:

- Segment مستقیم دکتر
- Segment سؤال / توضیح دیگران
- Segment unresolved

بنابراین chunking صرفاً بر اساس window ثابت بدون Speaker/Conversation boundary می‌تواند Attribution را خراب کند.

---

# 10. Deduplication Policy

NB09 نشان داد شباهت متنی به تنهایی اثبات Duplicate نیست.

نتایج:

- Exact Duplicate Groups: **192**
- Members: **931**
- Near-duplicate candidate pairs: **15,929**
- Cross-source candidate pairs: **37,796**
- Automatic deletion: **0**
- Automatic merge: **0**
- Automatic canonicalization: **0**

اصل:

> `Exact Duplicate ≠ Automatic Source Deletion`

و:

> `High Similarity ≠ Same Evidence`

در Chunking نیز این اصل ادامه دارد:

> دو Chunk مشابه از دو Source مختلف نباید صرفاً به دلیل similarity به یک Source واحد collapse شوند.

Source independence و lineage باید حفظ شود.

---

# 11. Rights / Release Gate

در وضعیت فعلی:

- Internal Processing Allowed: **19,456**
- Formal Release Eligible: **0**
- Rights state: `EVIDENCE_REQUIRED`
- Release status: `BLOCKED_PENDING_RIGHTS`

اصل:

> `EVIDENCE_REQUIRED` یک Release Gate است، نه Data Quality Failure.

بنابراین Chunking داخلی Phase 2 مجاز است، ولی Export / Publication / Formal Release باید Rights-aware باقی بماند.

---

# 12. Frozen Taxonomy v1

Artifact:

`artifacts/phase2/taxonomy/taxonomy_v1.json`

SHA256:

`335690044b2e4eff684f7f347809f2c5cb8c39624a939dc01408d9ca898fe977`

Status:

`FROZEN`

## 12.1. هفت Top-level Topic

1. `financial_literacy_foundations`
2. `spending_saving_money_management`
3. `credit_debt_banking`
4. `work_income`
5. `investment`
6. `risk_insurance`
7. `financial_decision_making`

---

# 13. Curriculum Nodes فریز‌شده

Taxonomy v1 دارای **7 Curriculum Node** است.

مهم‌ترین ساختار استخراج‌شده از Primary Curriculum:

`work_income`  
→ `children_business`

و زیر آن:

- `goods_and_services_basics`
- `entrepreneurship_production_resources`
- `children_business_pricing`
- `children_business_profit`
- `product_presentation_and_promotion`

همچنین:

- `giving_and_gifting`

به‌عنوان Curriculum Node واقعی ثبت شده و Bridge آن به:

`spending_saving_money_management`

است.

---

# 14. Taxation

`taxation_and_financial_obligations`

به‌عنوان:

`CROSS_TOPIC_EDUCATIONAL_MODULE`

در Level 2 ثبت شده است.

قواعد:

- Top-level Topic جدید نیست.
- به زور زیر یک Topic خاص قرار نگرفته است.
- Global alias نیست.
- در Chunking باید بتوان Evidence آن را از چند Context نگه داشت.
- Retrieval بعداً می‌تواند Module-specific باشد بدون دستکاری Top-level Taxonomy.

---

# 15. Context-dependent Terms

مفاهیمی مانند:

- انتخاب
- قیمت
- سود

در سطح Global به یک Topic واحد Alias نشده‌اند.

قیمت و سود فقط در Context مشخص `children_business` نقش Structural Local Subtopic دارند.

نتیجه برای Chunking:

> وجود term به تنهایی برای تعیین Topic Chunk کافی نیست؛ local structural context و source hierarchy مهم است.

---

# 16. Behavioral Economics

Evidence اصلی برای `behavioral_economics` در Core Primary Corpus برای Promotion به Core Taxonomy v1 کافی نبود.

وضعیت:

`NOT_PROMOTED_TO_CORE_TAXONOMY_V1`

بنابراین Secondary / Guest dispersion نباید در Chunking یا retrieval labeling باعث شود این مفهوم به شکل implicit به یک Core Topic تبدیل شود.

---

# 17. Frozen Competency / Prerequisite v1

Artifact:

`artifacts/phase2/competency/competency_prerequisite_v1.json`

SHA256:

`f12f6c1631d77f29042b2009ca9dc8dee406d23ccdccdbb103c0e8cade781e87`

Status:

`FROZEN`

ساختار:

- Competencies: **24**
- Top-level Topics: **7**
- Learning Stages: **6**
- Recommended Learning Progressions: **17**
- Hard Prerequisites: **0**
- Cross-topic prerequisite: **0**
- Cycles: **0**

اصل:

> Taxonomy Node الزاماً Competency مستقل ایجاد نمی‌کند.

---

# 18. Learning Stages

Stageها:

1. `understand`
2. `self_assess`
3. `analyze`
4. `plan`
5. `act`
6. `review_and_improve`

توزیع فعلی Competency:

- understand: 5
- self_assess: 7
- analyze: 2
- plan: 8
- act: 2
- review_and_improve: 0

خالی بودن `review_and_improve` در v1 Knowledge Gap اعلام نشده است.

---

# 19. Knowledge Gap Policy

در این پروژه:

`Unmapped Document != Knowledge Gap`

و:

`Retrieval Failure != Knowledge Gap`

و:

`Secondary-only Evidence != Proof of Knowledge Gap`

Knowledge Gap واقعی فقط پس از حداقل این مراحل قابل اثبات است:

1. تعریف Target Competency / Learning Objective
2. بررسی Core Primary Evidence
3. بررسی Coverage
4. بررسی Chunkability
5. بررسی Indexability
6. بررسی Retrieval
7. رد Retrieval failure
8. بررسی Answerability
9. بررسی Citation support
10. سپس اعلام Knowledge Gap

---

# 20. چرا Transcript Mapping پایین به معنی Gap نیست

در NB10 Top-level observability در Core Primary Corpus حدود 36.7% بود، اما این عدد به تنهایی Quality Failure نیست.

به‌ویژه در Transcript:

- Segmentها ممکن است کوتاه باشند.
- معنی آن‌ها به turnهای قبل و بعد وابسته باشد.
- pronoun / ellipsis داشته باشند.
- Topic term در همان Segment ظاهر نشود.
- Speaker context در Segment مجاور باشد.

بنابراین Chunking حرفه‌ای می‌تواند بخش مهمی از مسئلۀ Retrievability را حل کند بدون اینکه Taxonomy تغییر کند.

---

# 21. Local Conversation Context Discovery

NB10 نشان داد Local Conversation Context برای Transcript ارزشمند است.

سیاست Audit اولیه:

- فقط همان Conversation Unit
- حداکثر 3 Neighbor قبل
- حداکثر 3 Neighbor بعد
- Program و Speaker name به‌تنهایی Topic vote ایجاد نمی‌کنند
- حداقل 2 Neighbor supporting
- حداقل support ratio برابر 2/3
- خروجی فقط `LOCAL_CONTEXT_CANDIDATE`
- بدون Rechunk
- بدون تغییر Document Topic

این نتیجه برای NB11 مهم است:

> Chunking Transcript باید Context را بازیابی‌پذیر کند، اما نباید Contextual speaker content را به Primary speaker collapse کند.

---

# 22. الزامات Chunking برای Book

NB11 نباید یک chunk size واحد را کورکورانه روی Book اعمال کند.

حداقل باید Benchmark شود:

- Heading-aware segmentation
- Paragraph grouping
- Section boundary
- maximum / target token size
- overlap policy
- short-section handling
- heading inheritance
- parent context
- stable locator preservation
- cross-page continuity
- activity / exercise boundaries
- table/list handling در صورت وجود

Chunk باید بتواند Heading path را حفظ کند.

---

# 23. الزامات Chunking برای Website

Website دو Authority class دارد:

- Direct Author
- Editorial Supervision

Chunk باید metadata لازم برای این تفاوت را نگه دارد.

Benchmark باید بررسی کند:

- heading-aware chunk
- paragraph chunk
- semantic grouping
- boilerplate separation
- citation URL / locator retention
- article title / tag context
- Authority metadata propagation

---

# 24. الزامات Chunking برای Transcript

Transcript احتمالاً حساس‌ترین Source Type پروژه است.

باید Benchmark شود:

- Turn-level chunking
- multi-turn conversational windows
- speaker-aware windows
- question-answer pairing
- answer + minimal preceding question
- topic-shift boundary
- conversation-unit boundary
- episode boundary
- overlap between adjacent conversational chunks
- unresolved speaker handling
- long monologue segmentation
- short utterance aggregation
- attribution contamination rate

قواعد سخت:

1. Episode/Conversation boundary نباید شکسته شود.
2. Speaker باید در metadata حفظ شود.
3. Chunk چندSpeakerه باید explicit participant/speaker composition داشته باشد.
4. Chunk نباید متن Guest را به Dr. Roudi attribution کند.
5. سؤال Context می‌تواند همراه پاسخ باشد، ولی Attribution داخلی باید قابل بازیابی بماند.
6. Context window باید benchmark شود، نه حدس زده شود.
7. Fixed-size-only strategy نباید بدون مقایسه پذیرفته شود.

---

# 25. Chunking نباید Taxonomy را بازنویسی کند

Taxonomy و Competency v1 Frozen هستند.

NB11 می‌تواند:

- Chunk metadata بسازد.
- Chunk → Topic candidate بسازد.
- Parent Document relation بسازد.
- Hierarchy context منتقل کند.
- Retrieval labels آزمایشی بسازد.

اما نباید بدون Version جدید و Evidence جدید:

- Top-level Topic اضافه کند.
- Curriculum Node حذف/اضافه کند.
- Competency تغییر دهد.
- Authority layer تغییر دهد.
- Attribution را بازنویسی کند.

---

# 26. Chunk Lineage Contract پیشنهادی

هر Chunk حداقل باید بتواند به این زنجیره برگردد:

`chunk_id`  
→ `document_id`  
→ `source_id`  
→ `source_type`  
→ `source lineage`  
→ raw/interim source  
→ stable locator

Metadata مهم:

- chunk_id
- parent_document_id
- source_type
- source_id
- language
- authority_layer
- author / speaker
- content_origin
- title
- heading_path در صورت وجود
- conversation / episode ID در Transcript
- chunk ordinal
- character/token offsets در صورت قابل اتکا بودن
- rights
- attribution
- lineage
- taxonomy references فقط به شکل versioned metadata

---

# 27. Chunk ID

Chunk ID باید:

- deterministic باشد؛
- stable parent relation داشته باشد؛
- با تغییر chunking version قابل تشخیص باشد؛
- collision نداشته باشد؛
- از index position موقت وابسته نباشد.

Naming نهایی باید بعد از Discovery conventions Repository تعیین شود و نباید از قبل تحمیل شود.

---

# 28. Chunk Size نباید از قبل فرض شود

قبل از انتخاب Production Strategy باید چند Candidate Strategy ساخته و مقایسه شود.

برای مثال:

- کوچک
- متوسط
- بزرگ
- structural
- semantic
- hybrid structural-semantic
- source-specific

معیار انتخاب نباید «رایج بودن» باشد.

معیار:

> measured retrieval + context quality + attribution integrity + citation precision

---

# 29. معیارهای ارزیابی Chunking

حداقل دسته‌های Metric پیشنهادی:

## Structural

- chunk count
- token distribution
- very-short chunk rate
- overlong chunk rate
- boundary break rate
- empty chunk rate
- duplicate chunk rate
- parent lineage validity

## Authority / Attribution

- speaker contamination rate
- multi-speaker ambiguity rate
- primary/nonprimary mixing profile
- unresolved-speaker handling

## Retrieval

در صورت ساخت Evaluation Set:

- Recall@k
- MRR
- nDCG
- hit rate

## Context quality

- answer evidence completeness
- unnecessary context rate
- question-answer continuity
- topic coherence

## Citation

- citation correctness
- locator validity
- citation coverage

فقط Metricهای واقعاً محاسبه‌شده باید گزارش شوند.

---

# 30. Golden / Evaluation Dataset برای Chunking

برای انتخاب Strategy باید Sampleهای نماینده از هر Source Type وجود داشته باشد.

ضروری است نمونه‌ها شامل موارد سخت باشند:

### Book
- short heading
- long section
- exercise
- multi-topic page
- deep hierarchy
- children_business branch
- giving/gifting

### Website
- direct author
- supervised
- short article
- long article
- multi-topic strong evidence
- boilerplate-heavy case

### Transcript
- solo monologue
- question → answer
- host → doctor → participant
- unresolved speaker
- Chehelston guest
- Uni Tehran multi-speaker
- short utterance
- long utterance
- topic shift
- Taxation discussion
- giving/budget conversation

---

# 31. Final retrieval behavior مطلوب

در Generation نهایی، سیستم باید بتواند:

1. Evidence مستقیم دکتر را ترجیح دهد.
2. Secondary evidence را با هویت Secondary حفظ کند.
3. Context مجری / مهمان را فقط در صورت نیاز وارد کند.
4. Source و Speaker را اشتباه Attribution نکند.
5. Citation را به Parent Source قابل ردیابی نگه دارد.
6. از تکرار مصنوعی ناشی از cross-source reuse جلوگیری کند.
7. در تعارض، Authority را در ranking قابل استفاده نگه دارد.
8. در نبود Evidence کافی abstain کند.
9. Topic / Competency را با Retrieval Quality اشتباه نگیرد.

---

# 32. Open Gates که NB11 نباید فراموش کند

- Rights: 19,456 records هنوز `EVIDENCE_REQUIRED`
- 2,354 unresolved transcript speaker context
- 7 Khane-To review items
- 902 Asre-Shirin segments بدون season metadata
- near-duplicate universal threshold وجود ندارد
- cross-source similarity duplicate proof نیست
- automatic canonicalization انجام نشده
- `review_and_improve` هنوز Competency مستقل ندارد
- Knowledge Gap هنوز formally established نشده است

---

# 33. Source of Truth برای شروع NB11

## Accepted corpus

`data/phase2/processed/documents_dedup_quality_accepted_v1.jsonl`

SHA256:

`9d72c709f81b1218c5aac064052c7ed1da34869f671e6e32762864e0ad70ea40`

## NB09 acceptance

`reports/phase2/deduplication_quality_acceptance_v1.json`

SHA256:

`14dfa748988db17a19c6d9d5e1eac2eb7d23c0a1699dcc7add18a2bf461fe4f3`

## Frozen taxonomy

`artifacts/phase2/taxonomy/taxonomy_v1.json`

SHA256:

`335690044b2e4eff684f7f347809f2c5cb8c39624a939dc01408d9ca898fe977`

## Taxonomy freeze report

`reports/phase2/taxonomy_freeze_v1.json`

SHA256:

`fe182b0c7c6d5ad7d5dfc2aa794fa096e85001b517040a8396d5fb4c0b17e530`

## Frozen competency

`artifacts/phase2/competency/competency_prerequisite_v1.json`

SHA256:

`f12f6c1631d77f29042b2009ca9dc8dee406d23ccdccdbb103c0e8cade781e87`

## Competency freeze report

`reports/phase2/competency_freeze_v1.json`

SHA256:

`19bb27288f49e057859da3bc668f54fac440a89a2636ff5d2e49033665f0dd11`

---

# 34. قواعد انتقال به چت بعدی

چت بعدی نباید NB09 یا NB10 را از صفر بازسازی کند.

Workflow:

`DISCOVER → INSPECT → VALIDATE → DESIGN CHUNKING BENCHMARK → BUILD CANDIDATES → EVALUATE → DECIDE → FREEZE`

نه:

`guess chunk size → chunk everything → embed`

---

# 35. خلاصۀ یک‌خطی

**RAG Finance یک RAG تخصصی با محوریت دانش دکتر کمیل رودی است؛ Core Primary Knowledge ساختار اصلی دانش را تعیین می‌کند، Secondary Knowledge فقط Supporting است، Conversation Context باید بدون Attribution collapse حفظ شود، Taxonomy و Competency v1 اکنون Frozen هستند، و NB11 باید با Benchmark واقعی و Source-specific strategy بهترین Chunking را برای Book، Website و Transcript انتخاب کند.**

</div>
