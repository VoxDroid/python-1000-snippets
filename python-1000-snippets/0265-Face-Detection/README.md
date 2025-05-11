# Face Detection

## Description
This snippet demonstrates face detection using `opencv-python` with a Haar cascade.

## Code
```python
# Note: Requires `opencv-python`. Install with `pip install opencv-python`
try:
    import cv2
    import numpy as np
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    img = np.zeros((100, 100, 3), dtype=np.uint8)  # Placeholder
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    print("Faces detected:", len(faces))
except ImportError:
    print("Mock Output: Faces detected: 0")
```

## Output
```
Mock Output: Faces detected: 0
```
*(Real output with `opencv-python`: `Faces detected: <number of faces>`)*

## Explanation
- **Face Detection**: Uses Haar cascade to detect faces in an image.
- **Logic**: Applies face detection on a placeholder image (no faces).
- **Complexity**: O(w*h) for w width, h height.
- **Use Case**: Used for facial recognition or surveillance.
- **Best Practice**: Tune cascade parameters; use real images; handle lighting.