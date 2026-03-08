# sample1.py
# simple label display

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk(); r.title('Label1')
    tk.Label(r, text='Hello').pack()
    r.after(50, r.destroy)
    r.mainloop()
else:
    print('tkinter not available')
