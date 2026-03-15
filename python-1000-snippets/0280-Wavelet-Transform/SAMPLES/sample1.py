# sample1.py
# Perform a discrete wavelet decomposition using PyWavelets.

import numpy as np
import pywt


def main():
    rate = 256
    t = np.linspace(0, 1, rate, endpoint=False)
    signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

    coeffs = pywt.wavedec(signal, wavelet='db1', level=3)
    print('Levels:', len(coeffs))
    for i, c in enumerate(coeffs):
        print(f'  Level {i} length: {len(c)}')


if __name__ == '__main__':
    main()
