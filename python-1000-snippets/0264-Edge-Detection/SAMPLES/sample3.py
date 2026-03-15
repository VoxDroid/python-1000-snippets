# sample3.py
# Overlay detected Canny edges on a color image.

import cv2
import numpy as np


if __name__ == '__main__':
    # Create a color gradient image
    img = np.zeros((120, 160, 3), dtype=np.uint8)
    for x in range(img.shape[1]):
        img[:, x, 0] = int(255 * x / img.shape[1])
    for y in range(img.shape[0]):
        img[y, :, 1] = int(255 * y / img.shape[0])

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    overlay = img.copy()
    overlay[edges != 0] = (0, 255, 255)  # highlight edges in yellow

    cv2.imwrite('edges_overlay.png', overlay)
    print('Saved edge overlay image to edges_overlay.png')
