# 0111-Markov-Chain Cheatsheet

- A Markov chain evolves between states with probabilities given by a transition matrix `P[s][t]`.
- At each step, choose next state according to distribution of current row: use `random.choices` or `numpy.random.choice`.
- The chain is memoryless: `Pr(X_{n+1}=j | X_n=i, ...) = P[i][j]`.
- Stationary distribution π satisfies π = πP; can approximate by simulating long run.
- Useful for modeling sequences (e.g. text, weather), Monte Carlo sampling (e.g. MCMC).
- Ensure each row sums to 1; raise error or normalize if not.
