# 0146-Await-Usage Cheatsheet

- **Purpose**: demonstrate combining multiple awaitable tasks with `asyncio.gather`.
- **gather**: `results = await asyncio.gather(*tasks)` waits for all to complete.
- **Error handling**: exceptions propagate in the gathered results by default.
- **Coroutine examples**: `async def task()` returning values.

```python
import asyncio
async def f(x):
    await asyncio.sleep(1)
    return x
print(asyncio.run(asyncio.gather(f(1), f(2))))
```

- Equivalent to concurrently awaiting multiple awaits with `await` in loop.
- Use `return_exceptions=True` to collect exceptions instead of raising.

