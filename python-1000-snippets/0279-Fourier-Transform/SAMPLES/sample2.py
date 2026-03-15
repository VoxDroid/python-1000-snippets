# sample2.py
# Demonstrate inverse FFT reconstruction of a real signal.

import numpy as np


def main():
    rate = 500
    t = np.linspace(0, 1, rate, endpoint=False)
    signal = np.sin(2 * np.pi * 12 * t) + 0.5 * np.sin(2 * np.pi * 30 * t)

    fft = np.fft.rfft(signal)
    reconstructed = np.fft.irfft(fft, n=len(signal))

    error = np.max(np.abs(signal - reconstructed))
    print(f"Reconstruction max absolute error: {error:.3e}")


if __name__ == '__main__':
    main()
