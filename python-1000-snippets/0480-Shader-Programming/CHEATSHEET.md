# 0480-Shader-Programming Cheatsheet

## Quick Start
- Run a sample:
  ```bash
  python python-1000-snippets/0480-Shader-Programming/SAMPLES/sample1.py
  ```

## Concepts
- A "shader" maps UV coordinates (normalized pixel positions) to color values.
- This snippet uses CPU loops (or NumPy) to compute pixel colors.

## File Output
- `temp/shader_output.ppm` is a plain-text image format that can be opened by many viewers.

## Tips
- Modify `generate_shader_image` (in `sample1.py`) to experiment with wave patterns, noise, and color ramps.
- PPM is good for quick prototyping without external image libraries.
