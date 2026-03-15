# sample1.py
# Train a linear regression model and print coefficients.

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


def main():
    X, y = make_regression(n_samples=200, n_features=1, noise=10.0, random_state=42)

    model = LinearRegression()
    model.fit(X, y)

    print("Coefficient:", float(model.coef_[0]))
    print("Intercept:", float(model.intercept_))


if __name__ == "__main__":
    main()
