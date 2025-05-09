# Timer

## Description
This snippet implements a simple timer using the `time` module to measure the execution time of a code block.

## Code
```python
import time

start_time = time.time()
for i in range(1000000):
    pass
end_time = time.time()
elapsed = end_time - start_time
print(f"Elapsed time: {elapsed:.4f} seconds")
```

## Output
```
Elapsed time: 0.0312 seconds
```
*(Output varies based on system)*

## Explanation
- **time.time()**: Returns the current time in seconds since the epoch (January 1, 1970).
- **Timer Logic**: Subtract `start_time` from `end_time` to get elapsed time.
- **Use Case**: Timing is used for performance testing, benchmarking, or profiling code.
- **Precision**: `time.time()` is suitable for most purposes; use `time.perf_counter()` for higher precision.
- **Best Practice**: Use timers to identify bottlenecks but avoid micro-optimizations prematurely.