# 0422 - Telnet Protocol Handling Cheatsheet

## Quick Facts
- Uses `telnetlib3` to create both server and client in-process.
- Demonstrates text mode and binary mode (no encoding).
- Useful for learning how Telnet negotiation and data flows work.

## Run Samples
```bash
python python-1000-snippets/0422-Telnet-Protocol-Handling/SAMPLES/sample1.py
python python-1000-snippets/0422-Telnet-Protocol-Handling/SAMPLES/sample2.py
python python-1000-snippets/0422-Telnet-Protocol-Handling/SAMPLES/sample3.py
```

## Key APIs
- `telnetlib3.create_server(...)` - start a Telnet server with a callback shell.
- `telnetlib3.open_connection(...)` - open a Telnet client connection.
- `reader.readline()` / `writer.write(...)` - exchange data over Telnet.

## Tip
For binary transfers, disable encoding by passing `encoding=False` to both server and client.
