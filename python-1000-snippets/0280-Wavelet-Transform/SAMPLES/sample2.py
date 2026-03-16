# sample2.py
# Denoise a signal using wavelet thresholding (VisuShrink) and compare MSE.

import numpy as np
import pywt


def denoise_signal(signal, wavelet='db1', level=2):
    coeffs = pywt.wavedec(signal, wavelet=wavelet, level=level)
    sigma = np.median(np.abs(coeffs[-1])) / 0.6745
    threshold = sigma * np.sqrt(2 * np.log(len(signal)))
    denoised_coeffs = [pywt.threshold(c, threshold, mode='hard') for c in coeffs]
    return pywt.waverec(denoised_coeffs, wavelet)


if __name__ == '__main__':
    rng = np.random.default_rng(0)
    rate = 256
    t = np.linspace(0, 1, rate, endpoint=False)
    clean = np.sin(2 * np.pi * 5 * t)

    noisy = clean + 0.3 * rng.normal(size=rate)
    denoised = denoise_signal(noisy, level=3)

    mse_noisy = np.mean((clean - noisy) ** 2)
    mse_denoised = np.mean((clean - denoised) ** 2)

    print(f"MSE noisy: {mse_noisy:.4f}")
    print(f"MSE denoised: {mse_denoised:.4f}")
