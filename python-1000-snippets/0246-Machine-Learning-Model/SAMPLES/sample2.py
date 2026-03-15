# sample2.py
# Train a model, save it to disk with joblib, then load it and verify predictions match.

import tempfile
import os

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from joblib import dump, load


def main():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    with tempfile.NamedTemporaryFile(suffix='.joblib', delete=False) as tmp:
        path = tmp.name

    try:
        dump(model, path)
        loaded = load(path)
        print('Original accuracy:', model.score(X_test, y_test))
        print('Loaded model accuracy:', loaded.score(X_test, y_test))
    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == '__main__':
    main()
