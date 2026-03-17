# sample3.py
# Composite command that aggregates multiple sub-commands

class Command:
    def execute(self, state):
        raise NotImplementedError

    def undo(self, state):
        raise NotImplementedError


class AddCommand(Command):
    def __init__(self, value):
        self.value = value

    def execute(self, state):
        return state + self.value

    def undo(self, state):
        return state - self.value


class CompositeCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self, state):
        for cmd in self.commands:
            state = cmd.execute(state)
        return state

    def undo(self, state):
        for cmd in reversed(self.commands):
            state = cmd.undo(state)
        return state


def main():
    composite = CompositeCommand([AddCommand(3), AddCommand(7)])
    state = 0
    state = composite.execute(state)
    print("after execute:", state)
    state = composite.undo(state)
    print("after undo:", state)


if __name__ == "__main__":
    main()
