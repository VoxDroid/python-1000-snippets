# RNN Model Cheatsheet

## Key Concepts
- **RNN Cell**: updates hidden state using current input and previous hidden state: `h_t = tanh(x_t W_x + h_{t-1} W_h + b)`.
- **Backprop Through Time (BPTT)**: propagate gradients backward through timesteps to update weights.
- **Binary classification**: can use a sigmoid on the final hidden state to produce a probability.

## Running Samples
```bash
python python-1000-snippets/0255-RNN-Model/SAMPLES/sample1.py
python python-1000-snippets/0255-RNN-Model/SAMPLES/sample2.py
python python-1000-snippets/0255-RNN-Model/SAMPLES/sample3.py
```

## Tips
- Initialize weights small to stabilize training.
- For longer sequences, gradients can vanish; use LSTM/GRU in practice.
- Keep learning rate moderate (e.g., 0.1) and monitor loss for divergence.
