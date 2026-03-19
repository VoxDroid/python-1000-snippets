# sample2.py
# Use a RandomForestRegressor to forecast the next value in a time series.

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def make_lagged_dataset(series: np.ndarray, lag: int = 3):
    X, y = [], []
    for i in range(lag, len(series)):
        X.append(series[i - lag : i])
        y.append(series[i])
    return np.array(X), np.array(y)


def main() -> None:
    rng = np.random.RandomState(1)
    t = np.linspace(0, 10, 100)
    series = np.cos(t) + 0.1 * rng.randn(len(t))

    X, y = make_lagged_dataset(series, lag=4)
    split = int(0.8 * len(X))

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = RandomForestRegressor(n_estimators=25, random_state=0)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    print("Random forest forecast MAE:", round(mae, 4))
    print("Example predictions:", [round(x, 3) for x in preds[:5]])


if __name__ == "__main__":
    main()
