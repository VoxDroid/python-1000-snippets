# FastAPI Setup

## Description
This snippet demonstrates a basic FastAPI application with a single GET endpoint that returns a JSON response. The server is started programmatically to ensure immediate feedback.

## Prerequisites
- Install `fastapi` and `uvicorn`: Run `pip install fastapi uvicorn`.
- Ensure Python 3.7+ is installed.
- No other services should be using port 8000.

## Code
```python
# Save as `main.py`
try:
    from fastapi import FastAPI
    import uvicorn
    app = FastAPI()
    
    @app.get("/")
    async def root():
        return {"message": "Hello, FastAPI!"}
    
    if __name__ == "__main__":
        print("Starting FastAPI server...")
        uvicorn.run(app, host="127.0.0.1", port=8000)
except ImportError:
    print("Error: Please install fastapi and uvicorn with `pip install fastapi uvicorn`")
```

## Output
*(When running `python main.py`)*
```
Starting FastAPI server...
INFO:     Will watch for changes in these directories: ['/path/to/your/directory']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
*(Visiting `http://127.0.0.1:8000` in a browser or using `curl http://127.0.0.1:8000`)*
```json
{"message": "Hello, FastAPI!"}
```

## Explanation
- **FastAPI Setup**: Creates a FastAPI app with a single endpoint (`/`) that returns a JSON response.
- **Server Start**: Uses `uvicorn.run` to start the server programmatically when the script is executed.
- **Logic**: The `root` endpoint returns a dictionary, automatically serialized to JSON.
- **Complexity**: O(1) for endpoint execution.
- **Use Case**: Used for building high-performance APIs with automatic OpenAPI documentation.
- **Best Practice**:
  - Install dependencies (`pip install fastapi uvicorn`).
  - Run with `python main.py` to start the server.
  - Access `http://127.0.0.1:8000` in a browser or use `curl` to see the response.
  - Use async for I/O-bound tasks; validate inputs; deploy with a production server in production.
  - If port 8000 is in use, change the `port` parameter in `uvicorn.run`.

## Troubleshooting
- **No Output**: Ensure `fastapi` and `uvicorn` are installed. Run `pip list` to verify. If missing, install with `pip install fastapi uvicorn`.
- **Port Conflict**: If `http://127.0.0.1:8000` is inaccessible, check if another service is using port 8000 (`lsof -i :8000` on Unix-like systems) and change the port in the code (e.g., `port=8001`).
- **Blank Terminal**: If the server starts but you see no response, visit `http://127.0.0.1:8000` or use `curl http://127.0.0.1:8000`. The server waits for HTTP requests and doesn’t print endpoint output to the console.
- **Error Messages**: If you see an exception (e.g., `ModuleNotFoundError`, `OSError`), share the error for further assistance.