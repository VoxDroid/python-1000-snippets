# sample1.py
# Dense optical flow (Farneback) on two synthetic frames.

import cv2
import numpy as np


def create_frame(offset):
    img = np.zeros((200, 200), dtype=np.uint8)
    cv2.rectangle(img, (50 + offset, 50), (150 + offset, 150), 255, -1)
    return img


if __name__ == '__main__':
    frame1 = create_frame(0)
    frame2 = create_frame(5)

    flow = cv2.calcOpticalFlowFarneback(
        frame1,
        frame2,
        None,
        pyr_scale=0.5,
        levels=3,
        winsize=15,
        iterations=3,
        poly_n=5,
        poly_sigma=1.2,
        flags=0,
    )

    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    avg_mag = float(np.mean(mag))

    print(f"Average flow magnitude: {avg_mag:.3f}")
