# sample2.py
# Compute autocorrelation for a time series and identify the strongest lag.

import numpy as np


def autocorrelation(x):
    n = len(x)
    x = x - np.mean(x)
    corr = np.correlate(x, x, mode='full')
    return corr[corr.size // 2:] / np.arange(n, 0, -1)


if __name__ == '__main__':
    np.random.seed(0)
    t = np.arange(200)
    series = np.sin(2 * np.pi * t / 20) + 0.3 * np.random.randn(len(t))

    ac = autocorrelation(series)
    lag = np.argmax(ac[1:]) + 1

    print(f"Strongest autocorrelation at lag {lag} (value {ac[lag]:.3f})")
    print(f"First 10 autocorrelation values: {np.round(ac[:10], 3)}")
