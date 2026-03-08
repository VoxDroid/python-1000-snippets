# sample3.py
# Nested loop where continue skips inner iteration.

if __name__ == '__main__':
    for i in range(3):
        for j in range(3):
            if j == 1:
                continue
            print(f"i={i}, j={j}")

