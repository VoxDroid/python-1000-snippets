# sample2.py
# compare different reorder points over a fixed horizon

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
    print("=== reorder point comparison ===")
    for rp in (5, 10, 15):
        profit = inventory_simulation(50, rp, 20, 60, seed=42)
        print(f"reorder-point={rp} -> profit={profit}")
