# Edge Detection Cheatsheet

## Key Concepts
- **Canny**: multi-stage edge detector with hysteresis thresholding.
- **Sobel**: computes gradient along x and y, useful for edge magnitude.
- **Overlay**: highlight edges by blending with the original image.

## Running Samples
```bash
python python-1000-snippets/0264-Edge-Detection/SAMPLES/sample1.py
python python-1000-snippets/0264-Edge-Detection/SAMPLES/sample2.py
python python-1000-snippets/0264-Edge-Detection/SAMPLES/sample3.py
```

## Tips
- Adjust Canny thresholds (low/high) to control edge sensitivity.
- Use `cv2.Canny()` on grayscale images.
- Visualize edges by setting edge pixels to a bright color on a copy of the original image.
