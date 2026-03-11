# sample1.py
# start a simple echo server and then connect a client to it
import asyncio
import websockets

async def echo_handler(ws):
    msg = await ws.recv()
    await ws.send(f"echo:{msg}")

async def run():
    server = await websockets.serve(echo_handler, 'localhost', 8765)
    # client connects to the above server
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send('hello')
        reply = await ws.recv()
        print('client received', reply)
    server.close()
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(run())
