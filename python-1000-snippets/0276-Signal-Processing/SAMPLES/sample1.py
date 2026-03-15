# sample1.py
# Apply a simple moving-average filter to a noisy signal.

import numpy as np


def moving_average(signal, window_size=5):
    kernel = np.ones(window_size) / window_size
    return np.convolve(signal, kernel, mode="same")


if __name__ == '__main__':
    t = np.linspace(0, 1, 500, endpoint=False)
    clean = np.sin(2 * np.pi * 5 * t)
    noise = 0.5 * np.random.normal(size=t.shape)
    noisy = clean + noise

    smoothed = moving_average(noisy, window_size=11)

    print("Noisy signal mean:", noisy.mean())
    print("Smoothed signal mean:", smoothed.mean())
    print("Noisy signal std:", noisy.std())
    print("Smoothed signal std:", smoothed.std())
