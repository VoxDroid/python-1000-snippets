# Dynamic Strategy Selection

## Description
This snippet demonstrates the strategy pattern with dynamic selection.

## Code
```python
class Strategy:
    def execute(self, x):
        pass

class Add(Strategy):
    def execute(self, x):
        return x + 1

class Multiply(Strategy):
    def execute(self, x):
        return x * 2

strategies = {"add": Add(), "multiply": Multiply()}
strategy = strategies["add"]
print(strategy.execute(5))
```

## Output
```
6
```

## Explanation
- **Dynamic Strategy Selection**: Selects a strategy at runtime.
- **Logic**: Maps strategy names to objects and executes the chosen one.
- **Complexity**: O(1) for execution.
- **Use Case**: Used for pluggable algorithms or behaviors.
- **Best Practice**: Validate strategy keys; ensure interface consistency; document strategies.