# 0143-Thread-Synchronization Cheatsheet

- **Purpose**: use locks to coordinate access to shared data between threads.
- **Lock usage**: `lock = threading.Lock()`; protect critical sections with `with lock:` or `lock.acquire()`/`release()`.
- **Race condition**: without locks, simultaneous modifications can corrupt state.
- **Example pattern**:
  ```python
  import threading
  counter = 0
  lock = threading.Lock()
  def inc():
      global counter
      with lock:
          counter += 1
  ```
- For recursive situations use `threading.RLock`.

- Combine locks with other synchronization primitives (`Event`, `Semaphore`).
- Always release locks in `finally` blocks or by using `with`.

