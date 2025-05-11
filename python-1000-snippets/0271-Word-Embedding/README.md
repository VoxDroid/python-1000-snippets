# Word Embedding

## Description
This snippet demonstrates creating word embeddings using `gensim`’s Word2Vec.

## Code
```python
# Note: Requires `gensim`. Install with `pip install gensim`
try:
    from gensim.models import Word2Vec
    sentences = [["cat", "dog", "pet"], ["car", "bike", "vehicle"]]
    model = Word2Vec(sentences, vector_size=10, window=2, min_count=1)
    print("Vector for 'cat':", model.wv["cat"][:5])
except ImportError:
    print("Mock Output: Vector for 'cat': [0.1, -0.2, 0.3, -0.4, 0.5]")
```

## Output
```
Mock Output: Vector for 'cat': [0.1, -0.2, 0.3, -0.4, 0.5]
```
*(Real output with `gensim`: `Vector for 'cat': [<5 float values>]`)*

## Explanation
- **Word Embedding**: Trains a Word2Vec model to create vector representations of words.
- **Logic**: Uses a small corpus to train and retrieves the vector for "cat".
- **Complexity**: O(n*w*e) for n words, w window size, e epochs.
- **Use Case**: Used for NLP tasks like text classification or sentiment analysis.
- **Best Practice**: Use larger corpora; tune vector size; preprocess text.