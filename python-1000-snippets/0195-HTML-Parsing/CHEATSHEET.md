# 0195-HTML-Parsing Cheatsheet

* Requires `beautifulsoup4` (`pip install beautifulsoup4`).
* Create soup: `soup = BeautifulSoup(html, 'html.parser')`.
* Access by tag: `soup.h1`, `soup.find('p', class_='info')`.
* CSS selectors: `soup.select('div > a')`.
* Get text: `element.get_text()` or `.text`.
* Handle missing elements gracefully.

