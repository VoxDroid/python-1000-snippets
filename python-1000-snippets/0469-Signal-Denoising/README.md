# Signal Denoising

## Description
This snippet demonstrates basic signal denoising techniques using SciPy and NumPy.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Noisy signal sample: [0.441, 0.132, 0.308, 0.655, 0.593]
Denoised signal sample: [0.397, 0.365, 0.34, 0.322, 0.311]
```

## Explanation
- **Signal Denoising**: Reduces noise while preserving important signal characteristics.
- **sample1.py**: Uses a Savitzky-Golay filter for smoothing.
- **sample2.py**: Uses a Wiener filter for adaptive noise reduction.
- **sample3.py**: Uses a simple moving-average low-pass filter.
- **Best Practice**: Choose filter parameters based on noise characteristics and validate against clean signals.
