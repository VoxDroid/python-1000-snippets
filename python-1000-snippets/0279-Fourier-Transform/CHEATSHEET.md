# 0279 - Fourier Transform Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use `np.fft.rfft` for real-valued signals and `np.fft.irfft` to reconstruct.
- Frequency bins: `np.fft.rfftfreq(n, d=1/rate)`.
- A simple low-pass filter can be implemented by zeroing out FFT bins above a cutoff.
