# Penetration Testing

## Description
This snippet demonstrates a simple port scan using `socket`.

## Code
```python
try:
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex(("localhost", 80))
    print("Port 80 open" if result == 0 else "Port 80 closed")
    s.close()
except ImportError:
    print("Mock Output: Port 80 closed")
```

## Output
```
Mock Output: Port 80 closed
```
*(Real output: `Port 80 open` or `Port 80 closed`)*

## Explanation
- **Penetration Testing**: Checks if port 80 is open on localhost.
- **Logic**: Attempts a TCP connection to port 80.
- **Complexity**: O(1) per port scan.
- **Use Case**: Used in security audits or network testing.
- **Best Practice**: Scan ethically; handle timeouts; log results.