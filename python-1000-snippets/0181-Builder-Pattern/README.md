# Builder Pattern

## Description
This snippet implements the Builder pattern to construct complex objects step-by-step.

## Code
```python
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
    def __str__(self):
        return f"House with {self.walls} walls and {self.roof} roof"

class HouseBuilder:
    def __init__(self):
        self.house = House()
    def set_walls(self, walls):
        self.house.walls = walls
        return self
    def set_roof(self, roof):
        self.house.roof = roof
        return self
    def build(self):
        return self.house

builder = HouseBuilder()
house = builder.set_walls(4).set_roof("tile").build()
print(house)
```

## Output
```
House with 4 walls and tile roof
```

## Explanation
- **Builder Pattern**: `HouseBuilder` constructs a `House` object incrementally.
- **Logic**: Chained methods (`set_walls`, `set_roof`) configure the object; `build` returns it.
- **Complexity**: O(1) for building.
- **Use Case**: Used for objects with many optional components, like configurations.
- **Best Practice**: Use fluent interface; validate build state.