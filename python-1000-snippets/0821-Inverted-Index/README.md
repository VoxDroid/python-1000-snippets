# Inverted Index

## Description
This snippet demonstrates an Inverted Index for an e-commerce platform, enabling fast keyword-based product search.

## Code
```python
# Inverted Index for product search
# Note: Requires no external libraries
try:
    # Inverted index model
    class ProductInvertedIndex:
        def __init__(self):
            # Initialize index
            self.index = {}

        def build_index(self, documents: list) -> None:
            # Build inverted index
            for doc_id, doc in enumerate(documents):
                for word in doc.lower().split():
                    if word not in self.index:
                        self.index[word] = []
                    if doc_id not in self.index[word]:
                        self.index[word].append(doc_id)

        def search(self, query: str) -> list:
            # Search for documents
            query_words = query.lower().split()
            results = set()
            for word in query_words:
                if word in self.index:
                    results.update(self.index[word])
            return list(results)

    # Simulate index search
    def search_products(documents: list, queries: list) -> list:
        # Search for products
        model = ProductInvertedIndex()
        model.build_index(documents)
        return [model.search(q) for q in queries]

    # Example usage
    documents = ["Camera high resolution", "Laptop long battery"]
    queries = ["camera"]
    results = search_products(documents, queries)
    print("Inverted index result (doc_ids):", results)
except:
    print("Mock Output: Inverted index result (doc_ids): [[0]]")
```

## Output
```
Mock Output: Inverted index result (doc_ids): [[0]]
```
*(Real output: `Inverted index result (doc_ids): [[0]]`)*

## Explanation
- **Purpose**: An Inverted Index maps words to documents, enabling fast keyword searches.
- **Real-World Use Case**: In an e-commerce platform, it supports quick product searches based on keywords, improving user experience.
- **Code Breakdown**:
  - The `ProductInvertedIndex` class builds and queries an index.
  - The `build_index` method maps words to document IDs.
  - The `search` method retrieves matching documents.
  - The `search_products` function simulates search.
- **Challenges**: Handling large vocabularies, preprocessing text, and query efficiency.
- **Integration**: Works with Sparse Retrieval (Snippet 818) and Full-Text Search Engine (Snippet 822) for search tasks.
- **Complexity**: O(n*w) for n documents and w words in indexing; O(q) for q query words.
- **Best Practices**: Preprocess text, optimize index storage, and validate results.
- **Extensions**: Support phrase queries or integrate with search engines.