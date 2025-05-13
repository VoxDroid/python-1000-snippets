# Risk Assessment

## Description
This snippet demonstrates risk scoring using weighted features.

## Code
```python
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np
    features = np.array([1, 2, 3])
    weights = np.array([0.5, 0.3, 0.2])
    risk_score = np.dot(features, weights)
    print("Risk score:", round(risk_score, 2))
except ImportError:
    print("Mock Output: Risk score: 1.7")
```

## Output
```
Mock Output: Risk score: 1.7
```
*(Real output with `numpy`: `Risk score: 1.7`)*

## Explanation
- **Risk Assessment**: Calculates risk based on feature weights.
- **Logic**: Computes a weighted sum of features.
- **Complexity**: O(n) for n features.
- **Use Case**: Used in insurance or finance.
- **Best Practice**: Normalize features; validate weights; monitor scores.