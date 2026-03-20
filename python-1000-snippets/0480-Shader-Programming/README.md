# Shader Programming

## Description
This snippet demonstrates the core idea behind shader-based image generation using pure Python.
Instead of using a GPU library, it computes pixel colors in software and writes a simple PPM image.

## Code
The sample scripts show how to:
- Compute a procedural "shader" function over a grid of pixels
- Save an image as a PPM file (plain text image format)
- Print sampled shader output values

Run a sample:
```bash
python python-1000-snippets/0480-Shader-Programming/SAMPLES/sample1.py
```

## Output
Running `sample1.py` produces a file such as:
```
temp/shader_output.ppm
```
The file is a plain PPM image and can be opened by many image viewers.

Running `sample2.py` prints samples of the shader function, e.g.:
```
shader(0.10,0.20) -> (75, 143, 199)
shader(0.50,0.50) -> (254, 254, 35)
shader(0.90,0.10) -> (108, 75, 35)
```
(Values may vary if the shader math is changed.)

## Explanation
- **Shader Programming (CPU)**: We implement the logic of a fragment shader in Python using math on normalized pixel coordinates.
- **Logic**: Convert pixel positions into normalized UV coordinates, evaluate a function, and map the result to RGB.
- **Complexity**: O(width*height) for image generation.
- **Use Case**: Useful for procedural texture generation and testing shader logic without GPU dependencies.
- **Tip**: PPM is an easy text-based format, making it ideal for exploring image generation without external libraries.
