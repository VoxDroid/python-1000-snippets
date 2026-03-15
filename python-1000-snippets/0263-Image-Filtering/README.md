# Image Filtering

## Description
This snippet demonstrates applying filtering operations to images using Pillow and NumPy.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — applies a built-in blur filter.
- `sample2.py` — applies a custom sharpen kernel using Pillow's `Kernel` filter.
- `sample3.py` — implements convolution manually using NumPy for edge detection.

Run a sample with:

```bash
python python-1000-snippets/0263-Image-Filtering/SAMPLES/sample1.py
```

## Output
Each sample saves filtered images (e.g., `filtered_blur.png`, `filtered_sharpen.png`) and prints a status message.

## Notes
- Image filtering can be done with built-in filters or custom kernels.
- Manual convolution gives insight into how filtering works, but is slower than optimized libraries.
