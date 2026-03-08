# sample3.py
# using functions as observers (callbacks)

class Subject:
    def __init__(self):
        self._callbacks = []
    def register(self, func):
        self._callbacks.append(func)
    def notify(self, data):
        for func in self._callbacks:
            func(data)

if __name__ == '__main__':
    subj = Subject()
    subj.register(lambda d: print('lambda received', d))
    def handler(x):
        print('handler got', x)
    subj.register(handler)
    subj.notify('event')
