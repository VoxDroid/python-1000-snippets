# 0474-Visual-Odometry Cheatsheet

## Quick Tips
- Phase correlation finds translation between images by comparing their Fourier phases.
- A rigid transform (rotation + translation) can be estimated from matched keypoints via least squares.
- Lucas-Kanade optical flow solves for local motion using image gradients and least squares.

## Running examples
- `python SAMPLES/sample1.py` — estimate translation using phase correlation.
- `python SAMPLES/sample2.py` — estimate a rigid transform from point correspondences.
- `python SAMPLES/sample3.py` — compute a simple dense optical flow field.
