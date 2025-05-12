# Object Communication Mediator

## Description
This snippet demonstrates the mediator pattern for object communication.

## Code
```python
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.components = []
    
    def add(self, component):
        self.components.append(component)
    
    def notify(self, sender, event):
        for component in self.components:
            if component != sender:
                component.receive(event)

class Component:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def send(self, event):
        self.mediator.notify(self, event)
    
    def receive(self, event):
        print(f"Received: {event}")

mediator = ConcreteMediator()
c1 = Component(mediator)
c2 = Component(mediator)
mediator.add(c1)
mediator.add(c2)
c1.send("Hello")
```

## Output
```
Received: Hello
```

## Explanation
- **Object Communication Mediator**: Centralizes communication between objects.
- **Logic**: `Mediator` relays events from one component to others.
- **Complexity**: O(n) for n components.
- **Use Case**: Used in chat systems or GUI frameworks.
- **Best Practice**: Keep mediator simple; avoid tight coupling; test communication.