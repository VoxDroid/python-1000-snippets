# sample1.py
# simple single-run demonstration of inventory simulation

import random

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

if __name__ == '__main__':
    print("=== single simulation ===")
    profit = inventory_simulation(50, 10, 20, 60, seed=123)
    print("profit", profit)
