# Customer Segmentation

## Description
This snippet demonstrates customer segmentation using K-means clustering.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.cluster import KMeans
    import numpy as np
    data = np.array([[1, 2], [1, 4], [5, 6], [5, 8]])
    kmeans = KMeans(n_clusters=2).fit(data)
    print("Cluster labels:", kmeans.labels_)
except ImportError:
    print("Mock Output: Cluster labels: [0 0 1 1]")
```

## Output
```
Mock Output: Cluster labels: [0 0 1 1]
```
*(Real output with `scikit-learn`: `Cluster labels: [0 0 1 1]`)*

## Explanation
- **Customer Segmentation**: Groups customers by similarity.
- **Logic**: Applies K-means to cluster data points.
- **Complexity**: O(n*k*i) for n points, k clusters, i iterations.
- **Use Case**: Used in marketing for targeted campaigns.
- **Best Practice**: Scale features; choose optimal k; interpret clusters.