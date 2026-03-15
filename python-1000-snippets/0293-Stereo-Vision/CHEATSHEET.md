# 0293-Stereo-Vision Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0293-Stereo-Vision/SAMPLES/sample1.py`
  - `python python-1000-snippets/0293-Stereo-Vision/SAMPLES/sample2.py`
  - `python python-1000-snippets/0293-Stereo-Vision/SAMPLES/sample3.py`

## Concepts
- **Disparity Map**: Difference in pixel coordinates between left/right images.
- **Depth Estimation**: Depth = (focal length * baseline) / disparity.
- **Stereo Algorithms**: `StereoBM` is fast but less accurate; `StereoSGBM` is more robust.

## Tips
- Ensure stereo images are rectified (epipolar lines aligned) for correct disparity.
- Tune `numDisparities` and `blockSize` based on expected disparity range and texture.
- Use median filtering on disparity maps to reduce noise.
