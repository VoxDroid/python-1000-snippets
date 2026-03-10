# sample3.py
# drawing positions with mementos for rollback

class PositionMemento:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, x, y):
        self.x = x
        self.y = y
    def save(self):
        return PositionMemento(self.x, self.y)
    def restore(self, m):
        self.x = m.x
        self.y = m.y
    def __str__(self):
        return f"Shape at ({self.x},{self.y})"

if __name__ == '__main__':
    s = Shape()
    s.move(10, 10)
    m = s.save()
    s.move(20, 20)
    print('moved to', s)
    s.restore(m)
    print('restored to', s)
