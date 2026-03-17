# sample2.py
# Demonstrates broadcasting a message to multiple WebSocket clients.

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


async def run_broadcast() -> None:
    websockets = ensure_websockets()

    clients = set()

    async def handler(ws, path):
        clients.add(ws)
        try:
            async for _ in ws:
                # ignore messages from clients
                pass
        finally:
            clients.remove(ws)

    async with websockets.serve(handler, "localhost", 8765):
        async with websockets.connect("ws://localhost:8765") as c1, websockets.connect("ws://localhost:8765") as c2:
            # Broadcast a message to all connected clients.
            await asyncio.gather(*(client.send("Broadcast") for client in list(clients)))

            r1 = await c1.recv()
            r2 = await c2.recv()
            print("Received on client 1:", r1)
            print("Received on client 2:", r2)


def main() -> None:
    asyncio.run(run_broadcast())


if __name__ == "__main__":
    main()
