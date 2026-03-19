# sample3.py
# Compare base model and fine-tuned model performance.

import joblib
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


def evaluate(model_path: str, X, y):
    model = joblib.load(model_path)
    return model.score(X, y)


def main() -> None:
    base_model_path = "temp/transfer_base_model.joblib"

    digits = load_digits(as_frame=True)
    X, y = digits.data, digits.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    base_score = evaluate(base_model_path, X_test, y_test)
    print("Base model test accuracy:", base_score)

    # Fine-tune in place (assumes sample2 has run and updated the model file)
    fine_tuned_score = evaluate(base_model_path, X_test, y_test)
    print("Fine-tuned model test accuracy:", fine_tuned_score)


if __name__ == "__main__":
    main()
