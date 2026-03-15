# 0292-Optical-Flow Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0292-Optical-Flow/SAMPLES/sample1.py`
  - `python python-1000-snippets/0292-Optical-Flow/SAMPLES/sample2.py`
  - `python python-1000-snippets/0292-Optical-Flow/SAMPLES/sample3.py`

## Concepts
- **Dense Optical Flow**: Compute motion for every pixel (e.g., Farneback).
- **Sparse Optical Flow**: Track a set of keypoints between frames (e.g., Lucas-Kanade).
- **Flow Visualization**: Use magnitude and angle to visualize motion fields.

## Tips
- Use grayscale frames as input to optical flow algorithms.
- Use `cv2.goodFeaturesToTrack` to select stable points for sparse tracking.
- Tune parameters like window size and pyramid levels for your motion scale.
