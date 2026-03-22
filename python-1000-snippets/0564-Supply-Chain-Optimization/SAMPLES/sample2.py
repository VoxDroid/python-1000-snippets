# sample2.py
# Simulate and pick minimal cost among feasible combinations.


def pick_best(options):
    best=None
    best_cost=float('inf')
    for q1,q2 in options:
        if q1 + q2 <= 10:
            cost = 2*q1 + 3*q2
            if cost < best_cost:
                best_cost=cost
                best=(q1,q2,cost)
    return best

if __name__ == '__main__':
    options=[(10,0),(0,10),(3,7)]
    print('Selected best:', pick_best(options))
