# sample3.py
# start server then connect with a simple built-in client to verify

import socket, threading, time

HOST, PORT = 'localhost', 12347

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, _ = s.accept()
    conn.recv(1024)
    conn.send(b'ok')
    conn.close(); s.close()

if __name__ == '__main__':
    th = threading.Thread(target=server, daemon=True); th.start()
    time.sleep(0.1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        c.connect((HOST, PORT))
        c.send(b'ping')
        print('reply', c.recv(1024))
