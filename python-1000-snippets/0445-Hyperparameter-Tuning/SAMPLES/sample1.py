# sample1.py
# Demonstrate hyperparameter tuning using GridSearchCV.

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    model = LogisticRegression(max_iter=2000)
    param_grid = {
        "C": [0.1, 1.0, 10.0],
        "penalty": ["l2"],
        "solver": ["lbfgs"],
    }

    grid = GridSearchCV(model, param_grid, cv=5)
    grid.fit(X_train, y_train)

    print("Best params:", grid.best_params_)
    print("Best cross-validation score:", grid.best_score_)
    print("Test set score:", grid.score(X_test, y_test))


if __name__ == "__main__":
    main()
