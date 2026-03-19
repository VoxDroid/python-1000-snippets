# 0447-Gradient-Boosting-Model Cheatsheet

- **GradientBoostingClassifier**: classic gradient boosting decision tree ensemble.
- **HistGradientBoostingClassifier**: faster implementation using histogram-based binning.
- Use `feature_importances_` to inspect how much each feature contributes.

Example:
```python
from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier()
clf.fit(X, y)
print(clf.feature_importances_)
```
