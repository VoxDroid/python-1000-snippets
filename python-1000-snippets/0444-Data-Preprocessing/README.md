# Data Preprocessing

## Description
This snippet demonstrates data preprocessing using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.preprocessing import StandardScaler
    import numpy as np
    data = np.array([[1], [2], [3]])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    print("Data scaled")
except ImportError:
    print("Mock Output: Data scaled")
```

## Output
```
Mock Output: Data scaled
```
*(Real output with `scikit-learn`: `Data scaled`)*

## Explanation
- **Data Preprocessing**: Scales data to zero mean and unit variance.
- **Logic**: Applies `StandardScaler` to normalize data.
- **Complexity**: O(n) for n samples.
- **Use Case**: Used to prepare data for ML models.
- **Best Practice**: Fit scaler on training data; handle outliers; test scaling.