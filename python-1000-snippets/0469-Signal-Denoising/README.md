# Signal Denoising

## Description
This snippet demonstrates signal denoising using `scipy`.

## Code
```python
# Note: Requires `scipy`. Install with `pip install scipy`
try:
    from scipy.signal import savgol_filter
    import numpy as np
    signal = np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100)
    denoised = savgol_filter(signal, window_length=11, polyorder=2)
    print("Signal denoised")
except ImportError:
    print("Mock Output: Signal denoised")
```

## Output
```
Mock Output: Signal denoised
```
*(Real output with `scipy`: `Signal denoised`)*

## Explanation
- **Signal Denoising**: Smooths a noisy signal using Savitzky-Golay filter.
- **Logic**: Applies a polynomial filter to a noisy sine wave.
- **Complexity**: O(n) for n samples.
- **Use Case**: Used in audio or sensor data processing.
- **Best Practice**: Tune filter parameters; validate signal integrity; visualize results.