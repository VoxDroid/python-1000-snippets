# State Pattern

## Description
This snippet implements the State pattern to manage an object’s behavior based on its state.

## Code
```python
class State:
    def handle(self, context):
        pass

class OnState(State):
    def handle(self, context):
        print("Switching to Off")
        context.state = OffState()

class OffState(State):
    def handle(self, context):
        print("Switching to On")
        context.state = OnState()

class Switch:
    def __init__(self):
        self.state = OffState()
    def flip(self):
        self.state.handle(self)

switch = Switch()
switch.flip()
switch.flip()
```

## Output
```
Switching to On
Switching to Off
```

## Explanation
- **State Pattern**: `Switch` delegates behavior to `OnState` or `OffState`.
- **Logic**: `flip` triggers state transitions by updating `state`.
- **Complexity**: O(1) for state changes.
- **Use Case**: Used for state machines, like UI controls or game states.
- **Best Practice**: Define clear state transitions; avoid state explosion.