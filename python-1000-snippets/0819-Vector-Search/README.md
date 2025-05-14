# Vector Search

## Description
This snippet demonstrates Vector Search for an e-commerce platform, finding products similar to a query using cosine similarity on embeddings.

## Code
```python
# Vector Search for product similarity
# Note: Requires `sentence-transformers`. Install with `pip install sentence-transformers`
try:
    from sentence_transformers import SentenceTransformer, util

    # Vector search model
    class ProductVectorSearch:
        def __init__(self, products: list):
            # Initialize retriever and encode products
            self.retriever = SentenceTransformer("all-MiniLM-L6-v2")
            self.products = products
            self.product_embeddings = self.retriever.encode(products)

        def search(self, query: str, top_k: int = 1) -> list:
            # Search for similar products
            query_embedding = self.retriever.encode(query)
            scores = util.cos_sim(query_embedding, self.product_embeddings)[0]
            top_indices = scores.argsort(descending=True)[:top_k]
            return [self.products[i] for i in top_indices]

    # Simulate vector search
    def vector_search_products(products: list, queries: list) -> list:
        # Search for similar products
        model = ProductVectorSearch(products)
        return [model.search(q) for q in queries]

    # Example usage
    products = ["Camera: $99, high resolution.", "Laptop: $999, long battery."]
    queries = ["high resolution camera"]
    results = vector_search_products(products, queries)
    print("Vector search result (products):", results)
except ImportError:
    print("Mock Output: Vector search result (products): [['Camera: $99, high resolution.']]")
```

## Output
```
Mock Output: Vector search result (products): [['Camera: $99, high resolution.']]
```
*(Real output with `sentence-transformers`: `Vector search result (products): [<variable products>]`)*

## Explanation
- **Purpose**: Vector Search retrieves items based on similarity in embedding space, enabling semantic search.
- **Real-World Use Case**: In an e-commerce platform, it finds products similar to user queries, improving search relevance.
- **Code Breakdown**:
  - The `ProductVectorSearch` class uses a sentence transformer.
  - The `search` method retrieves top-k similar products.
  - The `vector_search_products` function simulates search.
- **Challenges**: Embedding quality, scaling to large datasets, and query ambiguity.
- **Integration**: Works with Dense Retrieval (Snippet 817) and Approximate Nearest Neighbors (Snippet 820) for search tasks.
- **Complexity**: O(n*d) for n products and d embedding dimensions.
- **Best Practices**: Optimize embeddings, validate results, and update product data.
- **Extensions**: Use advanced similarity metrics or integrate with recommendation systems.