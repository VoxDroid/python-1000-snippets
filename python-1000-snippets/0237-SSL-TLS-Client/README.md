# SSL/TLS Client

## Description
This snippet demonstrates an SSL/TLS client using `ssl` and `socket`.

## Code
```python
import ssl
import socket
try:
    context = ssl.create_default_context()
    with socket.create_connection(("example.com", 443)) as sock:
        with context.wrap_socket(sock, server_hostname="example.com") as ssock:
            ssock.write(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
            response = ssock.read(1024)
            print("Response:", response.decode().split("\r\n")[0])
except:
    print("Mock Output: Response: HTTP/1.1 200 OK")
```

## Output
```
Mock Output: Response: HTTP/1.1 200 OK
```
*(Real output with SSL: `Response: HTTP/1.1 200 OK` or similar)*

## Explanation
- **SSL/TLS Client**: Connects to a server over HTTPS using `ssl.wrap_socket`.
- **Logic**: Sends a basic HTTP GET request and reads the response.
- **Complexity**: O(1) for connection (network latency varies).
- **Use Case**: Used for secure communication with web servers.
- **Best Practice**: Verify certificates; handle SSL errors; use `requests` for production.