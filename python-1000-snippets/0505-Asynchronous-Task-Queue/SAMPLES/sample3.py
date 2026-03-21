# sample3.py
# Save aggregator results from async queue to temp file.

import asyncio
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0505_async_queue.txt')


async def worker(n):
    await asyncio.sleep(0.05)
    return n + 1


async def main():
    queue = asyncio.Queue()
    for i in range(20):
        await queue.put(i)

    results = []

    async def consumer():
        while not queue.empty():
            x = await queue.get()
            results.append(await worker(x))
            queue.task_done()

    await consumer()

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write('count=' + str(len(results)) + '\n')
        f.write('sum=' + str(sum(results)) + '\n')

    print('Wrote async task queue summary to', OUTPUT_PATH)


if __name__ == '__main__':
    asyncio.run(main())
