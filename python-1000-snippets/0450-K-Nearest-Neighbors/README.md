# K-Nearest Neighbors

## Description
This snippet demonstrates a KNN classifier using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.datasets import make_classification
    from sklearn.neighbors import KNeighborsClassifier
    X, y = make_classification(n_samples=100)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X, y)
    print("Model trained")
except ImportError:
    print("Mock Output: Model trained")
```

## Output
```
Mock Output: Model trained
```
*(Real output with `scikit-learn`: `Model trained`)*

## Explanation
- **K-Nearest Neighbors**: Trains a KNN classifier with k=3.
- **Logic**: Fits a model based on nearest neighbor distances.
- **Complexity**: O(n * d) for n samples, d features at prediction.
- **Use Case**: Used for small datasets or non-linear problems.
- **Best Practice**: Scale features; tune k; evaluate distance metrics.