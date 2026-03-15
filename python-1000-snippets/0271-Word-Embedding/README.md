# Word Embedding

## Description
This snippet demonstrates training a small Word2Vec model using `gensim` and querying word vectors.

## Dependencies
- `gensim`

Install with:
```bash
pip install gensim
```

## Samples
- `SAMPLES/sample1.py`: Train Word2Vec and print the vector for a word.
- `SAMPLES/sample2.py`: Find the most similar words to a target word.
- `SAMPLES/sample3.py`: Compute cosine similarity between word vectors.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Word2Vec learns vector representations of words from context.
- Use larger corpora for better vectors.
