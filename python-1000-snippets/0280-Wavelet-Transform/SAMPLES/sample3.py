# sample3.py
# Implement a simple Haar wavelet transform and its inverse.

import numpy as np


def haar_wavelet_transform(signal):
    n = len(signal)
    output = signal.copy().astype(float)
    coeffs = []
    while n > 1:
        avg = (output[:n:2] + output[1:n:2]) / 2
        diff = (output[:n:2] - output[1:n:2]) / 2
        coeffs.append(diff)
        output[:n//2] = avg
        n //= 2
    coeffs.append(output[0:1])
    return coeffs


def inverse_haar_wavelet(coeffs):
    output = coeffs[-1].copy()
    for diff in reversed(coeffs[:-1]):
        avg = output
        output = np.empty((avg.size + diff.size,))
        output[0::2] = avg + diff
        output[1::2] = avg - diff
    return output


if __name__ == '__main__':
    signal = np.array([3.0, 1.0, 0.0, 4.0, 8.0, 6.0, 2.0, 5.0])
    coeffs = haar_wavelet_transform(signal)
    reconstructed = inverse_haar_wavelet(coeffs)

    print("Original signal:", signal)
    print("Wavelet coeffs (detail levels):")
    for i, c in enumerate(coeffs):
        print(f"  level {i}: {np.round(c, 3)}")
    print("Reconstructed signal:", np.round(reconstructed, 3))
