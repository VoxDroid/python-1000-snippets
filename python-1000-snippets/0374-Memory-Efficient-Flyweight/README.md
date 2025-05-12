# Memory Efficient Flyweight

## Description
This snippet demonstrates the flyweight pattern to share common data.

## Code
```python
class Flyweight:
    def __init__(self, shared):
        self.shared = shared
    
    def operation(self, unique):
        return f"{self.shared} + {unique}"

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}
    
    def get_flyweight(self, shared):
        if shared not in self.flyweights:
            self.flyweights[shared] = Flyweight(shared)
        return self.flyweights[shared]

factory = FlyweightFactory()
flyweight = factory.get_flyweight("shared")
print(flyweight.operation("unique"))
```

## Output
```
shared + unique
```

## Explanation
- **Memory Efficient Flyweight**: Shares intrinsic state to reduce memory usage.
- **Logic**: `FlyweightFactory` reuses `Flyweight` instances based on shared state.
- **Complexity**: O(1) for retrieval.
- **Use Case**: Used for large numbers of similar objects, like characters in a text editor.
- **Best Practice**: Separate intrinsic/extrinsic state; ensure immutability; test sharing.