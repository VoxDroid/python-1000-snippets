# 0442-Supervised-Learning-Pipeline Cheatsheet

- Use `sklearn.pipeline.Pipeline` to chain preprocessing and modeling steps.
- `ColumnTransformer` lets you apply different transformers to different columns.
- Use `cross_val_score` to evaluate models with cross-validation.

Example:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([("scale", StandardScaler()), ("clf", LogisticRegression())])
```
