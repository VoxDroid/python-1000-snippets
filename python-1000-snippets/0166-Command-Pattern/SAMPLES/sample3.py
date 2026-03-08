# sample3.py
# macro command that runs multiple commands

class Command:
    def execute(self):
        pass

class PrintCommand(Command):
    def __init__(self, msg):
        self.msg = msg
    def execute(self):
        print(self.msg)

class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands
    def execute(self):
        for c in self.commands:
            c.execute()

if __name__ == '__main__':
    mc = MacroCommand([PrintCommand('one'), PrintCommand('two')])
    mc.execute()
