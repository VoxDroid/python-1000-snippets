# Image Filtering Cheatsheet

## Key Concepts
- Filtering is a form of convolution: output pixel = weighted sum of neighborhood pixels.
- Pillow provides built-in filters (`ImageFilter.BLUR`, `ImageFilter.SHARPEN`) and custom kernels via `ImageFilter.Kernel`.
- Implementing convolution manually in NumPy helps understand filter behavior.

## Running Samples
```bash
python python-1000-snippets/0263-Image-Filtering/SAMPLES/sample1.py
python python-1000-snippets/0263-Image-Filtering/SAMPLES/sample2.py
python python-1000-snippets/0263-Image-Filtering/SAMPLES/sample3.py
```

## Tips
- Use `ImageFilter.Kernel` to apply custom 3x3 or larger kernels.
- When implementing convolution manually, pay attention to padding and output size.
- Edge detection kernels (Sobel, Prewitt) highlight intensity changes.
