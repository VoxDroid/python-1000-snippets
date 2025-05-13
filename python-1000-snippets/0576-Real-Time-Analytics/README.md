# Real-Time Analytics

## Description
This snippet demonstrates real-time data aggregation using a sliding window.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    data = pd.Series([1, 2, 3, 4])
    window = data.rolling(window=2).mean()
    print("Real-time averages:", window.tolist())
except ImportError:
    print("Mock Output: Real-time averages: [nan, 1.5, 2.5, 3.5]")
```

## Output
```
Mock Output: Real-time averages: [nan, 1.5, 2.5, 3.5]
```
*(Real output with `pandas`: `Real-time averages: [nan, 1.5, 2.5, 3.5]`)*

## Explanation
- **Real-Time Analytics**: Computes moving averages for streaming data.
- **Logic**: Applies a rolling window to calculate means.
- **Complexity**: O(n) for n data points.
- **Use Case**: Used in monitoring dashboards or IoT.
- **Best Practice**: Optimize window size; handle streaming; visualize results.