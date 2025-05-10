# Await Usage

## Description
This snippet demonstrates using `await` to run multiple async tasks concurrently.

## Code
```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"Task {name} done"

async def main():
    tasks = [task("A", 1), task("B", 2)]
    results = await asyncio.gather(*tasks)
    print("Results:", results)

asyncio.run(main())
```

## Output
```
Results: ['Task A done', 'Task B done']
```

## Explanation
- **Await Usage**: Uses `asyncio.gather` with `await` to run multiple tasks concurrently.
- **Logic**: Tasks A and B run in parallel, completing after 1s and 2s, respectively.
- **Complexity**: O(max(delay)) time due to concurrency.
- **Use Case**: Used for parallel I/O operations like API calls.
- **Best Practice**: Use `gather` for concurrent tasks; handle task failures.