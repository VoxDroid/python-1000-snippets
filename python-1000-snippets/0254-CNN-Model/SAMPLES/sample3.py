# sample3.py
# Apply multiple convolution filters and print feature map statistics.

import numpy as np


def conv2d(input_map, kernel, bias=0.0, stride=1):
    h, w = input_map.shape
    kh, kw = kernel.shape
    out_h = (h - kh) // stride + 1
    out_w = (w - kw) // stride + 1
    output = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            window = input_map[i*stride:i*stride+kh, j*stride:j*stride+kw]
            output[i, j] = np.sum(window * kernel) + bias

    return output


def main():
    img = np.random.randn(8, 8)

    # Define multiple filters (e.g., horizontal and vertical edge detectors)
    kernels = [
        np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=float),
        np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=float),
    ]

    feature_maps = []
    for idx, k in enumerate(kernels, start=1):
        fmap = conv2d(img, k)
        feature_maps.append(fmap)
        print(f"Filter {idx} output mean/var: {fmap.mean():.4f}/{fmap.var():.4f}")

    stacked = np.stack(feature_maps, axis=-1)
    print("Stacked feature map shape:", stacked.shape)


if __name__ == "__main__":
    main()
