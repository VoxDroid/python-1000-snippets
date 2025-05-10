# Coroutine

## Description
This snippet defines and runs a coroutine to simulate a task with a delay.

## Code
```python
import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    return "Coroutine completed"

async def main():
    result = await my_coroutine()
    print(result)

asyncio.run(main())
```

## Output
```
Coroutine completed
```

## Explanation
- **Coroutine**: A function defined with `async def` that can be paused with `await`.
- **Execution**: `my_coroutine` pauses for 1s, then returns a result.
- **Complexity**: O(1) plus delay time.
- **Use Case**: Used in async programming for non-blocking operations.
- **Best Practice**: Ensure coroutines are awaited; use `asyncio.run` for top-level execution.