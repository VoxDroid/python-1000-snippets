# 0469-Signal-Denoising Cheatsheet

## Quick Tips
- Savitzky-Golay is good for smoothing while preserving local features (peaks/edges).
- Wiener filtering adapts to local noise statistics and works well for stationary noise.
- Moving average filters are simple low-pass filters; choose window size based on signal bandwidth.

## Running examples
- `python SAMPLES/sample1.py` — Savitzky-Golay smoothing.
- `python SAMPLES/sample2.py` — Wiener filter denoising.
- `python SAMPLES/sample3.py` — moving-average low-pass filter.
