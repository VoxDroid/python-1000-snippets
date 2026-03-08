# sample1.py
# simple switch state machine (from README)

class State:
    def handle(self, context):
        pass

class OnState(State):
    def handle(self, context):
        print("Switching to Off")
        context.state = OffState()

class OffState(State):
    def handle(self, context):
        print("Switching to On")
        context.state = OnState()

class Switch:
    def __init__(self):
        self.state = OffState()
    def flip(self):
        self.state.handle(self)

if __name__ == '__main__':
    switch = Switch()
    switch.flip()
    switch.flip()
