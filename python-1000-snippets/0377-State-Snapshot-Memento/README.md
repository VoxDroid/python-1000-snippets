# State Snapshot Memento

## Description
This snippet demonstrates the memento pattern to save and restore state.

## Code
```python
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

originator = Originator()
originator.set_state("State1")
memento = originator.create_memento()
originator.set_state("State2")
originator.restore_memento(memento)
print(originator.state)
```

## Output
```
State1
```

## Explanation
- **State Snapshot Memento**: Saves and restores an object’s state.
- **Logic**: `Originator` creates a `Memento` to store state and restores it later.
- **Complexity**: O(1) per operation.
- **Use Case**: Used for undo functionality in editors or games.
- **Best Practice**: Protect memento access; minimize state size; test restoration.