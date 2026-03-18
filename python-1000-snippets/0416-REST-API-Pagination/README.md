# REST API Pagination

## Description
Demonstrates a paginated REST API and how a client can request pages of data.

## Requirements
- Python 3.8+
- `Flask` (`pip install flask`)
- `requests` (`pip install requests`)

## Code (excerpt)
```python
# Start a small Flask service that returns a paginated list.
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/items")
def list_items():
    page = int(request.args.get("page", "1"))
    size = int(request.args.get("size", "5"))
    start = (page - 1) * size
    end = start + size
    return jsonify({
        "page": page,
        "size": size,
        "items": items[start:end],
    })
```

## Output (sample)
```
Page: 1 size: 5 total: 20
{'id': 1, 'name': 'item-1'}
{'id': 2, 'name': 'item-2'}
{'id': 3, 'name': 'item-3'}
{'id': 4, 'name': 'item-4'}
{'id': 5, 'name': 'item-5'}
```

## Notes
- The samples start a local Flask server on a random free port and shut it down when done.
- Pagination patterns include offset-style pages and cursor-style pagers.
