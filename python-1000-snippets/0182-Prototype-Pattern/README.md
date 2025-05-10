# Prototype Pattern

## Description
This snippet implements the Prototype pattern to clone objects efficiently.

## Code
```python
import copy

class Prototype:
    def __init__(self, value):
        self.value = value
    def clone(self):
        return copy.deepcopy(self)

original = Prototype("Original")
cloned = original.clone()
cloned.value = "Cloned"
print(f"Original: {original.value}, Cloned: {cloned.value}")
```

## Output
```
Original: Original, Cloned: Cloned
```

## Explanation
- **Prototype Pattern**: `Prototype.clone` creates a deep copy of the object.
- **Logic**: Uses `copy.deepcopy` to ensure independent copies.
- **Complexity**: O(n) for copying n attributes.
- **Use Case**: Used when object creation is costly, like in game object spawning.
- **Best Practice**: Use deep copy for complex objects; implement custom cloning if needed.