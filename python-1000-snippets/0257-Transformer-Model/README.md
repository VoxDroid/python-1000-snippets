# Transformer Model

## Description
This snippet demonstrates a simplified Transformer-style attention mechanism implemented using NumPy.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — scaled dot-product attention example with random input data.
- `sample2.py` — a mini Transformer classification pipeline using multi-head attention and a linear output head.
- `sample3.py` — inspects how multi-head attention splits and combines head outputs.

Run a sample with:

```bash
python python-1000-snippets/0257-Transformer-Model/SAMPLES/sample2.py
```

## Output
Each sample prints shape information and metrics (loss/accuracy) to demonstrate attention computations.

## Notes
- This is an educational implementation; real Transformer models use optimized libraries (e.g., Hugging Face Transformers, TensorFlow, PyTorch).
- Multi-head attention here is implemented in NumPy for clarity and does not include positional encoding or residual layers.
