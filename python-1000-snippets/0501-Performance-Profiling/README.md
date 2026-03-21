# Performance Profiling

## Description
This snippet demonstrates performance profiling and timing using Python standard libraries.

## Code
- `SAMPLES/sample1.py`: `cProfile` run on compute-bound work and prints aggregate data.
- `SAMPLES/sample2.py`: runtime measurement using `time.perf_counter`.
- `SAMPLES/sample3.py`: writes cProfile stats file to `temp/0501_profile.stats`.

## Output
- `sample1.py`: profiling report printed as text.
- `sample2.py`: timing output like `Result ... computed in 0.x seconds`.
- `sample3.py`: message showing saved file path.

## Explanation
- **Performance Profiling**: Measure function-level costs and identify hotspots.
- **Logic**: Use `cProfile` for profiling and `time.perf_counter` for wall-clock timing.
- **Complexity**: O(n) relative to loop iteration count.
- **Use Case**: build a lightweight profiler workflow for a codebase.
- **Best Practice**: keep profiling data in `temp/`, aggregate results with `pstats` or `snakeviz`.
