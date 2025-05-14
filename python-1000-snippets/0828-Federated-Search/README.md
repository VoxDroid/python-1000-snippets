# Federated Search

## Description
This snippet demonstrates Federated Search for an e-commerce platform, combining results from multiple product sources (e.g., electronics, clothing).

## Code
```python
# Federated Search for product search
# Note: Requires `sklearn`. Install with `pip install scikit-learn`
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np

    # Federated search model
    class ProductFederatedSearch:
        def __init__(self, sources: dict):
            # Initialize vectorizers for each source
            self.sources = sources
            self.vectorizers = {k: TfidfVectorizer() for k in sources}
            self.doc_vectors = {k: self.vectorizers[k].fit_transform(v) for k, v in sources.items()}

        def search(self, query: str, top_k: int = 1) -> list:
            # Search across sources and combine results
            results = []
            for source, documents in self.sources.items():
                query_vector = self.vectorizers[source].transform([query])
                scores = (self.doc_vectors[source] * query_vector.T).toarray().flatten()
                top_indices = np.argsort(scores)[::-1][:top_k]
                results.extend([(documents[i], source) for i in top_indices])
            return results

    # Simulate federated search
    def federated_search_products(sources: dict, queries: list) -> list:
        # Search across sources
        model = ProductFederatedSearch(sources)
        return [model.search(q) for q in queries]

    # Example usage
    sources = {
        "electronics": ["Camera: high resolution", "Laptop: long battery"],
        "clothing": ["Shirt: cotton", "Jeans: denim"]
    }
    queries = ["camera"]
    results = federated_search_products(sources, queries)
    print("Federated search result (documents, sources):", results)
except ImportError:
    print("Mock Output: Federated search result (documents, sources): [[('Camera: high resolution', 'electronics')]]")
```

## Output
```
Mock Output: Federated search result (documents, sources): [[('Camera: high resolution', 'electronics')]]
```
*(Real output with `sklearn`: `Federated search result (documents, sources): [<variable results>]`)*

## Explanation
- **Purpose**: Federated Search combines results from multiple sources, providing comprehensive results.
- **Real-World Use Case**: In an e-commerce platform, it searches across product categories, improving coverage.
- **Code Breakdown**:
  - The `ProductFederatedSearch` class uses TF-IDF per source.
  - The `search` method retrieves and combines results.
  - The `federated_search_products` function simulates search.
- **Challenges**: Normalizing scores, handling heterogeneous sources, and latency.
- **Integration**: Works with Personalized Search (Snippet 827) and Multi-Modal Search (Snippet 829) for search tasks.
- **Complexity**: O(n*d*s) for n documents, d vocabulary size, and s sources.
- **Best Practices**: Normalize scores, validate results, and optimize sources.
- **Extensions**: Support weighted sources or integrate with search platforms.