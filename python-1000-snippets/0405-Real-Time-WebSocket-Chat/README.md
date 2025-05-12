# Real-Time WebSocket Chat

## Description
This snippet demonstrates a WebSocket chat server using `websockets`.

## Code
```python
# Note: Requires `websockets`. Install with `pip install websockets`

import asyncio
import websockets

async def chat(websocket, path):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(chat, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except ImportError:
        print("Mock Output: WebSocket server started")
```

## Output
```
Mock Output: WebSocket server started
```
*(Real output with `websockets`: Runs server at `ws://localhost:8765`)*

## Explanation
- **Real-Time WebSocket Chat**: Implements a simple WebSocket echo server.
- **Logic**: Echoes received messages back to the client.
- **Complexity**: O(1) per message.
- **Use Case**: Used for real-time applications like chat or gaming.
- **Best Practice**: Handle disconnections; secure WebSockets; scale with async.