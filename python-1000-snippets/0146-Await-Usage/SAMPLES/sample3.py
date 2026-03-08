# sample3.py
# sequential vs concurrent demonstration

import asyncio

async def slow(n):
    await asyncio.sleep(0.2)
    return n

async def main():
    # sequential
    r1 = await slow(1)
    r2 = await slow(2)
    print('seq', r1, r2)
    # concurrent
    r1, r2 = await asyncio.gather(slow(1), slow(2))
    print('concurrent', r1, r2)

if __name__ == '__main__':
    asyncio.run(main())
