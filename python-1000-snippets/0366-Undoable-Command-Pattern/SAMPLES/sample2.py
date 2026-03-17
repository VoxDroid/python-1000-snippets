# sample2.py
# Command stack for undo functionality

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


class CommandManager:
    def __init__(self):
        self._stack = []

    def execute(self, command, state):
        new_state = command.execute(state)
        self._stack.append((command, state))
        return new_state

    def undo(self, state):
        if not self._stack:
            return state
        command, prev_state = self._stack.pop()
        return command.undo(state)


def main():
    manager = CommandManager()
    state = 0
    state = manager.execute(AddCommand(5), state)
    state = manager.execute(AddCommand(10), state)
    print("state after two commands:", state)

    state = manager.undo(state)
    print("state after undo:", state)


if __name__ == "__main__":
    main()
