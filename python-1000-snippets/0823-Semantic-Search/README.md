# Semantic Search

## Description
This snippet demonstrates Semantic Search for an e-commerce platform, retrieving products based on semantic similarity using embeddings.

## Code
```python
# Semantic Search for product search
# Note: Requires `sentence-transformers`. Install with `pip install sentence-transformers`
try:
    from sentence_transformers import SentenceTransformer, util

    # Semantic search model
    class ProductSemanticSearch:
        def __init__(self, products: list):
            # Initialize retriever and encode products
            self.retriever = SentenceTransformer("all-MiniLM-L6-v2")
            self.products = products
            self.product_embeddings = self.retriever.encode(products)

        def search(self, query: str, top_k: int = 1) -> list:
            # Search for semantically similar products
            query_embedding = self.retriever.encode(query)
            scores = util.cos_sim(query_embedding, self.product_embeddings)[0]
            top_indices = scores.argsort(descending=True)[:top_k]
            return [self.products[i] for i in top_indices]

    # Simulate semantic search
    def semantic_search_products(products: list, queries: list) -> list:
        # Search for products
        model = ProductSemanticSearch(products)
        return [model.search(q) for q in queries]

    # Example usage
    products = ["Camera: high resolution", "Laptop: long battery"]
    queries = ["good camera quality"]
    results = semantic_search_products(products, queries)
    print("Semantic search result (products):", results)
except ImportError:
    print("Mock Output: Semantic search result (products): [['Camera: high resolution']]")
```

## Output
```
Mock Output: Semantic search result (products): [['Camera: high resolution']]
```
*(Real output with `sentence-transformers`: `Semantic search result (products): [<variable products>]`)*

## Explanation
- **Purpose**: Semantic Search retrieves items based on meaning, improving relevance over keyword-based search.
- **Real-World Use Case**: In an e-commerce platform, it finds products matching user intent, enhancing search quality.
- **Code Breakdown**:
  - The `ProductSemanticSearch` class uses a sentence transformer.
  - The `search` method retrieves semantically similar products.
  - The `semantic_search_products` function simulates search.
- **Challenges**: Embedding quality, handling ambiguous queries, and scaling.
- **Integration**: Works with Vector Search (Snippet 819) and Query Expansion (Snippet 824) for search tasks.
- **Complexity**: O(n*d) for n products and d embedding dimensions.
- **Best Practices**: Use robust embeddings, validate results, and update product data.
- **Extensions**: Support multi-lingual search or integrate with search systems.