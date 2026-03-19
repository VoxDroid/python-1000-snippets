# sample2.py
# Demonstrate Multinomial Naive Bayes on synthetic count data.

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def main() -> None:
    # Synthetic count data (e.g., bag-of-words)
    rng = np.random.default_rng(0)
    X = rng.poisson(lam=2.0, size=(200, 10))

    # Create two classes with different average counts
    y = np.concatenate([np.zeros(100, dtype=int), np.ones(100, dtype=int)])
    X[y == 1] += 3

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    print("Test accuracy:", accuracy_score(y_test, preds))


if __name__ == "__main__":
    main()
