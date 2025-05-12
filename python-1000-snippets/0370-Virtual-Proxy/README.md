# Virtual Proxy

## Description
This snippet demonstrates a virtual proxy for lazy initialization.

## Code
```python
class RealSubject:
    def request(self):
        return "Real response"

class Proxy:
    def __init__(self):
        self.real = None
    
    def request(self):
        if self.real is None:
            self.real = RealSubject()
        return self.real.request()

proxy = Proxy()
print(proxy.request())
```

## Output
```
Real response
```

## Explanation
- **Virtual Proxy**: Delays creation of a resource until needed.
- **Logic**: Initializes `RealSubject` only on first request.
- **Complexity**: O(1) per call (after initialization).
- **Use Case**: Used for lazy loading of expensive resources.
- **Best Practice**: Ensure thread safety; handle initialization errors; document proxy behavior.