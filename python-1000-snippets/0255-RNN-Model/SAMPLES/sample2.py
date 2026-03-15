# sample2.py
# Train a small RNN model on a toy binary classification task using numpy.

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def binary_cross_entropy(y_pred, y_true):
    eps = 1e-8
    return -np.mean(y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps))


def rnn_forward(x, h_prev, Wx, Wh, b):
    hs = [h_prev]
    h = h_prev
    for t in range(x.shape[0]):
        h = np.tanh(x[t] @ Wx + h @ Wh + b)
        hs.append(h)
    return hs


def rnn_backward(x, hs, dh_next, Wx, Wh):
    # Backprop through time (BPTT) for a single sequence.
    dWx = np.zeros_like(Wx)
    dWh = np.zeros_like(Wh)
    db = np.zeros_like(hs[0])

    for t in reversed(range(x.shape[0])):
        h = hs[t + 1]
        h_prev = hs[t]
        dtanh = dh_next * (1 - h ** 2)
        dWx += np.outer(x[t], dtanh)
        dWh += np.outer(h_prev, dtanh)
        db += dtanh
        dh_next = dtanh @ Wh.T

    return dWx, dWh, db, dh_next


def predict(X, Wx, Wh, b, Wout, bout):
    logits = []
    for i in range(X.shape[0]):
        hs = rnn_forward(X[i], np.zeros(Wh.shape[0]), Wx, Wh, b)
        h_final = hs[-1]
        logits.append(float((h_final @ Wout)[0] + bout))
    logits = np.array(logits).reshape(-1)
    return sigmoid(logits)


if __name__ == '__main__':
    np.random.seed(0)

    # Synthetic dataset: sequence of 0/1 and label is 1 if sum > half the length.
    N = 200
    seq_len = 10
    input_dim = 1
    hidden_dim = 8

    X = np.random.randint(0, 2, size=(N, seq_len, input_dim)).astype(float)
    y = (X.sum(axis=1).flatten() > (seq_len / 2)).astype(float)

    Wx = np.random.randn(input_dim, hidden_dim) * 0.1
    Wh = np.random.randn(hidden_dim, hidden_dim) * 0.1
    b = np.zeros(hidden_dim)
    Wout = np.random.randn(hidden_dim, 1) * 0.1
    bout = 0.0

    lr = 1e-1
    num_epochs = 30

    for epoch in range(1, num_epochs + 1):
        # Forward + backward for each sample (stochastic/mini-batch style)
        loss_sum = 0.0
        for i in range(N):
            hs = rnn_forward(X[i], np.zeros(hidden_dim), Wx, Wh, b)
            h_final = hs[-1]
            logit = float((h_final @ Wout)[0] + bout)
            y_pred = sigmoid(logit)

            loss = - (y[i] * np.log(y_pred + 1e-8) + (1 - y[i]) * np.log(1 - y_pred + 1e-8))
            loss_sum += loss

            dlogit = y_pred - y[i]
            dWout = h_final.reshape(-1, 1) * dlogit
            dbout = dlogit

            dh = dlogit * Wout.reshape(-1)
            dWx, dWh, db, _ = rnn_backward(X[i], hs, dh, Wx, Wh)

            # Gradient descent updates
            Wx -= lr * dWx
            Wh -= lr * dWh
            b -= lr * db
            Wout -= lr * dWout
            bout -= lr * dbout

        if epoch % 5 == 0 or epoch == 1:
            y_pred = predict(X, Wx, Wh, b, Wout, bout)
            acc = (y_pred.round() == y).mean()
            print(f"Epoch {epoch}, loss: {loss_sum / N:.4f}, accuracy: {acc:.3f}")

    # Final accuracy
    y_pred = predict(X, Wx, Wh, b, Wout, bout)
    acc = (y_pred.round() == y).mean()
    print(f"Final accuracy: {acc:.3f}")
