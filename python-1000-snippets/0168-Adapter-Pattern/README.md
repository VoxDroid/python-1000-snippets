# Adapter Pattern

## Description
This snippet implements the Adapter pattern to make an incompatible interface compatible.

## Code
```python
class OldSystem:
    def old_request(self):
        return "Old system response"

class NewSystem:
    def new_request(self):
        pass

class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system
    def new_request(self):
        return self.old_system.old_request()

old = OldSystem()
adapter = Adapter(old)
print(adapter.new_request())
```

## Output
```
Old system response
```

## Explanation
- **Adapter Pattern**: `Adapter` makes `OldSystem` compatible with `NewSystem`’s interface.
- **Logic**: Wraps `old_request` to match `new_request`.
- **Complexity**: O(1) for method calls.
- **Use Case**: Used to integrate legacy code or third-party libraries.
- **Best Practice**: Keep adapters simple; document compatibility requirements.