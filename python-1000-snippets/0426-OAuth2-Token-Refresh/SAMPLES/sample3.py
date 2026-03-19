# sample3.py
# Demonstrates refreshing an OAuth2 access token and using it to access a protected endpoint.

import threading
import time

import requests
from flask import Flask, request, jsonify


VALID_REFRESH_TOKEN = "refresh123"
VALID_ACCESS_TOKEN = "new-access-token"


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
            access_token=VALID_ACCESS_TOKEN,
            token_type="Bearer",
            expires_in=3600,
            refresh_token=VALID_REFRESH_TOKEN,
        )

    @app.route("/protected")
    def protected():
        auth = request.headers.get("Authorization", "")
        if auth != f"Bearer {VALID_ACCESS_TOKEN}":
            return jsonify(error="invalid_token"), 401
        return jsonify(message="Access granted")

    return app


def run_server(port: int):
    app = create_app()
    from werkzeug.serving import make_server

    server = make_server("127.0.0.1", port, app)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def main() -> None:
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]

    server = run_server(port)
    time.sleep(0.1)

    try:
        token_url = f"http://127.0.0.1:{port}/oauth/token"
        refresh_resp = requests.post(
            token_url,
            data={
                "grant_type": "refresh_token",
                "refresh_token": VALID_REFRESH_TOKEN,
            },
        )
        refresh_resp.raise_for_status()
        access_token = refresh_resp.json()["access_token"]

        protected_url = f"http://127.0.0.1:{port}/protected"
        protected_resp = requests.get(
            protected_url, headers={"Authorization": f"Bearer {access_token}"}
        )
        print("Protected endpoint response:", protected_resp.json())
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
