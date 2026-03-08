# sample2.py
# multiple observers with detach

class Subject:
    def __init__(self):
        self._observers = []
    def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
    def notify(self, msg):
        for o in self._observers:
            o.update(msg)

class PrintObserver:
    def __init__(self, name):
        self.name = name
    def update(self, msg):
        print(self.name, 'got', msg)

if __name__ == '__main__':
    sub = Subject()
    o1 = PrintObserver('A')
    o2 = PrintObserver('B')
    sub.attach(o1)
    sub.attach(o2)
    sub.notify('hello')
    sub.detach(o1)
    sub.notify('world')
