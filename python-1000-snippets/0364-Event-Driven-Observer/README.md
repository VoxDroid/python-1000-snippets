# Event-Driven Observer

## Description
This snippet demonstrates the observer pattern for event notifications.

## Code
```python
class Observer:
    def update(self, message):
        print(f"Received: {message}")

class Subject:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

subject = Subject()
observer = Observer()
subject.add_observer(observer)
subject.notify("Event!")
```

## Output
```
Received: Event!
```

## Explanation
- **Event-Driven Observer**: Notifies observers of events.
- **Logic**: `Subject` maintains observers and notifies them with messages.
- **Complexity**: O(n) for n observers.
- **Use Case**: Used in GUI frameworks or pub-sub systems.
- **Best Practice**: Manage observer lifecycle; handle errors; ensure loose coupling.