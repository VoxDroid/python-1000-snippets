# sample3.py
# random walk turtle example

import random
try:
    import turtle
except ModuleNotFoundError:
    turtle = None


def random_walk(steps=10):
    if turtle is None:
        print("turtle not available")
        return
    try:
        t = turtle.Turtle()
        for _ in range(steps):
            angle = random.choice([0, 90, 180, 270])
            t.setheading(angle)
            t.forward(20)
        turtle.bye()
    except Exception:
        print("headless or other turtle error")

if __name__ == '__main__':
    random_walk()
