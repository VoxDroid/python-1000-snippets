# Queue Usage

## Description
This snippet shows how to use the `queue.Queue` class for thread-safe data sharing between threads, implementing a producer-consumer pattern.

## Code
```python
import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced {i}")
        time.sleep(0.1)

def consumer():
    while True:
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()
        time.sleep(0.2)

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer, daemon=True)
p.start()
c.start()
p.join()
```

## Output
```
Produced 0
Consumed 0
Produced 1
Consumed 1
Produced 2
Consumed 2
Produced 3
Consumed 3
Produced 4
Consumed 4
```
*(Order may vary slightly)*

## Explanation
- **Queue**: `queue.Queue` provides thread-safe FIFO (First-In-First-Out) storage.
- **Producer**: Adds items to the queue; `consumer` retrieves and processes them.
- **Methods**: `put()` adds items; `get()` retrieves; `task_done()` signals completion.
- **Use Case**: Queues are used in multi-threaded applications for task scheduling or data processing pipelines.
- **Best Practice**: Use `task_done()` and handle empty queues; consider `queue.Empty` exceptions for robustness.