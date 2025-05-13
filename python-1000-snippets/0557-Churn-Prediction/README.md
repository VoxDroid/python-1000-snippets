# Churn Prediction

## Description
This snippet demonstrates churn prediction using logistic regression.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.linear_model import LogisticRegression
    import numpy as np
    X = np.array([[1, 2], [2, 3], [3, 4]])
    y = np.array([0, 0, 1])
    model = LogisticRegression().fit(X, y)
    print("Prediction:", model.predict([[4, 5]])[0])
except ImportError:
    print("Mock Output: Prediction: 1")
```

## Output
```
Mock Output: Prediction: 1
```
*(Real output with `scikit-learn`: `Prediction: 1`)*

## Explanation
- **Churn Prediction**: Predicts customer churn using a model.
- **Logic**: Trains a logistic regression model on sample data.
- **Complexity**: O(n*m) for n samples, m features.
- **Use Case**: Used in retention strategies.
- **Best Practice**: Balance classes; validate model; use real data.