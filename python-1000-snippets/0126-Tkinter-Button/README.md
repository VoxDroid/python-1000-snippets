# Tkinter Button

## Description
This snippet adds a clickable button to a Tkinter window that prints a message when clicked.

## Code
```python
try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None

def on_click():
    print("Button clicked!")

if tk:
    root = tk.Tk()
    root.title("Tkinter Button")
    root.geometry("400x300")
    button = tk.Button(root, text="Click Me", command=on_click)
    button.pack()
    # simulate a press and close soon after
    root.after(50, button.invoke)
    root.after(100, root.destroy)
    root.mainloop()
else:
    print("tkinter not available")
```

## Output
<div style="text-align: center;">
  <img src="Output.png" alt="Output image">
  <p></p>
</div>

*(Visual Output)*: A 400x300 window with a "Click Me" button; clicking prints to console:
```
Button clicked!
```
In headless environments tkinter may be missing; the script will print a message and exit.

## Explanation
- **Tkinter Button**: `tk.Button` creates a button; `command` links to a callback (`on_click`).
- **pack**: Adds the button to the window.
- **Complexity**: O(1) per event.
- **Use Case**: Used in interactive GUIs.
- **Best Practice**: Customize button appearance; handle multiple buttons.