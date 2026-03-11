# 0205-WebSocket-Client Cheatsheet

* Install with `pip install websockets` (>=11.0 for latest API).
* Client connect: `async with websockets.connect(url) as ws:`.
* Send/receive: `await ws.send('msg')`, `await ws.recv()`.
* Handle errors: catch `ConnectionRefusedError`, `websockets.exceptions.*`.
* Use `asyncio.run()` to drive the coroutine in top-level script.
* Specify subprotocols or headers via `websockets.connect(..., subprotocols=[...], extra_headers={...})`.
* Close connection with `await ws.close()` or via context manager.
* Public echo endpoints (e.g., `wss://echo.websocket.events`) useful for testing.
* Example server:
  ```python
  async def handler(ws, path):
      msg = await ws.recv()
      await ws.send('echo:'+msg)
  server = await websockets.serve(handler, 'localhost', 8765)
  ```
* Use versions >=11 to avoid deprecated APIs; check via `websockets.__version__`.
* For SSL use `wss://` and supply `ssl` parameter to `connect`.
* Best practice: run server and client in same event loop for testing, or separate processes.
* Non-blocking: avoid long-running operations inside handlers; use `asyncio.create_task` for concurrency.

