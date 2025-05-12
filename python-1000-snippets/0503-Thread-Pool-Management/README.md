# Thread Pool Management

## Description
This snippet demonstrates thread pool usage with `concurrent.futures`.

## Code
```python
try:
    from concurrent.futures import ThreadPoolExecutor
    def task(x):
        return x**2
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
- **Thread Pool Management**: Executes tasks concurrently using threads.
- **Logic**: Squares numbers in a thread pool.
- **Complexity**: O(n) for n tasks (threading overhead).
- **Use Case**: Used for I/O-bound parallel tasks.
- **Best Practice**: Limit workers; handle exceptions; avoid shared state.