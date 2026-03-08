# 0142-Socket-Server Cheatsheet

- **Purpose**: listen on a TCP port, accept a connection, receive and reply to messages.
- **Basic pattern**:
  ```python
  import socket
  srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  srv.bind(('localhost', 12345))
  srv.listen(1)
  conn, addr = srv.accept()
  data = conn.recv(1024)
  conn.send(b'reply')
  conn.close(); srv.close()
  ```
- **Error handling**: catch `OSError` for bind failures or port in use.
- **Concurrency**: use threads or processes to handle multiple clients.

- For testing, you can start a client thread in the same script to connect to the server.
- Remember to close sockets and call `shutdown` if needed.

