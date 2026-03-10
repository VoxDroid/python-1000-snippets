# sample1.py
# basic memento example (from README)

class Memento:
    def __init__(self, state):
        self._state = state
    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = ""
    def set_state(self, state):
        self._state = state
    def create_memento(self):
        return Memento(self._state)
    def restore_memento(self, memento):
        self._state = memento.get_state()
    def get_state(self):
        return self._state

if __name__ == '__main__':
    originator = Originator()
    originator.set_state("State1")
    memento = originator.create_memento()
    originator.set_state("State2")
    originator.restore_memento(memento)
    print("Restored State:", originator.get_state())
