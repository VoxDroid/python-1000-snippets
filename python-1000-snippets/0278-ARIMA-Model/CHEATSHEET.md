# 0278 - ARIMA Model Cheatsheet

## Quick Commands
```bash
pip install statsmodels numpy
python SAMPLES/sample1.py  # Fit ARIMA and print AIC
python SAMPLES/sample2.py  # Forecast next values
python SAMPLES/sample3.py  # Inspect residuals
```

## Tips
- ARIMA(order=(p,d,q)) combines:
  - AR(p): autoregression on past values.
  - I(d): differencing for stationarity.
  - MA(q): moving average of residuals.
- Use `fit.get_forecast(steps=n)` for forecasts and confidence intervals.
- Examine residuals for white noise behavior.
