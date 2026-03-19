# sample3.py
# Demonstrate a naive persistence forecast baseline (predict last observed value).

import numpy as np
from sklearn.metrics import mean_squared_error


def persistence_forecast(series: np.ndarray, lag: int = 1):
    return series[:-lag], series[lag:]


def main() -> None:
    rng = np.random.RandomState(2)
    t = np.arange(0, 50)
    series = 0.2 * t + np.sin(t / 3.0) + 0.3 * rng.randn(len(t))

    # Use the previous value as the forecast for the next timestep.
    y_true, y_pred = persistence_forecast(series, lag=1)

    mse = mean_squared_error(y_true, y_pred)
    print("Persistence baseline MSE:", round(mse, 4))
    print("Example last true vs predicted:", y_true[-3:], y_pred[-3:])


if __name__ == "__main__":
    main()
