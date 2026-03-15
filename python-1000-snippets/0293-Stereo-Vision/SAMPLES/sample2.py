# sample2.py
# Compute a depth estimate from a disparity map using a pinhole camera model.

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
    # Stereo parameters (example values)
    focal_length_px = 700.0
    baseline_m = 0.1

    left, right = create_stereo_pair(disparity=16)
    stereo = cv2.StereoBM_create(numDisparities=64, blockSize=15)
    disp = stereo.compute(left, right).astype(np.float32) / 16.0

    # Convert disparity to depth (avoid division by zero)
    disp_safe = np.where(disp <= 0, 1e-6, disp)
    depth = (focal_length_px * baseline_m) / disp_safe

    # Provide statistics for a valid region
    valid_depth = depth[(disp > 0) & (disp < 64)]
    if valid_depth.size:
        print(f"Depth mean (m): {float(np.mean(valid_depth)):.3f}")
        print(f"Depth std (m): {float(np.std(valid_depth)):.3f}")
    else:
        print("No valid depth values (disparity too small or invalid)")
