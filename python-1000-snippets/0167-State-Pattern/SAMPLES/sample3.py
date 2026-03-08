# sample3.py
# stopwatch with Running and Stopped states

class State:
    def press(self, watch):
        pass

class Running(State):
    def press(self, watch):
        print('stopping')
        watch.state = Stopped()

class Stopped(State):
    def press(self, watch):
        print('starting')
        watch.state = Running()

class Stopwatch:
    def __init__(self):
        self.state = Stopped()
    def press(self):
        self.state.press(self)

if __name__ == '__main__':
    sw = Stopwatch()
    sw.press()
    sw.press()
