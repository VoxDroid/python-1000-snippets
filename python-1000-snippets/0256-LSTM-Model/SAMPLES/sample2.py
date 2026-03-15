# sample2.py
# Train an LSTM-based classifier with a fixed LSTM and trainable output layer.

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def lstm_forward(x, params):
    """Run a full sequence through an LSTM and return final hidden state."""
    h = np.zeros(params["hidden_dim"])
    c = np.zeros(params["hidden_dim"])
    for t in range(x.shape[0]):
        x_t = x[t]
        i = sigmoid(x_t @ params["Wi"] + h @ params["Ui"] + params["bi"])
        f = sigmoid(x_t @ params["Wf"] + h @ params["Uf"] + params["bf"])
        o = sigmoid(x_t @ params["Wo"] + h @ params["Uo"] + params["bo"])
        g = np.tanh(x_t @ params["Wc"] + h @ params["Uc"] + params["bc"])
        c = f * c + i * g
        h = o * np.tanh(c)
    return h


if __name__ == '__main__':
    np.random.seed(0)

    # Toy dataset: sequences of 0/1, label=1 if sum > half the length
    N = 200
    seq_len = 10
    input_dim = 1
    hidden_dim = 16

    X = np.random.randint(0, 2, size=(N, seq_len, input_dim)).astype(float)
    y = (X.sum(axis=1).flatten() > (seq_len / 2)).astype(float)

    params = {
        "hidden_dim": hidden_dim,
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

    # Only train output weights on top of fixed LSTM features.
    Wout = np.random.randn(hidden_dim, 1) * 0.1
    bout = 0.0

    lr = 1e-1
    epochs = 20

    for epoch in range(1, epochs + 1):
        # Extract last hidden state for each sequence
        hs = np.stack([lstm_forward(X[i], params) for i in range(N)])
        logits = (hs @ Wout).reshape(-1) + bout
        y_pred = sigmoid(logits)

        loss = -np.mean(y * np.log(y_pred + 1e-8) + (1 - y) * np.log(1 - y_pred + 1e-8))
        if epoch % 5 == 0 or epoch == 1:
            acc = (y_pred.round() == y).mean()
            print(f"Epoch {epoch}, loss: {loss:.4f}, accuracy: {acc:.3f}")

        # Gradient descent on output layer only (fixed LSTM features)
        dlogits = y_pred - y
        dWout = (hs.T @ dlogits.reshape(-1, 1)) / N
        dbout = dlogits.mean()
        Wout -= lr * dWout
        bout -= lr * dbout

    y_pred = sigmoid((hs @ Wout).reshape(-1) + bout)
    final_acc = (y_pred.round() == y).mean()
    print("Final accuracy:", final_acc)
