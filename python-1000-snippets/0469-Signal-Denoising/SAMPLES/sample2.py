# sample2.py
# Denoise a noisy signal with a Wiener filter (adaptive noise reduction).

import numpy as np
from scipy.signal import wiener


def main() -> None:
    rng = np.random.RandomState(1)
    x = np.linspace(0, 4 * np.pi, 300)
    noisy = np.sin(x) + 0.3 * rng.randn(len(x))

    denoised = wiener(noisy, mysize=11)

    print("Noisy signal mean:", round(float(np.mean(noisy)), 4))
    print("Denoised signal mean:", round(float(np.mean(denoised)), 4))
    print("First 5 denoised samples:", np.round(denoised[:5], 3).tolist())


if __name__ == "__main__":
    main()
