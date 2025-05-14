# Out-of-Distribution Detection

## Description
This snippet demonstrates out-of-distribution (OOD) detection for an e-commerce platform, identifying anomalous customer transactions that deviate from normal behavior.

## Code
```python
# Out-of-distribution detection for transactions
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # OOD detection model
    class OODModel:
        def __init__(self):
            # Initialize mean and covariance for in-distribution data
            self.mean = None
            self.cov = None

        def fit(self, in_dist_data: np.ndarray) -> None:
            # Fit to in-distribution data
            self.mean = np.mean(in_dist_data, axis=0)
            self.cov = np.cov(in_dist_data.T)

        def detect(self, data: np.ndarray) -> np.ndarray:
            # Compute Mahalanobis distance for OOD detection
            diff = data - self.mean
            inv_cov = np.linalg.inv(self.cov)
            distances = np.sqrt(np.sum(diff @ inv_cov * diff, axis=1))
            return distances > 2.0  # Threshold for OOD

    # Simulate OOD detection
    def detect_anomalous_transactions(in_dist_data: np.ndarray, test_data: np.ndarray) -> np.ndarray:
        # Detect OOD transactions
        model = OODModel()
        model.fit(in_dist_data)
        return model.detect(test_data)

    # Example usage
    in_dist_data = np.random.randn(100, 5)  # Normal transactions
    test_data = np.random.randn(3, 5) * 2  # Potentially anomalous
    result = detect_anomalous_transactions(in_dist_data, test_data)
    print("Out-of-distribution detection result:", result)
except ImportError:
    print("Mock Output: Out-of-distribution detection result: [True, False, True]")
```

## Output
```
Mock Output: Out-of-distribution detection result: [True, False, True]
```
*(Real output with `numpy`: `Out-of-distribution detection result: [<3 booleans>]`)*

## Explanation
- **Purpose**: OOD detection identifies data points that deviate from the training distribution, enhancing model reliability.
- **Real-World Use Case**: In an e-commerce platform, OOD detection flags unusual transactions (e.g., high-value purchases from new locations) for fraud review.
- **Code Breakdown**:
  - The `OODModel` class fits a Gaussian model to in-distribution data.
  - The `detect` method uses Mahalanobis distance to flag OOD samples.
  - The `detect_anomalous_transactions` function simulates OOD detection.
- **Challenges**: Setting robust thresholds, handling high-dimensional data, and avoiding false positives.
- **Integration**: Works with Robustness Testing (Snippet 734) and Drift Detection (Snippet 740) for reliable models.
- **Complexity**: O(d^3) for d features (covariance inversion), O(n*d) for n samples during detection.
- **Best Practices**: Tune thresholds, validate on diverse data, monitor false positives, and test sensitivity.