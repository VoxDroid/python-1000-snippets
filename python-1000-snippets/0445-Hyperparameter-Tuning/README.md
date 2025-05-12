# Hyperparameter Tuning

## Description
This snippet demonstrates hyperparameter tuning using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.datasets import make_classification
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import LogisticRegression
    X, y = make_classification(n_samples=100)
    param_grid = {"C": [0.1, 1, 10]}
    grid = GridSearchCV(LogisticRegression(), param_grid, cv=3)
    grid.fit(X, y)
    print("Best params:", grid.best_params_)
except ImportError:
    print("Mock Output: Best params: {'C': 1}")
```

## Output
```
Mock Output: Best params: {'C': 1}
```
*(Real output with `scikit-learn`: `Best params: <optimal C value>`)*

## Explanation
- **Hyperparameter Tuning**: Finds optimal model parameters.
- **Logic**: Uses `GridSearchCV` to test different `C` values.
- **Complexity**: O(n * k) for n samples, k parameter combinations.
- **Use Case**: Used to optimize ML model performance.
- **Best Practice**: Use cross-validation; limit parameter space; parallelize search.