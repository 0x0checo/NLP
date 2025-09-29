这个项目是关于“梯度-based 与 示例-based 解释方法在文本分类中的比较”。

首先，背景是：在AI模型越来越复杂的情况下，我们需要可解释性（XAI）来理解模型为什么做出某个预测。这个项目聚焦于文本分类任务，比如情感分析，我会比较两种类型的解释方法：梯度-based 的，比如 Integrated Gradients（IG），和示例-based 的，比如 LIME 和 SHAP。另外，我还会把 Attention 机制作为 baseline 来对比。

实验设计上，我会用 Hugging Face 的工具链来实现。先准备环境：用 Python 虚拟环境安装 Torch、Transformers、Captum 等包。然后数据用 SST-2 数据集（GLUE 的子集），这是短句情感分类，简单易跑。如果时间够，再扩展到 IMDb 长文本。

模型部分：我会微调 BERT-base 模型，用 Trainer API 训练 3 个 epoch，固定随机种子确保可重复。

核心是实现四个解释方法：
- Integrated Gradients：用 Captum 计算梯度积分，聚合 subword 到 word 级别。
- Attention：直接提取 BERT 的注意力权重，但注意它不一定是可靠解释。
- LIME：局部扰动文本拟合线性模型，得到词重要性。
- SHAP：基于 Shapley 值计算贡献。

评价指标主要看 faithfulness，用 deletion test：选 top-k 词删除后，看预测概率下降多少。下降越大，解释越忠实。另外，如果有带人工标注的数据，会测 plausibility 的重合度。还有稳定性测试，比如输入扰动后的解释一致性。

计划步骤：先建环境、训模型，然后实现解释器，对 500 条样本跑测试，生成表格和可视化。最后写报告，代码放 GitHub。

预期输出：模型文件、解释 CSV、评估表格、case study 可视化。引用一些论文如 Sundararajan 的 IG 和 Atanasova 的 faithfulness 测试。

我觉得这个项目可行，时间控制在几周内，能产出实打实的 artifacts。老师，有什么建议吗？谢谢！

### English Version (Oral Report Script)

Hi everyone, hello Professor! Today I'd like to briefly introduce my project plan, which is about "Gradient-based vs. Example-based Explainability in Text Classification."

First, the background: As AI models get more complex, we need explainable AI (XAI) to understand why a model makes a certain prediction. This project focuses on text classification tasks, like sentiment analysis. I'll compare two types of explanation methods: gradient-based ones, such as Integrated Gradients (IG), and example-based ones, like LIME and SHAP. I'll also use Attention mechanisms as a baseline for comparison.

For the experiment setup, I'll use Hugging Face's toolchain. Start with environment prep: Create a Python virtual env and install packages like Torch, Transformers, Captum, etc. Data will be the SST-2 dataset (from GLUE), which is short sentences for sentiment classification—easy and quick to run. If time allows, extend to IMDb for longer texts.

Model part: Fine-tune BERT-base using the Trainer API for 3 epochs, with fixed random seeds for reproducibility.

The core is implementing four explanation methods:
- Integrated Gradients: Use Captum to compute gradient integrals, aggregating subwords to word level.
- Attention: Directly extract BERT's attention weights, but note that it's not always a reliable explanation.
- LIME: Locally perturb the text to fit a linear model and get word importances.
- SHAP: Calculate contributions based on Shapley values.

Evaluation metrics focus on faithfulness, using deletion tests: Select top-k words, delete them, and see how much the prediction probability drops. The bigger the drop, the more faithful the explanation. If available, measure plausibility overlap with human rationales. Also, test stability, like consistency under input perturbations.

Plan steps: Set up env, train model, implement explainers, run tests on 500 samples, generate tables and visualizations. Finally, write a report and put code on GitHub.

Expected outputs: Model files, explanation CSVs, eval tables, case study visualizations. I'll cite papers like Sundararajan's IG and Atanasova's faithfulness tests.

I think this project is feasible, can be done in a few weeks, and produces solid artifacts. Professor, any suggestions? Thanks!
