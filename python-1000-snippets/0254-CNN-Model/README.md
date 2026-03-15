# CNN Model

## Description
This snippet demonstrates a small convolutional neural network (CNN) pipeline implemented using pure NumPy.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — perform a forward pass through a tiny CNN (conv + dense + softmax).
- `sample2.py` — train a simple conv+linear model with gradient descent on random data.
- `sample3.py` — apply multiple convolution filters and inspect feature map statistics.

Run any of them with:

```bash
python python-1000-snippets/0254-CNN-Model/SAMPLES/sample1.py
```

## Output
Each sample prints output tensors or loss values to demonstrate the CNN pipeline.

## Explanation
- **CNN model**: Uses convolution, ReLU activation, and a dense layer.
- **Logic**: Implements convolution operations manually and shows how filters produce feature maps.
- **Use Case**: Useful for learning CNN mechanics without requiring TensorFlow or PyTorch.
- **Best Practice**: Normalize inputs; choose appropriate learning rates; use vectorized operations for performance.
