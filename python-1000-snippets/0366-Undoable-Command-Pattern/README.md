# Undoable Command Pattern

## Description
This snippet demonstrates the command pattern with undo functionality.

## Code
```python
class Command:
    def execute(self):
        pass
    def undo(self):
        pass

class AddCommand(Command):
    def __init__(self, value):
        self.value = value
        self.previous = None
    
    def execute(self, state):
        self.previous = state
        return state + self.value
    
    def undo(self):
        return self.previous

state = 10
command = AddCommand(5)
state = command.execute(state)
print("After execute:", state)
state = command.undo()
print("After undo:", state)
```

## Output
```
After execute: 15
After undo: 10
```

## Explanation
- **Undoable Command Pattern**: Executes and undoes commands.
- **Logic**: `AddCommand` adds a value and stores state for undoing.
- **Complexity**: O(1) per operation.
- **Use Case**: Used in editors or transactional systems.
- **Best Practice**: Store minimal state; ensure reversibility; test undo logic.