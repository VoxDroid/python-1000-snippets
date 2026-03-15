# sample3.py
# Inspect LSTM gate activations and cell state over a sequence.

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    np.random.seed(0)

    seq_len = 6
    input_dim = 1
    hidden_dim = 4

    # A toy input sequence that starts small and grows
    x = np.linspace(0, 1, seq_len)[:, None]

    params = {
        "Wi": np.random.randn(input_dim, hidden_dim) * 0.2,
        "Wf": np.random.randn(input_dim, hidden_dim) * 0.2,
        "Wo": np.random.randn(input_dim, hidden_dim) * 0.2,
        "Wc": np.random.randn(input_dim, hidden_dim) * 0.2,
        "Ui": np.random.randn(hidden_dim, hidden_dim) * 0.2,
        "Uf": np.random.randn(hidden_dim, hidden_dim) * 0.2,
        "Uo": np.random.randn(hidden_dim, hidden_dim) * 0.2,
        "Uc": np.random.randn(hidden_dim, hidden_dim) * 0.2,
        "bi": np.zeros(hidden_dim),
        "bf": np.zeros(hidden_dim),
        "bo": np.zeros(hidden_dim),
        "bc": np.zeros(hidden_dim),
    }

    h = np.zeros(hidden_dim)
    c = np.zeros(hidden_dim)

    print("t | input | forget | input | output | cell (first 3 dims)")
    print("--|-------|--------|-------|--------|-------------------")
    for t in range(seq_len):
        x_t = x[t]
        i = sigmoid(x_t @ params["Wi"] + h @ params["Ui"] + params["bi"])
        f = sigmoid(x_t @ params["Wf"] + h @ params["Uf"] + params["bf"])
        o = sigmoid(x_t @ params["Wo"] + h @ params["Uo"] + params["bo"])
        g = np.tanh(x_t @ params["Wc"] + h @ params["Uc"] + params["bc"])

        c = f * c + i * g
        h = o * np.tanh(c)

        print(f"{t:>2} | {x_t[0]:.2f}  | {f[0]:.3f}   | {i[0]:.3f}  | {o[0]:.3f}   | {c[:3]}")

    print("Final hidden state:", h)
