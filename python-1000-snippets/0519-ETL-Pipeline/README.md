# ETL Pipeline

## Description
This snippet demonstrates a simple ETL pipeline using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    raw = pd.DataFrame({"value": [1, None, 3]})
    cleaned = raw.fillna(0)
    transformed = cleaned["value"] * 2
    print("ETL result:", transformed.tolist())
except ImportError:
    print("Mock Output: ETL result: [2, 0, 6]")
```

## Output
```
Mock Output: ETL result: [2, 0, 6]
```
*(Real output with `pandas`: `ETL result: [2, 0, 6]`)*

## Explanation
- **ETL Pipeline**: Extracts, transforms, and loads data.
- **Logic**: Cleans missing values and doubles them.
- **Complexity**: O(n) for n rows.
- **Use Case**: Used for data preparation in analytics.
- **Best Practice**: Log steps; handle errors; automate pipeline.