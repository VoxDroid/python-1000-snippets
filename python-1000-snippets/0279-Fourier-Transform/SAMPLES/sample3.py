# sample3.py
# Apply a simple frequency-domain filter by zeroing Fourier coefficients.

import numpy as np


def low_pass(signal, rate, cutoff_hz):
    n = len(signal)
    fft = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(n, d=1/rate)
    mask = freqs <= cutoff_hz
    filtered_fft = fft * mask
    return np.fft.irfft(filtered_fft, n=n)


if __name__ == '__main__':
    rate = 500
    t = np.linspace(0, 1, rate, endpoint=False)
    signal = np.sin(2 * np.pi * 5 * t) + 0.7 * np.sin(2 * np.pi * 90 * t)

    filtered = low_pass(signal, rate, cutoff_hz=20)
    orig_energy = np.sum(signal ** 2)
    filt_energy = np.sum(filtered ** 2)

    print(f"Original energy: {orig_energy:.3f}")
    print(f"Filtered energy: {filt_energy:.3f}")

    # Optionally show a sample snippet
    print("First 5 samples of filtered signal:", np.round(filtered[:5], 4))
