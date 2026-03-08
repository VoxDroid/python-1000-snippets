# sample2.py
# change the window title dynamically

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    root = tk.Tk()
    root.title('Before')
    def rename():
        root.title('After')
        root.after(50, root.destroy)
    root.after(50, rename)
    root.mainloop()
else:
    print('tkinter not available')
