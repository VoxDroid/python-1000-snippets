# sample1.py
# Basic memento pattern with a single state value

class Memento:
    def __init__(self, state):
        self.state = state


class Originator:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def restore_memento(self, memento):
        self.state = memento.state


def main():
    originator = Originator()
    originator.set_state("State1")
    memento = originator.create_memento()
    originator.set_state("State2")
    originator.restore_memento(memento)
    print(originator.state)


if __name__ == "__main__":
    main()
