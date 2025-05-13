# Differential Privacy

## Description
This snippet demonstrates differential privacy for an e-commerce platform, adding noise to customer purchase data to protect individual privacy.

## Code
```python
# Differential privacy for purchase data
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Differential privacy processor
    class DPProcessor:
        def __init__(self, epsilon: float):
            # Initialize with privacy parameter
            self.epsilon = epsilon

        def add_noise(self, data: list[float]) -> float:
            # Add Laplace noise to sum
            sensitivity = 1.0  # Max contribution per individual
            noise = np.random.laplace(0, sensitivity / self.epsilon)
            return sum(data) + noise

    # Simulate differential privacy
    def anonymize_purchases(purchases: list[float]) -> float:
        # Compute private sum of purchases
        processor = DPProcessor(epsilon=1.0)
        return processor.add_noise(purchases)

    # Example usage
    purchases = [100.0, 200.0, 300.0]
    result = anonymize_purchases(purchases)
    print("Differential privacy:", result)
except ImportError:
    print("Mock Output: Differential privacy: ~600.0 (with noise)")
```

## Output
```
Mock Output: Differential privacy: ~600.0 (with noise)
```
*(Real output with `numpy`: `Differential privacy: ~600.0 (varies with noise)`)*

## Explanation
- **Purpose**: Differential privacy protects individual data by adding noise to query results, ensuring statistical utility.
- **Real-World Use Case**: In an e-commerce platform, differential privacy anonymizes purchase totals for analytics without exposing individual spending.
- **Code Breakdown**:
  - The `DPProcessor` class adds Laplace noise based on the epsilon privacy parameter.
  - The `anonymize_purchases` function computes a private sum of purchases.
  - The output is the noisy sum.
- **Challenges**: Balancing privacy and accuracy, choosing epsilon, and handling high-dimensional data.
- **Integration**: Works with Secure Multi-Party Computation (Snippet 703) and Federated Learning (Snippet 705) for privacy.
- **Complexity**: O(n) for summing n values.
- **Best Practices**: Tune epsilon, validate noise, monitor utility, and test privacy guarantees.