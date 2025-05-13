# Data Warehouse Query

## Description
This snippet demonstrates a simulated SQL query using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    df = pd.DataFrame({"sales": [100, 200, 300]})
    result = df["sales"].sum()
    print("Total sales:", result)
except ImportError:
    print("Mock Output: Total sales: 600")
```

## Output
```
Mock Output: Total sales: 600
```
*(Real output with `pandas`: `Total sales: 600`)*

## Explanation
- **Data Warehouse Query**: Aggregates sales data.
- **Logic**: Sums a column in a DataFrame.
- **Complexity**: O(n) for n rows.
- **Use Case**: Used for analytics in data warehouses.
- **Best Practice**: Optimize queries; use indexes; validate results.