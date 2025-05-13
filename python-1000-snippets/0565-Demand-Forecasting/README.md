# Demand Forecasting

## Description
This snippet demonstrates demand forecasting using a simple linear model.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.linear_model import LinearRegression
    import numpy as np
    X = np.array([[1], [2], [3]])
    y = np.array([10, 12, 14])
    model = LinearRegression().fit(X, y)
    print("Forecasted demand:", int(model.predict([[4]])[0]))
except ImportError:
    print("Mock Output: Forecasted demand: 16")
```

## Output
```
Mock Output: Forecasted demand: 16
```
*(Real output with `scikit-learn`: `Forecasted demand: 16`)*

## Explanation
- **Demand Forecasting**: Predicts future demand using historical data.
- **Logic**: Fits a linear model to time series data.
- **Complexity**: O(n) for n samples.
- **Use Case**: Used in retail or supply chain planning.
- **Best Practice**: Use time series models; validate forecasts; handle seasonality.