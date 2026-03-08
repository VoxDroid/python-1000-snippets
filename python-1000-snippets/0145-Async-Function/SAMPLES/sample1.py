# sample1.py
# simple delayed task demonstration

import asyncio

async def delayed_task(name, delay):
    await asyncio.sleep(delay)
    return f"Task {name} completed after {delay}s"

async def main():
    result = await delayed_task("A", 0.5)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
