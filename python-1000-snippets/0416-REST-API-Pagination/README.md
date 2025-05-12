# REST API Pagination

## Description
This snippet demonstrates pagination in a Flask REST API.

## Code
```python
# Note: Requires `flask`. Install with `pip install flask`
try:
    from flask import Flask, request
    app = Flask(__name__)
    
    @app.route("/items")
    def get_items():
        page = int(request.args.get("page", 1))
        per_page = 2
        items = ["item1", "item2", "item3", "item4"]
        start = (page - 1) * per_page
        return {"items": items[start:start + per_page]}
    
    print("API with pagination configured")
except ImportError:
    print("Mock Output: API with pagination configured")
```

## Output
```
Mock Output: API with pagination configured
```
*(Real output with `flask`: Returns paginated items at `/items?page=1`)*

## Explanation
- **REST API Pagination**: Implements pagination for a list of items.
- **Logic**: Returns a subset of items based on page and per-page parameters.
- **Complexity**: O(n) for n items.
- **Use Case**: Used for large datasets in APIs.
- **Best Practice**: Validate page inputs; include metadata; optimize queries.