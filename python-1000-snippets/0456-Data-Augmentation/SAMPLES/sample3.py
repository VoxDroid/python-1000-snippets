# sample3.py
# Augment a dataset and show how the augmented set can be used to increase sample size.

import numpy as np
from sklearn.datasets import make_classification


def augment_with_noise(X, y, repeats=2, noise_scale=0.1):
    rng = np.random.default_rng(0)
    augmented = [X]
    augmented_y = [y]
    for _ in range(repeats - 1):
        noise = rng.normal(scale=noise_scale, size=X.shape)
        augmented.append(X + noise)
        augmented_y.append(y)
    return np.vstack(augmented), np.concatenate(augmented_y)


def main() -> None:
    X, y = make_classification(n_samples=100, n_features=10, n_classes=2, random_state=0)

    X_aug, y_aug = augment_with_noise(X, y, repeats=5, noise_scale=0.05)

    print("Original size:", X.shape[0])
    print("Augmented size:", X_aug.shape[0])
    print("Class distribution in augmented data:")
    unique, counts = np.unique(y_aug, return_counts=True)
    print(dict(zip(unique, counts)))


if __name__ == "__main__":
    main()
