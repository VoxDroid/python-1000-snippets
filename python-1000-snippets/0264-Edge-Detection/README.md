# Edge Detection

## Description
This snippet demonstrates edge detection techniques using OpenCV.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — Canny edge detection on a synthetic image.
- `sample2.py` — Sobel gradient magnitude for edge detection.
- `sample3.py` — overlays Canny edges on a color image.

Run a sample with:

```bash
python python-1000-snippets/0264-Edge-Detection/SAMPLES/sample1.py
```

## Output
Each sample writes an output image file (`edges_*.png`) and prints a summary line.

## Notes
- Edge detectors (Canny, Sobel) are common preprocessing steps in computer vision.
- Tuning thresholds (e.g., Canny low/high) controls sensitivity to edges.
- Overlaying edges on the original image can help visualize results.
