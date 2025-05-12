# Hierarchical Clustering

## Description
This snippet demonstrates hierarchical clustering using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=100, centers=3)
    clustering = AgglomerativeClustering(n_clusters=3)
    labels = clustering.fit_predict(X)
    print("Cluster labels:", labels[:5])
except ImportError:
    print("Mock Output: Cluster labels: [0 1 2 0 1]")
```

## Output
```
Mock Output: Cluster labels: [0 1 2 0 1]
```
*(Real output with `scikit-learn`: `Cluster labels: <array of labels>`)*

## Explanation
- **Hierarchical Clustering**: Builds a tree of clusters using a bottom-up approach.
- **Logic**: Applies agglomerative clustering to synthetic data.
- **Complexity**: O(n^2) for n samples.
- **Use Case**: Used for hierarchical data structures or dendrogram visualization.
- **Best Practice**: Choose linkage method; visualize dendrogram; validate clusters.