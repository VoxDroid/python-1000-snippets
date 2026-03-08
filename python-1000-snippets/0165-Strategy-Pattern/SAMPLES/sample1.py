# sample1.py
# basic add/multiply strategy example (from README)

class Strategy:
    def execute(self, a, b):
        pass

class Add(Strategy):
    def execute(self, a, b):
        return a + b

class Multiply(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    def set_strategy(self, strategy):
        self.strategy = strategy
    def execute(self, a, b):
        return self.strategy.execute(a, b)

if __name__ == '__main__':
    context = Context(Add())
    print('Add:', context.execute(5, 3))
    context.set_strategy(Multiply())
    print('Multiply:', context.execute(5, 3))
