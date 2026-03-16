# sample1.py
# Compute stereo disparity map from a simple synthetic stereo pair.

import cv2
import numpy as np


def create_stereo_pair(disparity):
    # Create a textured base image (gradient + random noise + shapes)
    base = np.tile(np.linspace(0, 255, 320, dtype=np.uint8), (240, 1))
    noise = (np.random.rand(240, 320) * 50).astype(np.uint8)
    base = cv2.add(base, noise)
    cv2.circle(base, (160, 120), 40, 255, 2)
    cv2.line(base, (0, 0), (319, 239), 128, 1)

    # Left image is base, right image is shifted to the right by `disparity` pixels
    left = base.copy()
    right = np.roll(base, -disparity, axis=1)
    # Fill the hole on the right image (leftmost region) with zeros
    right[:, -disparity:] = 0
    return left, right


if __name__ == '__main__':
    left, right = create_stereo_pair(disparity=16)

    stereo = cv2.StereoBM_create(numDisparities=64, blockSize=15)
    disp = stereo.compute(left, right).astype(np.float32) / 16.0

    # Disparity values might contain negatives; clip to valid range
    disp_valid = np.clip(disp, 0, 64)
    mean_disp = float(np.mean(disp_valid))
    max_disp = float(np.max(disp_valid))

    print(f"Mean disparity: {mean_disp:.2f}, max disparity: {max_disp:.2f}")
