# sample3.py
# connect to a public echo service (if reachable) and then close
import asyncio
import websockets

async def remote():
    uri = 'wss://echo.websocket.events'
    try:
        async with websockets.connect(uri) as ws:
            await ws.send('hello remote')
            print('remote replied', await ws.recv())
    except Exception as e:
        print('remote connection failed:', e)

if __name__ == '__main__':
    asyncio.run(remote())
