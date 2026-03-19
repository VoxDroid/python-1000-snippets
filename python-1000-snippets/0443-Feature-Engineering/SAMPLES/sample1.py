# sample1.py
# Demonstrate feature engineering by creating new features from existing ones.

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def main() -> None:
    data = load_iris(as_frame=True)
    df = data.frame.copy()

    # Add a derived feature: sepal area
    df["sepal area"] = df["sepal length (cm)"] * df["sepal width (cm)"]

    X = df[["sepal length (cm)", "sepal width (cm)", "sepal area"]]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = LogisticRegression(max_iter=500)
    clf.fit(X_train, y_train)

    print("Test accuracy with engineered feature:", clf.score(X_test, y_test))


if __name__ == "__main__":
    main()
