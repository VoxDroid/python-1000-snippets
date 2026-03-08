# sample1.py
# draw a spiral and exit automatically

try:
    import turtle
except ModuleNotFoundError:
    turtle = None


def draw_spiral(auto_close=True):
    if turtle is None:
        print("turtle not available")
        return
    try:
        t = turtle.Turtle()
        for i in range(50):
            t.forward(i / 5)
            t.right(45)
        if auto_close:
            turtle.bye()
    except Exception:
        print("headless or other turtle error")

if __name__ == '__main__':
    draw_spiral()
