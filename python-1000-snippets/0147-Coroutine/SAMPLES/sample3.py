# sample3.py
# coroutine raising an exception

import asyncio

async def fail():
    raise ValueError('oops')

async def main():
    try:
        await fail()
    except Exception as e:
        print('caught', e)

if __name__ == '__main__':
    asyncio.run(main())
