# Text Generation

## Description
This snippet demonstrates simple text generation using `tensorflow`’s LSTM model.

## Code
```python
# Note: Requires `tensorflow`. Install with `pip install tensorflow`
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense
    import numpy as np
    data = "hello"
    chars = list(set(data))
    char_to_idx = {c: i for i, c in enumerate(chars)}
    X = np.array([[char_to_idx[data[i]] for i in range(len(data)-1)]])
    y = np.array([char_to_idx[data[1]]])
    model = Sequential([LSTM(8, input_shape=(None, 1)), Dense(len(chars), activation="softmax")])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")
    model.fit(X.reshape(1, -1, 1), y, epochs=1, verbose=0)
    print("Model trained")
except ImportError:
    print("Mock Output: Model trained")
```

## Output
```
Mock Output: Model trained
```
*(Real output with `tensorflow`: `Model trained`)*

## Explanation
- **Text Generation**: Trains a minimal LSTM to predict the next character in a sequence.
- **Logic**: Uses a small string to train a character-level model.
- **Complexity**: O(n*t*h) for n samples, t timesteps, h hidden units.
- **Use Case**: Used for generating text like chatbots or stories.
- **Best Practice**: Use larger datasets; add temperature sampling; tune model size.