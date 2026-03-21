# Distributed Task Scheduling

## Description
This snippet demonstrates distributed-task-like scheduling using Python standard libraries.

## Code
- `SAMPLES/sample1.py`: uses `sched` to schedule sequential tasks.
- `SAMPLES/sample2.py`: uses `multiprocessing.Pool` to simulate distributed map.
- `SAMPLES/sample3.py`: logs scheduled jobs to `temp/0506_distributed_schedule.txt`.

## Output
- sample1: scheduled tasks execute with printed status.
- sample2: lists partial results from workers.
- sample3: writes all results to temp file.

## Explanation
- **Distributed Task Scheduling**: orchestrate jobs over time or parallel workers.
- **Logic**: `sched` schedules local tasks; `multiprocessing` parallelizes tasks.
- **Complexity**: O(n) tasks, plus scheduling overhead.
- **Use Case**: local proof of concept for task queueing and worker pool patterns.
- **Best Practice**: observe the `__name__ == '__main__'` guard for processes; manage task retries and error handling.
