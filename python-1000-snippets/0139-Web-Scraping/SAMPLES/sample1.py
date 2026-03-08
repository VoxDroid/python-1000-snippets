# sample1.py
# fetch and print page title

try:
    import requests
    from bs4 import BeautifulSoup
    r = requests.get('https://example.com', timeout=5)
    soup = BeautifulSoup(r.text, 'html.parser')
    print('Title:', soup.title.string)
except ImportError:
    print('Mock Title: Example Domain')
except Exception as e:
    print('Request failed:', e)
