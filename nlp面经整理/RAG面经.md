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

### Conceptual form:

```text
chunk_document(text, strategy, max_tokens, overlap, metadata)
    -> List[chunk]
