# sample1.py
# Simple RNN forward pass (no training)

import numpy as np


def rnn_forward(x, h_prev, Wx, Wh, b):
    """Compute the hidden state for an input sequence.

    Args:
        x: (seq_len, input_dim) input sequence
        h_prev: (hidden_dim,) initial hidden state
        Wx: (input_dim, hidden_dim) input-to-hidden weights
        Wh: (hidden_dim, hidden_dim) hidden-to-hidden weights
        b: (hidden_dim,) bias

    Returns:
        h: (hidden_dim,) final hidden state after processing the sequence
    """

    h = h_prev
    for t in range(x.shape[0]):
        h = np.tanh(x[t] @ Wx + h @ Wh + b)
    return h


if __name__ == '__main__':
    np.random.seed(0)

    seq_len = 10
    input_dim = 1
    hidden_dim = 8

    x = np.random.randn(seq_len, input_dim)
    h0 = np.zeros(hidden_dim)

    Wx = np.random.randn(input_dim, hidden_dim) * 0.1
    Wh = np.random.randn(hidden_dim, hidden_dim) * 0.1
    b = np.zeros(hidden_dim)

    h_final = rnn_forward(x, h0, Wx, Wh, b)

    print("Final hidden state:\n", h_final)
