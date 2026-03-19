# sample1.py
# Implement batch normalization from scratch for a single batch of data.

import numpy as np


def batch_norm(X, epsilon=1e-5):
    mean = X.mean(axis=0)
    var = X.var(axis=0)
    X_norm = (X - mean) / np.sqrt(var + epsilon)
    return X_norm, mean, var


def main() -> None:
    rng = np.random.default_rng(0)
    X = rng.normal(loc=5.0, scale=2.0, size=(5, 3))

    X_norm, mean, var = batch_norm(X)

    print("Original batch mean:", mean)
    print("Original batch var:", var)
    print("Normalized batch mean (approx 0):", X_norm.mean(axis=0))
    print("Normalized batch var (approx 1):", X_norm.var(axis=0))


if __name__ == "__main__":
    main()
