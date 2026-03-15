# RNN Model

## Description
This snippet demonstrates a simple Recurrent Neural Network (RNN) implemented in pure NumPy.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — forward pass through a minimal RNN and prints the final hidden state.
- `sample2.py` — trains an RNN on a toy binary classification task using backpropagation through time.
- `sample3.py` — prints how the hidden state evolves over each timestep for two example sequences.

Run a sample with:

```bash
python python-1000-snippets/0255-RNN-Model/SAMPLES/sample2.py
```

## Output
Each sample prints informative diagnostics (hidden states, loss/accuracy, etc.) to demonstrate RNN behavior.

## Notes
- This is a teaching implementation; production RNNs typically use frameworks like TensorFlow or PyTorch for speed and stability.
- The training loop in `sample2.py` uses a basic gradient descent update (no batching/optimizer).
