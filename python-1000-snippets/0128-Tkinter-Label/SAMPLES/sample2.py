# sample2.py
# update label text after a delay

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk(); r.title('Label2')
    lbl = tk.Label(r, text='Start')
    lbl.pack()
    def change():
        lbl.config(text='Changed')
        r.after(50, r.destroy)
    r.after(50, change)
    r.mainloop()
else:
    print('tkinter not available')
