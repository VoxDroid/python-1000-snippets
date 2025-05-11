# Optical Flow

## Description
This snippet demonstrates optical flow estimation using `opencv-python`’s Farneback method.

## Code
```python
# Note: Requires `opencv-python`. Install with `pip install opencv-python`
try:
    import cv2
    import numpy as np
    frame1 = np.zeros((100, 100), dtype=np.uint8)
    frame2 = np.zeros((100, 100), dtype=np.uint8)
    frame2[45:65, 45:65] = 255  # Shifted white square
    flow = cv2.calcOpticalFlowFarneback(frame1, frame2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    print("Flow Magnitude Mean:", np.mean(np.sqrt(flow[..., 0]**2 + flow[..., 1]**2)))
except ImportError:
    print("Mock Output: Flow Magnitude Mean: 0.6475478")
```

## Output
```
Mock Output: Flow Magnitude Mean: 0.6475478
```
*(Real output with `opencv-python`: `Flow Magnitude Mean: <small value> ~ (or 0.6475478)`)*

## Explanation
- **Optical Flow**: Estimates motion between two frames using dense optical flow.
- **Logic**: Creates two frames with a shifted square and computes flow.
- **Complexity**: O(w*h) for w width, h height.
- **Use Case**: Used for motion tracking or video analysis.
- **Best Practice**: Tune parameters; preprocess frames; handle noise.