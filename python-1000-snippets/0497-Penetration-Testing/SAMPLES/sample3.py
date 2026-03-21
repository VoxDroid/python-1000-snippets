# sample3.py
# Write port scan output to temp/file in reproducible format.

import os
import socket

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/port_scan_results.txt')


def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            return s.connect_ex((host, port)) == 0
    except OSError:
        return False


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    host = '127.0.0.1'
    ports = [22, 80, 443]
    with open(OUTPUT_PATH, 'w') as f:
        for p in ports:
            status = 'open' if check_port(host, p) else 'closed'
            line = f'port {p} {status}\n'
            f.write(line)
    print('Wrote scan output to', OUTPUT_PATH)


if __name__ == '__main__':
    main()
