# Naive Bayes Classifier

## Description
This snippet demonstrates a Naive Bayes classifier using `scikit-learn`.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.datasets import make_classification
    from sklearn.naive_bayes import GaussianNB
    X, y = make_classification(n_samples=100)
    model = GaussianNB()
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
- **Naive Bayes Classifier**: Trains a Gaussian Naive Bayes model.
- **Logic**: Fits a model assuming Gaussian feature distributions.
- **Complexity**: O(n * d) for n samples, d features.
- **Use Case**: Used for text classification or simple datasets.
- **Best Practice**: Handle feature independence; preprocess data; evaluate performance.