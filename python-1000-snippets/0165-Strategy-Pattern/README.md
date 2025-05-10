# Strategy Pattern

## Description
This snippet implements the Strategy pattern to switch between different algorithms at runtime.

## Code
```python
class Strategy:
    def execute(self, a, b):
        pass

class Add(Strategy):
    def execute(self, a, b):
        return a + b

class Multiply(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    def set_strategy(self, strategy):
        self.strategy = strategy
    def execute(self, a, b):
        return self.strategy.execute(a, b)

context = Context(Add())
print("Add:", context.execute(5, 3))
context.set_strategy(Multiply())
print("Multiply:", context.execute(5, 3))
```

## Output
```
Add: 8
Multiply: 15
```

## Explanation
- **Strategy Pattern**: `Context` uses a `Strategy` (e.g., `Add`, `Multiply`) to perform operations.
- **Logic**: Allows switching strategies dynamically via `set_strategy`.
- **Complexity**: O(1) for execution.
- **Use Case**: Used for interchangeable algorithms, like sorting or compression.
- **Best Practice**: Define a clear strategy interface; ensure strategies are stateless.