# Face Detection Cheatsheet

## Key Concepts
- Haar cascade classifiers are trained detectors for specific object types (e.g., frontal faces).
- Detection is done on grayscale images with `detectMultiScale()`.
- `minNeighbors` adjusts how strict detections must be (higher means fewer false positives).

## Running Samples
```bash
python python-1000-snippets/0265-Face-Detection/SAMPLES/sample1.py
python python-1000-snippets/0265-Face-Detection/SAMPLES/sample2.py
python python-1000-snippets/0265-Face-Detection/SAMPLES/sample3.py
```

## Tips
- If you have a real image, place it as `test_face.jpg` next to the script to use it.
- Use `cv2.CascadeClassifier(cv2.data.haarcascades + '<cascade>.xml')` to load built-in cascades.
- Adjust `scaleFactor` and `minNeighbors` to tune detection sensitivity.
