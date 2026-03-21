# Thread Pool Management

## Description
This snippet demonstrates thread pool usage with `concurrent.futures.ThreadPoolExecutor`.

## Code
- `SAMPLES/sample1.py`: compute squares in parallel and print sorted results.
- `SAMPLES/sample2.py`: simulate I/O-bound tasks via `sleep` and map.
- `SAMPLES/sample3.py`: write summary metrics to `temp/0503_thread_pool.txt`.

## Output
- sample1: `Squared values: [...]`
- sample2: `I/O bound results: [...]`
- sample3: file location message with summary file content in `temp/`.

## Explanation
- **Thread Pool Management**: manages concurrent execution for tasks.
- **Logic**: uses `ThreadPoolExecutor` with up to 5 workers.
- **Complexity**: O(n) tasks with worker scheduling overhead.
- **Use Case**: best for I/O-bound tasks; can be used with network/DB calls.
- **Best Practice**: choose pool size based on system cores; use thread-safe data structures.
