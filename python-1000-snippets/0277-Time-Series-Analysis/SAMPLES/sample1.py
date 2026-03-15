# sample1.py
# Compute a moving average over a time series.

import numpy as np


def moving_average(series, window):
    cumsum = np.cumsum(np.insert(series, 0, 0))
    return (cumsum[window:] - cumsum[:-window]) / window


if __name__ == '__main__':
    np.random.seed(42)
    series = np.cumsum(np.random.randn(100))  # random walk

    window = 5
    ma = moving_average(series, window)

    print("Original series (first 10):", np.round(series[:10], 2))
    print(f"{window}-point moving average (first 10):", np.round(ma[:10], 2))
