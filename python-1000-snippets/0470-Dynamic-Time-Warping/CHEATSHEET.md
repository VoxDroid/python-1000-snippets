# 0470-Dynamic-Time-Warping Cheatsheet

## Quick Tips
- DTW allows flexible alignment of two sequences by warping the time dimension.
- Complexity is O(n*m) for lengths n and m; constrain the warping window for longer sequences.
- Normalize sequences before comparison to reduce scale effects.

## Running examples
- `python SAMPLES/sample1.py` — compute DTW distance and warping path.
- `python SAMPLES/sample2.py` — classify a query series against templates.
- `python SAMPLES/sample3.py` — compute an average series (centroid) from multiple sequences.
