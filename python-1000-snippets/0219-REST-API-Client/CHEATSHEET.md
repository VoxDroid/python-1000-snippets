# 0219-REST-API-Client Cheatsheet

* Install requests: `pip install requests`.
* Send GET requests: `requests.get(url, params={'q': 'value'})`.
* Send POST requests: `requests.post(url, json={'key': 'value'})`.
* Check response status: `response.raise_for_status()`.
* Parse JSON: `data = response.json()`.
* Use timeouts to avoid hangs: `requests.get(url, timeout=5)`.
* Add headers: `headers={'Authorization': 'Bearer ...'}`.
* Handle redirects with `allow_redirects=False`.
* Stream large responses with `stream=True` and iterate `response.iter_content()`.
* Use sessions (`requests.Session()`) for connection reuse and cookies.
* Handle network errors via `requests.exceptions.RequestException`.

