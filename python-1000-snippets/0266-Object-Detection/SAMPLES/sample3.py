# sample3.py
# Detect objects using template matching to find a known pattern.

import cv2
import numpy as np


if __name__ == '__main__':
    # Create a simple template and a larger scene containing it.
    template = np.zeros((60, 60, 3), dtype=np.uint8)
    cv2.circle(template, (30, 30), 20, (0, 0, 255), -1)

    scene = np.zeros((240, 320, 3), dtype=np.uint8)
    scene[50:110, 80:140] = template
    scene[140:200, 180:240] = template

    gray_scene = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(gray_scene, gray_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    out = scene.copy()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(out, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

    out_path = 'object_detection_template.png'
    cv2.imwrite(out_path, out)
    print('Template matches found:', len(loc[0]), '-> output saved to', out_path)
