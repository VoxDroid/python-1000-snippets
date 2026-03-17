# 0336-Complex-String-Processing Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Word frequency / normalization
python SAMPLES/sample2.py  # Extract emails and URLs with regex
python SAMPLES/sample3.py  # Normalize and clean text
```

## Tips
- Use `re` for robust pattern matching (emails, URLs, dates).
- Use `.strip()`, `.lower()`, and `.replace()` to normalize text.
- Use `unicodedata.normalize("NFKD", text)` + `.encode('ascii', 'ignore')` to remove accents.
- Use `collections.Counter` to count tokens.

## Common patterns
- Tokenize words: `re.findall(r"\w+", text.lower())`
- Remove punctuation: `re.sub(r"[^\w\s]", "", text)`
- Extract emails: `re.findall(r"[\w.%-]+@[\w.-]+\.[A-Za-z]{2,6}", text)`
- Extract URLs: `re.findall(r"https?://\S+", text)`
