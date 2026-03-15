# sample2.py
# Load an image (or generate one) and detect faces using OpenCV's Haar cascade.

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

    # Try to load an optional image file; if not found, generate a test image.
    try:
        img = cv2.imread('test_face.jpg')
        if img is None:
            raise FileNotFoundError
        print('Loaded test_face.jpg')
    except Exception:
        img = make_test_image()
        print('Using generated test image')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    out_path = 'face_detection_result.png'
    cv2.imwrite(out_path, img)
    print('Detected faces:', len(faces), '-> output saved to', out_path)
