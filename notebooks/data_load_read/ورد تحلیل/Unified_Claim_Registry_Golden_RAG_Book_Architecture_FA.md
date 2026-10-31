# سند یکپارچه معماری دانش، Golden Dataset، Claim Registry، RAG و تولید کتاب

## مقدمه

این سند سه مسیر را که تا اینجا جداگانه درباره‌شان تصمیم گرفته شده بود، در یک معماری واحد به هم متصل می‌کند:

1. **ساخت و اصلاح Golden Dataset برای ارزیابی RAG**
2. **ساخت Claim Registry و Knowledge Graph به‌عنوان لایهٔ مرکزی دانش**
3. **استفادهٔ مشترک از همان دانش برای RAG، Benchmark و تولید کتاب**

هدف این سند این است که دیگر بین مفاهیم «Corpus»، «Chunk»، «Claim»، «Seed»، «Golden Dataset»، «Knowledge Graph» و «Book Knowledge Base» ابهامی باقی نماند و مسیر پروژه از این نقطه به بعد یکپارچه، ماژولار و قابل استفادهٔ مجدد باشد.

---

# بخش اول — مسئله‌ای که در Golden Dataset قبلی داشتیم

## 1. مشکل اصلی v1 چه بود؟

در نسخهٔ قبلی Golden Dataset تعداد ردیف‌ها زیاد شد، اما تعداد «واحدهای دانشی مستقل» به همان نسبت افزایش پیدا نکرد.

تقریباً از تعداد محدودی Seed، سؤال‌های مختلفی با بیان‌های متفاوت ساخته شد.

در نتیجه:

- Questionها زیاد شدند؛
- اما بسیاری از آن‌ها یک دانش مشترک را می‌سنجیدند؛
- تنوع واقعی Claimها پایین ماند؛
- Dataset نمایندهٔ کل فضای دانشی Corpus نبود؛
- و Benchmark Retrieval نیز کیفیت مطلوبی نداشت.

پس:

```text
573 Rows
≠
573 Independent Knowledge Units
```

مشکل «کم بودن تعداد سؤال» نبود.

مشکل این بود که:

```text
Question Diversity
بیشتر از
Knowledge Diversity
بود.
```

---

# بخش دوم — Claim، Question، Seed و Evidence

## 2. Claim چیست؟

**Claim یک گزارهٔ دانشی مستقل است که بتوان آن را مستقیم با Evidence موجود در Source اثبات کرد.**

مثال:

```text
Evidence:
«یکی از روش‌های مدیریت ریسک، انتقال ریسک از طریق بیمه است.»

Claim:
بیمه می‌تواند ابزار انتقال ریسک باشد.
```

Claim هنوز سؤال نیست.

Claim خودِ دانش است.

---

## 3. Question چیست؟

Question روشی برای آزمودن Claim است.

مثلاً:

```text
Claim:
بیمه می‌تواند ابزار انتقال ریسک باشد.

Question:
بیمه در مدیریت ریسک چه نقشی دارد؟

Answer:
انتقال ریسک

Evidence:
«یکی از روش‌های مدیریت ریسک، انتقال ریسک از طریق بیمه است.»
```

پس:

```text
Claim = واحد دانش
Question = شیوهٔ آزمودن آن دانش
Answer = پاسخ مورد انتظار
Evidence = شاهد مستقیم از Source
```

---

## 4. Seed چیست؟

در معماری جدید، Seed باید بر پایهٔ یک Claim مستقل و معتبر ساخته شود.

```text
Independent Claim
+ Direct Evidence
+ Source
+ Locator
+ Attribution
=
Candidate Seed
```

نمونه:

```text
Seed 001

Claim:
بیمه یکی از روش‌های انتقال ریسک است.

Evidence:
«یکی از روش‌های مدیریت ریسک، انتقال ریسک از طریق بیمه است.»

Source:
کتاب X

Locator:
فصل مدیریت ریسک، پاراگراف 42
```

بعداً از یک Seed می‌توان یک یا چند Evaluation Case ساخت.

---

## 5. چرا چند سؤال می‌توانند فقط یک Seed باشند؟

مثلاً:

- بیمه چه کمکی به مدیریت ریسک می‌کند؟
- نقش بیمه در مواجهه با ریسک چیست؟
- با بیمه چه اتفاقی برای ریسک می‌افتد؟

ممکن است هر سه فقط این Claim را بسنجند:

> بیمه می‌تواند ریسک را منتقل کند.

پس:

```text
3 Questions
≠
3 Independent Seeds
```

ممکن است فقط یک Seed دانشی وجود داشته باشد.

---

# بخش سوم — Claim Deduplication

## 6. چرا Claimها باید Dedup شوند؟

اگر از کل Corpus Claim استخراج کنیم، یک دانش ممکن است در چند کتاب، چند مقاله و چند Transcript تکرار شده باشد.

بنابراین بعد از Claim Extraction باید مشخص کنیم کدام Claimها واقعاً مستقل‌اند.

### Exact Duplicate

دو Claim دقیقاً یک چیز را می‌گویند.

```text
Claim A:
بیمه ابزار انتقال ریسک است.

Claim B:
بیمه ابزار انتقال ریسک است.
```

### Semantic Duplicate

جمله متفاوت است ولی معنی یکی است.

```text
Claim A:
بیمه ابزار انتقال ریسک است.

Claim B:
با بیمه می‌توان ریسک مالی را به شرکت بیمه منتقل کرد.
```

### Subsumed

یک Claim داخل Claim بزرگ‌تر قرار گرفته است.

```text
Claim A:
بیمه ابزار انتقال ریسک است.

Claim B:
روش‌های مدیریت ریسک شامل پذیرش، اجتناب، کاهش و انتقال هستند و بیمه نمونه‌ای از انتقال ریسک است.
```

### Partial Overlap

دو Claim بخشی مشترک دارند ولی یکی نیستند.

```text
Claim A:
بیمه باعث انتقال ریسک می‌شود.

Claim B:
بیمه می‌تواند اثر مالی زیان را کاهش دهد.
```

این‌ها مرتبط‌اند اما ممکن است هر دو مستقل و ارزشمند باشند.

---

# بخش چهارم — چرا Core-46 بهتر بود؟

## 7. مسیر درست Core-46

Core-46 کیفیت بهتری داشت چون مسیر ساخت آن Evidence-first بود:

```text
Real Source
↓
Exact Evidence
↓
Independent Claim
↓
Question
↓
Answer
```

در نتیجه:

- Grounding بهتر شد؛
- سؤال‌ها کمتر مصنوعی بودند؛
- پاسخ‌ها به Evidence واقعی متصل بودند؛
- و Caseها کیفیت حرفه‌ای‌تری داشتند.

محدودیت Core-46 این نبود که بد بود.

محدودیتش این بود که هنوز از فضای محدود Pilotهای قبلی شروع شده بود و نمایندهٔ کل Corpus نبود.

---

# بخش پنجم — معنی 19,456 Record

## 8. Corpus فعلی چیست؟

Corpus پذیرفته‌شده شامل:

- 529 Website Record
- 2,701 Book Record
- 16,226 Transcript Segment

مجموع:

```text
19,456 Processing Records
```

اما:

```text
19,456 Records
≠
19,456 Claims
≠
19,456 Seeds
```

ممکن است ده‌ها Record در نهایت فقط چند Claim مستقل داشته باشند.

---

# بخش ششم — RAG روی چه چیزی کار می‌کند؟

## 9. RAG اصلی روی Seed یا Golden Dataset اجرا نمی‌شود

معماری اصلی RAG:

```text
Original Sources
↓
Documents / Chunks
↓
Embeddings / Index
↓
Retriever
↓
Context
↓
LLM Answer
```

یعنی RAG مستقیماً از Corpus و Index استفاده می‌کند.

Golden Dataset منبع پاسخ‌گویی RAG نیست.

---

# بخش هفتم — Golden Dataset چه نقشی دارد؟

## 10. Golden Dataset برگهٔ امتحان RAG است

مسیر ارزیابی:

```text
Golden Question
↓
Run RAG
↓
Retrieved Evidence
↓
Generated Answer
↓
Compare with Expected Evidence / Answer
↓
Metrics
```

می‌توان سنجید:

- آیا Evidence درست Retrieval شد؟
- Rank مناسب بود؟
- Evidence کامل بود؟
- Attribution درست بود؟
- Answer صحیح بود؟
- Citation درست بود؟
- Context اضافی یا گمراه‌کننده بود؟

پس:

```text
Corpus = منبع دانشی RAG
Golden Dataset = امتحان RAG
Metrics = نمرهٔ RAG
```

اگر Golden Dataset بد باشد، Benchmark نیز قابل اعتماد نیست.

---

# بخش هشتم — آیا Golden Dataset باید تمام Claimها را داشته باشد؟

## 11. خیر

Golden Dataset یک **Representative Evaluation Set** است.

لازم نیست تمام Claimهای Corpus را شامل شود.

چیزی که مهم است:

- Coverage مناسب Topicها
- Coverage Source Typeها
- Coverage Difficulty
- Coverage Question Typeها
- Coverage Citation و Attribution
- Coverage Failure Modeها
- Evidence-grounding
- جلوگیری از Semantic Duplicate
- تعداد کافی Claim مستقل

پس برای Benchmark:

```text
Whole Corpus
↓
Coverage-aware Claim Discovery
↓
Representative Independent Claims
↓
Golden Seeds
↓
Questions / Answers / Evidence
↓
Golden Dataset v2
```

---

# بخش نهم — آیا برای خود RAG باید تمام Claimها استخراج شوند؟

## 12. خیر

برای کارکرد RAG، Claim Inventory کامل الزام نیست.

RAG می‌تواند مستقیماً از Chunkها و Index استفاده کند.

پس:

```text
RAG does not require a complete Claim Registry.
```

اما Claim Registry می‌تواند RAG را خیلی قوی‌تر، قابل تحلیل‌تر و قابل توسعه‌تر کند.

---

# بخش دهم — اگر بخواهیم از کل دانش برای کتاب استفاده کنیم چه؟

## 13. دو راه وجود دارد

### راه اول — فقط RAG + Chunks

```text
Book Topic
↓
Retrieve relevant chunks
↓
LLM synthesis
↓
Draft chapter
```

این روش ممکن است و برای Draft سریع مفید است.

اما محدودیت دارد:

- ممکن است Claim مهمی جا بماند؛
- ممکن است یک دانش چند بار تکرار شود؛
- Coverage فصل‌ها قابل اندازه‌گیری نیست؛
- کشف تناقض سخت است؛
- رابطهٔ بین مفاهیم روشن نیست.

### راه دوم — Claim Registry + Sources

```text
Claims
↓
Relations
↓
Topics
↓
Evidence Links
↓
Book Outline
↓
Chapter Knowledge Pack
↓
Draft
↓
Source Verification
```

برای یک کتاب جامع، کنترل‌شده و قابل ممیزی، این روش بسیار قوی‌تر است.

---

# بخش یازدهم — Claim Registry چیست؟

## 14. Claim Registry لایهٔ ساختاریافتهٔ دانش است

برای هر Claim می‌توان نگه داشت:

- claim_id
- claim_text
- atomicity
- topic
- subtopic
- source_ids
- evidence_spans
- locators
- authority
- attribution
- confidence
- duplicate relations
- supporting evidence
- conflicting evidence
- broader / narrower relations
- prerequisite relations
- conceptual relations
- author review status

این Registry پاسخ می‌دهد:

> چه می‌دانیم؟

> این دانش از کجا آمده؟

> چند Evidence دارد؟

> با چه Claimهای دیگری مرتبط است؟

> آیا Claim مخالف یا مکملی وجود دارد؟

---

# بخش دوازدهم — Knowledge Graph چه اضافه می‌کند؟

## 15. از Claim Registry به Knowledge Graph

وقتی Claimها استخراج و Dedup شدند، روابط میان آن‌ها ساخته می‌شود.

مثال:

```text
Claim A
"تورم قدرت خرید پول را کاهش می‌دهد"

RELATED_TO
↓
Claim B
"بازده اسمی با بازده واقعی متفاوت است"

REQUIRES_CONCEPT
↓
Claim C
"ارزش واقعی پول باید اثر تورم را لحاظ کند"
```

Knowledge Graph برای:

- طراحی ساختار کتاب
- کشف شکاف دانش
- کشف تناقض
- GraphRAG
- طراحی سؤال
- مسیرهای آموزشی
- اصلاح Retrieval
- تحلیل وابستگی مفهومی

مفید است.

---

# بخش سیزدهم — آیا Claim Registry می‌تواند RAG را بهتر کند؟

## 16. بله؛ حتی بدون اینکه مستقیماً وارد Runtime شود

Claim Registry می‌تواند ابزار تشخیص خطای RAG باشد.

```text
Claim معتبر داریم
↓
Evidence در Corpus وجود دارد
↓
RAG سؤال مربوط را جواب نمی‌دهد
```

بعد:

```text
Evidence داخل Chunk مناسب است؟
├── No → Chunking problem
└── Yes
     ↓
Retriever آن را پیدا می‌کند؟
├── No → Embedding / Query / Index problem
└── Yes
     ↓
Rank خوب است؟
├── No → Ranking problem
└── Yes
     ↓
LLM درست استفاده می‌کند؟
├── No → Context / Generation problem
└── Yes
     ↓
Citation درست است؟
├── No → Citation / Lineage problem
└── Yes → PASS
```

یعنی Claimها می‌توانند مسیر اصلاح RAG را هدایت کنند.

---

# بخش چهاردهم — Claimها چگونه Chunking را اصلاح می‌کنند؟

## 17. Claim-based Chunk Evaluation

فرض کنید:

```text
Claim:
X

Required Evidence:
Paragraph 125 + Paragraph 126
```

Variant A:

```text
Chunk 1 = Paragraph 125
Chunk 2 = Paragraph 126
```

Variant B:

```text
Chunk 1 = Paragraph 125 + 126
```

اگر Variant B در:

- Recall
- Evidence Completeness
- Citation Correctness
- Answer Quality

بهتر باشد، دلیل واقعی برای اصلاح Chunk Strategy داریم.

پس Claim Registry می‌تواند بهینه‌سازی Chunking را Evidence-driven کند.

---

# بخش پانزدهم — آیا Claim Registry می‌تواند وارد خود RAG شود؟

## 18. بله، در معماری پیشرفته‌تر

مثلاً:

```text
User Query
↓
Claim Retrieval
+
Chunk Retrieval
↓
Evidence Expansion
↓
LLM
```

یا:

```text
Query
↓
Knowledge Graph
↓
Relevant Claims
↓
Source Evidence
↓
Answer
```

این مسیر به Hybrid RAG یا GraphRAG نزدیک می‌شود.

اما برای فاز فعلی بهتر است ابتدا RAG پایه با Golden v2 درست ارزیابی شود.

---

# بخش شانزدهم — آیا تمام Claimهای Corpus باید استخراج شوند؟

## 19. بستگی به هدف دارد

### برای Golden Dataset

نه.

فقط Claimهای نماینده و باکیفیت لازم‌اند.

### برای Knowledge Registry کامل

بله، تا حد ممکن.

هدف می‌شود:

```text
Whole Corpus
↓
Extract meaningful claims
↓
Deduplicate
↓
Resolve relations
↓
Complete Claim Registry
```

### برای کتاب جامع

استخراج گستردهٔ Claimها بسیار ارزشمند است، چون:

- Coverage بهتر می‌شود؛
- ساختار فصل‌ها قابل طراحی می‌شود؛
- تکرار کاهش می‌یابد؛
- Evidence قابل ردیابی است؛
- تناقض‌ها قابل کشف‌اند.

---

# بخش هفدهم — یک تیر و سه نشان

## 20. معماری مرکزی پیشنهادی

بهترین تصمیم این است که Claim Registry یک Asset مرکزی باشد.

```text
SOURCE CORPUS
      ↓
CLAIM REGISTRY
      ↓
┌──────────────┬──────────────┬──────────────┐
↓              ↓              ↓
Golden v2      Book           GraphRAG
↓              ↓              ↓
Benchmark      Writing        Advanced RAG
```

یعنی Claim Extraction فقط یک بار انجام می‌شود.

بعد چند مصرف‌کننده دارد.

---

# بخش هجدهم — آیا کل Claim Extraction را می‌شود در یک Notebook انجام داد؟

## 21. بله، ولی Notebook باید Orchestrator باشد

برای 19,456 Record یک Notebook می‌تواند Pipeline را هدایت کند، ولی نباید همهٔ منطق در یک Cell یا اجرای یک‌باره باشد.

Pipeline باید:

- Batch-based باشد؛
- Resume-safe باشد؛
- Cache داشته باشد؛
- Versioned artifact تولید کند؛
- No-overwrite باشد؛
- مرحله‌ای Validate شود؛
- Failure Recovery داشته باشد.

ساختار مناسب:

```text
1. Input Freeze
2. Extraction Unit Build
3. Batch Claim Extraction
4. Machine Validation
5. Claim Normalization
6. Exact Dedup
7. Semantic Dedup
8. Subsumption / Partial-overlap
9. Evidence Aggregation
10. Claim Registry Freeze
11. Relation Graph Build
12. Coverage / Saturation Report
13. Export for RAG
14. Export for Book
```

---

# بخش نوزدهم — آیا همین NB12h را ادامه دهیم؟

## 22. پیشنهاد نهایی: خیر

NB12h الان هویت مشخص دارد:

```text
NB12h
Golden Dataset rebuild / orchestration
```

اگر Full Claim Registry، Graph، کتاب و Benchmark را هم داخل آن ببریم، Scope مخلوط می‌شود.

پس بهتر است Notebook جدید داشته باشیم:

```text
12i_claim_registry_and_knowledge_graph.ipynb
```

---

# بخش بیستم — مسئولیت Notebook جدید

## 23. وظیفهٔ 12i

```text
Whole Accepted Corpus
↓
Exhaustive / Progressive Claim Extraction
↓
Claim Validation
↓
Claim Dedup
↓
Evidence Aggregation
↓
Claim Registry
↓
Knowledge Relations
↓
Knowledge Graph Export
```

---

# بخش بیست‌ویکم — خروجی‌های اصلی 12i

## 24. Artifactهای پیشنهادی

```text
claims_raw_v1.jsonl
claims_validated_v1.jsonl
claims_deduplicated_v1.jsonl
claim_evidence_links_v1.jsonl
claim_relations_v1.jsonl
knowledge_graph_v1.json
claim_registry_report_v1.json
```

این Artifactها باید Versioned، Immutable و قابل مصرف توسط چند پروژه باشند.

---

# بخش بیست‌ودوم — رابطهٔ 12i با NB12h و NB13

## 25. مسیر RAG

```text
12i Full Claim Registry
↓
Coverage-aware Claim Selection
↓
NB12h Golden Dataset v2
↓
NB13 Benchmark
```

یعنی NB12h دیگر مجبور نیست Claim را از صفر کشف کند.

Golden Dataset از Claim Registry واقعی تغذیه می‌شود.

---

# بخش بیست‌وسوم — رابطهٔ 12i با Book_Production

## 26. مسیر کتاب

```text
claims_deduplicated_v1
+
claim_relations_v1
+
knowledge_graph_v1
↓
Book Outline
↓
Chapter Knowledge Packs
↓
Drafting
↓
Evidence Verification
```

به این ترتیب پروژهٔ کتاب لازم نیست Claim Extraction را دوباره انجام دهد.

---

# بخش بیست‌وچهارم — آیا Notebook را داخل Repo کتاب Copy کنیم؟

## 27. خیر

اگر دو کپی داشته باشیم:

```text
RAG repo / claim notebook
Book repo / claim notebook
```

به‌مرور:

- Schemaها متفاوت می‌شوند؛
- Claim IDها ناسازگار می‌شوند؛
- Dedupها متفاوت می‌شوند؛
- Sync دشوار می‌شود؛
- Provenance ممکن است واگرا شود.

بهتر:

```text
One Claim Registry Builder
+
Versioned Frozen Artifacts
```

Book repo فقط Consumer باشد.

---

# بخش بیست‌وپنجم — معماری ماژولار کد

## 28. Notebook فقط Orchestrator

بهتر است منطق اصلی به‌مرور به ماژول‌های مشترک منتقل شود:

```text
src/knowledge_registry/
    extraction.py
    validation.py
    dedup.py
    evidence.py
    relations.py
    graph.py
    export.py
```

بعد:

```text
RAG Notebook
↓
uses shared knowledge_registry code

Book Notebook
↓
uses same claim artifacts / shared logic
```

اگر Shared Package بین دو Repo فعلاً سخت باشد، حداقل Schema و Artifact Contract باید مشترک و ثابت بماند.

---

# بخش بیست‌وششم — چرا الان انجام‌دادن این کار ارزش دارد؟

## 29. مزایا

اگر Claim Registry را الان درست بسازیم:

- دوباره‌کاری حذف می‌شود؛
- Golden Dataset بهتر می‌شود؛
- Book Production از همان دانش استفاده می‌کند؛
- Coverage دانش قابل سنجش می‌شود؛
- تناقض‌ها قابل کشف می‌شوند؛
- RAG قابل عیب‌یابی‌تر می‌شود؛
- Chunking با Evidence واقعی قابل اصلاح می‌شود؛
- GraphRAG در آینده ساده‌تر می‌شود؛
- Knowledge Base پروژه قوی‌تر می‌شود.

اگر بعداً برای کتاب دوباره Claim Extraction انجام دهیم:

- Schema ممکن است متفاوت شود؛
- Dedup دوباره انجام می‌شود؛
- Claim IDها ممکن است ناسازگار شوند؛
- Provenance ممکن است متفاوت شود؛
- Sync بین RAG و Book دشوار می‌شود.

---

# بخش بیست‌وهفتم — Saturation در Golden Dataset

## 30. چه زمانی Claim کافی برای Golden داریم؟

برای Golden Dataset لازم نیست همهٔ Claimهای Registry وارد Dataset شوند.

وقتی:

1. Topicهای اصلی پوشش داده شده باشند؛
2. Website، Book و Transcript نمایندگی مناسب داشته باشند؛
3. Claimهای Primary و Secondary مطابق Authority Policy پوشش داشته باشند؛
4. Question Typeهای مختلف وجود داشته باشند؛
5. Difficulty مختلف وجود داشته باشد؛
6. Failure Modeهای Retrieval و Citation پوشش داده شده باشند؛
7. Batchهای جدید Claim مستقل کمی اضافه کنند؛

می‌توان گفت Golden Dataset به **Saturation مناسب** نزدیک شده است.

پس:

```text
Full Claim Registry
≠
Golden Dataset
```

بلکه:

```text
Full Claim Registry
↓
Representative Selection
↓
Golden Dataset
```

---

# بخش بیست‌وهشتم — معماری نهایی پروژه

## 31. تصویر کلان

```text
                           SOURCE CORPUS
                                │
                                ↓
                    12i CLAIM REGISTRY BUILDER
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
            ↓                   ↓                   ↓
      CLAIM REGISTRY       KNOWLEDGE GRAPH      EVIDENCE LINKS
            │                   │                   │
            ├──────────────┬────┴─────┬────────────┤
            │              │          │            │
            ↓              ↓          ↓            ↓
        GOLDEN v2       BOOK KB     GraphRAG     Diagnostics
            │              │          │            │
            ↓              ↓          ↓            ↓
          NB13         Book Writing  Advanced     Chunk /
        Benchmark                    Retrieval    Retrieval Fix
```

---

# بخش بیست‌ونهم — تصمیم نهایی پیشنهادی

## 32. مسیر اجرایی از اینجا

### NB12h

در نقش فعلی خود باقی بماند:

```text
Golden Dataset rebuild / orchestration
```

### Notebook جدید

ساخته شود:

```text
12i_claim_registry_and_knowledge_graph.ipynb
```

### 12i

Asset مرکزی دانش را بسازد:

```text
Whole Corpus
↓
Claims
↓
Validation
↓
Dedup
↓
Evidence Aggregation
↓
Relations
↓
Knowledge Graph
```

### RAG

از Claim Registry برای:

- Golden v2
- Diagnostics
- Chunk evaluation
- Retrieval optimization
- GraphRAG future

استفاده کند.

### Book_Production

از همان Registry برای:

- Book outline
- Chapter knowledge packs
- Drafting
- Source verification
- Coverage control

استفاده کند.

---

# بخش سی‌ام — خلاصهٔ بسیار کوتاه

```text
RAG
روی Corpus / Chunks اجرا می‌شود.

Golden Dataset
برای امتیازدهی RAG است.

Claim
واحد دانش مستقل و قابل اثبات است.

Seed
Claim پذیرفته‌شده + Evidence + Provenance است.

Claim Registry
لایهٔ مرکزی و ساختاریافتهٔ دانش است.

Knowledge Graph
رابطهٔ بین Claimها را مدل می‌کند.

Golden Dataset
از Claim Registry یک زیرمجموعهٔ نماینده انتخاب می‌کند.

Book
از Claim Registry و Knowledge Graph برای ساختار و نگارش استفاده می‌کند.

RAG آینده
می‌تواند از Claim Registry و Graph برای Retrieval پیشرفته‌تر استفاده کند.
```

---

# نتیجهٔ نهایی

تصمیم معماری پیشنهادی این است:

> **Claim Registry باید یک Asset مرکزی پروژه باشد، نه Artifact مخصوص Golden Dataset و نه Artifact مخصوص Book.**

و معماری اصلی از اینجا:

```text
SOURCE CORPUS
      ↓
12i CLAIM REGISTRY
      ↓
┌──────────────┬──────────────┬──────────────┐
↓              ↓              ↓
Golden v2      Book           GraphRAG
↓              ↓              ↓
Benchmark      Writing        Advanced RAG
```

این معماری با هدف ماژولار بودن پروژه سازگار است، دوباره‌کاری را کم می‌کند، دانش‌بنیاد RAG را قوی‌تر می‌کند و اجازه می‌دهد یک بار Claim Extraction انجام شود و چند پروژه از همان Asset معتبر استفاده کنند.
