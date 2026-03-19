# sample1.py
# Demonstrate a simple transfer learning workflow using scikit-learn models.

import os
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib


def main() -> None:
    os.makedirs("temp", exist_ok=True)
    model_path = "temp/transfer_base_model.joblib"

    digits = load_digits(as_frame=True)
    X, y = digits.data, digits.target

    # Split off a small 'new domain' from the original dataset to simulate transfer.
    X_base, X_new, y_base, y_new = train_test_split(X, y, test_size=0.2, random_state=0)

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=1000, random_state=0)),
        ]
    )

    pipeline.fit(X_base, y_base)
    joblib.dump(pipeline, model_path)

    print("Saved base model to", model_path)
    print("Base accuracy on held-out data:", pipeline.score(X_new, y_new))


if __name__ == "__main__":
    main()
