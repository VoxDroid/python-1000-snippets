# GAN Implementation

## Description
This snippet demonstrates a toy Generative Adversarial Network (GAN) implemented using NumPy.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — basic generator/discriminator forward pass.
- `sample2.py` — trains a simple GAN on a 1D real distribution.
- `sample3.py` — trains a GAN and then compares the generated distribution to the target distribution.

Run a sample with:

```bash
python python-1000-snippets/0258-GAN-Implementation/SAMPLES/sample2.py
```

## Output
Each sample prints loss values and statistics to demonstrate how generator and discriminator behave over training.

## Notes
- This is an educational implementation; modern GANs use deep architectures and frameworks like PyTorch or TensorFlow.
- Here the generator and discriminator are simple linear models for clarity.
