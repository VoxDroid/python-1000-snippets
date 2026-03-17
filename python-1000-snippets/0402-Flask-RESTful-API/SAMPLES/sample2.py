# sample2.py
# Demonstrates handling POST JSON payloads in a Flask API.

import json
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
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    @app.route("/api/echo", methods=["POST"])
    def echo():
        payload = request.get_json(force=True, silent=True) or {}
        return jsonify({"received": payload})

    with app.test_client() as client:
        payload = {"text": "Hello"}
        response = client.post(
            "/api/echo",
            data=json.dumps(payload),
            content_type="application/json",
        )
        print("Status code:", response.status_code)
        print("Response JSON:", response.get_json())


if __name__ == "__main__":
    main()
