# Queue Management

## Description
This snippet demonstrates managing a priority queue.

## Code
```python
# Note: Requires `queue`. Built-in module.
try:
    from queue import PriorityQueue
    q = PriorityQueue()
    q.put((2, "task1"))
    q.put((1, "task2"))
    print("Next task:", q.get()[1])
except ImportError:
    print("Mock Output: Next task: task2")
```

## Output
```
Mock Output: Next task: task2
```
*(Real output: `Next task: task2`)*

## Explanation
- **Queue Management**: Processes tasks by priority.
- **Logic**: Uses a priority queue to retrieve the highest-priority task.
- **Complexity**: O(log(n)) for n tasks per operation.
- **Use Case**: Used in task scheduling or event handling.
- **Best Practice**: Handle ties; monitor queue size; ensure thread safety.