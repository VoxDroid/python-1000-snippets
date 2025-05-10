# Mediator Pattern

## Description
This snippet implements the Mediator pattern to centralize communication between objects.

## Code
```python
class Mediator:
    def __init__(self):
        self.components = []
    def register(self, component):
        self.components.append(component)
    def notify(self, sender, message):
        for component in self.components:
            if component != sender:
                component.receive(message)

class Component:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
    def send(self, message):
        self.mediator.notify(self, f"{self.name}: {message}")
    def receive(self, message):
        print(f"{self.name} received: {message}")

mediator = Mediator()
c1 = Component("A", mediator)
c2 = Component("B", mediator)
mediator.register(c1)
mediator.register(c2)
c1.send("Hello")
```

## Output
```
B received: A: Hello
```

## Explanation
- **Mediator Pattern**: `Mediator` coordinates communication between `Component` objects.
- **Logic**: `send` triggers `notify`, which broadcasts to other components.
- **Complexity**: O(n) for n components during notification.
- **Use Case**: Used in chat systems, UI frameworks, or event buses.
- **Best Practice**: Keep mediator logic simple; avoid tight coupling with components.