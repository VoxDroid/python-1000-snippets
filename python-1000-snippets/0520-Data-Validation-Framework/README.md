# Data Validation Framework

## Description
This snippet demonstrates data validation using `great_expectations`.

## Code
```python
# Note: Requires `great_expectations` and `pandas`. Install with `pip install great_expectations pandas`
try:
    import great_expectations as ge
    import pandas as pd
    df = ge.from_pandas(pd.DataFrame({"value": [1, 2, 3]}))
    df.expect_column_values_to_be_between("value", 0, 10)
    print("Validation completed")
except ImportError:
    print("Mock Output: Validation completed")
```

## Output
```
Mock Output: Validation completed
```
*(Real output with `great_expectations`: `Validation completed`)*

## Explanation
- **Data Validation Framework**: Validates data against expectations.
- **Logic**: Checks if values are within a range.
- **Complexity**: O(n) for n rows.
- **Use Case**: Used for data quality assurance.
- **Best Practice**: Define clear expectations; log failures; integrate with ETL.