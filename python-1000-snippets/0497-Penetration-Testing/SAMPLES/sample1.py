# sample1.py
# Check common ports on localhost to identify open services.

import socket


def check_port(host, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except OSError:
        return False


def main() -> None:
    host = '127.0.0.1'
    ports = [22, 80, 443]
    results = {p: check_port(host, p) for p in ports}
    print('Port scan results:', results)


if __name__ == '__main__':
    main()
