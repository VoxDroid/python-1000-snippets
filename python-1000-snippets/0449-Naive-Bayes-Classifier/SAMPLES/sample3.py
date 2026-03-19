# sample3.py
# Demonstrate Bernoulli Naive Bayes on binary features.

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB


def main() -> None:
    rng = np.random.default_rng(0)

    # Binary features (e.g., presence/absence of terms)
    X = rng.integers(0, 2, size=(200, 10))
    y = np.concatenate([np.zeros(100, dtype=int), np.ones(100, dtype=int)])

    # Introduce a pattern for class 1
    X[y == 1, :3] = 1

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = BernoulliNB()
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    print("Test accuracy:", accuracy_score(y_test, preds))


if __name__ == "__main__":
    main()
