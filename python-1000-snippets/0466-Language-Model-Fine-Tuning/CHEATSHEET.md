# 0466-Language-Model-Fine-Tuning Cheatsheet

## Quick Tips
- Fine-tuning in this context is simulated by updating n-gram counts with new text.
- For real language models, fine-tuning adjusts model weights on task-specific data.
- Use smoothing (e.g., add-one/Laplace) to avoid zero probabilities for unseen n-grams.

## Running examples
- `python SAMPLES/sample1.py` — build a bigram model.
- `python SAMPLES/sample2.py` — update (fine-tune) the bigram model counts.
- `python SAMPLES/sample3.py` — generate text using bigram sampling.
