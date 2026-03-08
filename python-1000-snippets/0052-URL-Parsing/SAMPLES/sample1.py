# sample1.py
# Prompt user for a URL and print parsed components

from urllib.parse import urlparse

if __name__ == '__main__':
    url = input('URL: ')
    p = urlparse(url)
    print('scheme:', p.scheme)
    print('netloc:', p.netloc)
    print('path:', p.path)
    print('params:', p.params)
    print('query:', p.query)
    print('fragment:', p.fragment)
