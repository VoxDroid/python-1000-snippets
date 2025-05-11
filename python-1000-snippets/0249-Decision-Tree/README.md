# Decision Tree

## Description
This snippet demonstrates a decision tree classifier using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    print("Accuracy:", model.score(X, y))
except ImportError:
    print("Mock Output: Accuracy: 1.0")
```

## Output
```
Mock Output: Accuracy: 1.0
```
*(Real output with `scikit-learn`: `Accuracy: <value around 1.0>`)*

## Explanation
- **Decision Tree**: Trains a decision tree on synthetic classification data.
- **Logic**: Generates data, trains the model, and evaluates accuracy.
- **Complexity**: O(n*d*log(n)) for training (n samples, d features).
- **Use Case**: Used for interpretable classification or regression.
- **Best Practice**: Prune trees; limit depth; use cross-validation.