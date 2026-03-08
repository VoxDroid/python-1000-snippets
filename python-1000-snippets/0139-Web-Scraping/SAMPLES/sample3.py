# sample3.py
# use CSS selector to get header text

try:
    import requests
    from bs4 import BeautifulSoup
    r = requests.get('https://example.com')
    soup = BeautifulSoup(r.text, 'html.parser')
    h1 = soup.select_one('h1')
    print('h1:', h1.text if h1 else 'none')
except ImportError:
    print('Mock h1: Example Domain')
except Exception as e:
    print('error', e)
