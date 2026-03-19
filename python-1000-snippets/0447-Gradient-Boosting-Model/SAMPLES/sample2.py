# sample2.py
# Train a Histogram-based Gradient Boosting classifier for faster training on larger datasets.

from sklearn.datasets import load_iris
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = HistGradientBoostingClassifier(random_state=0)
    clf.fit(X_train, y_train)

    print("Test accuracy:", clf.score(X_test, y_test))


if __name__ == "__main__":
    main()
