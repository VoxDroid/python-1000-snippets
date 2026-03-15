# sample3.py
# Compare face detection results across different scaling factors.

import cv2
import numpy as np


def make_test_image():
    img = np.zeros((240, 240, 3), dtype=np.uint8)
    cv2.circle(img, (120, 120), 80, (255, 255, 255), -1)
    cv2.circle(img, (90, 100), 10, (0, 0, 0), -1)
    cv2.circle(img, (150, 100), 10, (0, 0, 0), -1)
    cv2.ellipse(img, (120, 150), (40, 20), 0, 0, 180, (0, 0, 0), 5)
    return img


if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = make_test_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    results = []
    for min_neighbors in [3, 5, 8]:
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=min_neighbors)
        results.append((min_neighbors, len(faces)))

    print('Face detection results (minNeighbors -> count):', results)
