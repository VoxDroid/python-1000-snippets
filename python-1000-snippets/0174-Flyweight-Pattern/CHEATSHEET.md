# 0174-Flyweight-Pattern Cheatsheet

- **Purpose**: minimize memory usage by sharing as much data as possible between similar objects.
- **Intrinsic vs extrinsic state**: intrinsic shared (stored in flyweight), extrinsic passed in by client (e.g., position).
- **Factory**: central cache (`get_flyweight`) returns existing instances or creates new ones.
- **Common use cases**: graphical objects, text formatting, object pools.
- **Thread-safety**: protect cache with locks if used concurrently.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
