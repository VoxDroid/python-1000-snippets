# Face Detection

## Description
This snippet demonstrates face detection using OpenCV's Haar cascade classifiers.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — generates a synthetic "face" pattern and runs Haar cascade detection.
- `sample2.py` — attempts to load `test_face.jpg` (optional) and falls back to a generated test image.
- `sample3.py` — compares detection results using different `minNeighbors` settings.

Run a sample with:

```bash
python python-1000-snippets/0265-Face-Detection/SAMPLES/sample1.py
```

## Output
Each sample prints detected face counts and writes an output image (or prints results) to disk.

## Notes
- Detection performance depends on image content and cascade parameters.
- Haar cascades work best on frontal faces; they are not robust to severe rotation.
- Use real photos to get meaningful detections; the generated image is for demonstration.
