# Dense Retrieval

## Description
This snippet demonstrates Dense Retrieval for an e-commerce platform, retrieving product documents using dense vector embeddings for search.

## Code
```python
# Dense Retrieval for product search
# Note: Requires `sentence-transformers`. Install with `pip install sentence-transformers`
try:
    from sentence_transformers import SentenceTransformer, util

    # Dense retrieval model
    class ProductDenseRetriever:
        def __init__(self, documents: list):
            # Initialize retriever and encode documents
            self.retriever = SentenceTransformer("all-MiniLM-L6-v2")
            self.documents = documents
            self.doc_embeddings = self.retriever.encode(documents)

        def retrieve(self, query: str, top_k: int = 1) -> list:
            # Retrieve top-k documents
            query_embedding = self.retriever.encode(query)
            scores = util.cos_sim(query_embedding, self.doc_embeddings)[0]
            top_indices = scores.argsort(descending=True)[:top_k]
            return [self.documents[i] for i in top_indices]

    # Simulate product retrieval
    def retrieve_products(documents: list, queries: list) -> list:
        # Retrieve relevant products
        model = ProductDenseRetriever(documents)
        return [model.retrieve(q) for q in queries]

    # Example usage
    documents = ["Camera: $99, high resolution.", "Laptop: $999, long battery."]
    queries = ["cheap camera"]
    results = retrieve_products(documents, queries)
    print("Dense retrieval result (documents):", results)
except ImportError:
    print("Mock Output: Dense retrieval result (documents): [['Camera: $99, high resolution.']]")
```

## Output
```
Mock Output: Dense retrieval result (documents): [['Camera: $99, high resolution.']]
```
*(Real output with `sentence-transformers`: `Dense retrieval result (documents): [<variable documents>]`)*

## Explanation
- **Purpose**: Dense Retrieval uses dense vector embeddings to retrieve relevant documents, improving search accuracy.
- **Real-World Use Case**: In an e-commerce platform, it retrieves product descriptions matching user queries, enhancing search functionality.
- **Code Breakdown**:
  - The `ProductDenseRetriever` class uses a sentence transformer.
  - The `retrieve` method retrieves top-k documents.
  - The `retrieve_products` function simulates retrieval.
- **Challenges**: Scaling to large document sets, handling semantic nuances, and embedding quality.
- **Integration**: Works with Retrieval-Augmented Generation (Snippet 816) and Vector Search (Snippet 819) for search tasks.
- **Complexity**: O(n*d) for n documents and d embedding dimensions.
- **Best Practices**: Optimize retriever, validate results, and update document embeddings.
- **Extensions**: Use larger models or integrate with search engines.