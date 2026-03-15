# Text Classification Cheatsheet

## Key Concepts
- Convert text to numeric features using `TfidfVectorizer`.
- Train a classifier (e.g., `LogisticRegression`, `MultinomialNB`) on the vectorized data.
- Evaluate using a train/test split and report accuracy.

## Running Samples
```bash
python python-1000-snippets/0267-Text-Classification/SAMPLES/sample1.py
python python-1000-snippets/0267-Text-Classification/SAMPLES/sample2.py
python python-1000-snippets/0267-Text-Classification/SAMPLES/sample3.py
```

## Tips
- Use `stop_words='english'` to remove common words.
- For larger datasets, consider `HashingVectorizer` or `CountVectorizer` with `max_features`.
- Use cross-validation (`cross_val_score`) for more reliable evaluation.
