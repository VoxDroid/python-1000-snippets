# Telnet Protocol Handling

## Description
This snippet demonstrates basic Telnet client/server interactions using the `telnetlib3` library.

It includes examples of:
- Connecting to a Telnet server and exchanging text.
- Running a simple command shell over Telnet.
- Sending raw binary data in non-UTF8 mode.

## Requirements
- Python 3.8+
- `telnetlib3` (`pip install telnetlib3`)

## Samples
- `SAMPLES/sample1.py`: Simple echo over Telnet.
- `SAMPLES/sample2.py`: Interactive command shell with a few built-in commands.
- `SAMPLES/sample3.py`: Binary-mode Telnet communication (no text encoding).

## Running
```bash
python python-1000-snippets/0422-Telnet-Protocol-Handling/SAMPLES/sample1.py
python python-1000-snippets/0422-Telnet-Protocol-Handling/SAMPLES/sample2.py
python python-1000-snippets/0422-Telnet-Protocol-Handling/SAMPLES/sample3.py
```

## Notes
- These examples run a Telnet server locally and connect a Telnet client to it. They do not require an external Telnet server.
- Telnet is an insecure protocol; use it only for learning or within trusted networks.
