# sample3.py
# Use setdefault to ensure a key exists before modifying.

d = {}
d.setdefault("count", 0)
d["count"] += 1
print(d)

