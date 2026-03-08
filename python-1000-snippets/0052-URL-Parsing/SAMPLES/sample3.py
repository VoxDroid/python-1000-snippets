# sample3.py
# Build a URL from components, then parse a query string

from urllib.parse import urlunparse, parse_qs

if __name__ == '__main__':
    components = ('https', 'example.com', '/search', '', 'q=test&lang=en', '')
    url = urlunparse(components)
    print('constructed URL:', url)
    print('parsed query:', parse_qs(components[4]))
