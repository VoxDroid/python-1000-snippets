# sample1.py
# Simple edge detection using OpenCV's Canny detector.

import cv2
import numpy as np


if __name__ == '__main__':
    # Create a synthetic image with simple shapes
    img = np.zeros((200, 200), dtype=np.uint8)
    cv2.rectangle(img, (20, 20), (180, 80), 255, -1)
    cv2.circle(img, (100, 140), 40, 255, -1)

    edges = cv2.Canny(img, threshold1=50, threshold2=150)
    edge_count = int(np.sum(edges > 0))

    print('Edge pixels detected:', edge_count)

    # Optionally show the image if running in an environment with GUI support
    # cv2.imshow('edges', edges)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
