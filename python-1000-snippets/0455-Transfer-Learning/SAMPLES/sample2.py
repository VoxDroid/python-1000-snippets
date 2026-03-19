# sample2.py
# Load a pre-trained model and fine-tune it on new data (transfer learning).

import joblib
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


def main() -> None:
    base_model_path = "temp/transfer_base_model.joblib"
    model = joblib.load(base_model_path)

    digits = load_digits(as_frame=True)
    X, y = digits.data, digits.target

    # Simulate a new task by training on a subset of the data.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    model.fit(X_train, y_train)
    print("Fine-tuned accuracy on new data:", model.score(X_test, y_test))


if __name__ == "__main__":
    main()
