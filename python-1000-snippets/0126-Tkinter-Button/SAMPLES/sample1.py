# sample1.py
# single button with simulated click

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    def on_click():
        print("clicked")
    r = tk.Tk(); r.title('Btn1'); r.geometry('200x100')
    b = tk.Button(r, text='Press', command=on_click)
    b.pack()
    r.after(50, b.invoke)
    r.after(100, r.destroy)
    r.mainloop()
else:
    print('tkinter not available')
