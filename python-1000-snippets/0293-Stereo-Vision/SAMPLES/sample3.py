# sample3.py
# Compare StereoBM and StereoSGBM disparity computation on a synthetic stereo pair.

import cv2
import numpy as np


def create_stereo_pair(disparity):
    rng = np.random.default_rng(0)
    base = rng.integers(0, 256, size=(240, 320), dtype=np.uint8)
    base = cv2.GaussianBlur(base, (7, 7), sigmaX=1.5)
    left = base.copy()
    right = np.roll(base, -disparity, axis=1)
    right[:, -disparity:] = 0
    return left, right


if __name__ == '__main__':
    left, right = create_stereo_pair(disparity=20)

    bm = cv2.StereoBM_create(numDisparities=64, blockSize=15)
    disp_bm = bm.compute(left, right).astype(np.float32) / 16.0

    sgbm = cv2.StereoSGBM_create(
        minDisparity=0,
        numDisparities=64,
        blockSize=5,
        P1=8 * 3 * 5 ** 2,
        P2=32 * 3 * 5 ** 2,
        disp12MaxDiff=1,
        uniquenessRatio=15,
        speckleWindowSize=50,
        speckleRange=2,
    )
    disp_sgbm = sgbm.compute(left, right).astype(np.float32) / 16.0

    print('BM mean disparity:', float(np.mean(np.clip(disp_bm, 0, 64))))
    print('SGBM mean disparity:', float(np.mean(np.clip(disp_sgbm, 0, 64))))
