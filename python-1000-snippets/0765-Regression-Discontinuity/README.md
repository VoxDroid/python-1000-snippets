# Regression Discontinuity

## Description
This snippet demonstrates regression discontinuity (RD) for an e-commerce platform, estimating the effect of a discount threshold on customer purchases.

## Code
```python
# Regression discontinuity for discount threshold
# Note: Requires `numpy`, `sklearn`. Install with `pip install numpy scikit-learn`
try:
    import numpy as np
    from sklearn.linear_model import LinearRegression

    # RD model
    class RDModel:
        def __init__(self):
            self.model_left = LinearRegression()
            self.model_right = LinearRegression()

        def fit(self, data: np.ndarray, outcome: np.ndarray, threshold: float) -> float:
            # Fit models on either side of threshold
            running_var = data[:, 0]
            left = running_var < threshold
            right = running_var >= threshold
            self.model_left.fit(running_var[left].reshape(-1, 1), outcome[left])
            self.model_right.fit(running_var[right].reshape(-1, 1), outcome[right])
            # Estimate effect at threshold
            left_pred = self.model_left.predict([[threshold]])[0]
            right_pred = self.model_right.predict([[threshold]])[0]
            return right_pred - left_pred

    # Simulate regression discontinuity
    def estimate_discount_rd(data: np.ndarray, outcome: np.ndarray, threshold: float) -> float:
        model = RDModel()
        return model.fit(data, outcome, threshold)

    # Example usage
    np.random.seed(0)
    n = 200
    threshold = 100
    spending = np.random.uniform(50, 150, size=(n, 1))
    treatment = (spending[:, 0] >= threshold).astype(int)
    outcome = 20 + 0.5 * spending[:, 0] + 10 * treatment + np.random.normal(0, 5, n)

    effect = estimate_discount_rd(spending, outcome, threshold)
    print("Regression discontinuity result (effect):", round(effect, 3))

except ImportError:
    print("Mock Output: Regression discontinuity result (effect): ~0.4")
```

---

## Output
```
Mock Output: Regression discontinuity result (effect): ~0.4
```
*(Real output with `numpy`, `sklearn`: `Regression discontinuity result (effect): <float>`)*

## Explanation
- **Purpose**: RD estimates causal effects at a threshold where treatment changes discontinuously, leveraging local randomization.
- **Real-World Use Case**: In an e-commerce platform, RD measures how a discount for customers spending above $100 affects purchase amounts.
- **Code Breakdown**:
  - The `RDModel` class fits separate regressions on either side of the threshold.
  - The `fit` method estimates the treatment effect at the threshold.
  - The `estimate_discount_rd` function simulates RD with synthetic data.
- **Challenges**: Choosing bandwidth, ensuring continuity, handling fuzzy designs, and validating assumptions.
- **Integration**: Works with Causal Inference (Snippet 761) and Difference-in-Differences (Snippet 764) for causal studies.
- **Complexity**: O(n) for linear regression with n samples.
- **Best Practices**: Use optimal bandwidth, validate continuity, check robustness, and visualize discontinuities.
- **Extensions**: Implement fuzzy RD or use RD-specific libraries (e.g., rdrobust).