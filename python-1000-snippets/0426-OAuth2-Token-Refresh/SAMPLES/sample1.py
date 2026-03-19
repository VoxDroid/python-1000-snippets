# sample1.py
# Demonstrates refreshing an OAuth2 access token by calling a local token endpoint.

import threading
import time

import requests
from flask import Flask, request, jsonify


VALID_REFRESH_TOKEN = "refresh123"


def create_app():
    app = Flask(__name__)

    @app.route("/oauth/token", methods=["POST"])
    def token():
        grant_type = request.form.get("grant_type")
        refresh_token = request.form.get("refresh_token")

        if grant_type != "refresh_token" or refresh_token != VALID_REFRESH_TOKEN:
            return (
                jsonify(
                    error="invalid_grant",
                    error_description="Invalid refresh token",
                ),
                400,
            )

        return jsonify(
            access_token="new-access-token",
            token_type="Bearer",
            expires_in=3600,
            refresh_token=VALID_REFRESH_TOKEN,
        )

    return app


def run_server(port: int):
    app = create_app()
    from werkzeug.serving import make_server

    server = make_server("127.0.0.1", port, app)

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def main() -> None:
    # Start a local token server on a random port.
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]

    server = run_server(port)
    time.sleep(0.1)

    try:
        token_url = f"http://127.0.0.1:{port}/oauth/token"
        resp = requests.post(
            token_url,
            data={
                "grant_type": "refresh_token",
                "refresh_token": VALID_REFRESH_TOKEN,
            },
        )
        resp.raise_for_status()

        data = resp.json()
        print("Refreshed access token:", data.get("access_token"))
        print("Expires in:", data.get("expires_in"))
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
