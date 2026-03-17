#!/usr/bin/env python3
"""GA optimization on a quadratic function (minimize (x-3)^2)."""

import random


def fitness(x):
    # We maximize fitness, so return negative of objective
    return -((x - 3.0) ** 2)


def mutate(x, rate=0.1):
    if random.random() < rate:
        x += random.uniform(-0.5, 0.5)
    return x


def crossover(a, b):
    return 0.5 * (a + b)


def tournament_selection(pop, k=3):
    return max(random.sample(pop, k), key=fitness)


def run_ga(pop_size=40, generations=60):
    population = [random.uniform(-5, 5) for _ in range(pop_size)]

    for _ in range(generations):
        new_pop = []
        for _ in range(pop_size):
            p1 = tournament_selection(population)
            p2 = tournament_selection(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)
        population = new_pop

    best = max(population, key=fitness)
    return best, -fitness(best)


def main():
    best, obj = run_ga()
    print(f"Best x: {best:.2f}, fitness: {obj:.4f}")


if __name__ == '__main__':
    main()
