# sample3.py
# Demonstrates cursor-style pagination (opaque cursor token) in a REST API.

import base64
import json
import threading
from typing import List, Optional

import requests
from flask import Flask, jsonify, request
from werkzeug.serving import make_server


def _encode_cursor(index: int) -> str:
    return base64.urlsafe_b64encode(str(index).encode("utf-8")).decode("utf-8")


def _decode_cursor(cursor: Optional[str]) -> int:
    if not cursor:
        return 0
    try:
        return int(base64.urlsafe_b64decode(cursor.encode("utf-8")).decode("utf-8"))
    except Exception:
        return 0


def _create_app() -> Flask:
    app = Flask(__name__)

    items: List[dict] = [
        {"id": i, "name": f"item-{i}"} for i in range(1, 51)
    ]

    @app.route("/items")
    def list_items():
        cursor = request.args.get("cursor")
        size = int(request.args.get("size", "10"))
        start = _decode_cursor(cursor)
        end = start + size
        page_items = items[start:end]
        next_cursor = _encode_cursor(end) if end < len(items) else ""
        return jsonify(
            {
                "items": page_items,
                "next_cursor": next_cursor,
            }
        )

    return app


def main() -> None:
    app = _create_app()
    server = make_server("127.0.0.1", 0, app)
    port = server.server_port

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        cursor = None
        all_items = []

        while True:
            params = {"size": 15}
            if cursor:
                params["cursor"] = cursor
            resp = requests.get(f"http://127.0.0.1:{port}/items", params=params)
            resp.raise_for_status()
            data = resp.json()

            all_items.extend(data["items"])
            cursor = data.get("next_cursor")
            if not cursor:
                break

        print(f"Retrieved {len(all_items)} items total")
        print("First item:", all_items[0])
        print("Last item:", all_items[-1])
    finally:
        server.shutdown()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
