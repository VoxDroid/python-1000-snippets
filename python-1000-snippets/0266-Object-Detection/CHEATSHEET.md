# Object Detection Cheatsheet

## Key Concepts
- Color thresholding (HSV) can find objects with consistent color.
- Contour analysis allows identifying shapes based on polygon approximations.
- Template matching finds instances of a known pattern within a larger image.

## Running Samples
```bash
python python-1000-snippets/0266-Object-Detection/SAMPLES/sample1.py
python python-1000-snippets/0266-Object-Detection/SAMPLES/sample2.py
python python-1000-snippets/0266-Object-Detection/SAMPLES/sample3.py
```

## Tips
- Convert to HSV color space for robust color segmentation.
- Use `cv2.approxPolyDP()` to classify shapes by the number of polygon vertices.
- Use `cv2.matchTemplate()` with `cv2.TM_CCOEFF_NORMED` and threshold on the result.
