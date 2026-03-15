# 0294-3D-Reconstruction Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0294-3D-Reconstruction/SAMPLES/sample1.py`
  - `python python-1000-snippets/0294-3D-Reconstruction/SAMPLES/sample2.py`
  - `python python-1000-snippets/0294-3D-Reconstruction/SAMPLES/sample3.py`

## Concepts
- **Triangulation**: Recover 3D points from corresponding 2D points in multiple views.
- **Projection matrices**: Combine camera intrinsics and extrinsics into a 3x4 matrix.
- **Plane fitting**: Use SVD to fit a plane to a point cloud in least-squares sense.

## Tips
- Ensure correspondences are accurate; errors propagate into 3D reconstruction.
- For stereo, calibrate cameras to obtain accurate projection matrices.
- Use robust methods (RANSAC) when fitting models to noisy data.
