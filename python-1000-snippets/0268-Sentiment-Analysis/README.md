# Sentiment Analysis

## Description
This snippet demonstrates sentiment analysis using lightweight methods without external NLP libraries.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — rule-based sentiment scoring using keyword dictionaries.
- `sample2.py` — trains a sentiment classifier using TF-IDF and logistic regression.
- `sample3.py` — scores sentiment using a simple lexicon-based function.

Run a sample with:

```bash
python python-1000-snippets/0268-Sentiment-Analysis/SAMPLES/sample1.py
```

## Output
Each sample prints sentiment labels or scores for example sentences.

## Notes
- The rule-based approach is quick but limited; it misses context and negation.
- A learned classifier (sample2) can generalize better but requires labeled data.
- Real sentiment analysis often uses pre-trained models (e.g., transformers) for best results.
