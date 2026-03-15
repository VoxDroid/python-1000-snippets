# sample2.py
# Detect circles in a synthetic image using Hough Circle Transform.

import cv2
import numpy as np


if __name__ == '__main__':
    img = np.zeros((300, 300), dtype=np.uint8)
    # Draw some circles
    cv2.circle(img, (80, 150), 40, 255, -1)
    cv2.circle(img, (220, 120), 30, 255, -1)
    cv2.circle(img, (200, 220), 20, 255, -1)

    img_blur = cv2.GaussianBlur(img, (9, 9), 2)
    circles = cv2.HoughCircles(
        img_blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=40,
        param1=50,
        param2=30,
        minRadius=10,
        maxRadius=60,
    )

    if circles is not None:
        circles = np.round(circles[0, :]).astype(int)
        print('Detected circles:', len(circles))
        for (x, y, r) in circles:
            print(f'  center=({x},{y}), radius={r}')
    else:
        print('No circles detected')
