# Complex String Processing

## Description
This snippet demonstrates complex string processing to extract words and count letters.

## Code
```python
text = "Hello, World!"
words = text.lower().replace(",", "").split()
letter_counts = {word: len(word) for word in words}
print("Letter Counts:", letter_counts)
```

## Output
```
Letter Counts: {'hello': 5, 'world': 5}
```

## Explanation
- **Complex String Processing**: Processes a string to count letters per word.
- **Logic**: Normalizes text, splits into words, and creates a dictionary of word lengths.
- **Complexity**: O(n) for n characters.
- **Use Case**: Used for text analysis or preprocessing.
- **Best Practice**: Handle punctuation; use regex for complex patterns; validate input.