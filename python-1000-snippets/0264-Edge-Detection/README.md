# Edge Detection

## Description
This snippet demonstrates edge detection using `opencv-python`.

## Code
```python
# Note: Requires `opencv-python`. Install with `pip install opencv-python`
try:
    import cv2
    import numpy as np
    img = np.zeros((100, 100), dtype=np.uint8)
    img[40:60, 40:60] = 255  # White square
    edges = cv2.Canny(img, 100, 200)
    print("Edges detected:", np.sum(edges) > 0)
except ImportError:
    print("Mock Output: Edges detected: True")
```

## Output
```
Mock Output: Edges detected: True
```
*(Real output with `opencv-python`: `Edges detected: True`)*

## Explanation
- **Edge Detection**: Uses Canny edge detection on a synthetic image.
- **Logic**: Creates a black image with a white square and detects edges.
- **Complexity**: O(w*h) for w width, h height.
- **Use Case**: Used for feature extraction in computer vision.
- **Best Practice**: Tune thresholds; preprocess images; handle noise.