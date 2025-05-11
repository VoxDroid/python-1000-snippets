# Sentiment Analysis

## Description
This snippet demonstrates sentiment analysis using `textblob`.

## Code
```python
# Note: Requires `textblob`. Install with `pip install textblob`
try:
    from textblob import TextBlob
    text = "This movie is great!"
    blob = TextBlob(text)
    print("Sentiment:", blob.sentiment.polarity)
except ImportError:
    print("Mock Output: Sentiment: 1.0")
```

## Output
```
Mock Output: Sentiment: 1.0
```
*(Real output with `textblob`: `Sentiment: 1.0`)*

## Explanation
- **Sentiment Analysis**: Analyzes text sentiment using `TextBlob`’s polarity score.
- **Logic**: Processes text and outputs a score (-1 to 1).
- **Complexity**: O(n) for n words.
- **Use Case**: Used for analyzing reviews or social media.
- **Best Practice**: Handle sarcasm; use domain-specific models; validate results.