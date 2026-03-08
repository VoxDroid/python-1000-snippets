# sample3.py
# using @dataclass for simple classes

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

if __name__ == '__main__':
    p = Point(1.0, 2.0)
    print(p)
    print('x coordinate', p.x)
