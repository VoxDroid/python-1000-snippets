# ARIMA Model

## Description
This snippet demonstrates fitting an ARIMA model to synthetic time series data using `statsmodels`.
It shows how to train the model, generate forecasts, and inspect residuals.

## Dependencies
- `statsmodels`
- `numpy`

Install with:
```bash
pip install statsmodels numpy
```

## Samples
- `SAMPLES/sample1.py`: Fit an ARIMA(1,0,0) model to AR(1) data and print AIC.
- `SAMPLES/sample2.py`: Fit an ARIMA model and forecast future values with confidence intervals.
- `SAMPLES/sample3.py`: Inspect residuals from the fitted ARIMA model.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- ARIMA models are used for forecasting time series by combining autoregression (AR), integration (I), and moving average (MA).
- For real data, check stationarity and difference series as needed.
