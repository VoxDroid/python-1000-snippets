# sample3.py
# Generate a heightmap by layering smoothed noise (fractal noise) using NumPy.

import numpy as np


def generate_noise(shape, scale=1.0):
    return np.random.rand(*shape) * scale


def smooth(data, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size))
    kernel /= kernel.sum()
    pad = kernel_size // 2
    padded = np.pad(data, pad, mode='wrap')
    out = np.zeros_like(data)
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            out[y, x] = np.sum(padded[y:y+kernel_size, x:x+kernel_size] * kernel)
    return out


def generate_heightmap(shape=(64, 64), octaves=4):
    height = np.zeros(shape)
    frequency = 1
    amplitude = 1.0

    for _ in range(octaves):
        noise = generate_noise(shape, scale=amplitude)
        height += smooth(noise, kernel_size=3)
        amplitude *= 0.5
        frequency *= 2
    return height


def main() -> None:
    heightmap = generate_heightmap((40, 40), octaves=3)
    print("Heightmap stats: min=", round(float(heightmap.min()), 3), "max=", round(float(heightmap.max()), 3))
    print("Sample row:", np.round(heightmap[0, :10], 3).tolist())


if __name__ == "__main__":
    main()
