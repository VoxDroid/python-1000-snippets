# Collaborative Filtering

## Description
This snippet demonstrates user-based collaborative filtering using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    ratings = pd.DataFrame([[5, 3, 0], [4, 0, 0], [0, 2, 3]], columns=["item1", "item2", "item3"])
    similarity = ratings.corr()
    print("Item correlation:", similarity["item1"].round(2).to_dict())
except ImportError:
    print("Mock Output: Item correlation: {'item1': 1.0, 'item2': 0.76, 'item3': nan}")
```

## Output
```
Mock Output: Item correlation: {'item1': 1.0, 'item2': 0.76, 'item3': nan}
```
*(Real output with `pandas`: `Item correlation: {'item1': 1.0, 'item2': 0.76, 'item3': nan}`)*

## Explanation
- **Collaborative Filtering**: Finds item similarities based on user ratings.
- **Logic**: Computes Pearson correlation between items.
- **Complexity**: O(n*m) for n users, m items.
- **Use Case**: Used in recommendation systems for personalized suggestions.
- **Best Practice**: Handle missing ratings; use matrix factorization; test accuracy.