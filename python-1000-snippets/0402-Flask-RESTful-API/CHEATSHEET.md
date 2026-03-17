# 0402-Flask-RESTful-API Cheatsheet

- Use `Flask` to build HTTP routes with decorators like `@app.route("/path")`.
- Use `app.test_client()` to run requests in-process without starting a server.
- Use `request.get_json()` to parse JSON request bodies.
- Return dictionaries from view functions and Flask will convert them to JSON.
- Use `abort(404)` or `abort(status_code, description=...)` for error responses.
