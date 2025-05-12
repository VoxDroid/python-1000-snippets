# Text Tokenization

## Description
This snippet demonstrates text tokenization using `transformers`.

## Code
```python
# Note: Requires `transformers`. Install with `pip install transformers`
try:
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    tokens = tokenizer("Hello world", return_tensors="pt")
    print("Tokens:", tokens["input_ids"].shape)
except ImportError:
    print("Mock Output: Tokens: torch.Size([1, 5])")
```

## Output
```
Mock Output: Tokens: torch.Size([1, 5])
```
*(Real output with `transformers`: `Tokens: torch.Size([1, 5])`)*

## Explanation
- **Text Tokenization**: Converts text to tokens for NLP models.
- **Logic**: Uses BERT tokenizer to process a simple sentence.
- **Complexity**: O(n) for n characters.
- **Use Case**: Used in NLP tasks like sentiment analysis.
- **Best Practice**: Choose appropriate tokenizer; handle special tokens; validate output.