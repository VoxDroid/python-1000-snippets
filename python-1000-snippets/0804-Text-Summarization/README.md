# Text Summarization

## Description
This snippet demonstrates Text Summarization for an e-commerce platform, performing extractive summarization on product reviews to highlight key customer feedback using a BERT-based approach.

## Code
```python
# Text Summarization for product reviews using BERT-based extractive method
# Note: Requires `transformers`, `torch`, `numpy`. Install with `pip install transformers torch numpy`
try:
    import numpy as np
    import torch
    from transformers import BertTokenizer, BertModel
    from sklearn.metrics.pairwise import cosine_similarity

    # BERT-based extractive summarization model
    class ReviewSummarizer:
        def __init__(self, top_n: int = 1):
            # Initialize BERT tokenizer and model
            self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
            self.model = BertModel.from_pretrained('bert-base-uncased')
            self.top_n = top_n  # Number of sentences to select

        def get_sentence_embeddings(self, sentences: list) -> np.ndarray:
            # Compute BERT embeddings for sentences
            embeddings = []
            for sent in sentences:
                inputs = self.tokenizer(sent, return_tensors='pt', padding=True, truncation=True, max_length=512)
                with torch.no_grad():
                    outputs = self.model(**inputs)
                # Use [CLS] token embedding
                embeddings.append(outputs.last_hidden_state[:, 0, :].squeeze().numpy())
            return np.array(embeddings)

        def summarize(self, review: str) -> str:
            # Split review into sentences and select top-ranked ones
            sentences = review.split('. ')
            if len(sentences) <= self.top_n:
                return review  # Return original if too short
            embeddings = self.get_sentence_embeddings(sentences)
            # Compute similarity to mean embedding for ranking
            mean_embedding = np.mean(embeddings, axis=0)
            similarities = cosine_similarity(embeddings, [mean_embedding])
            # Select top N sentences
            top_indices = np.argsort(similarities.flatten())[-self.top_n:]
            selected = [sentences[i] for i in sorted(top_indices)]
            return '. '.join(selected) + ('.' if selected else '')

    # Simulate review summarization
    def summarize_reviews(reviews: list) -> list:
        # Summarize multiple product reviews
        model = ReviewSummarizer(top_n=1)
        return [model.summarize(review) for review in reviews]

    # Example usage
    reviews = [
        "The camera is great but battery life is short. The autofocus is fast. Truly excellent.",
        "Excellent product with fast delivery. Highly recommend it. Packaging was sturdy."
    ]
    summaries = summarize_reviews(reviews)
    print("Text summarization result (summaries):", summaries)
except ImportError:
    print("Mock Output: Text summarization result (summaries): ['Truly excellent.', 'Excellent product with fast delivery.']")
```

## Output
```
Mock Output: Text summarization result (summaries): ['Truly excellent.', 'Excellent product with fast delivery.']
```
*(Real output with `transformers`, `torch`, `numpy`: `Text summarization result (summaries): ['Truly excellent.', 'Excellent product with fast delivery.']` or similar, depending on BERT ranking)*

## Explanation
- **Purpose**: This extractive summarization method selects the most representative sentences from product reviews, using BERT embeddings to capture semantic importance, ensuring concise and relevant summaries.
- **Real-World Use Case**: In an e-commerce platform, summarizing customer reviews helps highlight key feedback (e.g., "great camera" or "fast delivery") for product pages, aiding purchase decisions and reducing information overload.
- **Code Breakdown**:
  - The `ReviewSummarizer` class initializes a BERT tokenizer and model, with `top_n` controlling the number of sentences to select.
  - The `get_sentence_embeddings` method computes BERT embeddings for each sentence, using the [CLS] token for representation.
  - The `summarize` method splits reviews into sentences, ranks them based on cosine similarity to the mean embedding, and selects the top `top_n` sentences.
  - The `summarize_reviews` function applies summarization to multiple reviews.
- **Why This Approach?**: Unlike the original LSA-based method (using `sumy`), which struggled with short texts, BERT embeddings capture deeper semantic meaning, enabling better sentence ranking even for brief reviews. This ensures actual summarization rather than returning the full text.
- **Challenges**:
  - **Short Texts**: Reviews with one sentence can't be summarized further; the code handles this by returning the original text.
  - **Computational Cost**: BERT is resource-intensive, especially for large review datasets.
  - **Sentence Splitting**: Simple splitting on periods may fail for complex punctuation; advanced NLP tokenizers could improve this.
  - **Ranking Bias**: Mean embedding may favor generic sentences; alternative ranking (e.g., centrality in a sentence graph) could be explored.
- **Integration**:
  - Complements **Abstractive Summarization (Snippet 805)** for generating paraphrased summaries.
  - Pairs with **Extractive Summarization (Snippet 806)** for alternative extractive methods.
  - Enhances **Relation Extraction (Snippet 799)** by summarizing reviews before extracting attributes.
- **Complexity**: O(n*s*t) for n reviews, s sentences per review, and t BERT computation time per sentence.
- **Best Practices**:
  - Preprocess reviews to clean text (e.g., remove emojis, normalize whitespace).
  - Tune `top_n` based on desired summary length.
  - Validate summaries against human judgments to ensure relevance.
  - Use GPU acceleration for BERT to handle large datasets.
- **Extensions**:
  - Fine-tune BERT on e-commerce reviews for domain-specific performance.
  - Incorporate sentence weighting based on sentiment or keywords.
  - Integrate with product page APIs to display summaries dynamically.
  - Explore lightweight models (e.g., DistilBERT) for faster inference.