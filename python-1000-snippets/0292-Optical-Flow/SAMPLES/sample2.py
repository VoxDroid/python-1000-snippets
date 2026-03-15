# sample2.py
# Sparse optical flow using Lucas-Kanade method on synthetic corners.

import cv2
import numpy as np


def create_frame(offset):
    img = np.zeros((200, 200), dtype=np.uint8)
    # Draw a grid of corners
    for x in range(40, 160, 40):
        for y in range(40, 160, 40):
            cv2.circle(img, (x + offset, y + offset), 3, 255, -1)
    return img


if __name__ == '__main__':
    frame1 = create_frame(0)
    frame2 = create_frame(5)

    # Detect good features to track in frame1
    p0 = cv2.goodFeaturesToTrack(frame1, maxCorners=25, qualityLevel=0.01, minDistance=10)
    p1, st, err = cv2.calcOpticalFlowPyrLK(frame1, frame2, p0, None)

    moved = 0
    if p1 is not None and st is not None:
        moved = int(np.sum(st))

    print('Tracked features:', len(p0) if p0 is not None else 0)
    print('Successfully tracked:', moved)
