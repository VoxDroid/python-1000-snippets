# Text Generation

## Description
This snippet shows simple text generation techniques using Markov chains (bigram, trigram, character-level) without requiring heavy machine learning libraries.

## Dependencies
No external dependencies required (uses standard library).

## Samples
- `SAMPLES/sample1.py`: Bigram (word-level) Markov chain generator.
- `SAMPLES/sample2.py`: Trigram (word-level) Markov chain generator.
- `SAMPLES/sample3.py`: Character-level Markov chain generator.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- These models are stochastic; results vary per run.
- For larger corpora, consider using a real language model (e.g., GPT, LSTM).
