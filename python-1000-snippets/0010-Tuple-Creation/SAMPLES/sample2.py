# sample2.py
# Function returning multiple values packed in a tuple.

def min_max(numbers):
    return (min(numbers), max(numbers))

if __name__ == '__main__':
    nums = [4, 7, 1, 9]
    low, high = min_max(nums)
    print(f"Min: {low}, Max: {high}")

