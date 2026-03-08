# sample3.py
# multiple entries and a submit button

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    def on_submit():
        print('a=', e1.get(), 'b=', e2.get())
    root = tk.Tk()
    e1 = tk.Entry(root); e1.pack()
    e2 = tk.Entry(root); e2.pack()
    btn = tk.Button(root, text='OK', command=on_submit); btn.pack()
    e1.insert(0,'1'); e2.insert(0,'2')
    root.after(50, btn.invoke)
    root.after(100, root.destroy)
    root.mainloop()
else:
    print('tkinter not available')
