# sample2.py
# Demonstrate hyperparameter tuning using RandomizedSearchCV.

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
import numpy as np


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    model = RandomForestClassifier(random_state=0)
    param_dist = {
        "n_estimators": [10, 50, 100, 200],
        "max_depth": [None, 3, 5, 10],
        "max_features": [None, "sqrt", "log2"],
    }

    search = RandomizedSearchCV(model, param_dist, n_iter=10, cv=5, random_state=0)
    search.fit(X_train, y_train)

    print("Best params:", search.best_params_)
    print("Best CV score:", search.best_score_)
    print("Test set score:", search.score(X_test, y_test))


if __name__ == "__main__":
    main()
