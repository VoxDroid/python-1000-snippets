# sample3.py
# Demonstrate iterative hyperparameter tuning using HalvingGridSearchCV.

from sklearn.datasets import load_iris
from sklearn.experimental import enable_halving_search_cv  # noqa: F401
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import HalvingGridSearchCV, train_test_split


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    param_grid = {
        "C": [0.01, 0.1, 1.0, 10.0, 100.0],
        "penalty": ["l2"],
        "solver": ["lbfgs"],
    }

    base_estimator = LogisticRegression(max_iter=2000)
    halving = HalvingGridSearchCV(base_estimator, param_grid, cv=5, factor=2, random_state=0)
    halving.fit(X_train, y_train)

    print("Best params:", halving.best_params_)
    print("Best CV score:", halving.best_score_)
    print("Test set score:", halving.score(X_test, y_test))


if __name__ == "__main__":
    main()
