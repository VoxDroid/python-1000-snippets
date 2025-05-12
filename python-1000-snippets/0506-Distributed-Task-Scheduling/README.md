# Distributed Task Scheduling

## Description
This snippet demonstrates a task setup for `celery`.

## Code
```python
# Note: Requires `celery`. Install with `pip install celery`
try:
    from celery import Celery
    app = Celery('tasks', broker='redis://localhost:6379/0')
    @app.task
    def add(x, y):
        return x + y
    print("Celery task configured")
except ImportError:
    print("Mock Output: Celery task configured")
```

## Output
```
Mock Output: Celery task configured
```
*(Real output with `celery`: `Celery task configured`)*

## Explanation
- **Distributed Task Scheduling**: Sets up a Celery task for distributed execution.
- **Logic**: Defines an addition task with Redis backend.
- **Complexity**: O(1) for setup (execution-dependent).
- **Use Case**: Used for distributed job processing.
- **Best Practice**: Secure broker; monitor tasks; handle failures.