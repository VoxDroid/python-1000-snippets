# sample1.py
# Detect red objects in an image using color thresholding (HSV) with OpenCV.

import cv2
import numpy as np


if __name__ == '__main__':
    # Create an image with red and blue circles
    img = np.zeros((240, 320, 3), dtype=np.uint8)
    cv2.circle(img, (80, 120), 50, (0, 0, 255), -1)  # red circle
    cv2.circle(img, (240, 120), 50, (255, 0, 0), -1)  # blue circle

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Define red range (two ranges because red wraps Hue=0)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    out = img.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(out, (x, y), (x + w, y + h), (0, 255, 0), 2)

    out_path = 'object_detection_red.png'
    cv2.imwrite(out_path, out)
    print('Detected', len(contours), 'red object(s) -> output saved to', out_path)
