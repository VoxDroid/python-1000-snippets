# sample3.py
# generate proportion-based history and print susceptible fraction

def sir_model(S, I, R, beta, gamma, steps, seed=None):
    history = [(S, I, R)]
    for _ in range(steps):
        N = S + I + R
        new_infections = beta * S * I / N
        new_recoveries = gamma * I
        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries
        history.append((S, I, R))
    return history

if __name__ == '__main__':
    hist = sir_model(1000, 1, 0, 0.4, 0.1, 10)
    print('fractions', [(s/1000, i/1000, r/1000) for s,i,r in hist])
