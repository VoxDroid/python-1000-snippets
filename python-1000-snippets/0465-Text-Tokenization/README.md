# Text Tokenization

## Description
This snippet demonstrates basic text tokenization techniques using standard Python libraries.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Input: Hello, world! This is a test: tokenization.
Tokens: ['Hello', ',', 'world', '!', 'This', 'is', 'a', 'test', ':', 'tokenization', '.']
Token count: 11
```

## Explanation
- **Text Tokenization**: Splitting text into meaningful pieces (tokens) for NLP.
- **sample1.py**: Splits on whitespace and punctuation.
- **sample2.py**: Demonstrates a simplified subword tokenization strategy.
- **sample3.py**: Counts token frequencies using a basic tokenizer.
- **Best Practice**: Use a consistent tokenizer for training and inference, and normalize case/punctuation as needed.
