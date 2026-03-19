# sample3.py
# Use GridSearchCV to tune SVM hyperparameters.

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    param_grid = {
        "C": [0.1, 1, 10],
        "gamma": ["scale", "auto"],
        "kernel": ["rbf"],
    }

    grid = GridSearchCV(SVC(), param_grid, cv=5)
    grid.fit(X_train, y_train)

    print("Best params:", grid.best_params_)
    print("Test set score:", grid.score(X_test, y_test))


if __name__ == "__main__":
    main()
