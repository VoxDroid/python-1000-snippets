# Socket Server

## Description
This snippet creates a TCP socket server that accepts a client connection and responds.

## Code
```python
import socket

# Note: Run this before the client (Snippet 141)
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Server listening...")
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    print("Received:", data)
    conn.send("Server says: Hi, Client!".encode())
    conn.close()
    server.close()
except OSError:
    print("Mock Output: Server started, received 'Hello, Server!', sent 'Server says: Hi, Client!'")
```

## Output
```
Mock Output: Server started, received 'Hello, Server!', sent 'Server says: Hi, Client!'
```
*(Real output with client: `Server listening... Received: Hello, Server!`)*

## Explanation
- **Socket Server**: Listens for a client, receives a message, and sends a response.
- **Mock**: Simulates behavior if the server cannot bind.
- **Complexity**: O(1) for connection handling.
- **Use Case**: Used in networked applications or chat systems.
- **Best Practice**: Handle multiple clients; use threading for concurrency; manage port conflicts.