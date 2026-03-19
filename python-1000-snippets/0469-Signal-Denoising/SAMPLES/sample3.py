# sample3.py
# Low-pass filter a noisy signal using a simple moving average.

import numpy as np


def moving_average(signal: np.ndarray, window_size: int = 5) -> np.ndarray:
    kernel = np.ones(window_size) / window_size
    return np.convolve(signal, kernel, mode="same")


def main() -> None:
    rng = np.random.RandomState(2)
    x = np.linspace(0, 4 * np.pi, 250)
    noisy = np.sin(x) + 0.2 * rng.randn(len(x))

    smoothed = moving_average(noisy, window_size=9)

    print("Noisy sample:", np.round(noisy[:5], 3).tolist())
    print("Smoothed sample:", np.round(smoothed[:5], 3).tolist())


if __name__ == "__main__":
    main()
