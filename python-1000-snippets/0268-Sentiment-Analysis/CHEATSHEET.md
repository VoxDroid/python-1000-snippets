# Sentiment Analysis Cheatsheet

## Key Concepts
- Rule-based sentiment uses keyword lists to assign scores.
- Machine learning models (TF-IDF + classifier) learn patterns from labeled data.
- Scores can be aggregated with simple heuristics (positive - negative count).

## Running Samples
```bash
python python-1000-snippets/0268-Sentiment-Analysis/SAMPLES/sample1.py
python python-1000-snippets/0268-Sentiment-Analysis/SAMPLES/sample2.py
python python-1000-snippets/0268-Sentiment-Analysis/SAMPLES/sample3.py
```

## Tips
- Expand your lexicon for better coverage in rule-based methods.
- Clean text (lowercase, remove punctuation) before vectorization.
- For production, consider pretrained transformer models (e.g., HuggingFace Transformers).
