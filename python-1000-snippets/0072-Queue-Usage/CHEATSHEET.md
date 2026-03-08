# Queue Usage Cheatsheet

## Queue types
- `queue.Queue()` FIFO
- `queue.LifoQueue()` stack behavior
- `queue.PriorityQueue()` order by priority

## Operations
- `put(item)`, `get()`, `task_done()`, `join()`
- `get(block=False)` raises `queue.Empty`

## Tips
- Useful for producer-consumer patterns.
- Threads can share queue safely without locks.
- Use `queue.Queue(maxsize=n)` to throttle producers.

## Running samples
Activate virtual env and run scripts in `SAMPLES/`.
