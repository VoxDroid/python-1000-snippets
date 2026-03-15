# Wavelet Transform

## Description
This snippet demonstrates wavelet transforms using `pywt` (PyWavelets) and a simple Haar wavelet implementation.

## Dependencies
- `numpy`
- `pywavelets`

Install with:
```bash
pip install numpy pywavelets
```

## Samples
- `SAMPLES/sample1.py`: Decompose a signal using discrete wavelet transform (DWT) and print coefficient lengths.
- `SAMPLES/sample2.py`: Denoise a noisy signal using wavelet thresholding (VisuShrink).
- `SAMPLES/sample3.py`: Implement a simple Haar wavelet transform and inverse transform without external libraries.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Wavelet transforms provide time-frequency localization, useful for denoising and feature extraction.
- `pywt.wavedec` performs multi-level decomposition; `pywt.waverec` reconstructs the signal.
- The Haar transform is the simplest wavelet and can be implemented using pairwise averages and differences.
