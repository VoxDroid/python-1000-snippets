# sample2.py
# find all links on the page

try:
    import requests
    from bs4 import BeautifulSoup
    r = requests.get('https://example.com')
    soup = BeautifulSoup(r.text, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a')]
    print('Links:', links)
except ImportError:
    print('Mock Links: [/]')
except Exception as e:
    print('error', e)
