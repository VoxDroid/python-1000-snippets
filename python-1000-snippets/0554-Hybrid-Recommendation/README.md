# Hybrid Recommendation

## Description
This snippet demonstrates a hybrid recommendation combining collaborative and content-based filtering.

## Code
```python
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np
    collab_scores = np.array([0.8, 0.2, 0.5])
    content_scores = np.array([0.6, 0.9, 0.3])
    hybrid_scores = 0.5 * collab_scores + 0.5 * content_scores
    print("Hybrid scores:", hybrid_scores.round(2))
except ImportError:
    print("Mock Output: Hybrid scores: [0.7  0.55 0.4 ]")
```

## Output
```
Mock Output: Hybrid scores: [0.7  0.55 0.4 ]
```
*(Real output with `numpy`: `Hybrid scores: [0.7  0.55 0.4 ]`)*

## Explanation
- **Hybrid Recommendation**: Combines multiple recommendation strategies.
- **Logic**: Averages collaborative and content-based scores.
- **Complexity**: O(n) for n items.
- **Use Case**: Used for robust recommendations in diverse systems.
- **Best Practice**: Weight strategies; validate blending; monitor performance.