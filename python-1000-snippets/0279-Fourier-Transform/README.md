# Fourier Transform

## Description
This snippet demonstrates Fourier transform techniques using `numpy`.
It shows how to compute the FFT, reconstruct a signal using inverse FFT, and apply simple frequency-domain filtering.

## Dependencies
- `numpy`

Install with:
```bash
pip install numpy
```

## Samples
- `SAMPLES/sample1.py`: Compute FFT of a sine wave and identify the peak frequency.
- `SAMPLES/sample2.py`: Reconstruct a signal using inverse FFT and verify reconstruction error.
- `SAMPLES/sample3.py`: Apply a simple frequency-domain low-pass filter by zeroing FFT coefficients.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- FFT converts a time-domain signal to frequency domain; inverse FFT converts it back.
- Frequency bins correspond to `np.fft.rfftfreq(n, d=1/rate)`.
- Filtering in the frequency domain is done by scaling or zeroing FFT coefficients.
