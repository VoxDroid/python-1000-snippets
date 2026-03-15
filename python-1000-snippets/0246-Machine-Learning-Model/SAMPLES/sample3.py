# sample3.py
# Demonstrate a scikit-learn pipeline with scaling and logistic regression.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=500)),
    ])

    pipeline.fit(X_train, y_train)

    print("Pipeline accuracy:", pipeline.score(X_test, y_test))


if __name__ == "__main__":
    main()
