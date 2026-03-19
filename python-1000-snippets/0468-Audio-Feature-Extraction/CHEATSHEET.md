# 0468-Audio-Feature-Extraction Cheatsheet

## Quick Tips
- RMS measures the energy of a signal; zero-crossing rate is a simple proxy for noisiness.
- Spectral centroid is the "center of mass" of the spectrum and correlates with perceived brightness.
- Use windowing (e.g., Hann window) when computing short-time Fourier transforms.

## Running examples
- `python SAMPLES/sample1.py` — compute RMS and zero-crossing rate.
- `python SAMPLES/sample2.py` — compute spectral centroid and bandwidth.
- `python SAMPLES/sample3.py` — compute a simple spectrogram and energy per frame.
