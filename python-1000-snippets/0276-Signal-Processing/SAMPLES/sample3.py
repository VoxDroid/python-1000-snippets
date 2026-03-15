# sample3.py
# Filter a noisy signal by zeroing out high-frequency FFT coefficients.

import numpy as np


def low_pass_fft(signal, rate, cutoff_hz):
    n = len(signal)
    fft = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(n, d=1/rate)
    mask = freqs <= cutoff_hz
    fft_filtered = fft * mask
    return np.fft.irfft(fft_filtered, n=n)


if __name__ == '__main__':
    rate = 500
    t = np.linspace(0, 1, rate, endpoint=False)
    clean = np.sin(2 * np.pi * 5 * t)
    noise = 0.5 * np.sin(2 * np.pi * 80 * t)
    signal = clean + noise

    filtered = low_pass_fft(signal, rate, cutoff_hz=20)

    # Compare energy in high-frequency band
    orig_fft = np.fft.rfft(signal)
    filt_fft = np.fft.rfft(filtered)
    hf_band = (np.fft.rfftfreq(len(signal), d=1/rate) > 40)

    orig_hf_energy = np.sum(np.abs(orig_fft[hf_band]) ** 2)
    filt_hf_energy = np.sum(np.abs(filt_fft[hf_band]) ** 2)

    print(f"Original HF energy: {orig_hf_energy:.1f}")
    print(f"Filtered HF energy: {filt_hf_energy:.1f}")
