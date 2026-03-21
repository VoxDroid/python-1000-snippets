# sample2.py
# Run async tasks concurrently with limited semaphore concurrency.

import asyncio


async def task(n):
    await asyncio.sleep(0.1)
    return n * n


async def main():
    semaphore = asyncio.Semaphore(3)

    async def sem_task(i):
        async with semaphore:
            res = await task(i)
            print(f'task {i} -> {res}')
            return res

    results = await asyncio.gather(*(sem_task(i) for i in range(10)))
    print('All tasks done:', results)


if __name__ == '__main__':
    asyncio.run(main())
