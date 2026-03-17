# sample3.py
# Demonstrates returning custom status codes and headers from FastAPI.

import subprocess
import sys


def ensure_fastapi():
    try:
        import fastapi  # type: ignore
        return fastapi
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn"])  # nosec
        import fastapi  # type: ignore
        return fastapi


def main() -> None:
    fastapi = ensure_fastapi()
    from fastapi import FastAPI, Response

    app = FastAPI()

    @app.get("/status")
    def status(code: int = 202):
        return Response(content="Accepted", status_code=code, headers={"X-Example": "true"})

    from fastapi.testclient import TestClient

    client = TestClient(app)
    response = client.get("/status")
    print("Status code:", response.status_code)
    print("Headers:", response.headers.get("X-Example"))
    print("Body:", response.text)


if __name__ == "__main__":
    main()
