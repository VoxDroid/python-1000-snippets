# 0444-Data-Preprocessing Cheatsheet

- **Imputation**: Fill missing values with mean/median/mode using `SimpleImputer`.
- **Scaling**: Normalize or standardize features with `MinMaxScaler` / `StandardScaler`.
- **Pipelines**: Combine multiple preprocessing steps into a `Pipeline` or `ColumnTransformer`.

Example:
```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
])
```
