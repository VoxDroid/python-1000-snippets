# 0109-Monte-Carlo-Simulation Cheatsheet

- Monte Carlo techniques use random sampling to estimate mathematical quantities.
- π estimation via quarter-circle: sample (x,y) in [0,1]×[0,1], count inside x²+y²≤1, multiply ratio by 4.
- Confidence interval width ∝1/√N; doubling trials halves standard error.
- Can parallelize with multiprocessing or numpy vectorization.
- For reproducibility, set `random.seed()` or use `numpy.random` with fixed seed.
- Use high-quality RNG for sensitive applications.
