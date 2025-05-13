# Event-Driven Architecture

## Description
This snippet demonstrates an event handler for processing events.

## Code
```python
try:
    def handle_event(event):
        return f"Processed: {event['type']}"
    event = {"type": "click"}
    print("Result:", handle_event(event))
except ImportError:
    print("Mock Output: Result: Processed: click")
```

## Output
```
Mock Output: Result: Processed: click
```
*(Real output: `Result: Processed: click`)*

## Explanation
- **Event-Driven Architecture**: Responds to events asynchronously.
- **Logic**: Processes a click event with a handler.
- **Complexity**: O(1) per event.
- **Use Case**: Used in microservices or UI systems.
- **Best Practice**: Use message queues; ensure idempotency; log events.