# CNN Model Cheatsheet

## Key Concepts
- Convolution: slide a kernel over input to compute feature maps.
- Activation: use ReLU (`max(0, x)`) to introduce non-linearity.
- Flatten + Dense: convert feature maps to 1D and apply a linear layer.
- Softmax: convert logits to probabilities.

## Running Samples
```bash
python python-1000-snippets/0254-CNN-Model/SAMPLES/sample1.py
python python-1000-snippets/0254-CNN-Model/SAMPLES/sample2.py
python python-1000-snippets/0254-CNN-Model/SAMPLES/sample3.py
```

## Useful Patterns
- Convolution (Numpy): use `np.tensordot` and `np.pad` to implement valid and same convolutions.
- Backprop basics: compute gradients manually for weights and inputs when using numpy.
- Keep learning rate small (e.g., 1e-2) to prevent loss explosions.

## Notes
- This is a toy implementation; real-world CNNs use frameworks like TensorFlow or PyTorch.
- Use `np.random.seed(0)` for reproducible behavior.
