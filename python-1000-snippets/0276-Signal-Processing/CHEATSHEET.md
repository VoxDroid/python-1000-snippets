# 0276 - Signal Processing Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Moving average: `np.convolve(signal, np.ones(n)/n, mode='same')`.
- High-pass (trend removal): subtract a slow-moving average from the signal.
- FFT-based filtering: zero-out bins in `np.fft.rfft(signal)` beyond a cutoff frequency.
