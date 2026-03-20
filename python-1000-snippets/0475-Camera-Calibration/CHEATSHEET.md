# 0475-Camera-Calibration Cheatsheet

## Quick Tips
- DLT (Direct Linear Transform) solves for a projection matrix from 3D-2D point correspondences.
- Radial distortion can be approximated with a few coefficients (k1, k2) and corrected iteratively.
- Intrinsic parameters (focal length, principal point) are embedded in the camera matrix K.

## Running examples
- `python SAMPLES/sample1.py` — estimate a projection matrix from synthetic correspondences.
- `python SAMPLES/sample2.py` — apply and remove radial distortion on image points.
- `python SAMPLES/sample3.py` — project 3D points using a known camera intrinsics matrix.
