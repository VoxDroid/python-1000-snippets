# 0462-Anomaly-Detection Cheatsheet

## Quick Tips
- Anomaly detection is typically unsupervised: models learn what "normal" looks like and flag deviations.
- The `contamination` parameter controls the proportion of points flagged as anomalies.
- Always validate on a dataset where anomalies are known (if available).

## Running examples
- `python SAMPLES/sample1.py` — Isolation Forest.
- `python SAMPLES/sample2.py` — Local Outlier Factor.
- `python SAMPLES/sample3.py` — One-Class SVM.
