# sample1.py
# Perform a forward pass through a tiny CNN (conv + dense) using numpy.

import numpy as np


def conv2d(input_map, kernel, bias=0.0, stride=1):
    """Simple 2D convolution (no padding) for a single channel."""
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


def relu(x):
    return np.maximum(0, x)


def softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()


def main():
    # Create a random "image" (single channel)
    img = np.random.randn(8, 8)

    # Define a simple edge-detect kernel
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=float)
    bias = 0.0

    conv_out = conv2d(img, kernel)
    activated = relu(conv_out)
    flattened = activated.ravel()

    # Simple fully connected layer (random weights)
    fc_weights = np.random.randn(flattened.size, 3) * 0.1
    fc_bias = np.zeros(3)

    logits = flattened.dot(fc_weights) + fc_bias
    probs = softmax(logits)

    print("Conv output shape:", conv_out.shape)
    print("Softmax probabilities:", probs.tolist())


if __name__ == "__main__":
    main()
