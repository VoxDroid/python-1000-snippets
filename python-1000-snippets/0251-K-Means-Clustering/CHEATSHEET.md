# 0251 - K-Means Clustering Cheatsheet

## Quick Start
```bash
pip install scikit-learn
python python-1000-snippets/0251-K-Means-Clustering/SAMPLES/sample1.py
```

## Key Concepts
- `KMeans(n_clusters=k)` partitions points into k clusters.
- `kmeans.inertia_` is the sum of squared distances to cluster centers.
- Use `kmeans.predict(new_points)` to assign clusters to new data.

## Tips
- Use `KMeans(n_init=10)` or more for stable results.
- Scale data before clustering.
- Determine k via elbow method (look for inflection in inertia vs. k).
