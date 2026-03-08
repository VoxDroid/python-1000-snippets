# sample1.py
# gather two delay tasks and print combined results

import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name}" 

async def main():
    results = await asyncio.gather(task('A',0.5), task('B',1))
    print('Results:', results)

if __name__ == '__main__':
    asyncio.run(main())
