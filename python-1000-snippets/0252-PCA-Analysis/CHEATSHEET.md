# 0252 - PCA Analysis Cheatsheet

## Quick Start
```bash
pip install scikit-learn
python python-1000-snippets/0252-PCA-Analysis/SAMPLES/sample1.py
```

## Key Concepts
- PCA finds orthogonal directions (components) that explain variance.
- Use `PCA(n_components=k)` to project to k dimensions.
- `explained_variance_ratio_` shows how much variance each component explains.

## Common Patterns
- Fit and transform data:
  ```py
  pca = PCA(n_components=2)
  X_pca = pca.fit_transform(X)
  ```
- Reconstruct data:
  ```py
  X_recon = pca.inverse_transform(X_pca)
  ```
- Use PCA output as features for downstream models.
