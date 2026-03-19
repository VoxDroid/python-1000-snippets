# sample3.py
# Compose preprocessing steps for numeric and categorical data using a pipeline.

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main() -> None:
    df = pd.DataFrame(
        {
            "age": [25, 32, None, 40, 28],
            "salary": [50000, 60000, 55000, None, 52000],
            "department": ["sales", "engineering", "sales", "hr", None],
        }
    )

    numeric_features = ["age", "salary"]
    categorical_features = ["department"]

    numeric_transformer = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(sparse_output=False, handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    pipeline = Pipeline([("preprocess", preprocessor)])

    transformed = pipeline.fit_transform(df)
    print("Preprocessed feature matrix shape:", transformed.shape)
    print(transformed)


if __name__ == "__main__":
    main()
