# sample2.py
# Demonstrates paginated REST API results with a "has_more" indicator.

import threading
from typing import List

import requests
from flask import Flask, jsonify, request
from werkzeug.serving import make_server


def _create_app() -> Flask:
    app = Flask(__name__)

    items: List[dict] = [
        {"id": i, "name": f"item-{i}"} for i in range(1, 31)
    ]

    @app.route("/items")
    def list_items():
        page = int(request.args.get("page", "1"))
        size = int(request.args.get("size", "7"))
        start = (page - 1) * size
        end = start + size
        page_items = items[start:end]
        total = len(items)
        has_more = end < total
        return jsonify(
            {
                "page": page,
                "size": size,
                "total": total,
                "has_more": has_more,
                "items": page_items,
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
        # Request page 2
        resp = requests.get(
            f"http://127.0.0.1:{port}/items", params={"page": 2, "size": 7}
        )
        resp.raise_for_status()
        data = resp.json()

        print("Page:", data["page"], "size:", data["size"], "total:", data["total"])
        print("Has more:", data["has_more"])
        for item in data["items"]:
            print(item)
    finally:
        server.shutdown()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
