# sample3.py
# Early exit when element found; demonstrate worst-case cost

def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

if __name__ == '__main__':
    large = list(range(1000))
    print('search 999', linear_search(large, 999))
    print('search missing', linear_search(large, -1))
