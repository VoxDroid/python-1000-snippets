# sample3.py
# toggle button label each time invoked

try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

if tk:
    r = tk.Tk(); r.title('Toggle')
    state = {'on': False}
    def toggle():
        state['on'] = not state['on']
        btn.config(text='On' if state['on'] else 'Off')
        print('state', state['on'])
    btn = tk.Button(r, text='Off', command=toggle)
    btn.pack()
    # simulate two toggles
    r.after(50, btn.invoke)
    r.after(100, btn.invoke)
    r.after(150, r.destroy)
    r.mainloop()
else:
    print('tkinter not available')
