# Shader Programming

## Description
This snippet demonstrates a simple shader setup using `moderngl`.

## Code
```python
# Note: Requires `moderngl`. Install with `pip install moderngl`
try:
    import moderngl
    ctx = moderngl.create_standalone_context()
    vertex_shader = """
    #version 330
    in vec2 in_vert;
    void main() {
        gl_Position = vec4(in_vert, 0.0, 1.0);
    }
    """
    fragment_shader = """
    #version 330
    out vec4 fragColor;
    void main() {
        fragColor = vec4(1.0);
    }
    """
    program = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
    print("Shader program created")
except ImportError:
    print("Mock Output: Shader program created")
```

## Output
```
Mock Output: Shader program created
```
*(Real output with `moderngl`: `Shader program created`)*

## Explanation
- **Shader Programming**: Sets up a basic vertex shader.
- **Logic**: Creates a ModernGL context and compiles a shader.
- **Complexity**: O(1) for setup.
- **Use Case**: Used in real-time graphics rendering.
- **Best Practice**: Validate shaders; handle errors; test rendering pipeline.