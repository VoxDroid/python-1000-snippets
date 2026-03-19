# sample3.py
# Use discretization and one-hot encoding as feature engineering techniques.

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import KBinsDiscretizer, OneHotEncoder


def main() -> None:
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()

    # Convert a continuous feature into categories.
    df["petal length bin"] = pd.cut(df["petal length (cm)"], bins=3, labels=["short", "medium", "long"])

    X = df[["petal width (cm)", "petal length bin"]]
    y = df["target"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("bin", OneHotEncoder(), ["petal length bin"]),
        ],
        remainder="passthrough",
    )

    pipeline = Pipeline(
        [
            ("preprocess", preprocessor),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    pipeline.fit(X_train, y_train)

    print("Test accuracy with binned feature:", pipeline.score(X_test, y_test))


if __name__ == "__main__":
    main()
