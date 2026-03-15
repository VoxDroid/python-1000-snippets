# 3D Reconstruction

## Description
This snippet demonstrates basic 3D reconstruction techniques using OpenCV and NumPy.

## Samples
- `SAMPLES/sample1.py`: Triangulate a single 3D point from two camera views.
- `SAMPLES/sample2.py`: Triangulate multiple 3D points and compute reconstruction error.
- `SAMPLES/sample3.py`: Fit a plane to a point cloud using least-squares (SVD).

## Running
```bash
python python-1000-snippets/0294-3D-Reconstruction/SAMPLES/sample1.py
python python-1000-snippets/0294-3D-Reconstruction/SAMPLES/sample2.py
python python-1000-snippets/0294-3D-Reconstruction/SAMPLES/sample3.py
```

## Notes
- These examples use synthetic data with known geometry.
- Real-world reconstruction requires camera calibration and feature matching.
