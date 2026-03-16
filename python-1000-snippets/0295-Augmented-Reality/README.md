# Augmented Reality

## Description
This snippet demonstrates simple augmented reality techniques using OpenCV.

## Samples
- `SAMPLES/sample1.py`: Detect a square marker and overlay a virtual cube.
- `SAMPLES/sample2.py`: Feature matching (ORB + BFMatcher) between two views to support AR alignment.
- `SAMPLES/sample3.py`: Warp a texture onto a planar surface using a homography.

## Running
```bash
python python-1000-snippets/0295-Augmented-Reality/SAMPLES/sample1.py
python python-1000-snippets/0295-Augmented-Reality/SAMPLES/sample2.py
python python-1000-snippets/0295-Augmented-Reality/SAMPLES/sample3.py
```

## Notes
- These examples create synthetic images and do not require camera input.
- For real AR, use camera calibration and marker-based pose estimation.
