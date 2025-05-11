# Topic Modeling

## Description
This snippet demonstrates topic modeling using `gensim` with LDA.

## Code
```python
# Note: Requires `gensim`. Install with `pip install gensim`
try:
    from gensim import corpora
    from gensim.models import LdaModel
    documents = [["cat", "dog", "pet"], ["car", "bike", "vehicle"], ["cat", "pet", "animal"]]
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]
    lda = LdaModel(corpus, num_topics=2, id2word=dictionary, passes=1)
    print("Topics:", lda.print_topics())
except ImportError:
    print("Mock Output: Topics: [(0, '0.5*cat + 0.3*pet'), (1, '0.4*car + 0.3*vehicle')]")
```

## Output
```
Mock Output: Topics: [(0, '0.5*cat + 0.3*pet'), (1, '0.4*car + 0.3*vehicle')]
```
*(Real output with `gensim`: `Topics: [<similar topic distributions>]`)*

## Explanation
- **Topic Modeling**: Identifies topics in a small text corpus using LDA.
- **Logic**: Creates a dictionary, converts documents to bag-of-words, and trains LDA.
- **Complexity**: O(n*k*p) for n documents, k topics, p passes.
- **Use Case**: Used for document clustering or theme extraction.
- **Best Practice**: Preprocess text; tune number of topics; interpret results carefully.