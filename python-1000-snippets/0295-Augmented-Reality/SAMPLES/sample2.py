# sample2.py
# Feature matching (ORB + BFMatcher) between two synthetic views to simulate AR alignment.

import cv2
import numpy as np


def create_scene(shift_x=0, shift_y=0):
    img = np.zeros((300, 300), dtype=np.uint8)
    # Draw a simple pattern with multiple corners
    cv2.rectangle(img, (80 + shift_x, 80 + shift_y), (220 + shift_x, 220 + shift_y), 255, -1)
    cv2.circle(img, (150 + shift_x, 150 + shift_y), 40, 0, -1)
    cv2.line(img, (50 + shift_x, 250 + shift_y), (250 + shift_x, 50 + shift_y), 127, 2)
    return img


if __name__ == '__main__':
    img1 = create_scene(shift_x=0, shift_y=0)
    img2 = create_scene(shift_x=10, shift_y=5)

    orb = cv2.ORB_create(nfeatures=200)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda m: m.distance)

    print('Keypoints img1:', len(kp1))
    print('Keypoints img2:', len(kp2))
    print('Matches found:', len(matches))
    print('Top 5 match distances:', [m.distance for m in matches[:5]])

    # Optionally draw matches (uncomment if GUI is available)
    # out = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
    # cv2.imshow('Matches', out)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
