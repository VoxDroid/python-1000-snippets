# sample1.py
# Generate a heightmap using layered random noise and smoothing.

import numpy as np


def smooth(data: np.ndarray, kernel_size: int = 5) -> np.ndarray:
    kernel = np.ones((kernel_size, kernel_size))
    kernel /= kernel.sum()
    pad = kernel_size // 2
    padded = np.pad(data, pad, mode='wrap')
    out = np.zeros_like(data)
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            out[y, x] = np.sum(padded[y:y+kernel_size, x:x+kernel_size] * kernel)
    return out


def generate_heightmap(shape=(64, 64), octaves=3):
    height = np.zeros(shape)
    amplitude = 1.0
    for i in range(octaves):
        noise = np.random.rand(*shape) * amplitude
        height += smooth(noise, kernel_size=3)
        amplitude *= 0.5
    return height


def main() -> None:
    hm = generate_heightmap((50, 50), octaves=4)
    print("Heightmap stats: min=", round(float(hm.min()), 3), "max=", round(float(hm.max()), 3))
    print("Row sample:", np.round(hm[0, :10], 3).tolist())


if __name__ == "__main__":
    main()
