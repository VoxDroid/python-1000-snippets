# 0271 - Word Embedding Cheatsheet

## Quick Commands
```bash
pip install gensim
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Quick Tips
- `Word2Vec(sentences, vector_size=..., window=..., min_count=...)` trains the model.
- `model.wv["word"]` retrieves a word vector.
- `model.wv.most_similar("word")` finds semantically similar words.
- Use `model.save(path)` and `Word2Vec.load(path)` to persist models.
