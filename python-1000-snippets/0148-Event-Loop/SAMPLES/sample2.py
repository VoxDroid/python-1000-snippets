# sample2.py
# demonstrate run_forever with stop call

import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def shutdown():
    await asyncio.sleep(0.1)
    loop.stop()

try:
    loop.create_task(shutdown())
    print('starting loop')
    loop.run_forever()
    print('loop stopped')
finally:
    loop.close()
