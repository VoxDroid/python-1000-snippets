# Thread Creation

## Description
This snippet demonstrates creating and running multiple threads in Python using the `threading` module to perform tasks concurrently.

## Code
```python
import threading
import time

def worker(name):
    print(f"Thread {name} starting")
    time.sleep(1)
    print(f"Thread {name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed")
```

## Output
```
Thread 0 starting
Thread 1 starting
Thread 2 starting
Thread 0 finished
Thread 1 finished
Thread 2 finished
All threads completed
```
*(Order of thread output may vary)*

## Explanation
- **Threading**: The `threading.Thread` class creates a thread, with `target` specifying the function to run and `args` passing arguments.
- **start()**: Begins thread execution; `join()` waits for the thread to complete.
- **Use Case**: Threads are used for I/O-bound tasks (e.g., file operations, network requests) to improve performance.
- **Limitations**: Python’s GIL (Global Interpreter Lock) limits true parallelism for CPU-bound tasks; use `multiprocessing` for those.
- **Best Practice**: Ensure thread safety with locks for shared resources; avoid complex thread interactions.

## Additional Files
- `CHEATSHEET.md` notes threading basics, locks, and daemon threads.
- `SAMPLES/` includes:
  1. `sample1.py` – basic threads as shown.
  2. `sample2.py` – use a `Lock` to synchronize access to a shared counter.
  3. `sample3.py` – demonstrate daemon threads that exit when main thread ends.

Execute samples in a `.venv` to observe concurrent output.