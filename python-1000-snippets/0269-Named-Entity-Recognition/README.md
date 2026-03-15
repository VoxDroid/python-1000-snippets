# Named Entity Recognition

## Description
This snippet demonstrates simple named entity recognition (NER) techniques without external NLP libraries.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — extracts dates, currency, and proper nouns using regex.
- `sample2.py` — finds email addresses and URLs using regex patterns.
- `sample3.py` — matches a small set of known entities from a dictionary.

Run a sample with:

```bash
python python-1000-snippets/0269-Named-Entity-Recognition/SAMPLES/sample1.py
```

## Output
Each sample prints extracted entities detected in the input text.

## Notes
- This snippet is intended as a lightweight demonstration; real NER uses libraries like spaCy or Hugging Face transformers.
- Regex-based methods are fast but brittle; they miss context and complex entity boundaries.
