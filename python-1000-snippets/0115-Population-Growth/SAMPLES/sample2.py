# sample2.py
# compare exponential vs logistic

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
    print('exp', population_growth(100, 0.05, 5))
    print('log', population_growth(100, 0.05, 5, carrying_capacity=120))
