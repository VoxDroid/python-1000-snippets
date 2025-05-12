# Request Chain Handling

## Description
This snippet demonstrates the chain of responsibility pattern.

## Code
```python
class Handler:
    def __init__(self, successor=None):
        self.successor = successor
    
    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)
        return "Unhandled"

class ConcreteHandler(Handler):
    def handle(self, request):
        if request == "valid":
            return "Handled"
        return super().handle(request)

chain = ConcreteHandler(Handler())
print(chain.handle("valid"))
```

## Output
```
Handled
```

## Explanation
- **Request Chain Handling**: Passes requests along a chain until handled.
- **Logic**: `ConcreteHandler` processes valid requests, else delegates.
- **Complexity**: O(n) for n handlers.
- **Use Case**: Used for logging, event handling, or middleware.
- **Best Practice**: Define clear responsibilities; avoid long chains; test handling.