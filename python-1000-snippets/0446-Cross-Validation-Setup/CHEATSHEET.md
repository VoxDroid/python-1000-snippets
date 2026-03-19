# 0446-Cross-Validation-Setup Cheatsheet

- **KFold**: split data into `k` folds for cross-validation.
- **StratifiedKFold**: preserves class distribution across folds (important for classification).
- **LeaveOneOut**: extreme case where each sample is used once as a validation set.

Example:
```python
from sklearn.model_selection import cross_val_score, StratifiedKFold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(model, X, y, cv=cv)
```
