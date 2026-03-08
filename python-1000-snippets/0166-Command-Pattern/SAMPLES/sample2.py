# sample2.py
# command with undo functionality

class Command:
    def execute(self):
        pass
    def undo(self):
        pass

class AddCommand(Command):
    def __init__(self, value, receiver):
        self.value = value
        self.receiver = receiver
    def execute(self):
        self.receiver['total'] += self.value
    def undo(self):
        self.receiver['total'] -= self.value

if __name__ == '__main__':
    r = {'total': 0}
    cmd = AddCommand(5, r)
    cmd.execute()
    print('after execute', r)
    cmd.undo()
    print('after undo', r)
