1、**What is RAG?**

RAG is an architecture that combines retrieval with generation.
Instead of letting the LLM rely only on its internal parameters, the system retrieves the most relevant chunks from an external document store and injects them into the prompt so the answer becomes grounded and factual.
The goal is to reduce hallucinations and make the model respond based on real data.

RAG 的工作流程正如其名，分为三个步骤：

检索 (Retrieval)： 当你提出一个问题（比如：“公司最新的报销政策是什么？”），系统不会直接把问题丢给大模型，而是先去你的外部知识库（比如公司的文档数据库）中进行搜索，找到与“报销政策”最相关的几个段落。

增强 (Augmentation)： 系统将你原来的问题，加上刚刚检索到的那些“相关段落”，一起打包成一个新的、更丰富的提示词（Prompt）。

Prompt 示例： “用户问：公司报销政策是什么？请根据以下参考资料回答：[检索到的政策文档片段]...”

生成 (Generation)： 大模型接收到这个增强后的提示词，阅读参考资料，然后生成最终的答案。

2.**Chunking**
# Chunking Function: Principles and Strategies

## 1. What is Chunking?

Chunking is the process of splitting long documents into smaller, 
retrievable units ("chunks") that can be embedded, stored in a vector 
database, and provided to an LLM in a RAG pipeline.

A chunk is typically a short segment (e.g., 200–400 tokens) containing 
coherent information. Good chunking improves retrieval recall and 
grounds the LLM’s output more reliably.

---

## 2. What Does a Chunking Function Do?

A chunking function takes raw text and produces a list of structured chunks:

**Input**
- raw text  
- chunking strategy  
- parameters: `max_tokens`, `overlap`  
- optional metadata (page, section, part_id, language)

**Output**
- list of chunks, each containing:
  - text  
  - metadata  



# RAG Chunking Strategies

This document outlines the core chunking techniques used in Retrieval-Augmented Generation (RAG) systems. Choosing the right strategy is a critical trade-off that directly impacts **Retrieval Recall** and **Generation Precision**.

## 1. Fixed-size Chunking
This is the baseline approach, often used as a starting point.

* **Principle:** Split text into chunks of a fixed size $N$ (characters or tokens), disregarding content structure.
* **Mechanism:** Usually paired with **Overlap**.
    * *Example:* Chunk Size = 500, Overlap = 50.
    * Chunk 1: `[0:500]`, Chunk 2: `[450:950]`.
* **Pros & Cons:**
    * ✅ **Pros:** Computationally cheap; easy to implement; requires no NLP models.
    * ❌ **Cons:** **Semantic Discontinuity**. It blindly cuts through sentences, names, or logical groupings, potentially losing context (though overlap mitigates this slightly).

## 2. Sliding Window Chunking
A technique often combined with fixed-size chunking to enhance context window retrieval.

* **Principle:** Instead of simple overlap, this approach uses a sliding window to capture granular context or retrieval-time expansion.
* **Granularity:**
    * *Chunk 1:* Sentence A + Sentence B + Sentence C
    * *Chunk 2:* Sentence B + Sentence C + Sentence D
* **Core Value:** **Eliminates Boundary Effects**. It ensures that no critical information is lost simply because it fell on a "cut" line, as every data point will eventually appear in the center of a window.

## 3. Structure-aware Chunking (Recursive)
Also known as **Recursive Character Chunking**, this is currently the **industry standard** for processing structured documents (PDF, Markdown, HTML).

* **Principle:** Respects the document's native structure (Headers, Paragraphs, Lists, Code Blocks) rather than splitting by arbitrary character counts.
* **Workflow:**
    1.  **Parse:** Identify separators (e.g., Markdown `#`, `##` or HTML `<div>`).
    2.  **Recursive Split:** Attempt to split by the largest logical unit (e.g., Chapter). If the chunk is still too large for the token limit, recurse down to the next level (e.g., Paragraph).
    3.  **Integrity:** Ensures tables and code blocks remain intact.
* **Core Value:** **High Semantic Cohesion**. Content within a chunk is logically related, and metadata (headers) can be preserved for better retrieval.

## 4. Semantic Chunking
An advanced, **SOTA (State of the Art)** technique that prioritizes meaning over formatting.

* **Principle:** Splits text based on shifts in semantic meaning rather than physical delimiters.
* **Algorithm:**
    1.  **Sentence Embeddings:** Generate vector embeddings for individual sentences.
    2.  **Similarity Check:** Calculate Cosine Similarity between adjacent sentences.
    3.  **Threshold Split:** If similarity is high, merge sentences. If similarity drops below a threshold (indicating a topic change), create a split.
* **Core Value:** **High Signal-to-Noise Ratio**. Each chunk represents a distinct, complete semantic thought, which is crucial for answering complex questions.

## 5. Multilingual Chunking
Essential for globalized applications to handle language density differences.

* **The Problem:** "Length" is defined differently across languages.
    * *Tokenizer differences:* English relies on spaces; CJK (Chinese/Japanese/Korean) languages are dense and lack spacing.
    * *The Trap:* A 500-character limit is a paragraph in English but could be a short essay in Chinese. Using character counts leads to massive chunks in CJK, diluting retrieval accuracy.
* **Solution:**
    * Use **Language-specific splitters** (e.g., NLTK, SpaCy).
    * **Token-based Counting:** Standardize length using the LLM's tokenizer (e.g., `tiktoken`) rather than raw character counts to ensure consistent information density.

---

## ⚡️ Summary & Comparison

| Strategy | Core Logic | Best Use Case | Cost |
| :--- | :--- | :--- | :--- |
| **Fixed-size** | Hard split by length | Plain text, MVP / Baseline testing | 🟢 Low |
| **Sliding Window** | High overlap | High recall requirements; preventing boundary loss | 🟡 Medium |
| **Structure-aware** | **Document Syntax** | **Standard RAG** (Markdown/PDF/Code) | 🟡 Medium |
| **Semantic** | **Meaning/Topic** | Advanced RAG; High precision needs | 🔴 High (GPU) |
| **Multilingual** | Token/Language specific | Multi-language support (CJK mixed with En) | 🟡 Medium |

### 💡 Recommendation
* **Start with:** **Structure-aware (Recursive)** chunking. It offers the best balance of performance and cost.
* **Upgrade to:** **Semantic Chunking** only if you have unstructured text with shifting topics and require maximum accuracy.
