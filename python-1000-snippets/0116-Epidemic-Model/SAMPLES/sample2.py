# sample2.py
# compare outbreak curves for different infection rates

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
    for b in (0.1, 0.3, 0.5):
        print('beta', b, sir_model(990, 10, 0, b, 0.1, 5))
