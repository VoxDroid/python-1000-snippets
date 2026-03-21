# Process Pool Management

## Description
This snippet demonstrates process pool usage with `concurrent.futures.ProcessPoolExecutor`.

## Code
- `SAMPLES/sample1.py`: compute factorial values in parallel processes.
- `SAMPLES/sample2.py`: run CPU-bound loop in child processes with time budget.
- `SAMPLES/sample3.py`: save process pool summary to `temp/0504_process_pool.txt`.

## Output
- sample1: `Factorials: [...]`.
- sample2: `Process task results: [...]`.
- sample3: file with counts and sum; printed path.

## Explanation
- **Process Pool Management**: runs CPU-bound tasks in separate processes to avoid GIL limits.
- **Logic**: `ProcessPoolExecutor` for parallel map.
- **Complexity**: O(n) persistent, plus process startup overhead.
- **Use Case**: heavy numeric or data processing tasks.
- **Best Practice**: keep tasks pickleable; limit worker count to available cores; collect results to disk as needed.