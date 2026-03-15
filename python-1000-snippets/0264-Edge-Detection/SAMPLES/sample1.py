# sample1.py
# Detect edges using Canny edge detector on a synthetic image.

import cv2
import numpy as np


if __name__ == '__main__':
    # Create a black image with a white rectangle
    img = np.zeros((120, 160), dtype=np.uint8)
    cv2.rectangle(img, (30, 30), (130, 90), 255, -1)

    edges = cv2.Canny(img, 50, 150)
    cv2.imwrite('edges_canny.png', edges)

    print('Saved Canny edge image to edges_canny.png (nonzero pixels:', int(np.count_nonzero(edges)), ')')
