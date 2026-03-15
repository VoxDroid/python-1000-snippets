# sample2.py
# Train a simple CNN-like model (conv + linear) on random data using gradient descent.

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


def relu(x):
    return np.maximum(0, x)


def main():
    # Generate random "images" and targets derived from a stable function of the image.
    n_samples = 50
    imgs = np.random.randn(n_samples, 8, 8)
    # Use a deterministic target to avoid exploding gradients
    targets = np.array([np.sum(img) for img in imgs]) * 0.1

    # Fixed convolution kernel
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=float)

    # Initialize linear layer weights and bias
    hidden_size = 20
    feature_size = (8-2) * (8-2)  # after 3x3 conv
    W = np.random.randn(feature_size, hidden_size) * 0.1
    b = np.zeros(hidden_size)
    out_w = np.random.randn(hidden_size) * 0.1
    out_b = 0.0

    lr = 1e-4

    for epoch in range(10):
        total_loss = 0.0
        for i in range(n_samples):
            x = imgs[i]
            y = targets[i]

            conv_out = conv2d(x, kernel)
            h = relu(conv_out.ravel().dot(W) + b)
            pred = h.dot(out_w) + out_b

            err = pred - y
            total_loss += err**2

            # Simple gradient descent updates
            d_pred = 2 * err
            out_w -= lr * d_pred * h
            out_b -= lr * d_pred

            dh = d_pred * out_w
            dh[h <= 0] = 0

            W_grad = np.outer(conv_out.ravel(), dh)
            b_grad = dh

            W -= lr * W_grad
            b -= lr * b_grad

        print(f"Epoch {epoch+1}, loss: {total_loss / n_samples:.4f}")


if __name__ == "__main__":
    main()
