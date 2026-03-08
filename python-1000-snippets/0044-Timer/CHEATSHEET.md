# Timer Cheatsheet

## time module functions
- `time.time()` wall-clock time (epoch seconds).
- `time.perf_counter()` high-resolution timer.
- `time.sleep(sec)` pause execution.

## Tips
- Use `perf_counter()` for measuring short durations.
- Subtract start from end to compute elapsed.
- Can use `timeit` module for micro-benchmarks.

## Example
```python
import time
start = time.perf_counter()
# code
end = time.perf_counter()
print(end-start)
```

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
