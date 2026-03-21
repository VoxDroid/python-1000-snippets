# Asynchronous Task Queue

## Description
This snippet demonstrates asynchronous task queue patterns with `asyncio`.

## Code
- `SAMPLES/sample1.py`: uses `asyncio.Queue` and worker tasks to compute Fibonacci numbers.
- `SAMPLES/sample2.py`: uses `asyncio.Semaphore` to limit concurrency for tasks.
- `SAMPLES/sample3.py`: consumes an async queue and writes a summary to `temp/0505_async_queue.txt`.

## Output
- sample1: prints worker outputs for `fib` tasks.
- sample2: prints each task result and final aggregation.
- sample3: prints file path and stores count/sum results.

## Explanation
- **Asynchronous Task Queue**: manage queue-based workload asynchronously.
- **Logic**: produce tasks, process tasks concurrently with workers.
- **Complexity**: O(n) operations, concurrency overhead.
- **Use Case**: reactive IO workflows, event processing, message consumption.
- **Best Practice**: keep queue size bounded, handle exceptions in workers, and cancel cleanly.
