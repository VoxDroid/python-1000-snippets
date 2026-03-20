# sample3.py
# Solve a small optimization problem (Rosenbrock function) using PSO-like search and print the result.

import random


def rosenbrock(x):
    a, b = 1.0, 100.0
    return (a - x[0])**2 + b*(x[1] - x[0]**2)**2


def pso_minimize(func, lb, ub, swarmsize=30, maxiter=60):
    dim = len(lb)
    x = [[random.uniform(lb[i], ub[i]) for i in range(dim)] for _ in range(swarmsize)]
    v = [[0.0 for _ in range(dim)] for _ in range(swarmsize)]
    pbest = [xi[:] for xi in x]
    pbest_val = [func(xi) for xi in x]
    gbest = pbest[pbest_val.index(min(pbest_val))][:]
    gbest_val = min(pbest_val)

    for _ in range(maxiter):
        for i in range(swarmsize):
            for d in range(dim):
                r1, r2 = random.random(), random.random()
                v[i][d] = 0.5 * v[i][d] + 0.7 * r1 * (pbest[i][d] - x[i][d]) + 1.2 * r2 * (gbest[d] - x[i][d])
                x[i][d] += v[i][d]
                x[i][d] = max(lb[d], min(ub[d], x[i][d]))
            val = func(x[i])
            if val < pbest_val[i]:
                pbest_val[i] = val
                pbest[i] = x[i][:]
                if val < gbest_val:
                    gbest_val = val
                    gbest = x[i][:]
    return gbest, gbest_val


def main() -> None:
    lb = [-2, -1]
    ub = [2, 3]
    best, best_val = pso_minimize(rosenbrock, lb, ub)
    print("Rosenbrock best position:", best)
    print("Rosenbrock best value:", best_val)


if __name__ == '__main__':
    main()
