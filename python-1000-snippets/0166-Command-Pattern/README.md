# Command Pattern

## Description
This snippet implements the Command pattern to encapsulate actions as objects.

## Code
```python
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

remote = RemoteControl()
remote.set_command(LightOnCommand())
print(remote.press_button())
remote.set_command(LightOffCommand())
print(remote.press_button())
```

## Output
```
Light turned on
Light turned off
```

## Explanation
- **Command Pattern**: Encapsulates actions (`LightOnCommand`, `LightOffCommand`) as objects.
- **Logic**: `RemoteControl` invokes commands via `press_button`.
- **Complexity**: O(1) for execution.
- **Use Case**: Used for undo/redo, queuing tasks, or remote controls.
- **Best Practice**: Support undo operations; ensure commands are lightweight.