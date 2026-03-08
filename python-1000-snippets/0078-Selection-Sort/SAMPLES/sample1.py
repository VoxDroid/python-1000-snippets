# sample1.py
# Basic selection sort ascending

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    data = [29, 10, 14, 37, 13]
    print('before', data)
    print('after', selection_sort(data))
