# sample2.py
# Demonstrate feature engineering using polynomial features.

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    pipeline = Pipeline(
        [
            ("scale", StandardScaler()),
            ("poly", PolynomialFeatures(degree=2, include_bias=False)),
            ("clf", LogisticRegression(max_iter=2000)),
        ]
    )

    scores = cross_val_score(pipeline, X, y, cv=5)
    print("Cross-validation scores:", scores)
    print("Mean accuracy:", scores.mean())


if __name__ == "__main__":
    main()
