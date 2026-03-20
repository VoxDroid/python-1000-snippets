# sample3.py
# Compute a simple dense optical flow using image gradients (Lucas-Kanade approximation).

import numpy as np


def opt_flow_lk(img1: np.ndarray, img2: np.ndarray, window: int = 5):
    gx = np.gradient(img1, axis=1)
    gy = np.gradient(img1, axis=0)
    gt = img2 - img1

    flow = np.zeros(img1.shape + (2,))
    half = window // 2

    for i in range(half, img1.shape[0] - half):
        for j in range(half, img1.shape[1] - half):
            Ix = gx[i - half:i + half + 1, j - half:j + half + 1].ravel()
            Iy = gy[i - half:i + half + 1, j - half:j + half + 1].ravel()
            It = gt[i - half:i + half + 1, j - half:j + half + 1].ravel()

            A = np.vstack([Ix, Iy]).T
            b = -It
            # Solve for least squares flow vector
            nu, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            flow[i, j] = nu

    return flow


def main() -> None:
    # Shift an image slightly and compute optical flow.
    base = np.zeros((50, 50))
    rr, cc = np.ogrid[:50, :50]
    base[(rr - 25)**2 + (cc - 25)**2 < 100] = 1.0

    img2 = np.roll(np.roll(base, 1, axis=0), 1, axis=1)
    flow = opt_flow_lk(base, img2, window=9)

    # sample central flow vectors
    sample = flow[23:27, 23:27]
    print("Sample flow vectors (center 4x4):")
    for row in sample:
        print([tuple(np.round(v, 2)) for v in row])


if __name__ == "__main__":
    main()
