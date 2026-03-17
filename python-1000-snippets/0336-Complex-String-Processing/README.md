# Complex String Processing

## Description
This snippet demonstrates real-world string processing tasks such as tokenization, normalization, pattern extraction, and frequency analysis.

## Files
- `SAMPLES/sample1.py`: Normalize text and compute word frequency.
- `SAMPLES/sample2.py`: Extract emails and URLs from a block of text using regex.
- `SAMPLES/sample3.py`: Clean text by removing punctuation, normalizing whitespace, and lowercasing.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Word frequencies: {'hello': 2, 'world': 1}
Emails: ['user@example.com']
URLs: ['https://example.com']
Cleaned: hello world this is a test
```

## Explanation
- **Tokenization**: Split text into words while handling punctuation.
- **Normalization**: Lowercasing, accent removal, collapsing whitespace.
- **Pattern extraction**: Use regular expressions to find structured data like emails and URLs.
- **Best practice**: Use `re` with appropriate flags; avoid naive splitting for complex text.
