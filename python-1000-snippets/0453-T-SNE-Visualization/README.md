# T-SNE Visualization

## Description
This snippet demonstrates T-SNE dimensionality reduction using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.manifold import TSNE
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=100, centers=3)
    tsne = TSNE(n_components=2, random_state=42)
    X_tsne = tsne.fit_transform(X)
    print("T-SNE shape:", X_tsne.shape)
except ImportError:
    print("Mock Output: T-SNE shape: (100, 2)")
```

## Output
```
Mock Output: T-SNE shape: (100, 2)
```
*(Real output with `scikit-learn`: `T-SNE shape: (100, 2)`)*

## Explanation
- **T-SNE Visualization**: Reduces high-dimensional data to 2D for visualization.
- **Logic**: Applies T-SNE to synthetic data for 2D projection.
- **Complexity**: O(n^2) for n samples.
- **Use Case**: Used for visualizing high-dimensional datasets.
- **Best Practice**: Tune perplexity; preprocess data; interpret with caution.