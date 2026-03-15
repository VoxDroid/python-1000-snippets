# sample2.py
# Simple Transformer-style attention block and classifier using NumPy.

import numpy as np


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


def split_heads(x, num_heads):
    batch, seq_len, d_model = x.shape
    head_dim = d_model // num_heads
    x = x.reshape(batch, seq_len, num_heads, head_dim)
    return x.transpose(0, 2, 1, 3)


def combine_heads(x):
    batch, num_heads, seq_len, head_dim = x.shape
    return x.transpose(0, 2, 1, 3).reshape(batch, seq_len, num_heads * head_dim)


def scaled_dot_product_attention(Q, K, V):
    dk = Q.shape[-1]
    scores = Q @ K.swapaxes(-2, -1) / np.sqrt(dk)
    weights = softmax(scores, axis=-1)
    return weights @ V


def multi_head_attention(x, params):
    # x: (batch, seq_len, d_model)
    batch, seq_len, d_model = x.shape
    num_heads = params["num_heads"]

    Q = x @ params["Wq"]
    K = x @ params["Wk"]
    V = x @ params["Wv"]

    Qh = split_heads(Q, num_heads)
    Kh = split_heads(K, num_heads)
    Vh = split_heads(V, num_heads)

    attended = scaled_dot_product_attention(Qh, Kh, Vh)
    concat = combine_heads(attended)
    return concat @ params["Wo"]


if __name__ == '__main__':
    np.random.seed(0)

    # Toy dataset: sequences of 8 features, binary labels
    N = 200
    seq_len = 10
    d_model = 16
    num_heads = 4

    X = np.random.randn(N, seq_len, d_model)
    y = (X.mean(axis=(1, 2)) > 0).astype(float)

    params = {
        "num_heads": num_heads,
        "Wq": np.random.randn(d_model, d_model) * 0.1,
        "Wk": np.random.randn(d_model, d_model) * 0.1,
        "Wv": np.random.randn(d_model, d_model) * 0.1,
        "Wo": np.random.randn(d_model, d_model) * 0.1,
    }

    # Train a simple output head on top of the transformer block
    Wout = np.random.randn(d_model, 1) * 0.1
    bout = 0.0

    lr = 1e-1
    for epoch in range(1, 21):
        # Forward pass
        hidden = multi_head_attention(X, params)
        pooled = hidden.mean(axis=1)  # Global average pool

        logits = (pooled @ Wout).reshape(-1) + bout
        preds = 1 / (1 + np.exp(-logits))

        loss = -np.mean(y * np.log(preds + 1e-8) + (1 - y) * np.log(1 - preds + 1e-8))
        if epoch % 5 == 0 or epoch == 1:
            acc = (preds.round() == y).mean()
            print(f"Epoch {epoch}, loss={loss:.4f}, accuracy={acc:.3f}")

        # Simple gradient descent on output layer
        dlogits = preds - y
        dWout = (pooled.T @ dlogits.reshape(-1, 1)) / N
        dbout = dlogits.mean()
        Wout -= lr * dWout
        bout -= lr * dbout

    print("Final accuracy:", (preds.round() == y).mean())
