# sample2.py
# multiple async tasks executed sequentially

import asyncio

async def work(n):
    await asyncio.sleep(0.1)
    return n*2

async def main():
    for i in range(3):
        print(await work(i))

if __name__ == '__main__':
    asyncio.run(main())
