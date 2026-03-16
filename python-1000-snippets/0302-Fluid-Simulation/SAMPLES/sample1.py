# sample1.py
# Diffusion simulation: update a scalar density grid using a simple diffusion kernel.

import numpy as np


def diffuse(grid, diffusion_rate=0.1):
    # Use a simple 5-point stencil for diffusion (explicit)
    out = grid.copy()
    rows, cols = grid.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            out[i, j] = grid[i, j] + diffusion_rate * (
                grid[i - 1, j]
                + grid[i + 1, j]
                + grid[i, j - 1]
                + grid[i, j + 1]
                - 4 * grid[i, j]
            )
    return out


if __name__ == '__main__':
    # Initialize a density grid with a hot spot at the center
    grid = np.zeros((20, 20), dtype=float)
    grid[10, 10] = 1.0

    print('Initial center value:', grid[10, 10])
    for step in range(1, 6):
        grid = diffuse(grid, diffusion_rate=0.2)
        print(f'Step {step} center value: {grid[10, 10]:.4f}')

    print('Final grid slice:
', np.round(grid[8:13, 8:13], 4))
