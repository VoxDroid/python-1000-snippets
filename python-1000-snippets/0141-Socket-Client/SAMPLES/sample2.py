# sample2.py
# illustrate timeout and error handling

import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    try:
        client.connect(('localhost', 9999))  # assume no server
    except (ConnectionRefusedError, socket.timeout) as e:
        print('could not connect', e)
    finally:
        client.close()
