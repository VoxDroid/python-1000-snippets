# LSTM Model

## Description
This snippet demonstrates a simple Long Short-Term Memory (LSTM) network implemented using plain NumPy.

## Code
The `SAMPLES/` folder contains:

- `sample1.py` — a single-pass LSTM forward computation showing hidden and cell state updates.
- `sample2.py` — trains a simple classifier using an LSTM feature extractor and a linear output layer.
- `sample3.py` — prints gate activations (input/forget/output) and cell state across timesteps.

Run any sample with:

```bash
python python-1000-snippets/0256-LSTM-Model/SAMPLES/sample2.py
```

## Output
Each sample prints the internal LSTM state and/or training progress to help illustrate how LSTM gates work.

## Notes
- This is a teaching implementation; production LSTMs use optimized libraries like TensorFlow or PyTorch.
- The training example only updates the final output layer for simplicity.
