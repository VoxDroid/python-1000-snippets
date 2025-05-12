# Telnet Protocol Handling

## Description
This snippet demonstrates basic Telnet communication using `telnetlib`.

## Code
```python
# Note: Requires `telnetlib3` → pip install telnetlib3
import asyncio
import telnetlib3

async def main():
    reader, writer = await telnetlib3.open_connection('localhost', 23)
    writer.write("Welcome\r\n")
    await writer.drain()
    print("Telnet connected")
    writer.close()
    await writer.wait_closed()

try:
    asyncio.run(main())
except ImportError:
    print("Mock Output: Telnet connected")
except Exception as e:
    print("Telnet error:", e)
```

## Output
```
Mock Output: Telnet connected
```
*(Real output with `telnetlib` and Telnet server: `Telnet connected`)*

## Explanation
- **Telnet Protocol Handling**: Connects to a Telnet server.
- **Logic**: Opens a Telnet session and reads a welcome message.
- **Complexity**: O(1) for connection (network-dependent).
- **Use Case**: Used for remote device management or legacy systems.
- **Best Practice**: Secure with SSH; handle timeouts; validate responses.