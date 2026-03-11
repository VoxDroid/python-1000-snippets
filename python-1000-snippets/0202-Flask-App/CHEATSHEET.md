# 0202-Flask-App Cheatsheet

* Create app: `app = Flask(__name__)`.
* Routes: use `@app.route` decorator; specify methods with `methods=[...]`.
* `render_template` for HTML; templates in `templates/` folder.
* Use `app.test_client()` to simulate requests without running server.
* Error handlers: `@app.errorhandler(code)` to customize responses.
* Run server: `app.run(debug=True)` or via CLI `flask run` with `FLASK_APP` env var.
* Debug mode reloads on code changes; disable in production.
* Use `request` object for form data (`request.form`), query params (`request.args`).
* For JSON use `request.get_json()` and return dicts for automatic JSON response.
* Use `url_for('endpoint')` to build URLs.
* Best practices: validate input, use blueprints for large apps, secure sessions.
* Example test client call:
  ```python
  with app.test_client() as c:
      resp = c.post('/', data={'key': 'value'})
  ```
