# sample3.py
# create two sequential windows

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    w1 = tk.Tk(); w1.title('First'); w1.geometry('150x80')
    w1.after(50, lambda: w1.destroy())
    w1.mainloop()
    w2 = tk.Tk(); w2.title('Second'); w2.geometry('150x80')
    w2.after(50, lambda: w2.destroy())
    w2.mainloop()
else:
    print('tkinter not available')
