# Algorithmic Trading

## Description
This snippet demonstrates a simple moving average trading strategy.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    prices = pd.Series([100, 101, 102, 103, 104])
    ma = prices.rolling(window=2).mean()
    signal = prices.iloc[-1] > ma.iloc[-1]
    print("Buy signal:", signal)
except ImportError:
    print("Mock Output: Buy signal: True")
```

## Output
```
Mock Output: Buy signal: True
```
*(Real output with `pandas`: `Buy signal: True`)*

## Explanation
- **Algorithmic Trading**: Generates trading signals using moving averages.
- **Logic**: Compares current price to moving average.
- **Complexity**: O(n) for n prices.
- **Use Case**: Used in automated trading systems.
- **Best Practice**: Backtest strategy; manage risk; monitor signals.