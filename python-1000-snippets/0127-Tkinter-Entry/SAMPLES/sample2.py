# sample2.py
# entry with default text cleared on submit

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    def on_submit():
        print('Value:', entry.get())
        entry.delete(0, tk.END)
    root = tk.Tk()
    entry = tk.Entry(root)
    entry.pack()
    btn = tk.Button(root, text='Go', command=on_submit)
    btn.pack()
    entry.insert(0,'Hello')
    root.after(50, btn.invoke)
    root.after(100, root.destroy)
    root.mainloop()
else:
    print('tkinter not available')
