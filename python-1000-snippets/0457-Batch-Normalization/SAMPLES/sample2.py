# sample2.py
# Demonstrate how batch normalization can be applied during training (simulated).

import numpy as np


def batch_norm_training(X, gamma=None, beta=None, epsilon=1e-5):
    mean = X.mean(axis=0)
    var = X.var(axis=0)
    X_norm = (X - mean) / np.sqrt(var + epsilon)
    gamma = np.ones(X.shape[1]) if gamma is None else gamma
    beta = np.zeros(X.shape[1]) if beta is None else beta
    return gamma * X_norm + beta, mean, var


def main() -> None:
    rng = np.random.default_rng(0)
    X = rng.normal(loc=10.0, scale=5.0, size=(8, 4))

    gamma = np.array([1.0, 0.5, 2.0, 1.0])
    beta = np.array([0.0, 1.0, -1.0, 0.5])

    out, mean, var = batch_norm_training(X, gamma=gamma, beta=beta)

    print("Batch mean:", mean)
    print("Batch var:", var)
    print("Output sample:", out[0])


if __name__ == "__main__":
    main()
