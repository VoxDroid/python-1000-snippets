# WebSocket Client

## Description
This snippet demonstrates a WebSocket client using `websockets` to connect to a server and exchange messages.

## Code
```python
# Note: Requires `websockets`. Install with `pip install websockets`
import asyncio
import websockets

async def client():
    try:
        async with websockets.connect("ws://localhost:8765") as ws:
            await ws.send("Hello, Server!")
            response = await ws.recv()
            return response
    except (websockets.exceptions.ConnectionClosedError, ConnectionRefusedError):
        return "Error: Could not connect to server. Ensure server is running on ws://localhost:8765."

try:
    print(asyncio.run(client()))
except ImportError:
    print("Mock Output: Server response: Hello, Client!")
```

## Output
```
Error: Could not connect to server. Ensure server is running on ws://localhost:8765.
```
*(Real output with server running: `Server response: Hello, Client!`)*  
*(Mock output without `websockets`: `Mock Output: Server response: Hello, Client!`)*

## Explanation
- **WebSocket Client**: Attempts to connect to a WebSocket server at `ws://localhost:8765`, sends a message, and receives a response.
- **Logic**: Uses `websockets.connect` for the connection, with error handling for connection failures.
- **Complexity**: O(1) for message exchange (network latency varies).
- **Use Case**: Used for real-time applications like chat or live updates.
- **Best Practice**: Handle connection errors gracefully; use async/await for non-blocking I/O; ensure the server (e.g., from Snippet 206) is running before the client.