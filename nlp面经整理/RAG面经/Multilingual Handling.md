好嘞，Day 3 开课：**多语言 RAG（Multilingual RAG）** 🌍
这一块是他们 JD 里直接点名的重点（“Multilingual Handling”），你要做到：

* 能清楚讲出：**多语言有哪几种处理方案**
* 知道每种方案的 **优缺点 + 在技术文档里的坑**
* 能说出：**你会怎么在这个 thesis 里设计对比实验**

我会边讲概念，边给你“面试可以直接背的英文答案”。

---

## 一、先把场景说清楚（你可以复述给面试官）

他们这次题目的场景大概是：

* 文档是多语言的：**English / Swedish / German**
* 文档类型：technical manuals, parts lists, price lists
* 用户查询：

  * 可能是英文：

    > “Find part X-1234, what is its price and specs?”
  * 也可能是瑞典语 / 德语：

    > “Hitta del X-1234, vad kostar den och vilka specifikationer har den?”
* 有时候还会有**交叉语言**：

  * 用户用英文问，文档只有德文手册；

你在面试里可以先用一句话框住问题：

> So we’re in a **multilingual, domain-specific technical documentation** setting, with manuals and parts lists in English, Swedish, and German, and queries that can be in any of these languages.
> That means the RAG system must support **monolingual and cross-lingual retrieval** reliably.

---

## 二、两条主路线：Multilingual Embeddings vs Translate-then-Index

这是 Day 3 最核心的对比。
你只要把这张“对照表”讲顺，面试就很稳了。

### 2.1 方案 A：Multilingual Embeddings

**思路：**

* 文档保留原语言：English / Swedish / German
* 用一个**多语言 embedding 模型**（比如多语言的 OpenAI/Cohere、LaBSE 之类）
* 把所有语言映射到**同一个向量空间**
* 查询（任何语言）同样用这个模型编码，然后在一个统一的向量库里搜

你可以这么说：

> One natural approach is to use **multilingual embeddings**:
> we keep documents in their original languages and use a multilingual encoder so that all texts live in a shared vector space.
> Then a Swedish query can directly retrieve a German manual if they are semantically related.

**优点：**

* 不需要提前翻译整个文档库 → 省成本
* 避免翻译把**专有名词/术语/数字**搞错
* 天然支持**跨语言检索**（English → German doc）

**缺点 / 风险：**

* 多语言 embedding 在某些语言 / 专业领域可能表达不够好
* 瑞典语 / 德语技术术语、缩写、复合词（特别是德语）可能 embedding 表示不稳定
* 嵌入质量不够好时，**相似度排序会变差**

你可以再加一句他们爱听的：

> For this thesis, multilingual embeddings are a very attractive baseline, because Weaviate already integrates multilingual vectorizers, and it avoids the full translation cost upfront.

---

### 2.2 方案 B：Translate-then-Index（先翻译再建库）

**思路：**

* 把所有非英文文档（瑞典语/德语）离线翻译成英文
* 索引统一的英文版本（也可以保留原文作 metadata）
* 查询可以：

  * 原样丢给一个强多语言 embedding（也行）
  * 或者 **先翻译成英文再 embedding**

你可以这样说：

> The other straightforward option is **translate-then-index**:
> we translate non-English manuals into English offline, index the English versions, and optionally store the original text as metadata.
> Queries in other languages can also be translated to English before embedding.

**优点：**

* 可以用最强的**英文 embedding 模型**（很多模型英语表现最好）
* 下游处理统一在英语上做，比较简单
* 有些评估/规则匹配工作在英文上更成熟

**缺点：**

* 翻译是有噪声和成本的：

  * 术语可能被误翻
  * 单位、数值、缩写可能被搞乱
* 对超大文档库，**一次性翻译成本很高**
* 出现 bug 时很难判断是“翻译问题”还是“retrieval 问题”

你可以加一句：

> In technical documentation, translation errors on part names, tolerances, or safety instructions can be quite problematic.
> So any translate-then-index approach must be evaluated carefully on domain-specific examples.

---

### 2.3 Hybrid：两种一起上（可以当“未来工作/扩展”说）

你可以提一个混合方案（显得你想得远）：

> There is also a hybrid option:
>
> * store both the **original** and the **English-translated** text as separate chunks,
> * index them with appropriate metadata (`language`, `is_translated`)
>   and let the system retrieve from both.
>
> This might combine the robustness of English embeddings with the fidelity of original-language text.

不用细讲，只要表明你脑子里有这个扩展方向。

---

## 三、多语言 RAG 时，Weaviate / 向量库怎么建模？

你可以结合 Day2 的 chunking，讲一个**schema + 流程**。

### 3.1 index 阶段：简化伪代码

```python
def index_chunk(chunk, embed):
    vec = embed(chunk["text"])  # multilingual embedding 或 英文 embedding
    payload = {
        "text": chunk["text"],
        "language": chunk["language"],  # "en", "sv", "de"
        "doc_id": chunk["doc_id"],
        "part_number": chunk.get("part_number"),
        "section_title": chunk.get("section_title"),
        "is_translation": chunk.get("is_translation", False),
    }
    vector_db.insert(vector=vec, payload=payload)
```

你可以在面试这样说：

> In the vector store schema, I would make sure to include a `language` field and possibly an `is_translation` flag, in addition to `doc_id`, `part_number`, `section_title`, etc.
> That way, we can filter or analyse results by language and trace whether we are retrieving original or translated text.

### 3.2 query 阶段：语言检测 + 检索策略

一个合理的查询流程是：

1. 查询进来 → **语言检测**（可以用 langdetect / fastText / LLM 自己判断）
2. 根据选定方案：

   * multilingual embeddings：

     * 直接用原文 embedding → 在全局索引里搜
   * translate-then-index：

     * 把查询翻译成英文 → 用英文 embedding 搜

简单伪代码：

```python
def answer_query(query, embed, vector_db, llm, strategy="multilingual"):
    lang = detect_language(query)  # "en", "sv", "de", ...
    
    if strategy == "translate_then_index" and lang != "en":
        query_for_embedding = translate_to_english(query)
    else:
        query_for_embedding = query

    q_vec = embed(query_for_embedding)
    results = vector_db.search(q_vec, top_k=10)

    # 拼 context + 调 LLM 生成
    context = "\n\n".join([r.payload["text"] for r in results])
    prompt = f"Question ({lang}): {query}\n\nContext:\n{context}\n\nAnswer:"
    return llm(prompt)
```

你不需要完整背代码，只要会口述这个逻辑就行。

---

## 四、技术文档 + 多语言：要特别注意哪些坑？

这是在面试里**很加分**的一块：说明你真的考虑过他们的 domain。

### 4.1 部件编号 / 型号（part numbers）

* `X-1234`, `AB-5678` 这种**语言无关**
* 但 PDF 解析 / OCR / tokenization 可能把它们切断或错误识别
* 要保证：

  * 不在 chunking 时把 part number 分裂
  * 在 schema 里单独存一个 `part_number` 字段（结构化）

你可以说：

> Part numbers are language-independent, so they should ideally be extracted as structured fields and not rely solely on free-text search.
> Chunking and parsing should be careful not to break part numbers across chunks.

### 4.2 单位 / 数值 / 容差

* 比如 `5 mm`, `220 V`, `±0.5%` 这些信息 **极其敏感**
* 翻译时可能被错误变形（尤其是小数点 / 千分位 / 单位缩写）
* 多语言 embedding 通常对数字比较“麻木”，但结构化存储可以缓解：

  * `spec_value`: 5
  * `spec_unit`: "mm"

你可以讲：

> For specs like dimensions or voltage, small errors are unacceptable.
> Where possible, we could extract these as structured fields and use them in metadata filters, instead of relying only on embeddings.

### 4.3 德语/瑞典语复合词 & 术语

* 德语有非常多的**长复合词**（一个词包含很多意思）
* 瑞典语 / 德语里专有名词可能和英文完全不同翻译

你可以说：

> Multilingual embeddings can struggle with long German compound words or specialised technical terms.
> That’s another reason why we might want to **combine** semantic search with structured metadata, especially for parts and specs.

---

## 五、评估：你怎么判断哪种多语言方案更好？

这是 thesis 的重点之一。你可以把回答结构设计好：

> I would evaluate multilingual handling on **two levels**:
>
> 1. **Retrieval** quality
> 2. **End-to-end generation** quality

### 5.1 Retrieval 层面（最关键）

构建一个评估集：

* 多语言 queries（en/sv/de）
* 每个 query 有一个或多个 **标注的 gold chunks**：

  * 包含正确 part 的描述、价格、规格的 chunk

然后比较两个系统：

* System A：multilingual embeddings（原文直接索引）
* System B：translate-then-index（翻译成英文索引）

对每个系统，计算：

* **Recall@k**：在 top-k 里有没有至少一个正确 chunk
* **Precision@k**：top-k 里有多少是相关的
* **MRR** / nDCG：查看排序质量

你可以说：

> For each query, I would label the chunks that truly contain the correct part information, and then compare the multilingual vs translate-then-index setups using retrieval metrics such as Recall@k, Precision@k, and possibly MRR or nDCG.

### 5.2 Generation 层面（辅助验证）

对一部分 queries 跑完整 RAG pipeline，检查：

* **答案是否包含正确的 part number**
* **价格、关键规格是否匹配 ground truth（允许少量容差）**

你可以说：

> On top of retrieval metrics, I would sample a subset of queries and run the full RAG pipeline, checking whether the generated answers:
>
> * mention the correct part number,
> * and match the reference price and key specs.
>
> This confirms that better retrieval actually translates into better end-to-end answers.

---

## 六、面试 Q&A 模板（Day 3 精华）

### Q1：How would you handle multilingual documents in this RAG setup?

> I’d consider two main approaches.
>
> First, **multilingual embeddings**: keep documents in English, Swedish, and German, and use a multilingual encoder so that all texts live in a shared vector space. This naturally supports cross-lingual retrieval, e.g., an English query retrieving a German manual.
>
> Second, **translate-then-index**: translate non-English manuals into English offline, index the English versions, and possibly store the originals as metadata. Queries in other languages can also be translated to English before embedding.
>
> For this thesis, I would start with multilingual embeddings, since Weaviate supports this natively, and then build a translate-then-index baseline. I’d compare them using retrieval metrics on part-specific queries and see which handles our domain-specific terminology more robustly.

### Q2：Would you translate everything to English?

> I wouldn’t assume that translation is always the best default, especially for technical content.
> Translation can introduce noise in part names, units, and tolerances.
>
> So I’d prefer to:
>
> * start with **multilingual embeddings on original texts**,
> * and treat **translation as a controlled experiment** or as an additional index,
>   rather than translating the entire corpus upfront without evaluation.

### Q3：What are the specific challenges of multilingual technical manuals?

> * Part numbers are language-independent but can be broken by poor parsing or chunking.
> * Specs and units must be exact, so translation or embedding errors can be costly.
> * German and Swedish technical terms and compound words may be hard for generic multilingual models.
>
> That’s why I’d combine multilingual embeddings with **structure-aware chunking** and structured metadata like `part_number`, units, and language.

---

## 七、Day 3 小任务（你可以之后发给我改）

1. 用英文写一段（5–8 句）回答：

   > “Compare multilingual embeddings with translate-then-index for multilingual RAG. What are the pros and cons of each, especially for technical documentation?”

2. 想一想：

   * 如果你要在这篇 thesis 里**具体设计一个对比实验**，你会怎么写 3–4 行 “Method” 段落？
   * 比如：

     * Build two indices (multilingual vs translated English)
     * Evaluate on X queries in EN/SV/DE
     * Metrics: Recall@k, etc.

写好之后发给我，我可以帮你润色到“论文 / 面试答题水准”。

---

如果你觉得 Day 3 吸收得差不多了，下一步我们可以 Day 4：
**评估指标 & 实验设计**——这一块非常适合你现在的研究经验，也很好往“term paper / thesis 思维”上靠。
