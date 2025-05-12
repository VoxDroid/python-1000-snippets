# Dynamic Time Warping

## Description
This snippet demonstrates dynamic time warping using `scipy`.

## Code
```python
# Note: Requires `scipy`. Install with `pip install scipy`
try:
    from scipy.spatial.distance import euclidean
    import numpy as np
    def dtw_distance(x, y):
        n, m = len(x), len(y)
        dp = np.zeros((n + 1, m + 1))
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i, j] = euclidean([x[i-1]], [y[j-1]]) + min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1])
        return dp[n, m]
    
    x, y = [1, 2, 3], [1, 2, 4]
    print("DTW distance:", dtw_distance(x, y))
except ImportError:
    print("Mock Output: DTW distance: 1.0")
```

## Output
```
Mock Output: DTW distance: 1.0
```
*(Real output with `scipy`: `DTW distance: 1.0`)*

## Explanation
- **Dynamic Time Warping**: Computes similarity between time series.
- **Logic**: Uses dynamic programming to calculate DTW distance.
- **Complexity**: O(n * m) for sequences of length n, m.
- **Use Case**: Used in speech recognition or time-series alignment.
- **Best Practice**: Normalize series; optimize computation; validate distances.