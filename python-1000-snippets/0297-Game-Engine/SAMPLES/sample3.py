# sample3.py
# Basic 2D tile map and player movement logic (non-interactive simulation).

import random


def create_map(width, height):
    # 0=empty, 1=wall
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        grid[y][0] = 1
        grid[y][width - 1] = 1
    for x in range(width):
        grid[0][x] = 1
        grid[height - 1][x] = 1
    # Random interior walls
    for _ in range(int(width * height * 0.1)):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        grid[y][x] = 1
    return grid


def print_map(grid, player_pos):
    out = []
    for y, row in enumerate(grid):
        line = ''
        for x, cell in enumerate(row):
            if (x, y) == player_pos:
                line += 'P'
            elif cell == 1:
                line += '#'
            else:
                line += '.'
        out.append(line)
    print('\n'.join(out))


if __name__ == '__main__':
    width, height = 12, 8
    grid = create_map(width, height)
    player = (1, 1)

    moves = [(1, 0), (1, 0), (0, 1), (0, 1), (-1, 0), (-1, 0), (0, -1)]

    print('Initial map:')
    print_map(grid, player)

    for step, move in enumerate(moves, start=1):
        new_pos = (player[0] + move[0], player[1] + move[1])
        if grid[new_pos[1]][new_pos[0]] == 0:
            player = new_pos
        print(f'\nAfter move {step} {move}:')
        print_map(grid, player)
