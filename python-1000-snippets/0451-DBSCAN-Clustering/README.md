# DBSCAN Clustering

## Description
This snippet demonstrates DBSCAN clustering using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.cluster import DBSCAN
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=100, centers=3)
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(X)
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
- **DBSCAN Clustering**: Groups data points based on density.
- **Logic**: Applies DBSCAN to synthetic blob data with specified `eps` and `min_samples`.
- **Complexity**: O(n log n) for n samples with efficient indexing.
- **Use Case**: Used for non-spherical clusters or noise detection.
- **Best Practice**: Tune `eps` and `min_samples`; scale features; visualize results.