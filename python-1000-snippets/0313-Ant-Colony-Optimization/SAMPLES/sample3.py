#!/usr/bin/env python3
"""ACO with pheromone evaporation and reinforcement on a 6-node graph."""

import numpy as np


def tour_length(tour, distances):
    return sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))


def aco_tsp(distances, num_ants=30, iterations=200, alpha=1.0, beta=3.0, rho=0.2, q=1.0):
    n = distances.shape[0]
    pheromones = np.ones((n, n))
    heuristic = 1.0 / (distances + 1e-9)

    best_tour = None
    best_length = float('inf')

    for _ in range(iterations):
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
            if length < best_length:
                best_length = length
                best_tour = tour

        # Evaporation
        pheromones *= (1 - rho)
        # Reinforcement
        for i in range(len(best_tour) - 1):
            a, b = best_tour[i], best_tour[i + 1]
            pheromones[a, b] += q / best_length
            pheromones[b, a] += q / best_length

    return best_tour, best_length


def main():
    np.random.seed(0)
    n = 6
    base = np.random.rand(n, n)
    distances = (base + base.T) / 2
    np.fill_diagonal(distances, 0.0)

    best_tour, best_length = aco_tsp(distances)
    print(f"Best tour: {list(map(int, best_tour))}, length: {best_length:.2f}")


if __name__ == '__main__':
    main()
