# Feature Engineering

## Description
This snippet demonstrates feature engineering using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    df = pd.DataFrame({"age": [25, 30, None]})
    df["age_squared"] = df["age"] ** 2
    df["age"].fillna(df["age"].mean(), inplace=True)
    print("Features engineered")
except ImportError:
    print("Mock Output: Features engineered")
```

## Output
```
Mock Output: Features engineered
```
*(Real output with `pandas`: `Features engineered`)*

## Explanation
- **Feature Engineering**: Creates and cleans features in a dataset.
- **Logic**: Adds a squared feature and imputes missing values.
- **Complexity**: O(n) for n rows.
- **Use Case**: Used to improve ML model performance.
- **Best Practice**: Handle missing data; avoid data leakage; document transformations.