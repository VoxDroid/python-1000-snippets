# sample1.py
# Demonstrate K-Nearest Neighbors classification on the iris dataset.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = KNeighborsClassifier(n_neighbors=5)
    clf.fit(X_train, y_train)

    print("Test accuracy:", clf.score(X_test, y_test))
    print("Example prediction (first 5 samples):", clf.predict(X_test[:5]))


if __name__ == "__main__":
    main()
