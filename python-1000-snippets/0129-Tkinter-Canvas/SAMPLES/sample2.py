# sample2.py
# draw multiple rectangles with different colors

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk(); c = tk.Canvas(r, width=200, height=150); c.pack()
    colors = ['red','green','blue']
    for i,color in enumerate(colors):
        c.create_rectangle(10+i*30,10,30+i*30,40, fill=color)
    r.after(50, r.destroy)
    r.mainloop()
else:
    print('tkinter not available')
