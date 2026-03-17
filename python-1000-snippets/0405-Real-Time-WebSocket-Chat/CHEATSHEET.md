# 0405-Real-Time-WebSocket-Chat Cheatsheet

- Install `websockets` with `python -m pip install websockets`.
- Use `websockets.serve(handler, host, port)` to start a server.
- Use `websockets.connect(url)` on the client to connect.
- Run both server and client in the same event loop for tests.
- Always close connections and cancel tasks when finished.
