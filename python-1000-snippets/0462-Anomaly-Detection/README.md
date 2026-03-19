# Anomaly Detection

## Description
This snippet demonstrates anomaly detection using scikit-learn's unsupervised outlier detectors.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Data: [1, 2, 2, 3, 3, 4, 100]
Anomaly labels: [1, 1, 1, 1, 1, 1, -1]
```

## Explanation
- **Anomaly Detection**: Finds observations that deviate from the majority of the data.
- **sample1.py**: Uses `IsolationForest` to detect a clear outlier.
- **sample2.py**: Uses `LocalOutlierFactor` (unsupervised clustering-based detector).
- **sample3.py**: Uses `OneClassSVM` as a novelty detector.
- **Best Practice**: Tune contamination/thresholds, validate on known anomalies, and scale features consistently.
