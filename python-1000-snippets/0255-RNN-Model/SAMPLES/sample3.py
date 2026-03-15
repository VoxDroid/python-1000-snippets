# sample3.py
# Show how the hidden state evolves through a sequence in a simple RNN.

import numpy as np


def rnn_step(x_t, h_prev, Wx, Wh, b):
    return np.tanh(x_t @ Wx + h_prev @ Wh + b)


if __name__ == '__main__':
    np.random.seed(0)

    seq_len = 6
    input_dim = 1
    hidden_dim = 3

    # Two sequences: one increasing, one random.
    seqs = [np.linspace(0, 1, seq_len)[:, None], np.random.randn(seq_len, input_dim)]

    Wx = np.random.randn(input_dim, hidden_dim) * 0.5
    Wh = np.random.randn(hidden_dim, hidden_dim) * 0.5
    b = np.zeros(hidden_dim)

    for idx, x in enumerate(seqs, start=1):
        h = np.zeros(hidden_dim)
        print(f"Sequence {idx} (first 3 steps):", x[:3].flatten())
        for t in range(seq_len):
            h = rnn_step(x[t], h, Wx, Wh, b)
            print(f"  t={t:>2} hidden={h}")
        print("---")
