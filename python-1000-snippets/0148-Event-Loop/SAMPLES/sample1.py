# sample1.py
# use custom event loop to run two tasks

import asyncio

async def t(name):
    await asyncio.sleep(0.1)
    return name

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    results = loop.run_until_complete(asyncio.gather(t('A'), t('B')))
    print('Results:', results)
finally:
    loop.close()
