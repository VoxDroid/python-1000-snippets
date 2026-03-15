# sample3.py
# Measure performance of a linear regression model using R^2 score.

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def main():
    X, y = make_regression(n_samples=200, n_features=1, noise=10.0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)

    print("R^2 score:", score)


if __name__ == "__main__":
    main()
