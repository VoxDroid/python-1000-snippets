# 0139-Web-Scraping Cheatsheet

- **Purpose**: fetch HTML from a webpage and parse it with BeautifulSoup.
- **Dependencies**: `requests` and `beautifulsoup4` (`pip install requests beautifulsoup4`).
- **Basic flow**:
  ```python
  import requests
  from bs4 import BeautifulSoup
  r = requests.get('https://example.com')
  soup = BeautifulSoup(r.text, 'html.parser')
  title = soup.title.string
  ```
- **Selectors**: use `soup.find`, `soup.find_all`, CSS selectors with `soup.select`.
- **Mocking**: code can fall back to a static title if libs missing or offline.

- Respect `robots.txt`; set `User-Agent` header; add delays when scraping many pages.

