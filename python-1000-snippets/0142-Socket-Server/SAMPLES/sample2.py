# sample2.py
# handle one connection and echo back

import socket

if __name__ == '__main__':
    try:
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.bind(('localhost', 12346))
        srv.listen(1)
        conn, _ = srv.accept()
        msg = conn.recv(1024)
        conn.send(msg)
        conn.close()
        srv.close()
        print('echo server done')
    except OSError as e:
        print('server error', e)
