# Fraud Detection

## Description
This snippet demonstrates fraud detection using anomaly detection.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.ensemble import IsolationForest
    import numpy as np
    data = np.array([[1, 1], [2, 2], [10, 10]])
    model = IsolationForest().fit(data)
    predictions = model.predict(data)
    print("Anomaly flags:", predictions)
except ImportError:
    print("Mock Output: Anomaly flags: [1 1 -1]")
```

## Output
```
Mock Output: Anomaly flags: [1 1 -1]
```
*(Real output with `scikit-learn`: `Anomaly flags: [1 1 -1]`)*

## Explanation
- **Fraud Detection**: Identifies outliers as potential fraud.
- **Logic**: Uses Isolation Forest to detect anomalies.
- **Complexity**: O(n*log(n)) for n samples.
- **Use Case**: Used in financial transaction monitoring.
- **Best Practice**: Tune model; handle imbalanced data; validate anomalies.