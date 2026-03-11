# 0204-FastAPI-Setup Cheatsheet

* Install packages: `pip install fastapi uvicorn` (and `pydantic`).
* Create app: `app = FastAPI()`.
* Define path operations with decorators (`@app.get`, `@app.post`, etc.).
* Use Pydantic models for request bodies and automatic validation.
* Run server: `uvicorn main:app --reload` or programmatically `uvicorn.run(app, host='127.0.0.1', port=8000)`.
* `TestClient` from `fastapi.testclient` (uses `requests`) for offline testing without network.
* Automatic docs at `/docs` (Swagger UI) and `/redoc`; OpenAPI JSON at `/openapi.json`.
* Dependency injection via function parameters using `Depends`.
* Background tasks with `BackgroundTasks`; WebSockets support with `WebSocket` class.
* Request/response headers accessible via `Request`, `Response` objects.
* Use async def for concurrency; sync def also supported.
* Best practices: validate input, handle exceptions with `@app.exception_handler`, paginate large responses.
* Example TestClient usage:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  resp = client.get('/')
  ```
