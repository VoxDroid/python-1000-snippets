# Language Model Fine-Tuning

## Description
This snippet demonstrates a simple n-gram language model and how it can be "fine-tuned" by updating counts with new text.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Total tokens: 15
Total bigrams: 11
Samples from bigram model:
  ('the', 'quick'): 2
  ('quick', 'brown'): 2
  ('brown', 'fox'): 2
  ('fox', 'jumps'): 1
  ('jumps', 'over'): 1
```

## Explanation
- **Language Model Fine-Tuning**: Updating a language model with new data to better fit a target domain.
- **sample1.py**: Builds a simple bigram model from a small corpus.
- **sample2.py**: Shows how new text updates the bigram count distribution.
- **sample3.py**: Generates text by sampling from a bigram model.
- **Best Practice**: Use smoothing and larger corpora for reliable probabilities, and validate generated text for coherence.
