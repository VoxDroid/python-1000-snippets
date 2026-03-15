# sample3.py
# Estimate the average motion vector between two frames via dense optical flow.

import cv2
import numpy as np


def create_moving_frame(shift):
    img = np.zeros((150, 150), dtype=np.uint8)
    cv2.circle(img, (75 + shift, 75), 30, 255, -1)
    return img


if __name__ == '__main__':
    frame1 = create_moving_frame(0)
    frame2 = create_moving_frame(3)

    flow = cv2.calcOpticalFlowFarneback(
        frame1,
        frame2,
        None,
        pyr_scale=0.5,
        levels=3,
        winsize=13,
        iterations=3,
        poly_n=5,
        poly_sigma=1.1,
        flags=0,
    )

    # Average flow vector
    avg_flow = np.mean(flow.reshape(-1, 2), axis=0)
    print(f"Average flow vector: dx={avg_flow[0]:.3f}, dy={avg_flow[1]:.3f}")
