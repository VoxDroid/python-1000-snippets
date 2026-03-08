# 0141-Socket-Client Cheatsheet

- **Purpose**: connect to a TCP server and exchange messages using the `socket` module.
- **Basic workflow**:
  ```python
  import socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('localhost', 12345))
  s.send(b'Hello')
  data = s.recv(1024)
  s.close()
  ```
- **Error handling**: catch `ConnectionRefusedError` or generic `OSError` if server unavailable.
- **Cleanup**: always call `close()` on sockets (use `with socket.socket(...) as s:` in Python 3.7+).

- Use `socket.settimeout()` to avoid blocking indefinitely.
- Client and server can run in separate processes or threads for testing.

