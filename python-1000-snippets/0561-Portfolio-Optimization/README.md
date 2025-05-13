# Portfolio Optimization

## Description
This snippet demonstrates portfolio optimization using mean-variance analysis.

## Code
```python
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np
    returns = np.array([[0.1, 0.2], [0.15, 0.25]])
    cov_matrix = np.cov(returns.T)
    weights = np.array([0.5, 0.5])
    portfolio_var = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    print("Portfolio variance:", round(portfolio_var, 4))
except ImportError:
    print("Mock Output: Portfolio variance: 0.0354")
```

## Output
```
Mock Output: Portfolio variance: 0.0354
```
*(Real output with `numpy`: `Portfolio variance: 0.0354`)*

## Explanation
- **Portfolio Optimization**: Minimizes risk for a given return.
- **Logic**: Computes portfolio variance using covariance matrix.
- **Complexity**: O(n^2) for n assets.
- **Use Case**: Used in investment management.
- **Best Practice**: Optimize weights; use historical data; account for constraints.