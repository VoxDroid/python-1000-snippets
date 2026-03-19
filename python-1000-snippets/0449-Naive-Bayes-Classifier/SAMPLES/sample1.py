# sample1.py
# Demonstrate Gaussian Naive Bayes on the iris dataset.

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = GaussianNB()
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    print("Test accuracy:", accuracy_score(y_test, preds))


if __name__ == "__main__":
    main()
