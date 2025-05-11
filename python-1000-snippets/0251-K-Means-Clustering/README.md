# K-Means Clustering

## Description
This snippet demonstrates K-Means clustering using `scikit-learn` to group synthetic data.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=100, centers=3, random_state=42)
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)
    print("Cluster Labels:", labels[:5])
except ImportError:
    print("Mock Output: Cluster Labels: [1 2 0 2 1]")
```

## Output
```
Mock Output: Cluster Labels: [1 2 0 2 1]
```
*(Real output with `scikit-learn`: `Cluster Labels: [1 2 0 2 1]` or similar)*

## Explanation
- **K-Means Clustering**: Groups data into clusters based on feature similarity.
- **Logic**: Generates synthetic data with 3 clusters, applies K-Means, and outputs labels.
- **Complexity**: O(n*k*i) for n samples, k clusters, i iterations.
- **Use Case**: Used for customer segmentation or image compression.
- **Best Practice**: Choose k via elbow method; scale features; handle outliers.