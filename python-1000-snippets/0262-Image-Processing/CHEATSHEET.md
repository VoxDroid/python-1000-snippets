# Image Processing Cheatsheet

## Key Concepts
- Use `Pillow` (PIL) to create, load, transform, and save images.
- Convert images to NumPy arrays for pixel-level analysis (histograms, masks).
- Common operations: `resize()`, `rotate()`, `crop()`, `convert('L')`.

## Running Samples
```bash
python python-1000-snippets/0262-Image-Processing/SAMPLES/sample1.py
python python-1000-snippets/0262-Image-Processing/SAMPLES/sample2.py
python python-1000-snippets/0262-Image-Processing/SAMPLES/sample3.py
```

## Tips
- When rotating, `expand=True` keeps the whole image in view.
- Use `ImageDraw` to add text and shapes to images.
- Use `np.histogram()` on grayscale arrays to analyze brightness distribution.
