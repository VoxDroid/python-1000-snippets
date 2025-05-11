# Time Series Analysis

## Description
This snippet demonstrates time series analysis using `pandas` to compute a moving average.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    import numpy as np
    ts = pd.Series(np.random.random(100))
    ma = ts.rolling(window=5).mean()
    print("Moving Average (first 5):", ma[:5].values)
except ImportError:
    print("Mock Output: Moving Average (first 5): [nan, nan, nan, nan, 0.5]")
```

## Output
```
Mock Output: Moving Average (first 5): [nan, nan, nan, nan, 0.5]
```
*(Real output with `pandas`: `Moving Average (first 5): [nan, nan, nan, nan, <value>]`)*

## Explanation
- **Time Series Analysis**: Computes a moving average on a random time series.
- **Logic**: Uses `pandas` to apply a 5-period rolling mean.
- **Complexity**: O(n) for n data points.
- **Use Case**: Used for trend analysis or smoothing time series.
- **Best Practice**: Handle missing data; tune window size; validate trends.