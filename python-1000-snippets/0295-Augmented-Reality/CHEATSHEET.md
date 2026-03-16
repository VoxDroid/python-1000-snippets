# 0295-Augmented-Reality Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0295-Augmented-Reality/SAMPLES/sample1.py`
  - `python python-1000-snippets/0295-Augmented-Reality/SAMPLES/sample2.py`
  - `python python-1000-snippets/0295-Augmented-Reality/SAMPLES/sample3.py`

## Concepts
- **Marker Detection**: Detect markers or planar shapes to establish reference frames (e.g., contour-based squares).
- **Feature Matching**: Use ORB (or other descriptors) to match keypoints between frames for alignment.
- **Homography**: Warp a texture onto a planar surface using a 3x3 transform.
- **Overlay Rendering**: Draw virtual geometry aligned with image markers or matched keypoints.

## Tips
- Use camera calibration for accurate pose estimation in real AR setups.
- If working with live video, process each frame in a loop and overlay graphics in real-time.
- Use a stronger marker pattern (e.g., ArUco) for robustness to lighting and perspective changes.
