# 0457-Batch-Normalization Cheatsheet

- BatchNorm normalizes data per mini-batch: `(x - mean) / sqrt(var + eps)`.
- Learnable parameters `gamma` and `beta` allow scaling and shifting after normalization.
- During training, a running mean/variance is maintained for inference.

Example:
```python
mean = X.mean(axis=0)
var = X.var(axis=0)
x_norm = (X - mean) / np.sqrt(var + 1e-5)
```
