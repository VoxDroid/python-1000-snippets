# sample3.py
# Simple enemy chase behavior in a grid world.

import math


def next_move(enemy, player):
    # Move one step toward the player using Manhattan distance.
    ex, ey = enemy
    px, py = player
    dx = 1 if px > ex else -1 if px < ex else 0
    dy = 1 if py > ey else -1 if py < ey else 0
    return (ex + dx, ey + dy)


def main() -> None:
    player = (7, 7)
    enemy = (0, 0)
    path = [enemy]

    for _ in range(20):
        if enemy == player:
            break
        enemy = next_move(enemy, player)
        path.append(enemy)

    print("Enemy path length:", len(path))
    print("Path snippet:", path[:5], "...")
    print("Reached player:", enemy == player)


if __name__ == "__main__":
    main()
