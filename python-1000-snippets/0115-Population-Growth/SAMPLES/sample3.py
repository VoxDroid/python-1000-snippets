# sample3.py
# generate and print population history for different rates

def population_growth(initial_pop, growth_rate, time_steps, carrying_capacity=None):
    population = float(initial_pop)
    history = [population]
    for _ in range(time_steps):
        if carrying_capacity is None:
            population *= (1 + growth_rate)
        else:
            population = population + growth_rate * population * (1 - population / carrying_capacity)
        history.append(population)
    return history

if __name__ == '__main__':
    for r in [0.01, 0.05, 0.1]:
        print(r, population_growth(100, r, 5))
