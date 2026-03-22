# sample1.py
# Linear cost evaluation over candidate quantities (no LP solver).


def evaluate_cost(q1,q2,cost1=2,cost2=3):
    return q1*cost1 + q2*cost2


def feasible(q1,q2,max_total=10):
    return (q1 + q2) <= max_total

if __name__ == '__main__':
    options=[(10,0),(0,10),(3,7)]
    best=min((o for o in options if feasible(*o)), key=lambda x: evaluate_cost(*x))
    print('Best option:', best,'cost',evaluate_cost(*best))
