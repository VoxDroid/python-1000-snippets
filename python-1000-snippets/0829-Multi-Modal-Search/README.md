# Multi-Modal Search

## Description
This snippet demonstrates Multi-Modal Search for an e-commerce platform, combining text and embedding-based product search.

## Code
```python
# Multi-Modal Search for product search
# Note: Requires `sentence-transformers`, `sklearn`. Install with `pip install sentence-transformers scikit-learn`
try:
    from sentence_transformers import SentenceTransformer, util
    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np

    # Multi-modal search model
    class ProductMultiModalSearch:
        def __init__(self, products: list):
            # Initialize text and embedding search
            self.vectorizer = TfidfVectorizer()
            self.retriever = SentenceTransformer("all-MiniLM-L6-v2")
            self.products = products
            self.doc_vectors = self.vectorizer.fit_transform(products)
            self.product_embeddings = self.retriever.encode(products)

        def search(self, query: str, top_k: int = 1) -> list:
            # Combine text and embedding scores
            query_vector = self.vectorizer.transform([query])
            text_scores = (self.doc_vectors * query_vector.T).toarray().flatten()
            query_embedding = self.retriever.encode(query)
            embedding_scores = util.cos_sim(query_embedding, self.product_embeddings)[0]
            combined_scores = text_scores + embedding_scores.numpy()
            top_indices = np.argsort(combined_scores)[::-1][:top_k]
            return [self.products[i] for i in top_indices]

    # Simulate multi-modal search
    def multi_modal_search_products(products: list, queries: list) -> list:
        # Search with multi-modal approach
        model = ProductMultiModalSearch(products)
        return [model.search(q) for q in queries]

    # Example usage
    products = ["Camera: high resolution", "Laptop: long battery"]
    queries = ["high quality camera"]
    results = multi_modal_search_products(products, queries)
    print("Multi-modal search result (products):", results)
except ImportError:
    print("Mock Output: Multi-modal search result (products): [['Camera: high resolution']]")
```

## Output
```
Mock Output: Multi-modal search result (products): [['Camera: high resolution']]
```
*(Real output with `sentence-transformers`, `sklearn`: `Multi-modal search result (products): [<variable products>]`)*

## Explanation
- **Purpose**: Multi-Modal Search combines multiple data modalities (e.g., text, embeddings) for robust search.
- **Real-World Use Case**: In an e-commerce platform, it enhances product search by leveraging both keyword and semantic matching.
- **Code Breakdown**:
  - The `ProductMultiModalSearch` class combines TF-IDF and embeddings.
  - The `search` method fuses scores.
  - The `multi_modal_search_products` function simulates search.
- **Challenges**: Balancing modalities, handling modality misalignment, and computational cost.
- **Integration**: Works with Federated Search (Snippet 828) and Image Retrieval (Snippet 830) for multi-modal tasks.
- **Complexity**: O(n*d + n*e) for n products, d vocabulary size, and e embedding dimensions.
- **Best Practices**: Tune score weights, validate results, and preprocess data.
- **Extensions**: Include image data or integrate with search platforms.