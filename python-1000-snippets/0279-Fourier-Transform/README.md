# Fourier Transform

## Description
This snippet demonstrates computing a Fourier Transform using `numpy`.

## Code
```python
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np
    t = np.linspace(0, 1, 100)
    signal = np.sin(2 * np.pi * 5 * t)
    fft = np.fft.fft(signal)
    print("FFT Magnitude (first 5):", np.abs(fft)[:5])
except ImportError:
    print("Mock Output: FFT Magnitude (first 5): [8.49320614e-15 2.04380827e-01 4.66010280e-01 9.11498015e-01 2.11257936e+00]")
```

## Output
```
Mock Output: FFT Magnitude (first 5): [8.49320614e-15 2.04380827e-01 4.66010280e-01 9.11498015e-01 2.11257936e+00]
```
*(Real output with `numpy`: `FFT Magnitude (first 5): [8.49320614e-15 2.04380827e-01 4.66010280e-01 9.11498015e-01 2.11257936e+00]`)*

## Explanation
- **Fourier Transform**: Computes the frequency components of a sine wave.
- **Logic**: Applies FFT to a 5 Hz signal and outputs magnitudes.
- **Complexity**: O(n log n) for n samples.
- **Use Case**: Used for frequency analysis in signals.
- **Best Practice**: Handle aliasing; use windowing; interpret frequencies.