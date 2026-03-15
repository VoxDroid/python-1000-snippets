# sample1.py
# Train a logistic regression model and print accuracy on synthetic data.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def main():
    X, y = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, random_state=42)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    print('Accuracy:', model.score(X_test, y_test))


if __name__ == '__main__':
    main()
