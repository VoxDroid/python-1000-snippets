# sample3.py
# Monte Carlo study using multiprocessing to estimate average profit

import random
from multiprocessing import Pool


def inventory_simulation(initial_stock, reorder_point, reorder_amount, days, demand_max=5, seed=None):
    if seed is not None:
        random.seed(seed)
    stock = initial_stock
    profit = 0
    for _ in range(days):
        demand = random.randint(0, demand_max)
        sold = min(stock, demand)
        stock -= sold
        profit += sold * 10
        if stock <= reorder_point:
            stock += reorder_amount
            profit -= reorder_amount * 5
    return profit


def worker(args):
    # args: (initial_stock, reorder_point, reorder_amount, days, seed)
    return inventory_simulation(*args)

if __name__ == '__main__':
    trials = 100
    params = [(50, 10, 20, 60, i) for i in range(trials)]
    with Pool(4) as pool:
        results = pool.map(worker, params)
    avg = sum(results) / len(results)
    print(f"average profit over {trials} trials: {avg}")
