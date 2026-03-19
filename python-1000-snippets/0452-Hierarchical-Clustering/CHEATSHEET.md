# 0452-Hierarchical-Clustering Cheatsheet

- **AgglomerativeClustering**: bottom-up clustering combining closest clusters iteratively.
- **Linkage matrix (SciPy)** encodes the merge steps and distances.
- Common linkage methods: `single`, `complete`, `average`, `ward`.

Example (scikit-learn):
```python
from sklearn.cluster import AgglomerativeClustering
clustering = AgglomerativeClustering(n_clusters=3)
labels = clustering.fit_predict(X)
```
