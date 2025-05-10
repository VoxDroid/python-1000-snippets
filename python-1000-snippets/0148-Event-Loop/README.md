# Event Loop

## Description
This snippet demonstrates creating and using a custom asyncio event loop to run tasks.

## Code
```python
import asyncio

async def task(name):
    await asyncio.sleep(1)
    return f"Task {name} done"

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    results = loop.run_until_complete(asyncio.gather(task("A"), task("B")))
    print("Results:", results)
finally:
    loop.close()
```

## Output
```
Results: ['Task A done', 'Task B done']
```

## Explanation
- **Event Loop**: Manages async tasks; created with `asyncio.new_event_loop`.
- **Execution**: Runs two tasks concurrently using `gather` and the custom loop.
- **Complexity**: O(max(delay)) time.
- **Use Case**: Used in custom async applications or frameworks.
- **Best Practice**: Close loops properly; avoid running multiple loops concurrently.