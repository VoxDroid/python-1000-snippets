# 0206-WebSocket-Server Cheatsheet

* Install `websockets` (>=11.0): `pip install websockets`.
* Server creation: `server = await websockets.serve(handler, host, port)`.
* Handler typically accepts one argument (`websocket`); older versions passed `(websocket, path)`.
* Use `async for msg in websocket:` to iteratively receive messages.
* Send replies with `await websocket.send(data)`.
* Close server with `server.close()` and `await server.wait_closed()`.
* Run server with `asyncio.run()` or by attaching to existing loop.
* For SSL use `ssl=ssl_context` parameter to `serve` and `connect`.
* To handle multiple clients, simply write async handler; websockets library multiplexes connections.
* Catch `websockets.exceptions.ConnectionClosed` to detect disconnects.
* Example combined server/client in one script (see sample1) useful for quick tests.
* Use `asyncio.create_task` to run server and clients concurrently if needed.
* Best practice: validate input, limit message sizes, use ping/pong to keep connection alive.
* Version check: `websockets.__version__` and upgrade with `pip install --upgrade websockets` if necessary.
