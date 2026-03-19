# 0445-Hyperparameter-Tuning Cheatsheet

- **GridSearchCV**: exhaustively search over a parameter grid.
- **RandomizedSearchCV**: sample parameter settings from distributions for faster search.
- **HalvingGridSearchCV**: iteratively focus on top-performing parameter sets with successive resource allocation.

Example:
```python
from sklearn.model_selection import GridSearchCV

search = GridSearchCV(model, param_grid, cv=5)
search.fit(X, y)
print(search.best_params_)
```
