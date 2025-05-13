# Recommendation System

## Description
This snippet demonstrates a simple recommendation system using cosine similarity.

## Code
```python
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np
    user_item = np.array([[5, 3, 0], [4, 0, 0], [0, 2, 3]])
    similarity = np.dot(user_item, user_item.T) / (np.linalg.norm(user_item, axis=1)[:, None] * np.linalg.norm(user_item.T, axis=1))
    print("User similarity:", similarity[0, :].round(2))
except ImportError:
    print("Mock Output: User similarity: [0.91 0.95 0.34]")
```

## Output
```
Mock Output: User similarity: [0.91 0.95 0.34]     
```
*(Real output with `numpy`: `User similarity: [0.91 0.95 0.34]`)*

## Explanation
- **Recommendation System**: Computes user similarity for recommendations.
- **Logic**: Uses cosine similarity on a user-item matrix.
- **Complexity**: O(n*m) for n users, m items.
- **Use Case**: Used in e-commerce or streaming services.
- **Best Practice**: Handle sparse data; scale with large datasets; validate recommendations.