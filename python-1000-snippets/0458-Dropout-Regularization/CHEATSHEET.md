# 0458-Dropout-Regularization Cheatsheet

- Dropout randomly sets inputs to zero with probability `p` during training.
- Scale remaining activations by `1/(1-p)` so expected value remains the same.
- During inference, dropout is disabled (no scaling or masking).

Example:
```python
mask = rng.random(x.shape) >= p
out = x * mask / (1 - p)
```
