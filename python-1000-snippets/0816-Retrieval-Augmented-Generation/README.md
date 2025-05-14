# Retrieval-Augmented Generation

## Description
This snippet demonstrates Retrieval-Augmented Generation (RAG) for an e-commerce platform, generating product answers by retrieving relevant documents.

## Code
```python
# Retrieval-Augmented Generation for product answers
# Note: Requires `transformers`, `sentence-transformers`. Install with `pip install transformers sentence-transformers`
try:
    from transformers import pipeline
    from sentence_transformers import SentenceTransformer, util

    # RAG model
    class ProductRAG:
        def __init__(self, documents: list):
            # Initialize retriever and generator
            self.retriever = SentenceTransformer("all-MiniLM-L6-v2")
            self.generator = pipeline("text-generation", model="gpt2")
            self.documents = documents
            self.doc_embeddings = self.retriever.encode(documents)

        def retrieve_generate(self, query: str) -> str:
            # Encode query and retrieve top document
            query_embedding = self.retriever.encode(query)
            scores = util.cos_sim(query_embedding, self.doc_embeddings)[0]
            top_idx = scores.argmax()
            context = self.documents[top_idx]
            # Generate answer with context
            prompt = f"Answer using this information: {context}\nQuery: {query}"
            result = self.generator(prompt, max_length=100, num_return_sequences=1)
            return result[0]["generated_text"].strip()

    # Simulate RAG answers
    def rag_product_answers(documents: list, queries: list) -> list:
        # Generate answers with retrieval
        model = ProductRAG(documents)
        return [model.retrieve_generate(q) for q in queries]

    # Example usage
    documents = ["Camera: $99, high resolution.", "Laptop: $999, long battery."]
    queries = ["Camera price"]
    answers = rag_product_answers(documents, queries)
    print("RAG result (answers):", answers)
except ImportError:
    print("Mock Output: RAG result (answers): ['Camera price is $99.']")
```

## Output
```
Mock Output: RAG result (answers): ['Camera price is $99.']
```
*(Real output with `transformers`, `sentence-transformers`: `RAG result (answers): [<variable answers>]`)*

## Explanation
- **Purpose**: RAG combines document retrieval with text generation, improving answer relevance.
- **Real-World Use Case**: In an e-commerce platform, it answers product queries by retrieving relevant product data, enhancing accuracy.
- **Code Breakdown**:
  - The `ProductRAG` class uses a sentence transformer for retrieval and GPT-2 for generation.
  - The `retrieve_generate` method retrieves and generates answers.
  - The `rag_product_answers` function simulates RAG.
- **Challenges**: Scaling retrieval, handling noisy documents, and prompt design.
- **Integration**: Works with Knowledge-Augmented Models (Snippet 815) and Dense Retrieval (Snippet 817) for retrieval tasks.
- **Complexity**: O(n*d + m*t) for n documents, d embedding dimensions, m tokens, and t transformer layers.
- **Best Practices**: Optimize retriever, validate answers, and curate documents.
- **Extensions**: Use larger document sets or integrate with search systems.