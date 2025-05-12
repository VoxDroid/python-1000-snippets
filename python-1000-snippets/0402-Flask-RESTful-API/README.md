# Flask RESTful API

## Description
This snippet demonstrates a simple RESTful API using `flask`.

## Code
```python
# Note: Requires `flask`. Install with `pip install flask`
try:
    from flask import Flask
    app = Flask(__name__)
    
    @app.route("/api", methods=["GET"])
    def get_data():
        return {"data": "Hello"}
    
    if __name__ == "__main__":
        app.run(debug=True)
    print("API server started")
except ImportError:
    print("Mock Output: API server started")
```

## Output
```
Mock Output: API server started
```
*(Real output with `flask`: Runs server, accessible at `http://127.0.0.1:5000/api`)*

## Explanation
- **Flask RESTful API**: Creates a GET endpoint returning JSON.
- **Logic**: Defines a `/api` route with `flask` to return a dictionary.
- **Complexity**: O(1) per request.
- **Use Case**: Used for building web APIs or microservices.
- **Best Practice**: Handle errors; secure endpoints; use blueprints for modularity.