# sample1.py
# Runs an in-process WebSocket server and client to demonstrate message exchange.

import asyncio
import subprocess
import sys


def ensure_websockets():
    try:
        import websockets  # type: ignore
        return websockets
    except ImportError:
        print("Missing dependency: websockets. Install with: python -m pip install websockets")
        sys.exit(1)


async def run_chat() -> None:
    websockets = ensure_websockets()

    # In recent versions of `websockets`, the handler receives only the `websocket`.
    async def handler(ws):
        async for message in ws:
            await ws.send(f"Echo: {message}")

    server = await websockets.serve(handler, "localhost", 8765)

    async with server:
        async with websockets.connect("ws://localhost:8765") as ws:
            await ws.send("hello")
            reply = await ws.recv()
            print("Received:", reply)

    # The server is closed when exiting the async with context.


def main() -> None:
    asyncio.run(run_chat())


if __name__ == "__main__":
    main()
