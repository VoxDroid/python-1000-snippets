# LSTM Model Cheatsheet

## Key Concepts
- **Gates**: Input (i), forget (f), and output (o) gates control information flow.
- **Cell state**: `c_t = f_t * c_{t-1} + i_t * g_t` retains long-term information.
- **Hidden state**: `h_t = o_t * tanh(c_t)` is the output at each step.

## Running Samples
```bash
python python-1000-snippets/0256-LSTM-Model/SAMPLES/sample1.py
python python-1000-snippets/0256-LSTM-Model/SAMPLES/sample2.py
python python-1000-snippets/0256-LSTM-Model/SAMPLES/sample3.py
```

## Tips
- Use small weights (e.g., multiply by 0.2) to prevent saturation of sigmoid/tanh.
- Inspect gate values to understand how the LSTM uses input vs. memory.
- In real models, use built-in LSTM layers from frameworks to avoid manual implementation bugs.
