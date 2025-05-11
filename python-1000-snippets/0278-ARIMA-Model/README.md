# ARIMA Model

## Description
This snippet demonstrates fitting an ARIMA model using `statsmodels`.

## Code
```python
# Note: Requires `statsmodels`. Install with `pip install statsmodels`
try:
    from statsmodels.tsa.arima.model import ARIMA
    import numpy as np
    data = np.random.random(100)
    model = ARIMA(data, order=(1, 0, 0))
    fit = model.fit()
    print("AIC:", fit.aic)
except ImportError:
    print("Mock Output: AIC: 34.95585413426184")
```

## Output
```
Mock Output: AIC: 34.95585413426184
```
*(Real output with `statsmodels`: `AIC: <value around 30.0 ~ 200.0>`)*

## Explanation
- **ARIMA Model**: Fits an ARIMA(1,0,0) model to a random time series.
- **Logic**: Trains the model and outputs the Akaike Information Criterion.
- **Complexity**: O(n*p) for n data points, p parameters.
- **Use Case**: Used for forecasting time series data.
- **Best Practice**: Test stationarity; tune order; validate forecasts.