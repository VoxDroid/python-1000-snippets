# sample2.py
# Parse a list of URLs and print the network location

from urllib.parse import urlparse

if __name__ == '__main__':
    urls = [
        'https://example.com/page',
        'ftp://ftp.example.com/resource',
        'http://localhost:8000/test'
    ]
    for u in urls:
        parsed = urlparse(u)
        print(u, '->', parsed.netloc)
