# 0120-Turtle-Graphics Cheatsheet

- **Purpose**: draw geometric shapes using the standard `turtle` library.
- **Key functions**: `forward`, `backward`, `right`, `left`, `penup`, `pendown`.
- **Auto‑close**: call `turtle.bye()` to programmatically close the window.
- **Headless note**: catches `TurtleGraphicsError` if no display is present.

```python
from turtle_graphics import draw_spiral

# normal run
draw_spiral()

# during automated tests, close automatically
draw_spiral(auto_close=True)
```

- Useful for teaching geometry or simple animations.

