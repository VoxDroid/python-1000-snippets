# 0147-Coroutine Cheatsheet

- **Purpose**: define coroutines with `async def` for asynchronous programming.
- **Awaiting**: use `await` to suspend until another coroutine or awaitable completes.
- **Creating**: calling an `async def` returns a coroutine object; must be awaited or scheduled.

```python
async def c():
    await asyncio.sleep(1)
    return 42
coro = c()
print(asyncio.run(coro))
```

- Can be used with `asyncio.create_task` or `gather` for concurrency.
- Coroutines can raise exceptions; handle them in the caller.

