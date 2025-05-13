# Data Lake Integration

## Description
This snippet demonstrates writing to a data lake using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    df = pd.DataFrame({"data": [1, 2, 3]})
    df.to_parquet("data_lake.parquet")
    print("Data written to lake")
except ImportError:
    print("Mock Output: Data written to lake")
```

## Output
```
Mock Output: Data written to lake
```
*(Real output with `pandas`: `Data written to lake`)*

## Explanation
- **Data Lake Integration**: Saves data as a Parquet file.
- **Logic**: Writes a DataFrame to a Parquet file.
- **Complexity**: O(n) for n rows.
- **Use Case**: Used for scalable data storage.
- **Best Practice**: Use partitioning; compress files; validate writes.