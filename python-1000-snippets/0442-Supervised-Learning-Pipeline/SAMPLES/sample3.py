# sample3.py
# Use ColumnTransformer to preprocess different feature types in a pipeline.

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main() -> None:
    iris = load_iris(as_frame=True)

    # Make a small dataset with a categorical feature for demonstration.
    df = iris.frame.copy()
    df["species"] = df["target"].map(lambda t: iris.target_names[t])

    features = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)", "species"]
    X = df[features]
    y = df["target"]

    numeric_features = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]
    categorical_features = ["species"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(), categorical_features),
        ]
    )

    pipeline = Pipeline(
        [
            ("preprocess", preprocessor),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    pipeline.fit(X_train, y_train)

    score = pipeline.score(X_test, y_test)
    print(f"Test accuracy with preprocessed pipeline: {score:.3f}")


if __name__ == "__main__":
    main()
