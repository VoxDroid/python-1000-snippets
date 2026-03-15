# Signal Processing

## Description
This snippet demonstrates basic digital signal processing techniques using `numpy`.
It shows how to smooth noisy signals, apply a simple high-pass filter, and filter in the frequency domain using FFT.

## Dependencies
- `numpy`

Install with:
```bash
pip install numpy
```

## Samples
- `SAMPLES/sample1.py`: Smooth a noisy signal using a moving-average filter.
- `SAMPLES/sample2.py`: Apply a high-pass filter by subtracting a moving-average trend.
- `SAMPLES/sample3.py`: Apply a simple FFT-based low-pass filter.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Use `np.convolve` for FIR filters (e.g., moving average).
- FFT filtering works by zeroing out frequency bins.
- These examples are for demonstration; production systems should use robust libraries like SciPy.
