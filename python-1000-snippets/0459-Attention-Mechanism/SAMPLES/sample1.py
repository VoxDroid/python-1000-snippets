# sample1.py
# Compute scaled dot-product attention for a simple query/key/value.

import numpy as np


def scaled_dot_product_attention(q, k, v):
    dk = q.shape[-1]
    scores = q @ k.T / np.sqrt(dk)
    weights = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    weights = weights / np.sum(weights, axis=-1, keepdims=True)
    return weights @ v, weights


def main() -> None:
    q = np.array([[1.0, 0.0, 0.0]])
    k = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    v = np.array([[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]])

    out, attn = scaled_dot_product_attention(q, k, v)
    print("Attention weights:")
    print(attn)
    print("Output:")
    print(out)


if __name__ == "__main__":
    main()
