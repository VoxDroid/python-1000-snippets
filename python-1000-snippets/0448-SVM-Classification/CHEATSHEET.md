# 0448-SVM-Classification Cheatsheet

- **SVC**: Support Vector Classifier, can use kernels such as `linear`, `rbf`, and `poly`.
- **Kernel trick**: map inputs into higher-dimensional space without explicitly computing coordinates.
- Use `GridSearchCV` to tune `C`, `gamma`, and `kernel` parameters.

Example:
```python
from sklearn.svm import SVC
clf = SVC(kernel='rbf', gamma='scale')
clf.fit(X, y)
```
