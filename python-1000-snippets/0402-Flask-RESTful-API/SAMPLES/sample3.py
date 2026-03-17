# sample3.py
# Demonstrates a Flask API with URL path parameters and error handling.

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
    from flask import Flask, jsonify, abort

    app = Flask(__name__)
    items = {"1": "Item One", "2": "Item Two"}

    @app.route("/api/items/<item_id>")
    def get_item(item_id: str):
        if item_id not in items:
            abort(404, description="Item not found")
        return jsonify({"id": item_id, "value": items[item_id]})

    with app.test_client() as client:
        resp1 = client.get("/api/items/1")
        resp2 = client.get("/api/items/999")
        print("Existing item status:", resp1.status_code, resp1.get_json())
        print("Missing item status:", resp2.status_code)


if __name__ == "__main__":
    main()
