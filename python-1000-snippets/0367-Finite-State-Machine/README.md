# Finite State Machine

## Description
This snippet demonstrates a finite state machine for a simple lock.

## Code
```python
class Lock:
    def __init__(self):
        self.state = "locked"
    
    def enter(self, action):
        if self.state == "locked" and action == "unlock":
            self.state = "unlocked"
        elif self.state == "unlocked" and action == "lock":
            self.state = "locked"
        return self.state

lock = Lock()
print(lock.enter("unlock"))
print(lock.enter("lock"))
```

## Output
```
unlocked
locked
```

## Explanation
- **Finite State Machine**: Models a lock with locked/unlocked states.
- **Logic**: Transitions states based on actions.
- **Complexity**: O(1) per transition.
- **Use Case**: Used for protocol modeling or UI navigation.
- **Best Practice**: Define clear states; validate transitions; document FSM.