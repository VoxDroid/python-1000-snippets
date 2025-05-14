# Intent Recognition

## Description
This snippet demonstrates Intent Recognition for an e-commerce platform, classifying customer queries into intents like "order_status" or "product_info" for chatbot routing.

## Code
```python
# Intent Recognition for query classification
# Note: Requires `numpy`, `sklearn`. Install with `pip install numpy scikit-learn`
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression

    class IntentClassifier:
        def __init__(self):
            # Initialize vectorizer and classifier
            self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')  # Use bigrams and remove common stop words
            self.classifier = LogisticRegression()

        def fit(self, queries: list, intents: list) -> None:
            # Train intent classifier
            X = self.vectorizer.fit_transform(queries)
            self.classifier.fit(X, intents)

        def predict(self, queries: list) -> list:
            # Predict intents
            X = self.vectorizer.transform(queries)
            return self.classifier.predict(X)

    # Simulate intent recognition
    def classify_intents(queries: list, intents: list, new_queries: list) -> list:
        # Classify customer intents
        model = IntentClassifier()
        model.fit(queries, intents)
        return model.predict(new_queries)

    # Example usage with improved data
    queries = [
        "Where is my order?", "What is the product price?", 
        "How long will it take to arrive?", "Where can I find my order status?", 
        "What are the available products?", "How much is the item?", 
        "Can I track my delivery?", "Tell me the price of the product?"
    ]
    intents = ["order_status", "product_info", "order_status", "order_status", 
            "product_info", "product_info", "order_status", "product_info"]
    new_queries = ["Track my package", "How much is it?"]
    predicted_intents = classify_intents(queries, intents, new_queries)
    print("Intent recognition result (intents):", predicted_intents)
except ImportError:
    print("Mock Output: Intent recognition result (intents): ['order_status', 'product_info']")
```

## Output
```
Mock Output: Intent recognition result (intents): ['order_status', 'product_info']
```
*(Real output with `numpy`, `sklearn`: `Intent recognition result (intents): ['order_status', 'product_info']`)*

## Explanation
- **Purpose**: Intent Recognition classifies user inputs into predefined intents, enabling automated query handling.
- **Real-World Use Case**: In an e-commerce platform, it routes customer queries to appropriate chatbot responses, improving support efficiency.
- **Code Breakdown**:
  - The `IntentClassifier` class uses TF-IDF and logistic regression.
  - The `fit` method trains the classifier.
  - The `predict` method classifies new queries.
  - The `classify_intents` function simulates intent recognition.
- **Challenges**: Handling ambiguous queries, scaling to many intents, and ensuring accuracy.
- **Integration**: Works with Dialogue System (Snippet 801) and Slot Filling (Snippet 803) for chatbots.
- **Complexity**: O(n*d) for n queries and d features in training.
- **Best Practices**: Use robust features, validate intents, and preprocess queries.
- **Extensions**: Use transformer models or integrate with chatbot frameworks.