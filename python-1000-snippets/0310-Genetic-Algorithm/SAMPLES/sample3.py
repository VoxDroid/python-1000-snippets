#!/usr/bin/env python3
"""Genetic algorithm for the 0/1 knapsack problem."""

import random


items = [
    {'weight': 3, 'value': 4},
    {'weight': 4, 'value': 5},
    {'weight': 2, 'value': 3},
    {'weight': 5, 'value': 8},
    {'weight': 1, 'value': 2},
]
capacity = 10


def fitness(individual):
    total_weight = 0
    total_value = 0
    for gene, item in zip(individual, items):
        if gene:
            total_weight += item['weight']
            total_value += item['value']
    if total_weight > capacity:
        return 0
    return total_value


def random_individual():
    return [random.choice([0, 1]) for _ in items]


def crossover(a, b):
    point = random.randrange(1, len(a))
    return a[:point] + b[point:]


def mutate(ind, rate=0.1):
    return [gene ^ 1 if random.random() < rate else gene for gene in ind]


def tournament_selection(pop, k=3):
    return max(random.sample(pop, k), key=fitness)


def run_ga(pop_size=50, generations=80):
    population = [random_individual() for _ in range(pop_size)]
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
    return best, fitness(best)


def main():
    best, best_value = run_ga()
    total_weight = sum(item['weight'] for gene, item in zip(best, items) if gene)
    print(f"Best value: {best_value}, weight: {total_weight}")


if __name__ == '__main__':
    main()
