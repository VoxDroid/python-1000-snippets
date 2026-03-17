# sample2.py
# Demonstrates dependency injection with FastAPI and secure endpoints.

import subprocess
import sys


def ensure_fastapi():
    try:
        import fastapi  # type: ignore
        return fastapi
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn"] )  # nosec
        import fastapi  # type: ignore
        return fastapi


def main() -> None:
    fastapi = ensure_fastapi()
    from fastapi import FastAPI, Depends, HTTPException
    from fastapi.security import HTTPBasic, HTTPBasicCredentials

    app = FastAPI()
    security = HTTPBasic()

    def authenticate(credentials: HTTPBasicCredentials = Depends(security)) -> str:
        if credentials.username == "user" and credentials.password == "pass":
            return credentials.username
        raise HTTPException(status_code=401, detail="Unauthorized")

    @app.get("/secure")
    def secure_route(user: str = Depends(authenticate)):
        return {"message": f"Welcome, {user}"}

    # Use FastAPI test client to exercise the endpoint without running a server.
    from fastapi.testclient import TestClient

    client = TestClient(app)
    response = client.get("/secure", auth=("user", "pass"))
    print("Status code:", response.status_code)
    print("JSON:", response.json())


if __name__ == "__main__":
    main()
