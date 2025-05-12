# Anomaly Detection

## Description
This snippet demonstrates anomaly detection using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.ensemble import IsolationForest
    import numpy as np
    data = np.array([[1], [2], [100]])
    model = IsolationForest(contamination=0.1)
    predictions = model.fit_predict(data)
    print("Anomalies:", predictions)
except ImportError:
    print("Mock Output: Anomalies: [1 1 -1]")
```

## Output
```
Mock Output: Anomalies: [1 1 -1]
```
*(Real output with `scikit-learn`: `Anomalies: <array of labels>`)*

## Explanation
- **Anomaly Detection**: Identifies outliers using Isolation Forest.
- **Logic**: Fits a model to detect anomalies in a small dataset.
- **Complexity**: O(n log n) for n samples.
- **Use Case**: Used for fraud detection or network monitoring.
- **Best Practice**: Tune contamination; preprocess data; validate anomalies.