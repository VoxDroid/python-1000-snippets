# Socket Client

## Description
This snippet creates a TCP socket client that connects to a server and sends a message.

## Code
```python
import socket

# Note: Requires a running server (see Snippet 142) at localhost:12345
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))
    client.send("Hello, Server!".encode())
    response = client.recv(1024).decode()
    print("Server Response:", response)
    client.close()
except ConnectionRefusedError:
    print("Mock Response: Server says: Hi, Client!")
```

## Output
```
Mock Response: Server says: Hi, Client!
```
*(Real output with server: `Server Response: Server says: Hi, Client!`)*

## Explanation
- **Socket Client**: Connects to a TCP server, sends a message, and receives a response.
- **Mock**: Simulates a response if no server is running.
- **Complexity**: O(1) for connection and send/receive.
- **Use Case**: Used in networked applications or client-server systems.
- **Best Practice**: Handle connection errors; use timeouts; ensure server is running.