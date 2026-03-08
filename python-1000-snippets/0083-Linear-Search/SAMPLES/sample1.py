# sample1.py
# Basic linear search with enumerate

def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

if __name__ == '__main__':
    arr = [10, 20, 30, 40]
    print('idx of 30', linear_search(arr, 30))
    print('idx of 5', linear_search(arr, 5))
