# Query Expansion

## Description
This snippet demonstrates Query Expansion for an e-commerce platform, enhancing search queries with synonyms to improve recall.

## Code
```python
# Query Expansion for product search
# Note: Requires `nltk`. Install with `pip install nltk` and run `nltk.download('wordnet')`
try:
    from nltk.corpus import wordnet
    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np
    import nltk
    nltk.download('wordnet')

    # Query expansion model
    class ProductQueryExpander:
        def __init__(self, documents: list):
            # Initialize vectorizer and documents
            self.vectorizer = TfidfVectorizer()
            self.documents = documents
            self.doc_vectors = self.vectorizer.fit_transform(documents)

        def expand_query(self, query: str) -> str:
            # Expand query with synonyms
            words = query.lower().split()
            expanded = []
            for word in words:
                expanded.append(word)
                synonyms = [syn.name().split('.')[0] for syn in wordnet.synsets(word)][:2]
                expanded.extend(synonyms)
            return " ".join(expanded)

        def search(self, query: str, top_k: int = 1) -> list:
            # Search with expanded query
            expanded_query = self.expand_query(query)
            query_vector = self.vectorizer.transform([expanded_query])
            scores = (self.doc_vectors * query_vector.T).toarray().flatten()
            top_indices = np.argsort(scores)[::-1][:top_k]
            return [self.documents[i] for i in top_indices]

    # Simulate query expansion
    def expand_search_products(documents: list, queries: list) -> list:
        # Search with expanded queries
        model = ProductQueryExpander(documents)
        return [model.search(q) for q in queries]

    # Example usage
    documents = ["Camera: high resolution", "Laptop: long battery"]
    queries = ["camera"]
    results = expand_search_products(documents, queries)
    print("Query expansion result (documents):", results)
except ImportError:
    print("Mock Output: Query expansion result (documents): [['Camera: high resolution']]")
```

## Output
```
Mock Output: Query expansion result (documents): [['Camera: high resolution']]
```
*(Real output with `nltk`, `sklearn`: `Query expansion result (documents): [<variable documents>]`)*

## Explanation
- **Purpose**: Query Expansion adds synonyms or related terms to queries, improving search recall.
- **Real-World Use Case**: In an e-commerce platform, it enhances product search by including synonyms, capturing more relevant results.
- **Code Breakdown**:
  - The `ProductQueryExpander` class uses WordNet for synonyms and TF-IDF for search.
  - The `expand_query` method adds synonyms.
  - The `search` method retrieves documents.
  - The `expand_search_products` function simulates search.
- **Challenges**: Avoiding irrelevant synonyms, balancing recall and precision, and computational cost.
- **Integration**: Works with Semantic Search (Snippet 823) and Relevance Feedback (Snippet 825) for search tasks.
- **Complexity**: O(n*d + s) for n documents, d vocabulary size, and s synonyms.
- **Best Practices**: Filter synonyms, validate results, and tune expansion.
- **Extensions**: Use contextual embeddings or integrate with search systems.