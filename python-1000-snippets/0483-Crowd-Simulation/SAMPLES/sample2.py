# sample2.py
# Track crowd density per grid cell over time.


def generate_agents(count=50, size=20):
    import random
    return [[random.randint(0, size-1), random.randint(0, size-1)] for _ in range(count)]


def density_grid(agents, size=20):
    grid = [[0] * size for _ in range(size)]
    for x, y in agents:
        grid[y][x] += 1
    return grid


def main() -> None:
    agents = generate_agents()
    grid = density_grid(agents)
    print('Density at origin:', grid[0][0])
    print('Total agents:', sum(sum(row) for row in grid))


if __name__ == '__main__':
    main()
