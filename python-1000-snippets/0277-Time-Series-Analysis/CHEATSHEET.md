# 0277 - Time Series Analysis Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py  # moving average
python SAMPLES/sample2.py  # autocorrelation
python SAMPLES/sample3.py  # trend estimation
```

## Tips
- Moving average (window): use cumulative sum for efficient computation.
- Autocorrelation: `np.correlate(x-mean, x-mean, mode='full')` and take second half.
- Trend estimation: use least squares (`np.linalg.lstsq`) to fit a line.
