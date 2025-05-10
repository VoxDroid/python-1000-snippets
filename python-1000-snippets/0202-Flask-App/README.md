# Flask App

## Description
This snippet demonstrates a Flask web application with multiple routes, template rendering, and basic error handling to showcase a more realistic use case.

## Directory Structure
```
flask_app/
├── templates/
│   └── index.html
└── app.py
```

## Code
```python
# flask_app/app.py
# Note: Requires `flask`. Install with `pip install flask`
try:
    from flask import Flask, render_template, request
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html", title="Welcome to Flask")

    @app.route("/greet", methods=["GET", "POST"])
    def greet():
        if request.method == "POST":
            name = request.form.get("name", "Guest")
            return render_template("index.html", title="Greeting", message=f"Hello, {name}!")
        return render_template("index.html", title="Enter Name")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("index.html", title="Error", message="Page not found"), 404

    if __name__ == "__main__":
        app.run(debug=True)
except ImportError:
    print("Mock Output: Flask app running at http://127.0.0.1:5000")
```

```html
<!-- flask_app/templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    {% if message %}
        <p>{{ message }}</p>
    {% else %}
        <form method="POST" action="/greet">
            <input type="text" name="name" placeholder="Enter your name">
            <button type="submit">Greet</button>
        </form>
    {% endif %}
    <p><a href="/">Home</a></p>
</body>
</html>
```

## Output
```
Mock Output: Flask app running at http://127.0.0.1:5000
```
*(Real output with Flask: Server runs; visiting `http://127.0.0.1:5000` shows a form; submitting a name at `/greet` displays a greeting; invalid URLs show "Page not found")*

## Explanation
- **Flask App**: Defines a Flask app with a home route (`/`), a form-handling route (`/greet`), and a 404 error handler.
- **Logic**: Uses `render_template` to render `index.html`, passing dynamic data (`title`, `message`). The `/greet` route handles GET (shows form) and POST (processes form input).
- **Complexity**: O(1) for route handling and template rendering.
- **Use Case**: Used for building lightweight web applications or APIs with dynamic content.
- **Best Practice**: Disable debug mode in production; validate form inputs; use secure session management.