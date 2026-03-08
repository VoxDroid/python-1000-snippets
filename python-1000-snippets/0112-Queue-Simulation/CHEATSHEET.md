# 0112-Queue-Simulation Cheatsheet

- Simulate queue with random arrivals (Bernoulli or Poisson) and random service times (exponential or fixed).
- Keep list `queue` of arrival timestamps; service when server free.
- Track metrics: wait times, queue lengths, server utilization.
- Use `random.expovariate(service_rate)` for exponential service time with mean `1/service_rate`.
- For large simulations use `collections.deque` for efficient pops from front.
- Implementation assumes single server; extend to multiple servers by tracking busy servers.
