# Image Processing

## Description
This snippet demonstrates basic image processing using `Pillow`.

## Code
```python
# Note: Requires `Pillow`. Install with `pip install Pillow`
try:
    from PIL import Image
    img = Image.new("RGB", (100, 100), color="blue")
    img.save("Output.png")
    print("Image created")
except ImportError:
    print("Mock Output: Image created")
```

## Output
<div style="text-align: center;">
  <img src="Output.png" alt="Output image">
  <p></p>
</div>

```
Mock Output: Image created
```
*(Real output with `Pillow`: `Image created`, creates `output.png`)*

## Explanation
- **Image Processing**: Creates a solid blue image using `Pillow`.
- **Logic**: Initializes a 100x100 RGB image and saves it.
- **Complexity**: O(w*h) for w width, h height.
- **Use Case**: Used for image manipulation or preprocessing.
- **Best Practice**: Handle file I/O errors; validate image formats; optimize size.