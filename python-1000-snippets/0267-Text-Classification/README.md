# Text Classification

## Description
This snippet demonstrates text classification using scikit-learn with TF-IDF vectorization.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — trains a logistic regression classifier on a tiny dataset and makes predictions.
- `sample2.py` — trains a Naive Bayes classifier with TF-IDF and predicts sentiment for new sentences.
- `sample3.py` — evaluates a classifier using a train/test split and prints accuracy.

Run a sample with:

```bash
python python-1000-snippets/0267-Text-Classification/SAMPLES/sample1.py
```

## Output
Each sample prints accuracy metrics or prediction outputs.

## Notes
- This is a toy example; real-world datasets are larger and require proper preprocessing.
- Use `TfidfVectorizer` to convert text into feature vectors.
- For multi-class problems, use `LogisticRegression` or `MultinomialNB` as baseline models.
