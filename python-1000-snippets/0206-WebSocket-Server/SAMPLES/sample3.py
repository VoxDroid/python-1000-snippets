# sample3.py
# server that demonstrates graceful shutdown on KeyboardInterrupt (simulated)
import asyncio
import websockets

async def handler(ws):
    try:
        async for msg in ws:
            await ws.send(msg)
    except websockets.exceptions.ConnectionClosed:
        pass

async def run():
    server = await websockets.serve(handler, 'localhost', 8765)
    print('server running, will stop shortly')
    # simulate running then raising KeyboardInterrupt
    await asyncio.sleep(0.5)
    server.close()
    await server.wait_closed()
    print('server stopped')

if __name__ == '__main__':
    asyncio.run(run())
