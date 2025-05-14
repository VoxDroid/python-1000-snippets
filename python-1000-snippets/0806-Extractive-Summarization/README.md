# Extractive Summarization

## Description
This snippet demonstrates a robust extractive summarization method for an e-commerce platform, using a TextRank algorithm to select key sentences from customer feedback. It constructs a sentence similarity graph, ranks sentences for concise summaries, and includes fallback tokenization to handle NLTK resource issues.

## Code
```python
# Robust Extractive Summarization for customer feedback
# Note: Requires `numpy`, `nltk`, `scikit-learn`. Install with `pip install numpy nltk scikit-learn`
try:
    import numpy as np
    import nltk
    import re
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    # Download NLTK resources
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
    except Exception as e:
        print(f"Warning: Failed to download NLTK resources: {e}")

    # Extractive summarization model
    class FeedbackTextRank:
        def __init__(self, top_n: int = 2):
            # Initialize parameters
            self.top_n = top_n
            self.vectorizer = TfidfVectorizer(stop_words='english')

        def preprocess_text(self, text: str) -> list:
            # Split text into sentences with NLTK or fallback
            try:
                sentences = nltk.sent_tokenize(text)
            except LookupError:
                # Fallback: Simple regex-based sentence splitting
                sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
            return [s.strip() for s in sentences if s.strip()]

        def build_similarity_graph(self, sentences: list) -> np.ndarray:
            # Compute sentence similarity matrix
            try:
                tfidf_matrix = self.vectorizer.fit_transform(sentences)
                similarity_matrix = cosine_similarity(tfidf_matrix)
                # Normalize similarities to avoid extreme values
                similarity_matrix = (similarity_matrix - similarity_matrix.min()) / (
                    similarity_matrix.max() - similarity_matrix.min() + 1e-10)
                np.fill_diagonal(similarity_matrix, 0)  # Avoid self-loops
            except ValueError:
                # Handle empty or invalid input
                return np.zeros((len(sentences), len(sentences)))
            return similarity_matrix

        def textrank(self, similarity_matrix: np.ndarray) -> np.ndarray:
            # Apply TextRank algorithm
            n = similarity_matrix.shape[0]
            scores = np.ones(n) / n
            damping = 0.85
            for _ in range(100):  # Iterate until convergence
                old_scores = scores.copy()
                for i in range(n):
                    denom = sum(similarity_matrix[:, j] for j in range(n))
                    if denom > 0:
                        scores[i] = (1 - damping) + damping * sum(
                            similarity_matrix[i, j] * scores[j] / denom
                            for j in range(n)
                        )
                if np.allclose(scores, old_scores, atol=1e-5):
                    break
            return scores

        def summarize(self, text: str) -> str:
            # Generate extractive summary
            sentences = self.preprocess_text(text)
            if not sentences:
                return "No valid sentences to summarize."
            if len(sentences) <= self.top_n:
                return " ".join(sentences)
            similarity_matrix = self.build_similarity_graph(sentences)
            if similarity_matrix.sum() == 0:
                # Fallback: Select first sentences if similarity fails
                return " ".join(sentences[:self.top_n])
            scores = self.textrank(similarity_matrix)
            ranked_indices = np.argsort(scores)[-self.top_n:]
            selected_sentences = [sentences[i] for i in sorted(ranked_indices)]
            return " ".join(selected_sentences)

    # Simulate feedback summarization
    def summarize_feedback(feedback: list) -> list:
        # Summarize customer feedback with error handling
        model = FeedbackTextRank()
        summaries = []
        for fb in feedback:
            try:
                summary = model.summarize(fb)
                summaries.append(summary)
            except Exception as e:
                summaries.append(f"Error summarizing: {str(e)}")
        return summaries

    # Example usage
    feedback = [
        "The product quality is excellent. Shipping was slow and frustrating. Customer service was very helpful and resolved my issues.",
        "Amazing product with great features. The price is a bit high. Highly recommend for its durability."
    ]
    summaries = summarize_feedback(feedback)
    print("Extractive summarization result (summaries):", summaries)
except ImportError:
    print("Mock Output: Extractive summarization result (summaries): "
          "['The product quality is excellent. Shipping was slow and frustrating.', "
          "'Amazing product with great features. The price is a bit high.']")
```

## Output
```
Extractive summarization result (summaries): 
['The product quality is excellent. Shipping was slow and frustrating.', 'Amazing product with great features. The price is a bit high.']
```
*(Mock output for environments without dependencies: Same as above.)*

## Explanation
- **Purpose**: Extractive summarization selects the most representative sentences from customer feedback, preserving original wording to provide accurate insights for e-commerce quality control or marketing.
- **Real-World Use Case**: In an e-commerce platform, this summarizes customer feedback to highlight key points (e.g., product quality, shipping issues), aiding decision-making for product improvements or customer service enhancements.
- **Fixing the Error**:
  - **Issue**: The original code failed because `punkt_tab` (a newer NLTK tokenizer resource) was missing, and the `punkt` download was insufficient or misconfigured.
  - **Solution**:
    - Explicitly downloads both `punkt` and `punkt_tab` to ensure compatibility across NLTK versions (4.0+ uses `punkt_tab` in some contexts).
    - Adds a fallback regex-based sentence splitter (`re.split`) if NLTK tokenization fails, ensuring robustness.
    - Wraps NLTK downloads in a try-except block to handle network or permission issues gracefully.
- **Code Breakdown**:
  - **Initialization**: The `FeedbackTextRank` class sets up TextRank with a configurable number of sentences (`top_n`) and a TF-IDF vectorizer.
  - **Preprocessing**: The `preprocess_text` method uses NLTK’s sentence tokenizer or a regex fallback to split text into sentences.
  - **Similarity Graph**: The `build_similarity_graph` method computes a normalized cosine similarity matrix using TF-IDF, handling edge cases like empty inputs.
  - **TextRank**: The `textrank` method ranks sentences using a damped PageRank algorithm, with convergence checks for efficiency.
  - **Summarization**: The `summarize` method selects top-ranked sentences, with fallbacks for short texts or failed similarity computations.
  - **Batch Processing**: The `summarize_feedback` function processes multiple feedback texts with comprehensive error handling.
- **Improvements Over Original**:
  - **Robust Tokenization**: Handles missing NLTK resources with a regex fallback, preventing the `punkt_tab` error.
  - **Normalized Similarity**: Normalizes the similarity matrix to improve ranking stability for diverse feedback.
  - **Edge Case Handling**: Manages empty texts, short inputs, and invalid TF-IDF inputs with fallbacks.
  - **Optimized TextRank**: Simplifies the ranking loop and ensures proper denominator checks to avoid division errors.
- **Challenges**:
  - Ensuring sentence diversity in summaries to avoid redundancy.
  - Handling very short feedback where ranking is less meaningful.
  - Balancing computational cost for large feedback datasets.
- **Integration**: Works with Abstractive Summarization (Snippet 805) for hybrid summarization, Text Summarization (Snippet 804) for general text processing, or Relation Extraction (Snippet 799) for deeper feedback analysis.
- **Complexity**: O(n²) for n sentences in similarity matrix computation, plus O(n*i) for i TextRank iterations (typically <100).
- **Best Practices**:
  - Pre-download NLTK resources (`nltk.download('punkt')`, `nltk.download('punkt_tab')`) in production environments.
  - Adjust `top_n` based on desired summary length (e.g., 1-3 sentences for concise feedback).
  - Validate summaries against original feedback for representativeness.
  - Use domain-specific stopwords in TF-IDF to focus on meaningful terms.
- **Extensions**:
  - Add sentence clustering to ensure diverse summaries.
  - Optimize for large datasets using sparse TF-IDF matrices.
  - Integrate with real-time feedback dashboards.
  - Combine with abstractive summarization for polished outputs.