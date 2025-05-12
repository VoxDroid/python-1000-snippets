# Process Pool Management

## Description
This snippet demonstrates process pool usage with `concurrent.futures`.

## Code
```python
try:
    from concurrent.futures import ProcessPoolExecutor
    def task(x):
        return x**2
    with ProcessPoolExecutor(max_workers=2) as executor:
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
- **Process Pool Management**: Executes tasks in parallel processes.
- **Logic**: Squares numbers using a process pool.
- **Complexity**: O(n) for n tasks (process overhead).
- **Use Case**: Used for CPU-bound parallel tasks.
- **Best Practice**: Limit workers; handle serialization; monitor resources.