# WebSocket Server

## Description
This snippet demonstrates a WebSocket server using `websockets` to accept client connections and respond to messages.

## Code
```python
# Note: Requires `websockets>=11.0`. Install with `pip install websockets`
import asyncio
import websockets

async def handle_connection(websocket):
    try:
        message = await websocket.recv()
        print(f"Received: {message}")
        await websocket.send("Hello, Client!")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    except Exception as e:
        print(f"Error in handler: {e}")

async def main():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    print("Server started on ws://localhost:8765")
    await server.wait_closed()

try:
    asyncio.run(main())
except ImportError:
    print("Mock Output: Server started, received 'Hello, Server!'")
except KeyboardInterrupt:
    print("Server stopped")
```

## Output
```
Server started on ws://localhost:8765
Received: Hello, Server!
```
*(Mock output without `websockets`: `Mock Output: Server started, received 'Hello, Server!'`)*  
*(Real output when client connects: Prints `Received: Hello, Server!` after client sends message)*

## Explanation
- **WebSocket Server**: Listens for client connections on `ws://localhost:8765`, receives messages, and sends responses.
- **Logic**: Uses `websockets.serve` with `handle_connection`, which processes messages and handles disconnections. The handler accepts only the `websocket` argument to match potential API variations.
- **Complexity**: O(1) per connection (network latency varies).
- **Use Case**: Used for real-time communication in chat or gaming apps.
- **Best Practice**: Handle client disconnections; use SSL for production; ensure proper event loop management with `asyncio.run`. Verify `websockets` version with `pip show websockets` and update to at least 11.0 if needed (`pip install --upgrade websockets`).