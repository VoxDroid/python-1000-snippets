# sample2.py
# Generate a maze using randomized Prim's algorithm.

import random


def generate_maze(width: int, height: int):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    start = (1, 1)
    maze[start[1]][start[0]] = 0
    walls = []
    for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
        nx, ny = start[0] + dx, start[1] + dy
        if 1 <= nx < width - 1 and 1 <= ny < height - 1:
            walls.append((nx, ny, start))

    while walls:
        idx = random.randrange(len(walls))
        x, y, prev = walls.pop(idx)
        if maze[y][x] == 1:
            px, py = prev
            maze[y][x] = 0
            maze[(y+py)//2][(x+px)//2] = 0
            for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                nx, ny = x + dx, y + dy
                if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == 1:
                    walls.append((nx, ny, (x, y)))
    return maze


def main() -> None:
    maze = generate_maze(21, 21)
    print("Maze (1=wall,0=passage):")
    for row in maze:
        print("".join(["#" if c else " " for c in row]))


if __name__ == "__main__":
    main()
