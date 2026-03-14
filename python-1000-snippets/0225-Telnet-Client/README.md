# Telnet Client

## Description
This snippet demonstrates a simple Telnet client using `telnetlib3` and a local Telnet server for testing.

## Setup
The sample script starts a local Telnet server on `localhost:8023` and connects to it via the client. The server echoes input lines and supports `exit`/`quit` to close the session.

## Code
```python
# Run the sample script in python-1000-snippets/0225-Telnet-Client/SAMPLES/
# It starts a server and then uses a client to send/receive data.
```

## Output
The sample prints the welcome message, echo response, and the goodbye message.

## Explanation
- **Telnet Client**: Uses `telnetlib3.open_connection` to interact with a Telnet server.
- **Telnet Server**: Runs a minimal echo shell using `telnetlib3.create_server`.
- **Logic**: The client sends a line and reads the echoed response.
- **Use Case**: Useful for automating interactions with legacy Telnet-based services.
- **Best Practice**: Prefer SSH for secure remote shells; Telnet transmits data in plaintext.
