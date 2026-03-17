#!/usr/bin/env python3
"""Genetic algorithm to maximize number of 1s in a binary string."""

import random


def random_individual(length):
    return [random.choice([0, 1]) for _ in range(length)]


def fitness(individual):
    return sum(individual)


def tournament_selection(pop, k=3):
    best = None
    for _ in range(k):
        candidate = random.choice(pop)
        if best is None or fitness(candidate) > fitness(best):
            best = candidate
    return best


def crossover(a, b):
    point = random.randrange(1, len(a))
    return a[:point] + b[point:]


def mutate(ind, rate=0.05):
    return [gene ^ 1 if random.random() < rate else gene for gene in ind]


def run_ga(pop_size=50, length=10, generations=50):
    population = [random_individual(length) for _ in range(pop_size)]

    for _ in range(generations):
        new_pop = []
        for _ in range(pop_size):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_pop.append(child)
        population = new_pop

    best = max(population, key=fitness)
    return best, fitness(best)


def main():
    best, best_fit = run_ga()
    print(f"Best individual: {best}, fitness: {best_fit:.2f}")


if __name__ == '__main__':
    main()
