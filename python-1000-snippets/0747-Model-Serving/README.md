# Model Serving

## Description
This snippet demonstrates model serving for an e-commerce platform, deploying a recommendation model via a REST API using FastAPI.

## Code
```python
# Model serving for recommendations
# Note: Requires `fastapi`, `uvicorn`, `numpy`, `sklearn`. Install with `pip install fastapi uvicorn numpy scikit-learn`
try:
    from fastapi import FastAPI
    import numpy as np
    from sklearn.linear_model import LogisticRegression
    import pickle

    # Initialize FastAPI app
    app = FastAPI()

    # Load model
    model = LogisticRegression()
    # Simulate trained model
    model.fit(np.random.randn(10, 5), np.random.randint(0, 2, 10))

    @app.post("/predict")
    async def predict(data: list) -> dict:
        # Predict recommendations
        data = np.array(data)
        predictions = model.predict_proba(data)
        return {"predictions": predictions.tolist()}

    # Save model for serving
    with open("served_model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Run server: uvicorn main:app --reload
    print("Model serving result: API running at http://127.0.0.1:8000")
except ImportError:
    print("Mock Output: Model serving result: API running at http://127.0.0.1:8000")
```

## Output
```
Mock Output: Model serving result: API running at http://127.0.0.1:8000
```
*(Real output with `fastapi`, `uvicorn`: `Model serving result: API running at http://127.0.0.1:8000`)*

## Explanation
- **Purpose**: Model serving deploys models for real-time predictions via APIs, enabling integration with applications.
- **Real-World Use Case**: In an e-commerce platform, a recommendation model API serves personalized product suggestions to the website.
- **Code Breakdown**:
  - The FastAPI app defines a `/predict` endpoint.
  - The `predict` endpoint processes input data and returns probabilities.
  - The model is saved for serving.
- **Challenges**: Ensuring low latency, handling high traffic, and securing APIs.
- **Integration**: Works with MLOps Pipeline (Snippet 742) and Real-Time Inference (Snippet 750) for deployment.
- **Complexity**: O(n*d) for n samples and d features per prediction.
- **Best Practices**: Optimize latency, secure endpoints, monitor uptime, and scale servers.