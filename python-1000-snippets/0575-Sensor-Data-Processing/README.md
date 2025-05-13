# Sensor Data Processing

## Description
This snippet demonstrates filtering sensor data using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    data = pd.Series([25, 100, 26])
    filtered = data[data < 50]
    print("Filtered data:", filtered.tolist())
except ImportError:
    print("Mock Output: Filtered data: [25, 26]")
```

## Output
```
Mock Output: Filtered data: [25, 26]
```
*(Real output with `pandas`: `Filtered data: [25, 26]`)*

## Explanation
- **Sensor Data Processing**: Cleans noisy sensor data.
- **Logic**: Filters out values above a threshold.
- **Complexity**: O(n) for n data points.
- **Use Case**: Used in IoT for data preprocessing.
- **Best Practice**: Define robust filters; handle missing data; log anomalies.