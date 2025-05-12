# SVM Classification

## Description
This snippet demonstrates SVM classification using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.datasets import make_classification
    from sklearn.svm import SVC
    X, y = make_classification(n_samples=100)
    model = SVC(kernel="linear")
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
- **SVM Classification**: Trains a linear SVM classifier.
- **Logic**: Fits an SVM model on synthetic data.
- **Complexity**: O(n^2) for n samples (kernel-dependent).
- **Use Case**: Used for small to medium datasets with clear margins.
- **Best Practice**: Scale features; tune kernel/parameters; evaluate accuracy.