# Observer Pattern

## Description
This snippet implements the Observer pattern to notify subscribers of state changes.

## Code
```python
class Subject:
    def __init__(self):
        self._observers = []
    def attach(self, observer):
        self._observers.append(observer)
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received: {message}")

subject = Subject()
observer = Observer()
subject.attach(observer)
subject.notify("Event occurred")
```

## Output
```
Received: Event occurred
```

## Explanation
- **Observer Pattern**: `Subject` maintains a list of `Observer` objects and notifies them of changes.
- **Logic**: `notify` calls each observer’s `update` method.
- **Complexity**: O(n) for n observers during notification.
- **Use Case**: Used in event systems, GUI frameworks, or pub-sub models.
- **Best Practice**: Allow observer detachment; handle observer failures.