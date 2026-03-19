# sample1.py
# Demonstrate simple data augmentation for numeric datasets by adding noise.

import numpy as np


def augment_data(X, factor=3, noise_scale=0.1):
    rng = np.random.default_rng(0)
    augmented = [X]
    for _ in range(factor - 1):
        noise = rng.normal(scale=noise_scale, size=X.shape)
        augmented.append(X + noise)
    return np.vstack(augmented)


def main() -> None:
    rng = np.random.default_rng(0)
    X = rng.uniform(-1, 1, size=(100, 5))

    augmented = augment_data(X, factor=4, noise_scale=0.05)

    print("Original shape:", X.shape)
    print("Augmented shape:", augmented.shape)
    print("First row (original):", X[0])
    print("First row (augmented):", augmented[0])


if __name__ == "__main__":
    main()
