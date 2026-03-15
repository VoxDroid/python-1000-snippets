# sample2.py
# Apply a simple high-pass filter (remove low-frequency trend) via detrending.

import numpy as np


def high_pass(signal, window_size=31):
    # Approximate low-frequency trend with moving average and subtract
    trend = np.convolve(signal, np.ones(window_size) / window_size, mode="same")
    return signal - trend


if __name__ == '__main__':
    t = np.linspace(0, 1, 500, endpoint=False)
    low_freq = 0.5 * np.sin(2 * np.pi * 1 * t)
    high_freq = 0.3 * np.sin(2 * np.pi * 20 * t)
    signal = low_freq + high_freq

    filtered = high_pass(signal, window_size=41)

    print("Original signal mean:", signal.mean())
    print("Filtered signal mean (should be near 0):", filtered.mean())
    print("Original signal std:", signal.std())
    print("Filtered signal std:", filtered.std())
