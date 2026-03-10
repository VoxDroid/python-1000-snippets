# Prototype Pattern

## Description
This snippet implements the Prototype pattern by cloning existing objects to create new ones.

## Code
```python
import copy

class Prototype:
    def __init__(self, field):
        self.field = field
    def clone(self):
        return copy.deepcopy(self)

p1 = Prototype([1, 2, 3])
p2 = p1.clone()
p2.field.append(4)
print(p1.field)  # original unaffected
print(p2.field)
```

## Output
```
[1, 2, 3]
[1, 2, 3, 4]
```

## Explanation
- **Prototype Pattern**: uses a prototype instance to create copies rather than instantiating new objects directly.
- **Logic**: `clone` returns a deep copy to ensure independent state.
- **Use Case**: useful when object creation is expensive or complex.
- **Best Practice**: implement a `clone`/`copy` method; consider shallow vs deep copy.
