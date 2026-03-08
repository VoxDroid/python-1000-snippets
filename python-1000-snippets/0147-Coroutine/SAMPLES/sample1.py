# sample1.py
# basic coroutine that returns a value

import asyncio

async def my_coroutine():
    await asyncio.sleep(0.2)
    return "Coroutine completed"

async def main():
    result = await my_coroutine()
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
