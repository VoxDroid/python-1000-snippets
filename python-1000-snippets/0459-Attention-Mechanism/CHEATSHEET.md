# 0459-Attention-Mechanism Cheatsheet

- **Scaled dot-product attention** computes weights from queries, keys, and values.
- Attention weights are softmax-normalized to sum to 1 over the key dimension.
- Multi-head attention splits embeddings into multiple heads for parallel attention.

Quick formula:
```
Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V
```
