# sample2.py
# Detect simple geometric objects (circles and rectangles) using contour approximation.

import cv2
import numpy as np


if __name__ == '__main__':
    # Create an image with a rectangle and a circle
    img = np.zeros((240, 320, 3), dtype=np.uint8)
    cv2.rectangle(img, (40, 40), (140, 140), (0, 255, 0), -1)
    cv2.circle(img, (220, 120), 60, (255, 0, 0), -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    out = img.copy()
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        if len(approx) == 4:
            shape = 'rectangle'
            color = (0, 255, 0)
        else:
            shape = 'circle'
            color = (255, 0, 0)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(out, (x, y), (x + w, y + h), color, 2)
        cv2.putText(out, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    out_path = 'object_detection_shapes.png'
    cv2.imwrite(out_path, out)
    print('Detected', len(contours), 'objects -> output saved to', out_path)
