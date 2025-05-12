# Interface Adapter

## Description
This snippet demonstrates an adapter to convert incompatible interfaces.

## Code
```python
class OldSystem:
    def old_request(self):
        return "Old response"

class NewSystem:
    def new_request(self):
        pass

class Adapter(NewSystem):
    def __init__(self, old):
        self.old = old
    
    def new_request(self):
        return self.old.old_request()

old = OldSystem()
adapter = Adapter(old)
print(adapter.new_request())
```

## Output
```
Old response
```

## Explanation
- **Interface Adapter**: Adapts an old interface to a new one.
- **Logic**: Wraps `OldSystem` to provide `new_request` method.
- **Complexity**: O(1) per call.
- **Use Case**: Used to integrate legacy systems with new code.
- **Best Practice**: Ensure interface compatibility; minimize adaptation logic; test thoroughly.