# Proxy Pattern

## Description
This snippet implements the Proxy pattern to control access to an object.

## Code
```python
class Resource:
    def access(self):
        return "Accessing resource"

class Proxy:
    def __init__(self):
        self._resource = Resource()
    def access(self):
        print("Proxy checking access...")
        return self._resource.access()

proxy = Proxy()
print(proxy.access())
```

## Output
```
Proxy checking access...
Accessing resource
```

## Explanation
- **Proxy Pattern**: `Proxy` controls access to `Resource`, adding a check before delegating.
- **Logic**: Prints a message before calling the real `access` method.
- **Complexity**: O(1) for access.
- **Use Case**: Used for lazy loading, access control, or logging.
- **Best Practice**: Keep proxy logic lightweight; ensure transparency to clients.