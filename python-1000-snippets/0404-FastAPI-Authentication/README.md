# FastAPI Authentication

## Description
This snippet demonstrates basic authentication with `fastapi`.

## Code
```python
# Note: Requires `fastapi`. Install with `pip install fastapi`
try:
    from fastapi import FastAPI, Depends, HTTPException
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    app = FastAPI()
    security = HTTPBasic()
    
    @app.get("/protected")
    def protected(credentials: HTTPBasicCredentials = Depends(security)):
        if credentials.username == "user" and credentials.password == "pass":
            return {"message": "Authenticated"}
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    print("FastAPI server configured")
except ImportError:
    print("Mock Output: FastAPI server configured")
```

## Output
```
Mock Output: FastAPI server configured
```
*(Real output with `fastapi`: Runs server, accessible at `/protected` with credentials)*

## Explanation
- **FastAPI Authentication**: Implements basic HTTP authentication.
- **Logic**: Protects a route with username/password validation.
- **Complexity**: O(1) per request.
- **Use Case**: Used for securing API endpoints.
- **Best Practice**: Use OAuth2/JWT for production; secure credentials; handle errors.