# 0125-Tkinter-Window Cheatsheet

- **Purpose**: open a basic Tkinter window with a title and size.
- **Import guard**: wrap `import tkinter as tk` in `try/except` to handle environments without Tk.
- **Auto-close**: use `root.after(ms, root.destroy)` to exit automatically in scripts/tests.

```python
try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk(); r.title('Hello'); r.geometry('200x100')
    r.after(100, r.destroy); r.mainloop()
``` 

- Useful as a starting point for GUI apps; add widgets via `tk.Button`, `tk.Label`, etc.
- In CI or headless servers the code will print "tkinter not available" instead.

