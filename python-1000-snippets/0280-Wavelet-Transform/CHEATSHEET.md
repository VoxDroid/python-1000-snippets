# 0280 - Wavelet Transform Cheatsheet

## Quick Commands
```bash
pip install numpy pywavelets
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use `pywt.wavedec(signal, wavelet, level)` to decompose and `pywt.waverec(coeffs, wavelet)` to reconstruct.
- Denoising can be done with soft thresholding: `pywt.threshold(coeff, threshold, mode='soft')`.
- The Haar wavelet is a simple orthogonal wavelet; pairwise averages/differences implement it.
