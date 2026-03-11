# sample2.py
# attempt connection to local server, show error handling
import asyncio
import websockets

async def client():
    try:
        async with websockets.connect('ws://localhost:8765') as ws:
            await ws.send('ping')
            print('server responded', await ws.recv())
    except Exception as e:
        print('Failed to connect or communicate:', e)

if __name__ == '__main__':
    asyncio.run(client())
