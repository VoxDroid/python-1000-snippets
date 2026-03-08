# sample2.py
# coroutine returning computed value

import asyncio

async def compute(x):
    await asyncio.sleep(0.1)
    return x * x

async def main():
    print(await compute(3))

if __name__ == '__main__':
    asyncio.run(main())
