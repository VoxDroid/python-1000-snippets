# Decorator Pattern

## Description
This snippet implements the Decorator pattern to add behavior to an object dynamically.

## Code
```python
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost() + 1

coffee = Coffee()
coffee_with_milk = MilkDecorator(coffee)
coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
print("Total Cost:", coffee_with_milk_sugar.cost())
```

## Output
```
Total Cost: 8
```

## Explanation
- **Decorator Pattern**: `MilkDecorator` and `SugarDecorator` wrap `Coffee` to add costs.
- **Logic**: Chains decorators to compute total cost (base + milk + sugar).
- **Complexity**: O(n) for n decorators.
- **Use Case**: Used for extending functionality, like middleware or feature toggles.
- **Best Practice**: Ensure decorators maintain the base interface; avoid excessive wrapping.