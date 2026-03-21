# sample2.py
# Parse a simple URL query string into a dictionary.


def parse_query(qs):
    params = {}
    for pair in qs.split('&'):
        if '=' in pair:
            k, v = pair.split('=', 1)
            params[k] = v
    return params


def main() -> None:
    query = 'a=1&b=hello+world&c=42'
    parsed = parse_query(query)
    print('Parsed query:', parsed)


if __name__ == '__main__':
    main()
