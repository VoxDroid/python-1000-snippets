# sample2.py
# draw a square

try:
    import turtle
except ModuleNotFoundError:
    turtle = None


def draw_square(size=100):
    if turtle is None:
        print("turtle not available")
        return
    try:
        t = turtle.Turtle()
        for _ in range(4):
            t.forward(size)
            t.right(90)
        turtle.bye()
    except Exception:
        print("headless or other turtle error")

if __name__ == '__main__':
    draw_square()
