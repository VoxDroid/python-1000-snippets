# sample1.py
# Compute FFT of a sine wave and print peak frequency.

import numpy as np


def main():
    rate = 500
    t = np.linspace(0, 1, rate, endpoint=False)
    freq = 7
    signal = np.sin(2 * np.pi * freq * t)

    fft = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), d=1/rate)
    magnitude = np.abs(fft)

    peak_idx = np.argmax(magnitude)
    print("Peak frequency (Hz):", freqs[peak_idx])
    print("Top 5 magnitudes:", np.round(magnitude[:5], 3))


if __name__ == '__main__':
    main()
