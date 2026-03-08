# sample3.py
# Nested loops: break exits inner loop only.

if __name__ == '__main__':
    for i in range(3):
        for j in range(3):
            if j == 1:
                break
            print(f"i={i}, j={j}")

