# Supervised Learning Pipeline

## Description
This snippet demonstrates a supervised learning pipeline using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    X, y = make_classification(n_samples=100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, y_train)
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
- **Supervised Learning Pipeline**: Trains a logistic regression model.
- **Logic**: Generates data, splits it, and trains a model.
- **Complexity**: O(n) for n samples (model-dependent).
- **Use Case**: Used for classification or regression tasks.
- **Best Practice**: Preprocess data; tune models; evaluate performance.