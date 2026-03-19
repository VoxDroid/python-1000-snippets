# 0450-K-Nearest-Neighbors Cheatsheet

- **KNeighborsClassifier** (classification) and **KNeighborsRegressor** (regression) support simple nearest-neighbor learning.
- Choose `n_neighbors` (k) based on validation; small k = high variance, large k = high bias.

Example:
```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
```
