# Async Function

## Description
This snippet defines an asynchronous function to simulate a delayed task using `asyncio`.

## Code
```python
import asyncio

async def delayed_task(name, delay):
    await asyncio.sleep(delay)
    return f"Task {name} completed after {delay}s"

async def main():
    result = await delayed_task("A", 1)
    print(result)

asyncio.run(main())
```

## Output
```
Task A completed after 1s
```

## Explanation
- **Async Function**: Defines `delayed_task` with `async def`; uses `await` for non-blocking sleep.
- **Execution**: `asyncio.run` executes the async `main` function.
- **Complexity**: O(delay) time, non-blocking.
- **Use Case**: Used for I/O-bound tasks like network requests or file operations.
- **Best Practice**: Use `await` only for awaitable objects; handle exceptions in async code.