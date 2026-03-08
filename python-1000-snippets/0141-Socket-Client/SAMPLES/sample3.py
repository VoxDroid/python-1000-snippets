# sample3.py
# simple looped send/receive

import socket

if __name__ == '__main__':
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(('localhost', 12345))
            for msg in [b'one', b'two', b'three']:
                client.send(msg)
                resp = client.recv(1024)
                print('got', resp)
    except Exception:
        print('could not perform loop, maybe no server')
