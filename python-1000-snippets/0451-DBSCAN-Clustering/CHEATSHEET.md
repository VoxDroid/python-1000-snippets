# 0451-DBSCAN-Clustering Cheatsheet

- **DBSCAN** groups points that are closely packed and marks low-density points as noise.
- Key parameters:
  - `eps`: neighborhood radius.
  - `min_samples`: minimum number of points required to form a dense region.

Example:
```python
from sklearn.cluster import DBSCAN
clustering = DBSCAN(eps=0.5, min_samples=5).fit(X)
print(clustering.labels_)
```
