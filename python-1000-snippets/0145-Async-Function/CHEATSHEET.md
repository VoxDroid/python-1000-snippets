# 0145-Async-Function Cheatsheet

- **Purpose**: define `async def` functions that use `await` to pause execution.
- **Awaitables**: `asyncio.sleep`, I/O calls, or other coroutines.
- **Running**: use `asyncio.run(coro())` at top level, or get event loop with `asyncio.get_event_loop()`.

```python
import asyncio
async def f():
    await asyncio.sleep(1)
    return 'done'
print(asyncio.run(f()))
```

- Async functions return coroutine objects until awaited.
- Use them for non-blocking I/O (network, file) or concurrent tasks.
- Exceptions inside async functions propagate when awaited.

