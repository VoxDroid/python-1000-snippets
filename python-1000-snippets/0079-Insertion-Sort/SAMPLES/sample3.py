# sample3.py
# Sort strings by length using key

def insertion_sort_key(arr, key=lambda x: x):
    for i in range(1, len(arr)):
        keyval = arr[i]
        j = i - 1
        while j >= 0 and key(arr[j]) > key(keyval):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = keyval
    return arr

if __name__ == '__main__':
    data = ['dog','elephant','cat']
    print('sorted by length', insertion_sort_key(data.copy(), key=len))
    print('builtin sorted', sorted(data, key=len))
