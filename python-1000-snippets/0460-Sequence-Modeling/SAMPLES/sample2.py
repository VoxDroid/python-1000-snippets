# sample2.py
# Demonstrate sequence modeling via lag-feature regression (no deep learning library required).

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def create_lag_features(series: np.ndarray, lag: int = 3):
    X, y = [], []
    for i in range(lag, len(series)):
        X.append(series[i - lag : i])
        y.append(series[i])
    return np.array(X), np.array(y)


def main() -> None:
    # Generate a simple noisy sine wave.
    rng = np.random.RandomState(0)
    t = np.linspace(0, 4 * np.pi, 40)
    series = np.sin(t) + 0.2 * rng.randn(len(t))

    X, y = create_lag_features(series, lag=5)
    split = int(0.7 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    print("Test MSE:", round(mse, 5))
    print("First 3 true vs predicted:")
    for true, pred in zip(y_test[:3], preds[:3]):
        print(f"  {true:.4f} -> {pred:.4f}")


if __name__ == "__main__":
    main()
