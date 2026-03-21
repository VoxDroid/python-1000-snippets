# sample1.py
# Parse HTTP headers from a raw request string.


def parse_headers(raw):
    headers = {}
    for line in raw.split('\r\n'):
        if not line:
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            headers[key.strip()] = val.strip()
    return headers


def main() -> None:
    raw_headers = 'Host: example.com\r\nUser-Agent: test-agent\r\nAccept: */*\r\n\r\n'
    parsed = parse_headers(raw_headers)
    print('Parsed headers:', parsed)


if __name__ == '__main__':
    main()
