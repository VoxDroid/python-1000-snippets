# Image Segmentation

## Description
This snippet demonstrates basic image segmentation techniques using NumPy and scikit-learn.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample2.py`)
```
Image shape: (100, 150)
Cluster centers: [209.83, 35.0, 115.35]
Segment label counts:
  label=0: 5318 pixels
  label=1: 6441 pixels
  label=2: 3241 pixels
```

## Explanation
- **Image Segmentation**: Partition an image into regions or clusters.
- **sample1.py**: Simple threshold-based segmentation on a synthetic image.
- **sample2.py**: KMeans clustering on pixel intensity values to segment regions.
- **sample3.py**: Connected component labeling on a binary mask.
- **Best Practice**: Choose segmentation method based on data, and visualize results to validate.
