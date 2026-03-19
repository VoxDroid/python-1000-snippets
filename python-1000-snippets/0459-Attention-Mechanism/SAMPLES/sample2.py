# sample2.py
# Implement a simple multi-head attention operation.

import numpy as np


def split_heads(x, num_heads):
    batch_size, seq_len, depth = x.shape
    assert depth % num_heads == 0
    depth_head = depth // num_heads
    x = x.reshape(batch_size, seq_len, num_heads, depth_head)
    return x.transpose(0, 2, 1, 3)


def scaled_dot_product_attention(q, k, v):
    dk = q.shape[-1]
    scores = q @ k.transpose(0, 1, 3, 2) / np.sqrt(dk)
    weights = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    weights = weights / np.sum(weights, axis=-1, keepdims=True)
    return weights @ v, weights


def main() -> None:
    batch_size = 1
    seq_len = 2
    depth = 8
    num_heads = 2

    rng = np.random.default_rng(0)
    x = rng.standard_normal((batch_size, seq_len, depth))

    q = split_heads(x, num_heads)
    k = split_heads(x, num_heads)
    v = split_heads(x, num_heads)

    out, weights = scaled_dot_product_attention(q, k, v)

    print("Attention weights shape:", weights.shape)
    print("Output shape:", out.shape)


if __name__ == "__main__":
    main()
