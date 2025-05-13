# Scheduling Algorithm

## Description
This snippet demonstrates task scheduling using earliest deadline first.

## Code
```python
try:
    tasks = [{"id": 1, "deadline": 2}, {"id": 2, "deadline": 1}]
    schedule = sorted(tasks, key=lambda x: x["deadline"])
    print("Schedule:", [task["id"] for task in schedule])
except ImportError:
    print("Mock Output: Schedule: [2, 1]")
```

## Output
```
Mock Output: Schedule: [2, 1]
```
*(Real output: `Schedule: [2, 1]`)*

## Explanation
- **Scheduling Algorithm**: Prioritizes tasks by deadline.
- **Logic**: Sorts tasks using earliest deadline first.
- **Complexity**: O(n*log(n)) for n tasks.
- **Use Case**: Used in job scheduling or real-time systems.
- **Best Practice**: Handle conflicts; account for task duration; validate schedules.