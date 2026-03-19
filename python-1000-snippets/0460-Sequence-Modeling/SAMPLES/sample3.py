# sample3.py
# Demonstrate a simple sequence classification task using k-NN with lag features.

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def make_sequence_examples(n_samples: int = 100, seq_len: int = 10):
    """Create synthetic sequences for two classes (sine waves and square waves)."""
    rng = np.random.RandomState(0)
    X = []
    y = []

    for _ in range(n_samples // 2):
        t = np.linspace(0, 2 * np.pi, seq_len)
        X.append(np.sin(t) + 0.1 * rng.randn(seq_len))
        y.append(0)

    for _ in range(n_samples // 2):
        t = np.linspace(0, 2 * np.pi, seq_len)
        X.append(np.sign(np.sin(t)) + 0.1 * rng.randn(seq_len))
        y.append(1)

    return np.array(X), np.array(y)


def main() -> None:
    X, y = make_sequence_examples(n_samples=120, seq_len=20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0, stratify=y
    )

    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)

    print("Test accuracy:", round(clf.score(X_test, y_test), 3))
    print("Example predictions:", clf.predict(X_test[:5]).tolist())


if __name__ == "__main__":
    main()
