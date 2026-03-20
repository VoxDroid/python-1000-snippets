# Dynamic Time Warping

## Description
This snippet demonstrates Dynamic Time Warping (DTW) distance computation and simple uses in time-series comparison.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
DTW distance: 0.0
Warping path (first 10): [...]
Aligned pairs (first 5):
  x[0]=1.0 vs y[0]=0.0
  ...
```

## Explanation
- **Dynamic Time Warping**: Computes a distance between two sequences by allowing non-linear alignment in time.
- **sample1.py**: Computes DTW distance between two sequences and reports the warping path.
- **sample2.py**: Uses DTW to classify a query series against template series.
- **sample3.py**: Shows a simple approach to compute a centroid/average of multiple time series (using alignment).
- **Best Practice**: Normalize series, constrain warping window for performance, and validate with domain knowledge.
