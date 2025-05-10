# Memento Pattern

## Description
This snippet implements the Memento pattern to save and restore an object’s state.

## Code
```python
class Memento:
    def __init__(self, state):
        self._state = state
    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = ""
    def set_state(self, state):
        self._state = state
    def create_memento(self):
        return Memento(self._state)
    def restore_memento(self, memento):
        self._state = memento.get_state()
    def get_state(self):
        return self._state

originator = Originator()
originator.set_state("State1")
memento = originator.create_memento()
originator.set_state("State2")
originator.restore_memento(memento)
print("Restored State:", originator.get_state())
```

## Output
```
Restored State: State1
```

## Explanation
- **Memento Pattern**: `Memento` stores `Originator`’s state; `Originator` can save and restore it.
- **Logic**: `create_memento` saves state; `restore_memento` reverts to saved state.
- **Complexity**: O(1) for state operations.
- **Use Case**: Used for undo/redo functionality or checkpoints.
- **Best Practice**: Keep memento immutable; limit state exposure.