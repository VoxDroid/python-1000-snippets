# 0144-Multiprocessing Cheatsheet

- **Purpose**: perform CPU-bound tasks in parallel across multiple processes.
- **Pool**: use `from multiprocessing import Pool`; create with `Pool(processes=n)`.
- **map vs apply**: `pool.map(func, iterable)` distributes work; `apply_async` for finer control.
- **Start guard**: on Windows, wrap pool creation in `if __name__ == '__main__':`.
- **Cleanup**: use `with Pool() as pool:` to handle close/join automatically.

```python
from multiprocessing import Pool
with Pool(4) as pool:
    print(pool.map(lambda x: x*x, range(5)))
```

- Beware of pickling restrictions: functions must be top‑level.
- Use `multiprocessing.Manager` for shared state.

