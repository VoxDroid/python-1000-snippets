# RNN Model

## Description
This snippet demonstrates a simple Recurrent Neural Network (RNN) using `tensorflow` for sequence classification.

## Code
```python
# Note: Requires `tensorflow`. Install with `pip install tensorflow`
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import SimpleRNN, Dense
    import numpy as np
    X = np.random.random((100, 10, 1))  # 100 sequences, 10 timesteps
    y = (X.mean(axis=1) > 0.5).astype(int).flatten()
    model = Sequential([
        SimpleRNN(8, input_shape=(10, 1)),
        Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(X, y, epochs=1, verbose=0)
    print("Accuracy:", model.evaluate(X, y, verbose=0)[1])
except ImportError:
    print("Mock Output: Accuracy: 0.45")
```

## Output
```
Mock Output: Accuracy: 0.45
```
*(Real output with `tensorflow`: `Accuracy: <value around 0.45 ~ 0.99>`)*

## Explanation
- **RNN Model**: Trains an RNN on synthetic sequence data for binary classification.
- **Logic**: Uses a simple RNN layer to process sequences and a dense layer for output.
- **Complexity**: O(n*t*h) for n samples, t timesteps, h hidden units.
- **Use Case**: Used for time-series or sequence modeling.
- **Best Practice**: Use LSTM/GRU for long sequences; prevent vanishing gradients; tune units.