# Chain of Responsibility

## Description
This snippet implements the Chain of Responsibility pattern to pass requests along a chain of handlers.

## Code
```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor
    def handle(self, request):
        pass

class LowPriorityHandler(Handler):
    def handle(self, request):
        if request <= 10:
            return f"Handled by Low: {request}"
        return self._successor.handle(request) if self._successor else "Not handled"

class HighPriorityHandler(Handler):
    def handle(self, request):
        if request > 10:
            return f"Handled by High: {request}"
        return self._successor.handle(request) if self._successor else "Not handled"

chain = LowPriorityHandler(HighPriorityHandler())
print(chain.handle(5))
print(chain.handle(15))
```

## Output
```
Handled by Low: 5
Handled by High: 15
```

## Explanation
- **Chain of Responsibility**: Passes requests through a chain (`LowPriorityHandler` to `HighPriorityHandler`) until handled.
- **Logic**: Each handler checks if it can process the request; otherwise, it forwards to the successor.
- **Complexity**: O(n) for n handlers in the chain.
- **Use Case**: Used in event handling, logging, or request processing.
- **Best Practice**: Define clear handling criteria; avoid infinite chains.