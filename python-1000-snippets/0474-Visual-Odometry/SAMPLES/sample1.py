# sample1.py
# Estimate translation between two images using phase correlation.

import numpy as np


def phase_correlation(img1: np.ndarray, img2: np.ndarray):
    f1 = np.fft.fft2(img1)
    f2 = np.fft.fft2(img2)
    R = f1 * np.conj(f2)
    R /= np.abs(R) + 1e-8
    corr = np.fft.ifft2(R)
    maxima = np.unravel_index(np.argmax(np.abs(corr)), corr.shape)
    shifts = np.array(maxima, dtype=float)
    for i in range(2):
        if shifts[i] > img1.shape[i] // 2:
            shifts[i] -= img1.shape[i]
    # Phase correlation returns the shift that aligns img2 to img1.
    # In this example we report the shift of img2 relative to img1.
    return (-shifts[0], -shifts[1])


def main() -> None:
    # Create a 2D sinusoidal pattern and shift it
    x = np.linspace(0, 2 * np.pi, 128)
    y = np.linspace(0, 2 * np.pi, 128)
    xv, yv = np.meshgrid(x, y)
    img = np.sin(xv) + np.cos(yv)

    shift = (5, -3)
    img_shifted = np.roll(np.roll(img, shift[0], axis=0), shift[1], axis=1)

    estimated_shift = phase_correlation(img, img_shifted)
    print("True shift:", shift)
    print("Estimated shift:", estimated_shift)


if __name__ == "__main__":
    main()
