# sample3.py
# Display feature importances from a gradient boosting model.

from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = GradientBoostingClassifier(random_state=0)
    clf.fit(X_train, y_train)

    print("Test accuracy:", clf.score(X_test, y_test))
    print("Feature importances:")
    for name, imp in zip(X.columns, clf.feature_importances_):
        print(f"  {name}: {imp:.4f}")


if __name__ == "__main__":
    main()
