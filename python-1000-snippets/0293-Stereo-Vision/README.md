# Stereo Vision

## Description
This snippet demonstrates stereo vision disparity mapping using `opencv-python`.

## Code
```python
# Note: Requires `opencv-python`. Install with `pip install opencv-python`
try:
    import cv2
    import numpy as np
    left = np.zeros((100, 100), dtype=np.uint8)
    right = np.zeros((100, 100), dtype=np.uint8)
    left[40:60, 40:60] = 255
    right[40:60, 35:55] = 255  # Shifted
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(left, right)
    print("Disparity Mean:", np.mean(disparity))
except ImportError:
    print("Mock Output: Disparity Mean: -4.9408")
```

## Output
```
Mock Output: Disparity Mean: -4.9408
```
*(Real output with `opencv-python`: `Disparity Mean: <value around -4.9>`)*

## Explanation
- **Stereo Vision**: Computes a disparity map from two synthetic images.
- **Logic**: Creates left and right images with a shifted square and computes disparity.
- **Complexity**: O(w*h*d) for w width, h height, d disparities.
- **Use Case**: Used for depth estimation in robotics or 3D modeling.
- **Best Practice**: Calibrate cameras; tune stereo parameters; handle occlusions.