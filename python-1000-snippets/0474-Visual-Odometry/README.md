# Visual Odometry

## Description
This snippet demonstrates simplified visual odometry techniques using NumPy-only implementations (no OpenCV dependency).

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
True shift: (5, -3)
Estimated shift: (5.0, -3.0)
```

## Explanation
- **Visual Odometry**: Estimates camera motion from image sequences.
- **sample1.py**: Uses phase correlation to estimate translation between two images.
- **sample2.py**: Estimates a rigid transform between matched keypoints (rotation + translation).
- **sample3.py**: Computes a simple Lucas-Kanade optical flow by solving for local motion vectors.
- **Best Practice**: Use robust feature matches, handle outliers, and validate motion estimates on real data.
