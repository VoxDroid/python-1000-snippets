# sample1.py
# Simple particle swarm optimization implemented in pure Python.

import random


def objective(x):
    return x[0] ** 2 + x[1] ** 2


def pso(objective, lb, ub, swarmsize=20, maxiter=50, w=0.5, c1=0.8, c2=0.9):
    dim = len(lb)
    x = [[random.uniform(lb[i], ub[i]) for i in range(dim)] for _ in range(swarmsize)]
    v = [[0.0 for _ in range(dim)] for _ in range(swarmsize)]
    pbest = [xi[:] for xi in x]
    pbest_val = [objective(xi) for xi in x]
    gbest = pbest[pbest_val.index(min(pbest_val))][:]
    gbest_val = min(pbest_val)

    for iteration in range(maxiter):
        for i in range(swarmsize):
            for d in range(dim):
                r1, r2 = random.random(), random.random()
                v[i][d] = (w * v[i][d] +
                           c1 * r1 * (pbest[i][d] - x[i][d]) +
                           c2 * r2 * (gbest[d] - x[i][d]))
                x[i][d] += v[i][d]
                x[i][d] = max(lb[d], min(ub[d], x[i][d]))
            val = objective(x[i])
            if val < pbest_val[i]:
                pbest_val[i] = val
                pbest[i] = x[i][:]
                if val < gbest_val:
                    gbest_val = val
                    gbest = x[i][:]
    return gbest, gbest_val


def main() -> None:
    lb = [-10, -10]
    ub = [10, 10]
    best, best_val = pso(objective, lb, ub, swarmsize=30, maxiter=100)
    print("Found best point", best, "with value", best_val)


if __name__ == '__main__':
    main()
