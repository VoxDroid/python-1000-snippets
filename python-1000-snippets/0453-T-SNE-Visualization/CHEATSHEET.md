# 0453-T-SNE-Visualization Cheatsheet

- **t-SNE**: non-linear dimensionality reduction technique useful for visualization.
- Key parameter: `perplexity` (controls balance between local and global structure).
- t-SNE results can vary between runs unless `random_state` is fixed.

Example:
```python
from sklearn.manifold import TSNE
emb = TSNE(n_components=2, random_state=0).fit_transform(X)
```
