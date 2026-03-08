# sample1.py
# basic entry with automatic submission

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    def on_submit():
        print('Entered:', entry.get())
    root = tk.Tk()
    entry = tk.Entry(root)
    entry.pack()
    btn = tk.Button(root, text='Submit', command=on_submit)
    btn.pack()
    entry.insert(0,'Test')
    root.after(50, btn.invoke)
    root.after(100, root.destroy)
    root.mainloop()
else:
    print('tkinter not available')
