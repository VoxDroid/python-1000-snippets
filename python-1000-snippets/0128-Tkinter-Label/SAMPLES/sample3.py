# sample3.py
# multiple labels stacked

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk(); r.title('Labels')
    for text in ('One','Two','Three'):
        tk.Label(r, text=text).pack()
    r.after(50, r.destroy)
    r.mainloop()
else:
    print('tkinter not available')
