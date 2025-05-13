# Schema Evolution

## Description
This snippet demonstrates handling schema changes using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    old_df = pd.DataFrame({"col1": [1, 2]})
    new_df = pd.DataFrame({"col1": [3, 4], "col2": [5, 6]})
    merged = old_df.assign(col2=None)._append(new_df, ignore_index=True)
    print("Schema evolved:", merged.columns.tolist())
except ImportError:
    print("Mock Output: Schema evolved: ['col1', 'col2']")
```

## Output
```
Mock Output: Schema evolved: ['col1', 'col2']
```
*(Real output with `pandas`: `Schema evolved: ['col1', 'col2']`)*

## Explanation
- **Schema Evolution**: Adapts to new columns in data.
- **Logic**: Merges DataFrames with different schemas.
- **Complexity**: O(n) for n rows.
- **Use Case**: Used in data pipelines with changing schemas.
- **Best Practice**: Validate merges; handle nulls; document changes.