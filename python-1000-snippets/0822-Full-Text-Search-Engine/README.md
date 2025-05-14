# Full-Text Search Engine

## Description
This snippet demonstrates a Full-Text Search Engine for an e-commerce platform, using Elasticsearch to search product descriptions.

## Code
```python
# Full-Text Search Engine for product search
# Note: Requires `elasticsearch`. Install with `pip install elasticsearch`
try:
    from elasticsearch import Elasticsearch

    # Full-text search model
    class ProductSearchEngine:
        def __init__(self, index_name: str = "products"):
            # Initialize Elasticsearch client
            self.es = Elasticsearch(["http://localhost:9200"])
            self.index_name = index_name

        def index_documents(self, documents: list) -> None:
            # Index product documents
            for i, doc in enumerate(documents):
                self.es.index(index=self.index_name, id=i, body={"description": doc})

        def search(self, query: str, top_k: int = 1) -> list:
            # Search for products
            response = self.es.search(index=self.index_name, query={"match": {"description": query}}, size=top_k)
            return [hit["_source"]["description"] for hit in response["hits"]["hits"]]

    # Simulate full-text search
    def search_products_es(documents: list, queries: list) -> list:
        # Search for products
        model = ProductSearchEngine()
        model.index_documents(documents)
        return [model.search(q) for q in queries]

    # Example usage
    documents = ["Camera high resolution", "Laptop long battery"]
    queries = ["camera"]
    results = search_products_es(documents, queries)
    print("Full-text search result (documents):", results)
except ImportError:
    print("Mock Output: Full-text search result (documents): [['Camera high resolution']]")
```

## Output
```
Mock Output: Full-text search result (documents): [['Camera high resolution']]
```
*(Real output with `elasticsearch` and running server: `Full-text search result (documents): [<variable documents>]`)*

## Explanation
- **Purpose**: A Full-Text Search Engine enables robust text-based searches, supporting complex queries.
- **Real-World Use Case**: In an e-commerce platform, it searches product descriptions, improving search functionality.
- **Code Breakdown**:
  - The `ProductSearchEngine` class uses Elasticsearch.
  - The `index_documents` method indexes products.
  - The `search` method retrieves matching documents.
  - The `search_products_es` function simulates search.
- **Challenges**: Setting up Elasticsearch, handling large indices, and query optimization.
- **Integration**: Works with Inverted Index (Snippet 821) and Semantic Search (Snippet 823) for search tasks.
- **Complexity**: O(n) for indexing n documents; O(q) for query complexity.
- **Best Practices**: Optimize indices, validate results, and configure Elasticsearch.
- **Extensions**: Support advanced queries or integrate with e-commerce platforms.