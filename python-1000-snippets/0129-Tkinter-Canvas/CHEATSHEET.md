# 0129-Tkinter-Canvas Cheatsheet

- **Purpose**: draw shapes on a `tk.Canvas` inside a Tkinter window.
- **Import guard**: use `try/except` for environments lacking tkinter.
- **Auto-close**: schedule `root.after(...)` to destroy the window automatically.

```python
try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None
if tk:
    r = tk.Tk(); c = tk.Canvas(r, width=100, height=100); c.pack()
    c.create_line(0,0,50,50); r.after(20,r.destroy); r.mainloop()
```

- Methods: `create_rectangle`, `create_oval`, `create_line`, etc.
- To capture image, use `canvas.postscript` then convert with PIL/ external tool.
- Combine with event bindings (`<Button-1>`) for interactivity.

