# sample1.py
# Demonstrate a minimal LSTM forward pass using numpy (no TensorFlow required).

import numpy as np


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def tanh(x: np.ndarray) -> np.ndarray:
    return np.tanh(x)


class SimpleLSTM:
    """A tiny LSTM implementation for educational purposes."""

    def __init__(self, input_dim: int, hidden_dim: int, seed: int = 0):
        rng = np.random.RandomState(seed)
        self.hidden_dim = hidden_dim

        # Input gate
        self.W_i = rng.randn(hidden_dim, input_dim) * 0.5
        self.U_i = rng.randn(hidden_dim, hidden_dim) * 0.5
        self.b_i = np.zeros(hidden_dim)

        # Forget gate
        self.W_f = rng.randn(hidden_dim, input_dim) * 0.5
        self.U_f = rng.randn(hidden_dim, hidden_dim) * 0.5
        self.b_f = np.zeros(hidden_dim)

        # Output gate
        self.W_o = rng.randn(hidden_dim, input_dim) * 0.5
        self.U_o = rng.randn(hidden_dim, hidden_dim) * 0.5
        self.b_o = np.zeros(hidden_dim)

        # Candidate cell state
        self.W_c = rng.randn(hidden_dim, input_dim) * 0.5
        self.U_c = rng.randn(hidden_dim, hidden_dim) * 0.5
        self.b_c = np.zeros(hidden_dim)

    def step(self, x_t: np.ndarray, h_prev: np.ndarray, c_prev: np.ndarray):
        i = sigmoid(self.W_i @ x_t + self.U_i @ h_prev + self.b_i)
        f = sigmoid(self.W_f @ x_t + self.U_f @ h_prev + self.b_f)
        o = sigmoid(self.W_o @ x_t + self.U_o @ h_prev + self.b_o)
        c_tilde = tanh(self.W_c @ x_t + self.U_c @ h_prev + self.b_c)

        c = f * c_prev + i * c_tilde
        h = o * tanh(c)
        return h, c

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Forward pass over a sequence X shaped (T, input_dim)."""
        h = np.zeros(self.hidden_dim)
        c = np.zeros(self.hidden_dim)
        outputs = []
        for t in range(X.shape[0]):
            h, c = self.step(X[t], h, c)
            outputs.append(h.copy())
        return np.vstack(outputs)


def main() -> None:
    np.random.seed(0)

    # Create a simple increasing sequence as input.
    seq_len = 8
    X = np.linspace(0, 1, seq_len).reshape(seq_len, 1)

    lstm = SimpleLSTM(input_dim=1, hidden_dim=10, seed=0)
    outputs = lstm.forward(X)

    print("Input sequence:", X.ravel())
    print("LSTM output (last time step):", outputs[-1])
    print("LSTM output shape:", outputs.shape)


if __name__ == "__main__":
    main()
