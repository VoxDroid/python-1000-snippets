# sample1.py
# start server, then connect a client to it to exercise handler
import asyncio
import websockets

async def handle_connection(ws):
    message = await ws.recv()
    await ws.send("Hello, Client!")

async def run():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    # test client
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send("Hello, Server!")
        reply = await ws.recv()
        print("client received", reply)
    server.close()
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(run())
