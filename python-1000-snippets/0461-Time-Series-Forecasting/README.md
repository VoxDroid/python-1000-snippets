# Time Series Forecasting

## Description
This snippet shows basic time series forecasting patterns using lag features and scikit-learn models.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Linear forecast MSE: 0.0755
Example true vs predicted:
  4.572 -> 4.920
  4.880 -> 4.382
  4.303 -> 4.787
```

## Explanation
- **Forecasting**: Predicts future values given past observations.
- **sample1.py**: Uses linear regression with lag features.
- **sample2.py**: A non-linear model using a random forest regressor.
- **sample3.py**: A simple persistence baseline (predict last value).
- **Best Practice**: Use proper train/test splits, cross-validation, and feature scaling.
