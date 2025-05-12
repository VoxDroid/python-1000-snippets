# Transfer Learning

## Description
This snippet demonstrates transfer learning using `tensorflow` with a pre-trained model.

## Code
```python
# Note: Requires `tensorflow`. Install with `pip install tensorflow`
try:
    import tensorflow as tf
    base_model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    model = tf.keras.Sequential([base_model, tf.keras.layers.GlobalAveragePooling2D(), tf.keras.layers.Dense(1)])
    model.compile(optimizer='adam', loss='binary_crossentropy')
    print("Transfer learning model configured")
except ImportError:
    print("Mock Output: Transfer learning model configured")
```

## Output
```
Mock Output: Transfer learning model configured
```
*(Real output with `tensorflow`: `Transfer learning model configured`)*

## Explanation
- **Transfer Learning**: Uses a pre-trained MobileNetV2 for a new task.
- **Logic**: Freezes base model and adds custom layers.
- **Complexity**: O(1) for model setup (training-dependent).
- **Use Case**: Used for image classification with limited data.
- **Best Practice**: Fine-tune layers; preprocess inputs; validate performance.