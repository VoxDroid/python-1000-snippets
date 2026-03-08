# sample2.py
# two buttons with different callbacks

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    def a(): print('A')
    def b(): print('B')
    r = tk.Tk(); r.title('TwoBtn')
    btnA = tk.Button(r, text='A', command=a); btnA.pack()
    btnB = tk.Button(r, text='B', command=b); btnB.pack()
    r.after(50, btnA.invoke)
    r.after(100, btnB.invoke)
    r.after(150, r.destroy)
    r.mainloop()
else:
    print('tkinter not available')
