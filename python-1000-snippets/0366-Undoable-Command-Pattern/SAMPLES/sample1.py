# sample1.py
# Simple undoable add command

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


def main():
    state = 10
    cmd = AddCommand(5)

    state = cmd.execute(state)
    print("After execute:", state)

    state = cmd.undo(state)
    print("After undo:", state)


if __name__ == "__main__":
    main()
