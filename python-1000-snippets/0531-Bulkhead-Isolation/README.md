# Bulkhead Isolation

## Description
This snippet demonstrates bulkhead isolation using thread pools to limit resource usage.

## Code
```python
# Note: Requires `concurrent.futures`. Built-in module.
try:
    from concurrent.futures import ThreadPoolExecutor
    def task(x):
        return x * x
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(task, [1, 2, 3]))
    print("Results:", results)
except ImportError:
    print("Mock Output: Results: [1, 4, 9]")
```

## Output
```
Mock Output: Results: [1, 4, 9]
```
*(Real output: `Results: [1, 4, 9]`)*

## Explanation
- **Bulkhead Isolation**: Limits concurrent tasks to prevent resource exhaustion.
- **Logic**: Uses a thread pool with 2 workers to process tasks.
- **Complexity**: O(n) for n tasks, constrained by worker count.
- **Use Case**: Used in microservices to isolate critical tasks.
- **Best Practice**: Tune worker count; monitor resource usage; handle failures.