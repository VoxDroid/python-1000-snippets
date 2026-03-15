# 0291-Computer-Vision Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0291-Computer-Vision/SAMPLES/sample1.py`
  - `python python-1000-snippets/0291-Computer-Vision/SAMPLES/sample2.py`
  - `python python-1000-snippets/0291-Computer-Vision/SAMPLES/sample3.py`

## Concepts
- **Edge Detection**: Use Canny to find edges in images.
- **Hough Transforms**: Detect simple shapes (circles, lines) in edge maps.
- **Contour Detection**: Find and analyze connected components via contours.

## Tips
- Use `cv2.imshow()` for visualization when running locally with a display.
- Tune thresholds (Canny, Hough) for your object sizes and contrast levels.
- Use `cv2.findContours()` output to compute shape properties (area, perimeter).
