# Content-Based Filtering

## Description
This snippet demonstrates content-based filtering using item features.

## Code
```python
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np
    item_features = np.array([[1, 0], [0, 1], [1, 1]])
    user_pref = np.array([1, 0])
    scores = np.dot(item_features, user_pref)
    print("Recommendation scores:", scores)
except ImportError:
    print("Mock Output: Recommendation scores: [1 0 1]")
```

## Output
```
Mock Output: Recommendation scores: [1 0 1]
```
*(Real output with `numpy`: `Recommendation scores: [1 0 1]`)*

## Explanation
- **Content-Based Filtering**: Recommends items based on feature similarity.
- **Logic**: Scores items by dot product with user preferences.
- **Complexity**: O(n*m) for n items, m features.
- **Use Case**: Used in content recommendation like articles or movies.
- **Best Practice**: Normalize features; update user profiles; handle cold starts.