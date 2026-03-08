# 0126-Tkinter-Button Cheatsheet

- **Purpose**: place a clickable button in a Tkinter window and attach a callback.
- **Import guard**: use `try/except ModuleNotFoundError` for headless compatibility.
- **Simulate click**: call `button.invoke()` programmatically; schedule `root.destroy()` to auto-close.

```python
try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    def on_click(): print('clicked')
    r = tk.Tk(); b = tk.Button(r, text='OK', command=on_click); b.pack()
    r.after(10, b.invoke); r.after(20, r.destroy); r.mainloop()
```

- Useful for GUIs, forms or triggering actions.
- Add multiple buttons or change `command` dynamically.

