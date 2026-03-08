# sample2.py
# Function returning multiple statistics as tuple.

def stats(numbers):
    return (min(numbers), max(numbers), sum(numbers))

if __name__ == '__main__':
    nums = [5, 2, 9, 4]
    lo, hi, total = stats(nums)
    print(f"min={lo}, max={hi}, sum={total}")

