# Real-Time WebSocket Chat

## Description
Demonstrates WebSocket interactions using the `websockets` library. Examples run server and client in the same process to avoid manual testing.

## Files
- `SAMPLES/sample1.py` — Echo server: client sends a message and receives it back.
- `SAMPLES/sample2.py` — Broadcasts a message to multiple connected clients.
- `SAMPLES/sample3.py` — Shows server-initiated disconnect and client response.

## Usage
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Script installs `websockets` if missing.
- These examples run entirely in-process and do not expose a permanent server port.
