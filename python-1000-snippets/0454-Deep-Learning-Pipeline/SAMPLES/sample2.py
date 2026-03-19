# sample2.py
# Demonstrate saving and loading a trained MLP model using joblib.

import joblib
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    model_path = "temp/mlp_pipeline.joblib"

    data = load_digits(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("mlp", MLPClassifier(hidden_layer_sizes=(64,), max_iter=300, random_state=0)),
        ]
    )

    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, model_path)

    loaded = joblib.load(model_path)
    print("Saved and reloaded model; test accuracy:", loaded.score(X_test, y_test))


if __name__ == "__main__":
    main()
