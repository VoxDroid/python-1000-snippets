# 0108-Probability-Simulation Cheatsheet

- Monte Carlo simulation approximates probabilities by repeated random trials.
- Use `random` module functions such as `randint`, `random()`, or `choices`.
- Estimate probability P(event) ≈ (count of successes)/N where N = number of trials.
- Variance of estimate ≈ p(1-p)/N; error decreases as √N.
- Seed RNG (`random.seed()`) for reproducibility in examples.
- For simple discrete cases, compare with exact probability (e.g., 6-sided dice sums).
