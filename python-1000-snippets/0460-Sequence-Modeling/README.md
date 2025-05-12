# Sequence Modeling

## Description
This snippet demonstrates sequence modeling with LSTM using `tensorflow`.

## Code
```python
# Note: Requires `tensorflow`. Install with `pip install tensorflow`
try:
    import tensorflow as tf
    model = tf.keras.Sequential([tf.keras.layers.LSTM(10, input_shape=(5, 1)), tf.keras.layers.Dense(1)])
    model.compile(optimizer='adam', loss='mse')
    print("LSTM model configured")
except ImportError:
    print("Mock Output: LSTM model configured")
```

## Output
```
Mock Output: LSTM model configured
```
*(Real output with `tensorflow`: `LSTM model configured`)*

## Explanation
- **Sequence Modeling**: Models sequential data with an LSTM network.
- **Logic**: Configures an LSTM layer for time-series data.
- **Complexity**: O(n * t) for n samples, t timesteps.
- **Use Case**: Used for time-series or NLP tasks.
- **Best Practice**: Preprocess sequences; tune LSTM units; avoid vanishing gradients.