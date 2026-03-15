# sample2.py
# Detect edges using Sobel derivatives.

import cv2
import numpy as np


if __name__ == '__main__':
    img = np.zeros((120, 160), dtype=np.uint8)
    cv2.circle(img, (80, 60), 40, 255, -1)

    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    mag = np.sqrt(sobelx**2 + sobely**2)
    mag = np.uint8(np.clip(mag, 0, 255))

    cv2.imwrite('edges_sobel.png', mag)
    print('Saved Sobel magnitude image to edges_sobel.png')
