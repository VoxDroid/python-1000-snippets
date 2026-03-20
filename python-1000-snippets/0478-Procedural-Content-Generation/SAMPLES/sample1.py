# sample1.py
# Generate a dungeon-like map using cellular automata.

import numpy as np


def cellular_automata(seed_map: np.ndarray, iterations: int = 4) -> np.ndarray:
    grid = seed_map.copy()
    for _ in range(iterations):
        new_grid = grid.copy()
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                neighbors = np.sum(grid[max(0, y-1):y+2, max(0, x-1):x+2]) - grid[y, x]
                if neighbors > 4:
                    new_grid[y, x] = 1
                elif neighbors < 4:
                    new_grid[y, x] = 0
        grid = new_grid
    return grid


def main() -> None:
    rng = np.random.RandomState(0)
    grid = (rng.rand(40, 60) > 0.45).astype(int)

    dungeon = cellular_automata(grid, iterations=5)
    print("Dungeon map (1=wall,0=floor):")
    for row in dungeon[:10]:
        print("".join(["#" if v else "." for v in row[:40]]))


if __name__ == "__main__":
    main()
