# 0461-Time-Series-Forecasting Cheatsheet

## Quick Tips
- Convert a time series into a supervised learning problem by using lagged values as features.
- Always keep the time order (no random shuffling) when splitting train/test sets for forecasting.
- Compare to a persistence baseline (predict last known value) to ensure your model adds value.

## Running examples
- `python SAMPLES/sample1.py` — linear regression forecast with lag features.
- `python SAMPLES/sample2.py` — random forest forecast.
- `python SAMPLES/sample3.py` — persistence baseline.
