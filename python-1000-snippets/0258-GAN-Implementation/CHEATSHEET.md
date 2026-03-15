# GAN Implementation Cheatsheet

## Key Concepts
- **Generator**: maps random noise to synthetic samples.
- **Discriminator**: predicts whether input is real or fake.
- **Adversarial training**: generator tries to fool discriminator; discriminator tries to distinguish real vs fake.

## Running Samples
```bash
python python-1000-snippets/0258-GAN-Implementation/SAMPLES/sample1.py
python python-1000-snippets/0258-GAN-Implementation/SAMPLES/sample2.py
python python-1000-snippets/0258-GAN-Implementation/SAMPLES/sample3.py
```

## Notes
- A very small learning rate and simple models help keep training stable in this implementation.
- For real-world GANs, use deeper networks and frameworks like PyTorch/TensorFlow.
