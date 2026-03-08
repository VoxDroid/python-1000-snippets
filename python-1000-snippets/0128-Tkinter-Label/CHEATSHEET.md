# 0128-Tkinter-Label Cheatsheet

- **Purpose**: display static text using `tk.Label`.
- **Import guard**: use `try/except` to detect absence of tkinter.
- **Auto-close**: schedule `root.after(...)` to destroy window automatically.

```python
try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None
if tk:
    r = tk.Tk(); tk.Label(r, text='Hi').pack(); r.after(50,r.destroy); r.mainloop()
```

- Modify label with `label.config(text='new text')` to update dynamically.
- Combine with other widgets (Entry, Button) for more complex GUIs.

