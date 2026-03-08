# 0127-Tkinter-Entry Cheatsheet

- **Purpose**: capture text input from the user via `tk.Entry`.
- **Key methods**: `entry.get()` retrieves current text; `entry.insert` pre-fills.
- **Import guard**: wrap tkinter import to handle missing module.
- **Simulation**: use `entry.insert(...)` and `button.invoke()` for automated tests; schedule `root.destroy()`.

```python
try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk()
    e = tk.Entry(r); e.pack()
    b = tk.Button(r, text='ok', command=lambda: print(e.get())); b.pack()
    e.insert(0,'hello'); r.after(10,b.invoke); r.after(20,r.destroy); r.mainloop()
```

- Use labels to describe the field, validate input before processing.

