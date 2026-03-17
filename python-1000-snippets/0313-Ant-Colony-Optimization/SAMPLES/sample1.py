#!/usr/bin/env python3
"""ACO solving a small TSP instance on a fixed graph."""

import numpy as np


def tour_length(tour, distances):
    length = 0.0
    for i in range(len(tour) - 1):
        length += distances[tour[i], tour[i + 1]]
    return length


def aco_tsp(distances, num_ants=10, iterations=100, alpha=1.0, beta=2.0, rho=0.1, q=1.0):
    n = distances.shape[0]
    pheromones = np.ones((n, n))
    heuristic = 1.0 / (distances + 1e-9)

    best_tour = None
    best_length = float('inf')

    for _ in range(iterations):
        all_tours = []
        all_lengths = []

        for _ in range(num_ants):
            start = np.random.randint(n)
            tour = [start]
            visited = {start}

            while len(tour) < n:
                current = tour[-1]
                candidates = [i for i in range(n) if i not in visited]
                pher = pheromones[current, candidates] ** alpha
                heur = heuristic[current, candidates] ** beta
                probs = pher * heur
                probs /= probs.sum()
                next_node = np.random.choice(candidates, p=probs)
                tour.append(next_node)
                visited.add(next_node)

            tour.append(start)
            length = tour_length(tour, distances)
            all_tours.append(tour)
            all_lengths.append(length)

            if length < best_length:
                best_length = length
                best_tour = tour

        # Pheromone evaporation
        pheromones *= (1 - rho)
        # Reinforce best tour
        for i in range(len(best_tour) - 1):
            a, b = best_tour[i], best_tour[i + 1]
            pheromones[a, b] += q / best_length
            pheromones[b, a] += q / best_length

    return best_tour, best_length


def main():
    # Fixed graph distances
    distances = np.array([
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0],
    ], dtype=float)

    best_tour, best_length = aco_tsp(distances)
    print(f"Best tour: {list(map(int, best_tour))}, length: {best_length:.2f}")


if __name__ == '__main__':
    main()
