# Transformer Model Cheatsheet

## Key Concepts
- **Scaled Dot-Product Attention**: `softmax((QK^T)/sqrt(d_k)) * V`.
- **Multi-Head Attention**: splits `d_model` into heads, attends separately, and concatenates results.
- **Pooled Output**: average across sequence length (often used for classification tasks).

## Running Samples
```bash
python python-1000-snippets/0257-Transformer-Model/SAMPLES/sample1.py
python python-1000-snippets/0257-Transformer-Model/SAMPLES/sample2.py
python python-1000-snippets/0257-Transformer-Model/SAMPLES/sample3.py
```

## Tips
- Ensure `d_model % num_heads == 0` when splitting into heads.
- Use scaled attention (`/ sqrt(d_k)`) to keep gradients stable.
- This implementation does not include positional encoding or residual connections.
