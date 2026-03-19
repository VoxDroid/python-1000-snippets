# sample2.py
# Perform simple image-style augmentation on numeric arrays (flip, jitter).

import numpy as np


def augment_flip(X):
    return np.flip(X, axis=1)


def augment_jitter(X, scale=0.05):
    rng = np.random.default_rng(0)
    return X + rng.normal(scale=scale, size=X.shape)


def main() -> None:
    rng = np.random.default_rng(0)
    X = rng.uniform(0, 1, size=(3, 4))

    print("Original:")
    print(X)

    X_flipped = augment_flip(X)
    print("Flipped:")
    print(X_flipped)

    X_jitter = augment_jitter(X)
    print("Jittered:")
    print(X_jitter)


if __name__ == "__main__":
    main()
