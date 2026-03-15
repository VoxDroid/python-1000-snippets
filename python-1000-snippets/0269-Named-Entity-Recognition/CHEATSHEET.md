# Named Entity Recognition Cheatsheet

## Key Concepts
- NER identifies entities such as people, locations, dates, and organizations in text.
- Regex-based NER can detect patterns like dates, emails, and URLs quickly.
- Dictionary-based matching can find known entities but cannot generalize to new names.

## Running Samples
```bash
python python-1000-snippets/0269-Named-Entity-Recognition/SAMPLES/sample1.py
python python-1000-snippets/0269-Named-Entity-Recognition/SAMPLES/sample2.py
python python-1000-snippets/0269-Named-Entity-Recognition/SAMPLES/sample3.py
```

## Tips
- For production NER, use NLP libraries like spaCy or transformers.
- When using regex, be aware of false positives and overlapping matches.
- Expanding your entity dictionary improves recall but may increase false positives.
