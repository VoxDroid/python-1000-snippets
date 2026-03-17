"""Simple TSP solver using branch-and-bound on a small graph."""

from typing import List


def tsp_branch_and_bound(dist: List[List[float]]) -> float:
    n = len(dist)
    best = float('inf')

    # Precompute a naive lower bound: min outgoing edge for each node
    min_edge = [min([dist[i][j] for j in range(n) if j != i]) for i in range(n)]

    def search(path: List[int], visited: List[bool], length: float):
        nonlocal best
        if length >= best:
            return
        if len(path) == n:
            # return to start
            total = length + dist[path[-1]][path[0]]
            best = min(best, total)
            return

        # Lower bound estimate: current length + sum of min edges for unvisited nodes
        estimate = length + sum(min_edge[i] for i in range(n) if not visited[i])
        if estimate >= best:
            return

        last = path[-1]
        for nxt in range(n):
            if visited[nxt]:
                continue
            visited[nxt] = True
            path.append(nxt)
            search(path, visited, length + dist[last][nxt])
            path.pop()
            visited[nxt] = False

    visited = [False] * n
    visited[0] = True
    search([0], visited, 0.0)
    return best


if __name__ == "__main__":
    # Symmetric distance matrix for 4 cities
    dist = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0],
    ]
    best = tsp_branch_and_bound(dist)
    print("Best TSP tour length:", best)
