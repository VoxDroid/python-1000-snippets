# 0148-Event-Loop Cheatsheet

- **Purpose**: manually create and manage an `asyncio` event loop instead of using `asyncio.run`.
- **Creation**: `loop = asyncio.new_event_loop(); asyncio.set_event_loop(loop)`.
- **Execution**: run tasks with `loop.run_until_complete(coro)` or `run_forever()`.
- **Cleanup**: always `loop.close()` in a `finally` block.

```python
import asyncio
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(asyncio.sleep(0))
finally:
    loop.close()
```

- Useful when embedding asyncio inside other frameworks or reusing loops.
- Do not run multiple loops concurrently on the same thread.

