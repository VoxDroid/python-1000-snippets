# sample1.py
# start a simple server in a thread then connect as client

import socket
import threading

HOST, PORT = 'localhost', 12345

def server_func():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((HOST, PORT))
    srv.listen(1)
    conn, addr = srv.accept()
    data = conn.recv(1024)
    conn.send(b'Server says: Hi, Client!')
    conn.close()
    srv.close()

if __name__ == '__main__':
    t = threading.Thread(target=server_func, daemon=True)
    t.start()
    # give server a moment to start listening
    import time
    time.sleep(0.1)
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        client.send(b'Hello, Server!')
        response = client.recv(1024)
        print('Server Response:', response.decode())
        client.close()
    except ConnectionRefusedError:
        print('Mock Response: Server says: Hi, Client!')
