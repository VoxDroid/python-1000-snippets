# sample1.py
# Fibonacci generation with an async queue.

import asyncio


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


async def worker(name, queue):
    while True:
        n = await queue.get()
        if n is None:
            queue.task_done()
            break
        result = fib(n)
        print(f'Worker {name} fib({n}) = {result}')
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    tasks = [asyncio.create_task(worker(f'W{i}', queue)) for i in range(3)]
    for i in range(5, 11):
        await queue.put(i)
    for _ in tasks:
        await queue.put(None)
    await queue.join()
    for t in tasks:
        await t


if __name__ == '__main__':
    asyncio.run(main())
