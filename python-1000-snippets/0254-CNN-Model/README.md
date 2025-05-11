# CNN Model

## Description
This snippet demonstrates a simple Convolutional Neural Network (CNN) using `tensorflow` for digit classification.

## Code
```python
# Note: Requires `tensorflow`. Install with `pip install tensorflow`
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, Dense, Flatten
    from tensorflow.keras.datasets import mnist
    (X, y), _ = mnist.load_data()
    X = X[:100, :, :, None] / 255.0  # Subset for demo
    y = y[:100]
    model = Sequential([
        Conv2D(8, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        Flatten(),
        Dense(10, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
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
- **CNN Model**: Trains a CNN on a subset of MNIST digits.
- **Logic**: Uses a single convolutional layer and dense layer for classification.
- **Complexity**: O(n*k*f) for n samples, k kernels, f feature map size.
- **Use Case**: Used for image classification or object detection.
- **Best Practice**: Use data augmentation; add pooling layers; tune hyperparameters.