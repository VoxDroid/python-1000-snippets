# sample1.py
# draw rectangle and oval

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk(); c = tk.Canvas(r, width=200, height=150); c.pack()
    c.create_rectangle(20,20,100,60, fill='red')
    c.create_oval(110,30,150,70, fill='blue')
    r.after(50, r.destroy)
    r.mainloop()
else:
    print('tkinter not available')
