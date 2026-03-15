# sample3.py
# Demonstrate thresholding and contour detection in a synthetic image.

import cv2
import numpy as np


if __name__ == '__main__':
    # Create image with random blobs
    img = np.zeros((240, 240), dtype=np.uint8)
    rng = np.random.default_rng(0)
    for _ in range(15):
        center = tuple(rng.integers(20, 220, size=2))
        radius = int(rng.integers(10, 25))
        cv2.circle(img, center, radius, 255, -1)

    blurred = cv2.GaussianBlur(img, (7, 7), 0)
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print('Total contours found:', len(contours))
    if contours:
        areas = [cv2.contourArea(c) for c in contours]
        print('Largest contour area:', max(areas))

    # Draw contours on an image (optional visualization)
    # output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # cv2.drawContours(output, contours, -1, (0, 255, 0), 2)
    # cv2.imshow('contours', output)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
