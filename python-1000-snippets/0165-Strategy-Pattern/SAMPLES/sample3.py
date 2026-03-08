# sample3.py
# strategy pattern using callable objects

class Add:
    def __call__(self, a, b):
        return a + b

class Multiply:
    def __call__(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    def execute(self, a, b):
        return self.strategy(a, b)

if __name__ == '__main__':
    ctx = Context(Add())
    print(ctx.execute(2, 3))
    ctx.strategy = Multiply()
    print(ctx.execute(2, 3))
