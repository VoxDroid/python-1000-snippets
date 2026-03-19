# sample1.py
# Build a simple supervised learning pipeline using scikit-learn.

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def main() -> None:
    data = load_iris(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=500)),
        ]
    )

    pipeline.fit(X_train, y_train)
    score = pipeline.score(X_test, y_test)

    print(f"Test accuracy: {score:.3f}")


if __name__ == "__main__":
    main()
