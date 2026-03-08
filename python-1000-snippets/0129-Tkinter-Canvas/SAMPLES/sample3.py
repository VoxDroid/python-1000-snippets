# sample3.py
# save canvas postscript to file if tkinter available

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk(); c = tk.Canvas(r, width=100, height=100); c.pack()
    c.create_line(0,0,100,100, fill='black')
    r.update()
    try:
        c.postscript(file='canvas.ps')
        print('saved canvas.ps')
    except Exception:
        pass
    r.after(50, r.destroy)
    r.mainloop()
else:
    print('tkinter not available')
