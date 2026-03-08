# sample1.py
# open a window then close automatically

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    root = tk.Tk()
    root.title('Test 1')
    root.geometry('200x100')
    root.after(50, root.destroy)
    root.mainloop()
else:
    print('tkinter not available')
