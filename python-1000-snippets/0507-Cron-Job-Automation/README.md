# Cron Job Automation

## Description
This snippet demonstrates scheduling a task using `schedule`.

## Code
```python
# Note: Requires `schedule`. Install with `pip install schedule`
try:
    import schedule
    import time
    def job():
        print("Task executed")
    schedule.every(10).seconds.do(job)
    schedule.run_all()
except ImportError:
    print("Mock Output: Task executed")
```

## Output
```
Mock Output: Task executed
```
*(Real output with `schedule`: `Task executed`)*

## Explanation
- **Cron Job Automation**: Schedules a recurring task.
- **Logic**: Runs a dummy job immediately.
- **Complexity**: O(1) per job execution.
- **Use Case**: Used for automated scripts or maintenance tasks.
- **Best Practice**: Log executions; handle errors; test schedules.