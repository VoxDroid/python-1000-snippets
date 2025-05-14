# Non-Negative Matrix Factorization

## Description
This snippet demonstrates Non-Negative Matrix Factorization (NMF) for an e-commerce platform, decomposing customer-product interactions to identify purchase patterns.

## Code
```python
# Non-Negative Matrix Factorization for purchase patterns
# Note: Requires `numpy`, `sklearn`. Install with `pip install numpy scikit-learn`
try:
    import numpy as np
    from sklearn.decomposition import NMF

    # NMF model for interactions
    class PurchaseNMF:
        def __init__(self, n_components: int = 2):
            # Initialize NMF model
            self.model = NMF(n_components=n_components, init='random', random_state=42)

        def fit(self, data: np.ndarray) -> tuple:
            # Decompose interaction matrix
            W = self.model.fit_transform(data)
            H = self.model.components_
            return W, H

    # Simulate purchase pattern analysis
    def analyze_purchase_patterns(interactions: np.ndarray) -> tuple:
        # Identify patterns
        model = PurchaseNMF()
        return model.fit(interactions)

    # Example usage
    interactions = np.random.rand(100, 50)  # Customer-product matrix
    W, H = analyze_purchase_patterns(interactions)
    print("NMF result (W shape, H shape):", W.shape, H.shape)
except ImportError:
    print("Mock Output: NMF result (W shape, H shape): (100, 2), (2, 50)")
```

## Output
```
Mock Output: NMF result (W shape, H shape): (100, 2), (2, 50)
```
*(Real output with `numpy`, `sklearn`: `NMF result (W shape, H shape): (100, 2), (2, 50)`)*

## Explanation
- **Purpose**: NMF decomposes non-negative matrices into low-rank factors, revealing latent patterns in data.
- **Real-World Use Case**: In an e-commerce platform, NMF identifies customer purchase patterns (e.g., electronics vs. fashion) for recommendation systems.
- **Code Breakdown**:
  - The `PurchaseNMF` class applies NMF to an interaction matrix.
  - The `fit` method decomposes into customer and product factors.
  - The `analyze_purchase_patterns` function simulates decomposition.
- **Challenges**: Choosing the number of components, handling sparse data, and interpreting factors.
- **Integration**: Works with Topic Modeling (Snippet 778) and Spectral Clustering (Snippet 780) for pattern analysis.
- **Complexity**: O(n*m*k) for n customers, m products, and k components.
- **Best Practices**: Tune component count, handle sparsity, validate factors, and visualize patterns.
- **Extensions**: Use sparse NMF or integrate with recommendation engines.