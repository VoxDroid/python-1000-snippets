# Image Filtering

## Description
This snippet demonstrates applying a blur filter to an image using `Pillow`.

## Code
```python
# Note: Requires `Pillow`. Install with `pip install Pillow`
try:
    from PIL import Image, ImageFilter
    img = Image.new("RGB", (100, 100), color="blue")
    blurred = img.filter(ImageFilter.BLUR)
    blurred.save("Blurred.png")
    print("Image blurred")
except ImportError:
    print("Mock Output: Image blurred")
```

## Output
<div style="text-align: center;">
  <img src="Blurred.png" alt="Output image">
  <p></p>
</div>

```
Mock Output: Image blurred
```
*(Real output with `Pillow`: `Image blurred`, creates `blurred.png`)*

## Explanation
- **Image Filtering**: Applies a Gaussian blur to an image.
- **Logic**: Creates a blue image and applies a blur filter.
- **Complexity**: O(w*h*k) for w width, h height, k kernel size.
- **Use Case**: Used for smoothing or preprocessing images.
- **Best Practice**: Choose appropriate filters; handle large images; validate output.