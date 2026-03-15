# sample2.py
# Predict on new data using a trained linear regression model.

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


def main():
    X, y = make_regression(n_samples=200, n_features=1, noise=10.0, random_state=42)

    model = LinearRegression()
    model.fit(X, y)

    new_X = [[-1.0], [0.0], [1.0]]
    predictions = model.predict(new_X)

    print("New inputs:", new_X)
    print("Predictions:", [float(p) for p in predictions])


if __name__ == "__main__":
    main()
