# 0456-Data-Augmentation Cheatsheet

- **Noise injection**: duplicate samples by adding small random perturbations.
- **Flipping**: reverse axes to create a mirrored sample (common in images).
- **Repetition**: repeat the dataset with slight perturbations to increase sample size.

Example:
```python
X_aug = np.vstack([X, X + np.random.normal(scale=0.1, size=X.shape)])
```
