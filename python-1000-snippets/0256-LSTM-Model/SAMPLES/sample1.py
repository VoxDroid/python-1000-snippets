# sample1.py
# Simple LSTM forward pass using NumPy.

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def lstm_step(x_t, h_prev, c_prev, params):
    """Single LSTM step."""
    Wi, Wf, Wo, Wc = params["Wi"], params["Wf"], params["Wo"], params["Wc"]
    Ui, Uf, Uo, Uc = params["Ui"], params["Uf"], params["Uo"], params["Uc"]
    bi, bf, bo, bc = params["bi"], params["bf"], params["bo"], params["bc"]

    i = sigmoid(x_t @ Wi + h_prev @ Ui + bi)
    f = sigmoid(x_t @ Wf + h_prev @ Uf + bf)
    o = sigmoid(x_t @ Wo + h_prev @ Uo + bo)
    g = np.tanh(x_t @ Wc + h_prev @ Uc + bc)

    c = f * c_prev + i * g
    h = o * np.tanh(c)

    return h, c, dict(i=i, f=f, o=o, g=g)


if __name__ == '__main__':
    np.random.seed(0)

    seq_len = 5
    input_dim = 1
    hidden_dim = 4

    # Synthetic sequence: increasing values
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

    print("Input sequence:", x.flatten())
    for t in range(seq_len):
        h, c, gates = lstm_step(x[t], h, c, params)
        print(f"t={t} h={h} c={c}")

    print("Final hidden state:", h)
