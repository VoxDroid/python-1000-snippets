# sample3.py
# Explore how different values of k affect KNN classification accuracy.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    for k in [1, 3, 5, 7, 9]:
        clf = KNeighborsClassifier(n_neighbors=k)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        print(f"k={k}: test accuracy={score:.3f}")


if __name__ == "__main__":
    main()
