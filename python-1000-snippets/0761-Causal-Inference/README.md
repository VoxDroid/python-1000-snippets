# Causal Inference

## Description
This snippet demonstrates causal inference for an e-commerce platform, estimating the effect of a discount campaign on customer purchases using propensity score weighting.

## Code
```python
# Causal inference for discount campaign
# Note: Requires `numpy`, `sklearn`. Install with `pip install numpy scikit-learn`
try:
    import numpy as np
    from sklearn.linear_model import LogisticRegression

    # Causal inference model
    class CausalModel:
        def __init__(self):
            # Initialize propensity score model
            self.propensity_model = LogisticRegression()

        def fit(self, data: np.ndarray, treatment: np.ndarray) -> None:
            # Fit propensity score model
            self.propensity_model.fit(data, treatment)

        def estimate_effect(self, data: np.ndarray, treatment: np.ndarray, outcome: np.ndarray) -> float:
            # Estimate average treatment effect with IPW
            propensity_scores = self.propensity_model.predict_proba(data)[:, 1]
            weights = np.where(treatment == 1, 1/propensity_scores, 1/(1-propensity_scores))
            treated_outcome = np.sum(outcome[treatment == 1] * weights[treatment == 1]) / np.sum(weights[treatment == 1])
            control_outcome = np.sum(outcome[treatment == 0] * weights[treatment == 0]) / np.sum(weights[treatment == 0])
            return treated_outcome - control_outcome

    # Simulate causal inference
    def estimate_discount_effect(data: np.ndarray, treatment: np.ndarray, outcome: np.ndarray) -> float:
        # Estimate campaign effect
        model = CausalModel()
        model.fit(data, treatment)
        return model.estimate_effect(data, treatment, outcome)

    # Example usage
    data = np.random.randn(100, 5)  # Customer features
    treatment = np.random.randint(0, 2, 100)  # Discount received
    outcome = np.random.randn(100) + treatment * 0.5  # Purchases
    result = estimate_discount_effect(data, treatment, outcome)
    print("Causal inference result (ATE):", result)
except ImportError:
    print("Mock Output: Causal inference result (ATE): ~0.5")
```

## Output
```
Mock Output: Causal inference result (ATE): ~0.5
```
*(Real output with `numpy`, `sklearn`: `Causal inference result (ATE): <float>`)*

## Explanation
- **Purpose**: Causal inference estimates the true effect of an intervention, distinguishing correlation from causation.
- **Real-World Use Case**: In an e-commerce platform, causal inference measures how a discount campaign increases purchases, guiding marketing budgets.
- **Code Breakdown**:
  - The `CausalModel` class fits a propensity score model and estimates effects.
  - The `estimate_effect` method uses inverse propensity weighting (IPW).
  - The `estimate_discount_effect` function simulates causal analysis.
- **Challenges**: Ensuring unconfoundedness, handling imbalanced treatments, and validating propensity scores.
- **Integration**: Works with Propensity Score Matching (Snippet 762) and Time Series Causal Analysis (Snippet 767) for causal studies.
- **Complexity**: O(n*d) for n samples and d features in propensity modeling.
- **Best Practices**: Validate assumptions, use robust estimators, check balance, and test sensitivity.
- **Extensions**: Use doubly robust estimators or integrate with causal libraries (e.g., DoWhy).