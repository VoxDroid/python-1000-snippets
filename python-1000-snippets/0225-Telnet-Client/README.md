# Telnet Client

## Description
This snippet demonstrates a Telnet client using `telnetlib3`.

## Code
```python
import telnetlib3
try:
    tn = telnetlib3.Telnet("localhost", 23)
    tn.write("user\r\npassword\r\n")
    response = tn.read_until(b"login:", timeout=5)
    print("Response:", response.decode())
    tn.close()
except:
    print("Mock Output: Response: Welcome to the server")
```

## Output
```
Mock Output: Response: Welcome to the server
```
*(Real output with Telnet: `Response: <server message>`)*

## Explanation
- **Telnet Client**: Connects to a Telnet server and sends login credentials.
- **Logic**: Writes credentials and reads the server’s response.
- **Complexity**: O(1) for connection (network latency varies).
- **Use Case**: Used for interacting with legacy network devices.
- **Best Practice**: Use timeouts; handle connection failures; prefer SSH for security.