# 0465-Text-Tokenization Cheatsheet

## Quick Tips
- Tokenization is the first step in most NLP pipelines; consistent tokenization ensures consistent model input.
- Decide whether you need word-level, character-level, or subword-level tokens based on your task and vocabulary size.
- Always normalize casing and punctuation if your model expects it.

## Running examples
- `python SAMPLES/sample1.py` — whitespace + punctuation tokenization.
- `python SAMPLES/sample2.py` — simplified subword (WordPiece-like) tokenization.
- `python SAMPLES/sample3.py` — token frequency counting.
