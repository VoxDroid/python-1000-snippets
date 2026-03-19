# sample1.py
# Forecast a noisy trend line using lag features + LinearRegression.

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def make_lagged_dataset(series: np.ndarray, lag: int = 5):
    X, y = [], []
    for i in range(lag, len(series)):
        X.append(series[i - lag : i])
        y.append(series[i])
    return np.array(X), np.array(y)


def main() -> None:
    rng = np.random.RandomState(0)
    t = np.arange(0, 60)
    series = 0.1 * t + np.sin(t / 5.0) + 0.2 * rng.randn(len(t))

    X, y = make_lagged_dataset(series, lag=6)
    split = int(0.75 * len(X))

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    print("Linear forecast MSE:", round(mse, 4))
    print("Example true vs predicted:")
    for true, pred in zip(y_test[:3], preds[:3]):
        print(f"  {true:.3f} -> {pred:.3f}")


if __name__ == "__main__":
    main()
