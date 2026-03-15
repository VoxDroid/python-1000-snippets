# Topic Modeling Cheatsheet

## Key Concepts
- Topic modeling discovers latent themes (topics) in a corpus.
- LDA treats each document as a mixture of topics and each topic as a distribution over words.
- The `components_` matrix in scikit-learn's LDA contains topic-word weights.

## Running Samples
```bash
python python-1000-snippets/0270-Topic-Modeling/SAMPLES/sample1.py
python python-1000-snippets/0270-Topic-Modeling/SAMPLES/sample2.py
python python-1000-snippets/0270-Topic-Modeling/SAMPLES/sample3.py
```

## Tips
- Use `CountVectorizer` or `TfidfVectorizer` to prepare input data.
- Choose `n_components` to match the number of topics you want to discover.
- Inspect the top words per topic to interpret what each topic represents.
