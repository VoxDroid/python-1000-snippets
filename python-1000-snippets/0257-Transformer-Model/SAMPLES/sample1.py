# sample1.py
# Simple scaled dot-product attention using NumPy.

import numpy as np


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


def scaled_dot_product_attention(Q, K, V, mask=None):
    """Compute scaled dot-product attention."""
    dk = Q.shape[-1]
    scores = Q @ K.swapaxes(-2, -1) / np.sqrt(dk)
    if mask is not None:
        scores = scores + (mask * -1e9)
    weights = softmax(scores, axis=-1)
    return weights @ V, weights


if __name__ == '__main__':
    np.random.seed(0)

    batch, seq_len, d_model = 2, 5, 8
    x = np.random.randn(batch, seq_len, d_model)

    # Use the same input for Q, K, V for self-attention
    Q = x
    K = x
    V = x

    out, attn = scaled_dot_product_attention(Q, K, V)
    print("Output shape:", out.shape)
    print("Attention weights shape:", attn.shape)
    print("Attention weights (first sample, first head):\n", attn[0])
