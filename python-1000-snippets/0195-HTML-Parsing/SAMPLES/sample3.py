# sample3.py
try:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup("<div><a href='x'>link</a></div>", "html.parser")
    link = soup.select_one("a")
    print("link href:", link['href'])
except ImportError:
    print("no bs4")

