# sample1.py
# run server and client within same script to demonstrate communication

import socket
import threading

HOST, PORT = 'localhost', 12345

def server_func():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((HOST, PORT))
    srv.listen(1)
    conn, addr = srv.accept()
    data = conn.recv(1024).decode()
    conn.send(b'Server says: Hi, Client!')
    conn.close()
    srv.close()

if __name__ == '__main__':
    t = threading.Thread(target=server_func, daemon=True)
    t.start()
    import time; time.sleep(0.1)
    # client side
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
            c.connect((HOST, PORT))
            c.send(b'Hello, Server!')
            resp = c.recv(1024)
            print('Server Response:', resp.decode())
    except Exception as e:
        print('client failed', e)
