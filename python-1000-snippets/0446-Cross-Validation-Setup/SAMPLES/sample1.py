# sample1.py
# Demonstrate k-fold cross-validation using cross_val_score.

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, KFold


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    clf = LogisticRegression(max_iter=2000)
    cv = KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(clf, X, y, cv=cv)

    print("KFold scores:", scores)
    print("Mean score:", scores.mean())


if __name__ == "__main__":
    main()
