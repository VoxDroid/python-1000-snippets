# Asynchronous Task Queue

## Description
This snippet demonstrates an async task queue using `asyncio`.

## Code
```python
try:
    import asyncio
    async def task(x):
        await asyncio.sleep(1)
        return x**2
    async def main():
        results = await asyncio.gather(*(task(i) for i in [1, 2, 3]))
        print("Results:", results)
    asyncio.run(main())
except ImportError:
    print("Mock Output: Results: [1, 4, 9]")
```

## Output
```
Mock Output: Results: [1, 4, 9]
```
*(Real output: `Results: [1, 4, 9]`)*

## Explanation
- **Asynchronous Task Queue**: Runs tasks concurrently using `asyncio`.
- **Logic**: Squares numbers with simulated delays.
- **Complexity**: O(n) for n tasks (I/O-bound).
- **Use Case**: Used for async I/O operations like API calls.
- **Best Practice**: Handle exceptions; limit concurrency; use event loops.