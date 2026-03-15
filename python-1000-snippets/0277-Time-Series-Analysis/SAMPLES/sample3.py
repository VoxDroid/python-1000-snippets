# sample3.py
# Estimate a linear trend in a time series using least squares fitting.

import numpy as np


def linear_trend(x):
    # Fit y = a*t + b via least squares
    t = np.arange(len(x))
    A = np.vstack([t, np.ones(len(t))]).T
    slope, intercept = np.linalg.lstsq(A, x, rcond=None)[0]
    return slope, intercept


if __name__ == '__main__':
    np.random.seed(1)
    t = np.arange(150)
    trend = 0.05 * t
    noise = np.random.normal(0, 1.0, size=len(t))
    series = trend + noise

    slope, intercept = linear_trend(series)
    print(f"Estimated trend: slope={slope:.4f}, intercept={intercept:.3f}")
    print(f"Actual trend slope=0.05")
