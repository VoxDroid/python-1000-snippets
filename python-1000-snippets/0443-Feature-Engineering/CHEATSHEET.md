# 0443-Feature-Engineering Cheatsheet

- **Derived features**: combine existing features (e.g., area = length * width).
- **Polynomial features**: expand feature set with interaction terms using `PolynomialFeatures`.
- **Binning**: discretize a continuous variable (e.g., `pd.cut`) and one-hot encode bins.

Example pipeline:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

pipeline = Pipeline([("poly", PolynomialFeatures(degree=2)), ("clf", LogisticRegression())])
```
