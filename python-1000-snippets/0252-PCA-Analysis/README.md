# PCA Analysis

## Description
This snippet demonstrates Principal Component Analysis (PCA) using `scikit-learn` for dimensionality reduction.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.decomposition import PCA
    from sklearn.datasets import make_classification
    X, _ = make_classification(n_samples=100, n_features=4, random_state=42)
    pca = PCA(n_components=2)
    X_transformed = pca.fit_transform(X)
    print("Explained Variance Ratio:", pca.explained_variance_ratio_)
except ImportError:
    print("Mock Output: Explained Variance Ratio: [0.70068485 0.29931515]")
```

## Output
```
Mock Output: Explained Variance Ratio: [0.70068485 0.29931515]
```
*(Real output with `scikit-learn`: `Explained Variance Ratio: [<values summing to ~1.0>]`)*

## Explanation
- **PCA Analysis**: Reduces dimensionality while preserving variance.
- **Logic**: Generates 4D data, reduces to 2D, and prints variance ratios.
- **Complexity**: O(min(n,d)^2 * max(n,d)) for n samples, d features.
- **Use Case**: Used for visualization or speeding up ML models.
- **Best Practice**: Scale features; choose components via cumulative variance; validate results.