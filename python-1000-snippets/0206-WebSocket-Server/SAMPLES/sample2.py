# sample2.py
# server that echoes messages uppercased
import asyncio
import websockets

async def echo(ws):
    async for msg in ws:
        await ws.send(msg.upper())

async def run():
    server = await websockets.serve(echo, 'localhost', 8765)
    # keep server running for a short interval, then stop
    await asyncio.sleep(1)
    server.close()
    await server.wait_closed()
    print('server shut down')

if __name__ == '__main__':
    asyncio.run(run())
