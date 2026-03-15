# sample3.py
# Compare generator output distribution to real data distribution after training.

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def generator(z, Wg, bg):
    return z @ Wg + bg


def discriminator(x, Wd, bd):
    logits = x @ Wd + bd
    return sigmoid(logits)


def train_gan(num_steps=200, batch_size=256, noise_dim=2, lr=1e-2):
    # Data distribution: real data sampled from N(2, 0.5^2)
    Wg = np.random.randn(noise_dim, 1) * 0.5
    bg = np.zeros(1)
    Wd = np.random.randn(1, 1) * 0.5
    bd = np.zeros(1)

    for step in range(1, num_steps + 1):
        real = np.random.randn(batch_size, 1) * 0.5 + 2.0
        real_labels = np.ones((batch_size, 1))

        z = np.random.randn(batch_size, noise_dim)
        fake = generator(z, Wg, bg)
        fake_labels = np.zeros((batch_size, 1))

        d_real, _ = discriminator(real, Wd, bd)
        d_fake, _ = discriminator(fake, Wd, bd)

        d_loss = -np.mean(real_labels * np.log(d_real + 1e-8) + (1 - real_labels) * np.log(1 - d_real + 1e-8))
        d_loss += -np.mean(fake_labels * np.log(d_fake + 1e-8) + (1 - fake_labels) * np.log(1 - d_fake + 1e-8))

        # Update discriminator (simple gradient step)
        d_real_grad = (d_real - real_labels) / batch_size
        d_fake_grad = (d_fake - fake_labels) / batch_size
        dlogits = np.vstack([d_real_grad, d_fake_grad])
        x_concat = np.vstack([real, fake])

        dWd = x_concat.T @ dlogits
        dbd = np.sum(dlogits, axis=0)
        Wd -= lr * dWd
        bd -= lr * dbd

        # Generator update
        z = np.random.randn(batch_size, noise_dim)
        fake = generator(z, Wg, bg)
        d_fake, _ = discriminator(fake, Wd, bd)
        g_loss = -np.mean(np.log(d_fake + 1e-8))

        dlogit_fake = -(1 - d_fake) / batch_size
        d_fake_dx = dlogit_fake @ Wd.T
        dWg = z.T @ d_fake_dx
        dbg = np.sum(d_fake_dx, axis=0)
        Wg -= lr * dWg
        bg -= lr * dbg

        if step % 50 == 0 or step == 1:
            print(f"Step {step}, D loss={d_loss:.4f}, G loss={g_loss:.4f}")

    return Wg, bg


if __name__ == '__main__':
    Wg, bg = train_gan()

    # Inspect generated sample distribution
    z = np.random.randn(1000, 2)
    gen = generator(z, Wg, bg)
    print("Generated mean, std:", float(gen.mean()), float(gen.std()))
    print("Target mean, std:", 2.0, 0.5)
