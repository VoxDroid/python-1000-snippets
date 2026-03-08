# sample3.py
# layered decorators with logging and timing

import time

class Component:
    def operation(self):
        return 'base'

class LoggingDecorator:
    def __init__(self, comp):
        self._comp = comp
    def operation(self):
        print('log: calling operation')
        return self._comp.operation()

class TimingDecorator:
    def __init__(self, comp):
        self._comp = comp
    def operation(self):
        start = time.time()
        result = self._comp.operation()
        print('time', time.time() - start)
        return result

if __name__ == '__main__':
    c = Component()
    c = LoggingDecorator(c)
    c = TimingDecorator(c)
    print(c.operation())
