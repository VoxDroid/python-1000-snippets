# Instrumental Variable Analysis

## Description
This snippet demonstrates instrumental variable (IV) analysis for an e-commerce platform, estimating the causal effect of discounts on purchases using an IV (e.g., random coupon distribution).

## Code
```python
# Instrumental variable analysis for discounts
# Note: Requires `numpy`, `sklearn`. Install with `pip install numpy scikit-learn`
try:
    import numpy as np
    from sklearn.linear_model import LinearRegression

    # IV model
    class IVModel:
        def __init__(self):
            # Initialize first and second stage models
            self.first_stage = LinearRegression()
            self.second_stage = LinearRegression()

        def fit(self, data: np.ndarray, treatment: np.ndarray, outcome: np.ndarray, instrument: np.ndarray) -> None:
            # First stage: predict treatment from instrument
            self.first_stage.fit(instrument.reshape(-1, 1), treatment)
            predicted_treatment = self.first_stage.predict(instrument.reshape(-1, 1))
            # Second stage: predict outcome from predicted treatment
            self.second_stage.fit(predicted_treatment.reshape(-1, 1), outcome)

        def estimate_effect(self) -> float:
            # Return causal effect
            return self.second_stage.coef_[0]

    # Simulate IV analysis
    def estimate_discount_iv(data: np.ndarray, treatment: np.ndarray, outcome: np.ndarray, instrument: np.ndarray) -> float:
        # Estimate causal effect
        model = IVModel()
        model.fit(data, treatment, outcome, instrument)
        return model.estimate_effect()

    # Example usage
    data = np.random.randn(100, 5)  # Customer features
    instrument = np.random.randint(0, 2, 100)  # Random coupon
    treatment = instrument * 0.8 + np.random.randn(100) * 0.2  # Discount
    outcome = treatment * 0.5 + np.random.randn(100)  # Purchases
    result = estimate_discount_iv(data, treatment, outcome, instrument)
    print("Instrumental variable result (causal effect):", result)
except ImportError:
    print("Mock Output: Instrumental variable result (causal effect): ~0.5")
```

## Output
```
Mock Output: Instrumental variable result (causal effect): ~0.5
```
*(Real output with `numpy`, `sklearn`: `Instrumental variable result (causal effect): <float>`)*

## Explanation
- **Purpose**: IV analysis estimates causal effects when treatment is confounded, using an instrument correlated with treatment but not outcome.
- **Real-World Use Case**: In an e-commerce platform, IV analysis uses random coupon distribution to estimate discounts’ effect on purchases, controlling for self-selection.
- **Code Breakdown**:
  - The `IVModel` class performs two-stage least squares.
  - The `fit` method predicts treatment and then outcome.
  - The `estimate_discount_iv` function simulates IV analysis.
- **Challenges**: Finding valid instruments, ensuring instrument strength, and handling weak instruments.
- **Integration**: Works with Causal Inference (Snippet 761) and Difference-in-Differences (Snippet 764) for causal studies.
- **Complexity**: O(n) for linear regression in both stages.
- **Best Practices**: Validate instrument validity, test instrument strength, check robustness, and use diagnostics.
- **Extensions**: Use 2SLS libraries (e.g., statsmodels) or incorporate multiple instruments.