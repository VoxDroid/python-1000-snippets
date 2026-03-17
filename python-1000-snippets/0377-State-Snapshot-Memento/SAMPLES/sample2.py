# sample2.py
# Caretaker storing a history of mementos for undo functionality

class Memento:
    def __init__(self, state):
        self.state = state


class Originator:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def save(self):
        return Memento(self.state)

    def restore(self, memento):
        self.state = memento.state


class Caretaker:
    def __init__(self):
        self.history = []

    def backup(self, memento):
        self.history.append(memento)

    def undo(self):
        if not self.history:
            return None
        return self.history.pop()


def main():
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("A")
    caretaker.backup(originator.save())

    originator.set_state("B")
    caretaker.backup(originator.save())

    originator.set_state("C")
    memento = caretaker.undo()
    originator.restore(memento)

    print(originator.state)


if __name__ == "__main__":
    main()
