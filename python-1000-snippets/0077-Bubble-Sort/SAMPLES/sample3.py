# sample3.py
# Bubble sort with custom key using Python's built-in sorted for comparison

def bubble_sort_key(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(arr[j]) > key(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    data = ['banana', 'apple', 'cherry']
    print('sort by length', bubble_sort_key(data.copy(), key=len))
    print('builtin sort for reference', sorted(data, key=len))
