# Object Detection

## Description
This snippet demonstrates simple object detection techniques using OpenCV.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — detects red objects via HSV color thresholding and draws bounding boxes.
- `sample2.py` — detects simple geometric shapes (circle, rectangle) using contour analysis.
- `sample3.py` — finds a template pattern in a scene using template matching.

Run a sample with:

```bash
python python-1000-snippets/0266-Object-Detection/SAMPLES/sample1.py
```

## Output
Each sample saves an image showing detections and prints a summary count.

## Notes
- These examples use simple heuristics rather than deep learning models.
- For real-world object detection, use pre-trained models (e.g., YOLO, SSD) with OpenCV DNN.
