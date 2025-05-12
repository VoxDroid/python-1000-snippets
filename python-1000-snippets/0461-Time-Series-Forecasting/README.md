# Time Series Forecasting

## Description
This snippet demonstrates time series forecasting using `tensorflow`.

## Code
```python
# Note: Requires `tensorflow`. Install with `pip install tensorflow`
try:
    import tensorflow as tf
    import numpy as np
    data = np.array([1, 2, 3, 4, 5]).reshape(-1, 1, 1)
    model = tf.keras.Sequential([tf.keras.layers.LSTM(10), tf.keras.layers.Dense(1)])
    model.compile(optimizer='adam', loss='mse')
    model.fit(data, data, epochs=1, verbose=0)
    print("Forecast model trained")
except ImportError:
    print("Mock Output: Forecast model trained")
```

## Output
```
Mock Output: Forecast model trained
```
*(Real output with `tensorflow`: `Forecast model trained`)*

## Explanation
- **Time Series Forecasting**: Predicts future values using LSTM.
- **Logic**: Trains an LSTM on a simple sequence.
- **Complexity**: O(n * t) for n samples, t timesteps.
- **Use Case**: Used for stock prices or weather prediction.
- **Best Practice**: Use windowing; preprocess data; evaluate forecasts.