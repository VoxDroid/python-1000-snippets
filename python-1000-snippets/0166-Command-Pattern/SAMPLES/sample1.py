# sample1.py
# basic light on/off commands (from README)

class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def execute(self):
        return "Light turned on"

class LightOffCommand(Command):
    def execute(self):
        return "Light turned off"

class RemoteControl:
    def __init__(self):
        self.command = None
    def set_command(self, command):
        self.command = command
    def press_button(self):
        return self.command.execute()

if __name__ == '__main__':
    remote = RemoteControl()
    remote.set_command(LightOnCommand())
    print(remote.press_button())
    remote.set_command(LightOffCommand())
    print(remote.press_button())
