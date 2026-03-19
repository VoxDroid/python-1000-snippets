# sample3.py
# Demonstrate leave-one-out cross-validation (LOOCV).

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut, cross_val_score


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    clf = LogisticRegression(max_iter=2000)
    cv = LeaveOneOut()

    scores = cross_val_score(clf, X, y, cv=cv)

    print("LOOCV mean accuracy:", scores.mean())


if __name__ == "__main__":
    main()
