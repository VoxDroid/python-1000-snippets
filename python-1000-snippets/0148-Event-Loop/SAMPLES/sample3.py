# sample3.py
# create and reuse an event loop for sequential tasks

import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def say(msg):
    print(msg)

try:
    loop.run_until_complete(say('Hello'))
    loop.run_until_complete(say('World'))
finally:
    loop.close()
