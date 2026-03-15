# sample2.py
# Train a toy GAN using NumPy.

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def generator(z, Wg, bg):
    return z @ Wg + bg


def discriminator(x, Wd, bd):
    logits = x @ Wd + bd
    return sigmoid(logits), logits


if __name__ == '__main__':
    np.random.seed(0)

    # Data distribution: real data sampled from N(2, 0.5^2)
    N = 256
    noise_dim = 2

    Wg = np.random.randn(noise_dim, 1) * 0.5
    bg = np.zeros(1)
    Wd = np.random.randn(1, 1) * 0.5
    bd = np.zeros(1)

    lr = 1e-2
    epochs = 100

    for epoch in range(1, epochs + 1):
        # Real samples
        real = np.random.randn(N, 1) * 0.5 + 2.0
        real_labels = np.ones((N, 1))

        # Fake samples
        z = np.random.randn(N, noise_dim)
        fake = generator(z, Wg, bg)
        fake_labels = np.zeros((N, 1))

        # Discriminator forward
        d_real, logit_real = discriminator(real, Wd, bd)
        d_fake, logit_fake = discriminator(fake, Wd, bd)

        # Discriminator loss (binary cross entropy)
        d_loss = -np.mean(real_labels * np.log(d_real + 1e-8) + (1 - real_labels) * np.log(1 - d_real + 1e-8))
        d_loss += -np.mean(fake_labels * np.log(d_fake + 1e-8) + (1 - fake_labels) * np.log(1 - d_fake + 1e-8))

        # Discriminator gradients
        d_real_grad = (d_real - real_labels) / N
        d_fake_grad = (d_fake - fake_labels) / N
        dlogits = np.vstack([d_real_grad, d_fake_grad])
        x_concat = np.vstack([real, fake])

        dWd = x_concat.T @ dlogits
        dbd = np.sum(dlogits, axis=0)

        # Update discriminator
        Wd -= lr * dWd
        bd -= lr * dbd

        # Generator forward (use updated discriminator)
        z = np.random.randn(N, noise_dim)
        fake = generator(z, Wg, bg)
        d_fake, logit_fake = discriminator(fake, Wd, bd)

        # Generator loss (tries to fool discriminator)
        g_loss = -np.mean(np.log(d_fake + 1e-8))

        # Generator gradients
        # dL/dlogit = -(1 - D)
        dlogit_fake = -(1 - d_fake) / N
        # dlogit / dfake = D(1-D) but dlogit_fake already accounts for that using chain rule
        # Backprop through discriminator weights
        # dlogits/dx = Wd
        d_fake_dx = dlogit_fake @ Wd.T
        dWg = z.T @ d_fake_dx
        dbg = np.sum(d_fake_dx, axis=0)

        # Update generator
        Wg -= lr * dWg
        bg -= lr * dbg

        if epoch % 20 == 0 or epoch == 1:
            print(f"Epoch {epoch}, D loss={d_loss:.4f}, G loss={g_loss:.4f}")

    print("Finished training")
