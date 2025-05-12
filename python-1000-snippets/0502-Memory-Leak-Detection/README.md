# Memory Leak Detection

## Description
This snippet demonstrates memory usage tracking using `tracemalloc`.

## Code
```python
try:
    import tracemalloc
    tracemalloc.start()
    lst = [[] for _ in range(100)]
    snapshot = tracemalloc.take_snapshot()
    print("Memory snapshot taken")
except ImportError:
    print("Mock Output: Memory snapshot taken")
```

## Output
```
Mock Output: Memory snapshot taken
```
*(Real output with `tracemalloc`: `Memory snapshot taken`)*

## Explanation
- **Memory Leak Detection**: Tracks memory allocation.
- **Logic**: Creates a list and captures a memory snapshot.
- **Complexity**: O(n) for n objects tracked.
- **Use Case**: Used for debugging memory leaks.
- **Best Practice**: Compare snapshots; focus on large allocations; test repeatedly.