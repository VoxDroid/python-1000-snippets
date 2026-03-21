# sample2.py
# Perform a port range scan and report the first few open ports.

import socket


def scan_range(host, start, end):
    open_ports = []
    for p in range(start, end + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.2)
                if s.connect_ex((host, p)) == 0:
                    open_ports.append(p)
        except OSError:
            continue
    return open_ports


def main() -> None:
    host = '127.0.0.1'
    open_ports = scan_range(host, 20, 30)
    print('Open ports in [20-30]:', open_ports)


if __name__ == '__main__':
    main()
