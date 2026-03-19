# sample1.py
# Denoise a noisy sine wave using a Savitzky-Golay filter.

import numpy as np
from scipy.signal import savgol_filter


def main() -> None:
    rng = np.random.RandomState(0)
    x = np.linspace(0, 2 * np.pi, 200)
    noisy = np.sin(x) + 0.25 * rng.randn(len(x))

    denoised = savgol_filter(noisy, window_length=17, polyorder=2)

    print("Noisy signal sample:", np.round(noisy[:5], 3).tolist())
    print("Denoised signal sample:", np.round(denoised[:5], 3).tolist())


if __name__ == "__main__":
    main()
