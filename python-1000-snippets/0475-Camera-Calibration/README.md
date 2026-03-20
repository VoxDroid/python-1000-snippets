# Camera Calibration

## Description
This snippet demonstrates camera calibration concepts using pure NumPy: estimating projection matrices, modeling radial distortion, and projecting 3D points into image space.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Estimated projection matrix (first 3 cols are K*R):
[[...]]
```

## Explanation
- **Camera Calibration**: Estimates how 3D points map to 2D image points.
- **sample1.py**: Uses DLT to estimate a projection matrix from 3D-2D correspondences.
- **sample2.py**: Demonstrates simple radial distortion/undistortion of image points.
- **sample3.py**: Projects 3D points to 2D image coordinates using a known intrinsics matrix.
- **Best Practice**: Collect multiple views, normalize data, and validate with held-out points.
