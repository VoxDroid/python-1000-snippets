# sample3.py
# Inspect a multi-head attention output and how heads are combined.

import numpy as np


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


def split_heads(x, num_heads):
    batch, seq_len, d_model = x.shape
    head_dim = d_model // num_heads
    return x.reshape(batch, seq_len, num_heads, head_dim).transpose(0, 2, 1, 3)


def combine_heads(x):
    batch, num_heads, seq_len, head_dim = x.shape
    return x.transpose(0, 2, 1, 3).reshape(batch, seq_len, num_heads * head_dim)


def scaled_dot_product_attention(Q, K, V):
    dk = Q.shape[-1]
    scores = Q @ K.swapaxes(-2, -1) / np.sqrt(dk)
    weights = softmax(scores, axis=-1)
    return weights @ V, weights


if __name__ == '__main__':
    np.random.seed(0)

    batch, seq_len, d_model = 1, 4, 8
    num_heads = 2

    x = np.random.randn(batch, seq_len, d_model)

    # Learnable projections (for demonstration, random)
    Wq = np.random.randn(d_model, d_model) * 0.1
    Wk = np.random.randn(d_model, d_model) * 0.1
    Wv = np.random.randn(d_model, d_model) * 0.1

    Q = x @ Wq
    K = x @ Wk
    V = x @ Wv

    Qh = split_heads(Q, num_heads)
    Kh = split_heads(K, num_heads)
    Vh = split_heads(V, num_heads)

    out, weights = scaled_dot_product_attention(Qh, Kh, Vh)
    out_combined = combine_heads(out)

    print("Q head shape:", Qh.shape)
    print("Attention weights shape:", weights.shape)
    print("Output shape before combining:", out.shape)
    print("Output shape after combining:", out_combined.shape)

    print("Attention weights (head 0):\n", weights[0, 0])
    print("Attention weights (head 1):\n", weights[0, 1])
