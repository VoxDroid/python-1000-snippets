# Wavelet Transform

## Description
This snippet demonstrates computing a Wavelet Transform using `pywt`.

## Code
```python
# Note: Requires `pywt`. Install with `pip install pywavelets`
try:
    import pywt
    import numpy as np
    signal = np.sin(2 * np.pi * 5 * np.linspace(0, 1, 100))
    coeffs = pywt.wavedec(signal, "db1", level=2)
    print("Coefficient Length:", len(coeffs[0]))
except ImportError:
    print("Mock Output: Coefficient Length: 25")
```

## Output
```
Mock Output: Coefficient Length: 25
```
*(Real output with `pywt`: `Coefficient Length: <value around 25>`)*

## Explanation
- **Wavelet Transform**: Decomposes a signal using discrete wavelet transform.
- **Logic**: Applies `db1` wavelet to a sine wave with 2 levels.
- **Complexity**: O(n) for n samples.
- **Use Case**: Used for time-frequency analysis or denoising.
- **Best Practice**: Choose wavelet type; tune levels; reconstruct signals.