# Stream Processing Pipeline

## Description
This snippet demonstrates a simple stream processing setup using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    data = pd.DataFrame({"value": [1, 2, 3]})
    stream = data["value"].rolling(window=2).mean()
    print("Stream processed:", stream.tolist())
except ImportError:
    print("Mock Output: Stream processed: [nan, 1.5, 2.5]")
```

## Output
```
Mock Output: Stream processed: [nan, 1.5, 2.5]
```
*(Real output with `pandas`: `Stream processed: [nan, 1.5, 2.5]`)*

## Explanation
- **Stream Processing Pipeline**: Computes a rolling mean on a data stream.
- **Logic**: Applies a rolling window to a small dataset.
- **Complexity**: O(n) for n data points.
- **Use Case**: Used for real-time data analytics.
- **Best Practice**: Optimize window size; handle missing data; scale for large streams.