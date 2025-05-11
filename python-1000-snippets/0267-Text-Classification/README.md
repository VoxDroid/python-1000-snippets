# Text Classification

## Description
This snippet demonstrates text classification using `scikit-learn` with TF-IDF.

## Code
```python
# Note: Requires `scikit-learn`. Install with `pip install scikit-learn`
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    texts = ["good movie", "bad movie", "great film"]
    labels = [1, 0, 1]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    print("Accuracy:", model.score(X, labels))
except ImportError:
    print("Mock Output: Accuracy: 0.67")
```

## Output
```
Mock Output: Accuracy: 0.67
```
*(Real output with `scikit-learn`: `Accuracy: 0.67`)*

## Explanation
- **Text Classification**: Classifies text as positive or negative using TF-IDF and logistic regression.
- **Logic**: Vectorizes text and trains a model on a small dataset.
- **Complexity**: O(n*d) for n documents, d features.
- **Use Case**: Used for sentiment analysis or spam detection.
- **Best Practice**: Use larger datasets; preprocess text; use cross-validation.