# sample1.py
# Run face detection on a generated simplistic "face" image using OpenCV Haar cascades.

import cv2
import numpy as np


if __name__ == '__main__':
    # Draw a simple face-like pattern
    img = np.zeros((240, 240, 3), dtype=np.uint8)
    cv2.circle(img, (120, 120), 80, (255, 255, 255), -1)  # face
    cv2.circle(img, (90, 100), 10, (0, 0, 0), -1)  # left eye
    cv2.circle(img, (150, 100), 10, (0, 0, 0), -1)  # right eye
    cv2.ellipse(img, (120, 150), (40, 20), 0, 0, 180, (0, 0, 0), 5)  # smile

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    out_path = 'face_detection_output.png'
    cv2.imwrite(out_path, img)
    print('Detected faces:', len(faces), '-> output saved to', out_path)
