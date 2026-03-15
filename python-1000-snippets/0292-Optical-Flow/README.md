# Optical Flow

## Description
This snippet demonstrates optical flow techniques using OpenCV.

## Samples
- `SAMPLES/sample1.py`: Dense optical flow (Farneback) on synthetic moving shapes.
- `SAMPLES/sample2.py`: Sparse optical flow (Lucas-Kanade) tracking corner features.
- `SAMPLES/sample3.py`: Compute average motion vector from dense optical flow.

## Running
```bash
python python-1000-snippets/0292-Optical-Flow/SAMPLES/sample1.py
python python-1000-snippets/0292-Optical-Flow/SAMPLES/sample2.py
python python-1000-snippets/0292-Optical-Flow/SAMPLES/sample3.py
```

## Notes
- These examples use synthetic frames; replace with real video frames for real use.
- Use `cv2.calcOpticalFlowFarneback()` for dense flow and `cv2.calcOpticalFlowPyrLK()` for sparse tracking.
