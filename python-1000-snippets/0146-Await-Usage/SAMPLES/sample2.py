# sample2.py
# show return_exceptions option

import asyncio

async def fail():
    raise RuntimeError('err')

async def main():
    res = await asyncio.gather(fail(), return_exceptions=True)
    print(res)

if __name__ == '__main__':
    asyncio.run(main())
