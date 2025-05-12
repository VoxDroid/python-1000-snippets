# Performance Profiling

## Description
This snippet demonstrates profiling code using `cProfile`.

## Code
```python
try:
    import cProfile
    def slow_function():
        sum(i**2 for i in range(1000))
    cProfile.run("slow_function()")
    print("Profile completed")
except ImportError:
    print("Mock Output: Profile completed")
```

## Output
```
Mock Output: Profile completed
```
*(Real output with `cProfile`: `Profile completed` (prints profiling stats))*

## Explanation
- **Performance Profiling**: Measures execution time of a function.
- **Logic**: Profiles a function that computes a sum of squares.
- **Complexity**: O(n) for n iterations in profiled code.
- **Use Case**: Used for optimizing code performance.
- **Best Practice**: Focus on bottlenecks; repeat profiling; save results.