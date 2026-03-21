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
`sample1.py` prints localhost scan results for ports 22, 80, 443.
`sample2.py` prints open ports in range 20-30.
`sample3.py` writes scan output to `temp/port_scan_results.txt`.

## Explanation
- **Penetration Testing**: Simulates port scanning on localhost.
- **Logic**: Attempts socket connection attempts with timeout.
- **Complexity**: O(n) for n scanned ports.
- **Use Case**: Useful in local network security checks.
- **Best Practice**: Perform authorized scans, avoid intrusive behavior, log results.
