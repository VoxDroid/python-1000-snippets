# Data Augmentation

## Description
This snippet demonstrates image data augmentation using `tensorflow`.

## Code
```python
# Note: Requires `tensorflow`. Install with `pip install tensorflow`
try:
    import tensorflow as tf
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=20, width_shift_range=0.2)
    print("Data augmentation configured")
except ImportError:
    print("Mock Output: Data augmentation configured")
```

## Output
```
Mock Output: Data augmentation configured
```
*(Real output with `tensorflow`: `Data augmentation configured`)*

## Explanation
- **Data Augmentation**: Applies transformations to image data.
- **Logic**: Configures an `ImageDataGenerator` for rotation and shifting.
- **Complexity**: O(1) for setup (augmentation-dependent).
- **Use Case**: Used to increase dataset size for image tasks.
- **Best Practice**: Balance augmentation; avoid unrealistic transforms; test impact.