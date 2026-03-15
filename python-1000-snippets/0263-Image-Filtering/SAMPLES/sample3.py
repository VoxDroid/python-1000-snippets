# sample3.py
# Perform manual convolution with a custom kernel using numpy and Pillow.

import numpy as np
from PIL import Image


def convolve(image_arr, kernel):
    """Perform 2D convolution (valid) on grayscale image array."""
    k = np.array(kernel)
    kh, kw = k.shape
    h, w = image_arr.shape
    out = np.zeros((h - kh + 1, w - kw + 1), dtype=np.float32)
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i, j] = np.sum(image_arr[i:i+kh, j:j+kw] * k)
    # normalize to 0-255
    out = np.clip(out, 0, 255).astype(np.uint8)
    return out


if __name__ == '__main__':
    # Create a grayscale gradient image.
    img = Image.linear_gradient('L').resize((200, 120))
    arr = np.array(img)

    # Simple edge detection kernel (Sobel-like)
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    edges = convolve(arr, kernel)

    Image.fromarray(edges).save('filtered_edge_manual.png')
    print('Saved manually convolved edge image to filtered_edge_manual.png')
