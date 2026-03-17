# sample3.py
# Demonstrates handling server-side disconnects from a WebSocket client.

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


async def run_disconnect_demo() -> None:
    websockets = ensure_websockets()

    async def handler(ws, path):
        await ws.send("Welcome")
        # Close the connection immediately after sending.
        await ws.close(code=1000, reason="Normal closure")

    async with websockets.serve(handler, "localhost", 8765):
        try:
            async with websockets.connect("ws://localhost:8765") as client:
                message = await client.recv()
                print("Received:", message)
                try:
                    await client.recv()
                except websockets.ConnectionClosed as e:
                    print("Connection closed by server:", e.code, e.reason)
        except Exception as e:
            print("Client error:", e)


def main() -> None:
    asyncio.run(run_disconnect_demo())


if __name__ == "__main__":
    main()
