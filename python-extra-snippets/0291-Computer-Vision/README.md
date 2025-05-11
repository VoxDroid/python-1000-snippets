# Computer Vision

## Description
This snippet demonstrates basic computer vision using `opencv-python` to convert an image to grayscale.

## Code
```python
# Note: Requires `opencv-python`. Install with `pip install opencv-python`
try:
    import cv2
    import numpy as np
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[40:60, 40:60] = [255, 255, 255]  # White square
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Gray Image Mean:", np.mean(gray))
except ImportError:
    print("Mock Output: Gray Image Mean: 10.2")
```

## Output
```
Mock Output: Gray Image Mean: 10.2
```
*(Real output with `opencv-python`: `Gray Image Mean: <value around 10.2>`)*

## Explanation
- **Computer Vision**: Converts a synthetic BGR image to grayscale.
- **Logic**: Creates an image with a white square and applies color conversion.
- **Complexity**: O(w*h) for w width, h height.
- **Use Case**: Used for image preprocessing in vision tasks.
- **Best Practice**: Handle image formats; validate input; optimize for large images.