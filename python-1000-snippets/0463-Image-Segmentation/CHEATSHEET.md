# 0463-Image-Segmentation Cheatsheet

## Quick Tips
- Segmenting an image can be as simple as thresholding intensities for binary masks.
- Clustering (e.g., KMeans) works well when pixel intensities or colors form distinct groups.
- Connected component labeling can identify separate regions in a binary mask.

## Running examples
- `python SAMPLES/sample1.py` — threshold-based segmentation.
- `python SAMPLES/sample2.py` — k-means clustering on pixel intensities.
- `python SAMPLES/sample3.py` — connected components labeling.
