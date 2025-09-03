**1.Transformer为何使用多头注意力机制？**

**2.layernorm和batchnorm的区别？为什么Transformer使用layernorm？**

bn:在batch维度上（即对一个 mini-batch 中同一维度的特征做归一化）

ln:在特征维度上（即对单个样本的所有特征做归一化）

why: 

✅ 原因 1：Batch 大小通常较小
NLP 或序列任务中，batch size 可能很小（甚至为 1），BN 在这种情况下统计量不稳定，性能下降。
LN 完全不依赖 batch size，保证一致性。

✅ 原因 2：Transformer 的输入是序列
在 Transformer 中，每个 token 都有一个 embedding 向量，LN 是在 embedding 的维度上做归一化，非常自然。
如果用 BN，会在 batch 内不同句子的 token 之间混合统计量，反而破坏语义。

✅ 原因 3：训练/推理一致性
BN 在训练和推理阶段使用的统计量不同（训练时用 mini-batch 统计，推理时用移动平均），可能带来不一致问题。
LN 在训练和推理时行为完全一样，更稳定。

Transformer 使用 LayerNorm，因为它对 batch size 不敏感，更适合序列建模，不会破坏 token 的独立性，而且训练和推理阶段行为一致。
