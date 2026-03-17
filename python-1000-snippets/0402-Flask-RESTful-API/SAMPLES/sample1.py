# sample1.py
# Demonstrates a basic Flask RESTful endpoint and uses the test client.

import subprocess
import sys


def ensure_flask():
    try:
        import flask  # type: ignore
        return flask
    except ImportError:
        print("Missing dependency: flask. Install with: python -m pip install flask")
        sys.exit(1)


def main() -> None:
    flask = ensure_flask()
    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route("/api/hello")
    def hello():
        return jsonify({"message": "Hello"})

    # Use Flask's built-in test client to avoid running an external server.
    with app.test_client() as client:
        response = client.get("/api/hello")
        print("Status code:", response.status_code)
        print("JSON response:", response.get_json())


if __name__ == "__main__":
    main()
